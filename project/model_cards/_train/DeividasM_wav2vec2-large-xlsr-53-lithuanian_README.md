---

language: lt

datasets:

- common_voice

tags:

- audio

- automatic-speech-recognition

- speech

- xlsr-fine-tuning-week

license: apache-2.0

model-index:

- name: XLSR Wav2Vec2 Lithuanina by Deividas Mataciunas

  results:

  - task: 

      name: Speech Recognition

      type: automatic-speech-recognition

    dataset:

      name: Common Voice lt

      type: common_voice

      args: lt  

    metrics:

       - name: Test WER

         type: wer

         value: 56.55

---

# Wav2Vec2-Large-XLSR-53-Lithuanian

Fine-tuned [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) in Lithuanian using the [Common Voice](https://huggingface.co/datasets/common_voice)

When using this model, make sure that your speech input is sampled at 16kHz.

## Usage

The model can be used directly (without a language model) as follows:

```python

import torch

import torchaudio

from datasets import load_dataset

from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

test_dataset = load_dataset("common_voice", "lt", split="test[:2%]")

processor = Wav2Vec2Processor.from_pretrained("DeividasM/wav2vec2-large-xlsr-53-lithuanian")

model = Wav2Vec2ForCTC.from_pretrained("DeividasM/wav2vec2-large-xlsr-53-lithuanian")

resampler = torchaudio.transforms.Resample(48_000, 16_000)

# Preprocessing the datasets.

# We need to read the audio files as arrays

def speech_file_to_array_fn(batch):

\\tspeech_array, sampling_rate = torchaudio.load(batch["path"])

\\tbatch["speech"] = resampler(speech_array).squeeze().numpy()

\\treturn batch

test_dataset = test_dataset.map(speech_file_to_array_fn)

inputs = processor(test_dataset["speech"][:2], sampling_rate=16_000, return_tensors="pt", padding=True)

with torch.no_grad():

\\tlogits = model(inputs.input_values, attention_mask=inputs.attention_mask).logits

predicted_ids = torch.argmax(logits, dim=-1)

print("Prediction:", processor.batch_decode(predicted_ids))

print("Reference:", test_dataset["sentence"][:2])

```

## Evaluation

The model can be evaluated as follows on the Lithuanian test data of Common Voice.

```python

import torch

import torchaudio

from datasets import load_dataset, load_metric

from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

import re

test_dataset = load_dataset("common_voice", "lt", split="test")

wer = load_metric("wer")

processor = Wav2Vec2Processor.from_pretrained("DeividasM/wav2vec2-large-xlsr-53-lithuanian")

model = Wav2Vec2ForCTC.from_pretrained("DeividasM/wav2vec2-large-xlsr-53-lithuanian")

model.to("cuda")

chars_to_ignore_regex = '[\\\\,\\\\?\\\\.\\\\!\\\\-\\\\;\\\\:\\\\"\\\\“]'

resampler = torchaudio.transforms.Resample(48_000, 16_000)

# Preprocessing the datasets.

# We need to read the audio files as arrays

def speech_file_to_array_fn(batch):

\\tbatch["sentence"] = re.sub(chars_to_ignore_regex, '', batch["sentence"]).lower()

\\tspeech_array, sampling_rate = torchaudio.load(batch["path"])

\\tbatch["speech"] = resampler(speech_array).squeeze().numpy()

\\treturn batch

test_dataset = test_dataset.map(speech_file_to_array_fn)

# Preprocessing the datasets.

# We need to read the audio files as arrays

def evaluate(batch):

\\tinputs = processor(batch["speech"], sampling_rate=16_000, return_tensors="pt", padding=True)

\\twith torch.no_grad():

\\t\\tlogits = model(inputs.input_values.to("cuda"), attention_mask=inputs.attention_mask.to("cuda")).logits

    pred_ids = torch.argmax(logits, dim=-1)

\\tbatch["pred_strings"] = processor.batch_decode(pred_ids)

\\treturn batch

result = test_dataset.map(evaluate, batched=True, batch_size=8)

print("WER: {:2f}".format(100 * wer.compute(predictions=result["pred_strings"], references=result["sentence"])))

```

**Test Result**: 56.55 %

## Training

The Common Voice `train`, `validation` datasets were used for training.
