---
language: de
datasets:
- common_voice
tags:
- audio
- automatic-speech-recognition
- speech
- xlsr-fine-tuning-week
license: apache-2.0
model-index:
- name: wav2vec2-large-xlsr-53-German by Mehdi Hosseini Moghadam
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice de
      type: common_voice
      args: de
    metrics:
       - name: Test WER
         type: wer
         value:  25.284593
---

# wav2vec2-large-xlsr-53-German

Fine-tuned [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) in German using the [Common Voice](https://huggingface.co/datasets/common_voice)

When using this model, make sure that your speech input is sampled at 16kHz.

## Usage

The model can be used directly (without a language model) as follows:

```python

import torch

import torchaudio

from datasets import load_dataset

from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

test_dataset = load_dataset("common_voice", "de", split="test[:2%]")

processor = Wav2Vec2Processor.from_pretrained("MehdiHosseiniMoghadam/wav2vec2-large-xlsr-53-German")

model = Wav2Vec2ForCTC.from_pretrained("MehdiHosseiniMoghadam/wav2vec2-large-xlsr-53-German")

resampler = torchaudio.transforms.Resample(48_000, 16_000)

# Preprocessing the datasets.

# We need to read the aduio files as arrays

def speech_file_to_array_fn(batch):

  speech_array, sampling_rate = torchaudio.load(batch["path"])

  batch["speech"] = resampler(speech_array).squeeze().numpy()

  return batch

test_dataset = test_dataset.map(speech_file_to_array_fn)

inputs = processor(test_dataset["speech"][:2], sampling_rate=16_000, return_tensors="pt", padding=True)

with torch.no_grad():

  logits = model(inputs.input_values, attention_mask=inputs.attention_mask).logits

predicted_ids = torch.argmax(logits, dim=-1)

print("Prediction:", processor.batch_decode(predicted_ids))

print("Reference:", test_dataset["sentence"][:2])

```

## Evaluation

The model can be evaluated as follows on the Czech test data of Common Voice.

```python

import torch

import torchaudio

from datasets import load_dataset, load_metric

from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

import re

test_dataset = load_dataset("common_voice", "de", split="test[:15%]")

wer = load_metric("wer")

processor = Wav2Vec2Processor.from_pretrained("MehdiHosseiniMoghadam/wav2vec2-large-xlsr-53-German")

model = Wav2Vec2ForCTC.from_pretrained("MehdiHosseiniMoghadam/wav2vec2-large-xlsr-53-German")

model.to("cuda")

chars_to_ignore_regex = '[\,\?\.\!\-\;\:\"\“\%\‘\”\�]'

resampler = torchaudio.transforms.Resample(48_000, 16_000)

# Preprocessing the datasets.

# We need to read the aduio files as arrays

def speech_file_to_array_fn(batch):

  batch["sentence"] = re.sub(chars_to_ignore_regex, '', batch["sentence"]).lower()

  

  speech_array, sampling_rate = torchaudio.load(batch["path"])

  

  batch["speech"] = resampler(speech_array).squeeze().numpy()

  

  return batch

test_dataset = test_dataset.map(speech_file_to_array_fn)

# Preprocessing the datasets.

# We need to read the aduio files as arrays

def evaluate(batch):

    inputs = processor(batch["speech"], sampling_rate=16_000, return_tensors="pt", padding=True)

    

    with torch.no_grad():

    

      logits = model(inputs.input_values.to("cuda"), attention_mask=inputs.attention_mask.to("cuda")).logits

    

    pred_ids = torch.argmax(logits, dim=-1)

    

    batch["pred_strings"] = processor.batch_decode(pred_ids)

    

    return batch

result = test_dataset.map(evaluate, batched=True, batch_size=8)

print("WER: {:2f}".format(100 * wer.compute(predictions=result["pred_strings"], references=result["sentence"])))

```

**Test Result**:  25.284593 %

## Training

10% of the Common Voice `train`, `validation` datasets were used for training.

## Testing

15% of the Common Voice `Test` dataset were used for training.