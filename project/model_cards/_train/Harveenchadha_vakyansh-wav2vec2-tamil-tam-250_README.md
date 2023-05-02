---
language: ta
#datasets:
#- Interspeech 2021
metrics:
- wer
tags:
- audio
- automatic-speech-recognition
- speech
license: mit
model-index:
- name: Wav2Vec2 Vakyansh Tamil Model by Harveen Chadha
  results:
  - task:
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice ta
      type: common_voice
      args: ta
    metrics:
    - name: Test WER
      type: wer
      value: 53.64
---

## Pretrained Model

Fine-tuned on Multilingual Pretrained Model [CLSRIL-23](https://arxiv.org/abs/2107.07402). The original fairseq checkpoint is present [here](https://github.com/Open-Speech-EkStep/vakyansh-models). When using this model, make sure that your speech input is sampled at 16kHz.

**Note: The result from this model is without a language model so you may witness a higher WER in some cases.**

## Dataset

This model was trained on 4200 hours of Hindi Labelled Data. The labelled data is not present in public domain as of now.

## Training Script

Models were trained using experimental platform setup by Vakyansh team at Ekstep. Here is the [training repository](https://github.com/Open-Speech-EkStep/vakyansh-wav2vec2-experimentation).

In case you want to explore training logs on wandb they are [here](https://wandb.ai/harveenchadha/tamil-finetuning-multilingual).


## [Colab Demo](https://github.com/harveenchadha/bol/blob/main/demos/hf/tamil/hf_tamil_tnm_4200_demo.ipynb)

## Usage

The model can be used directly (without a language model) as follows:

```python
import soundfile as sf
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import argparse

def parse_transcription(wav_file):
    # load pretrained model
    processor = Wav2Vec2Processor.from_pretrained("Harveenchadha/vakyansh-wav2vec2-tamil-tam-250")
    model = Wav2Vec2ForCTC.from_pretrained("Harveenchadha/vakyansh-wav2vec2-tamil-tam-250")

    # load audio
    audio_input, sample_rate = sf.read(wav_file)

    # pad input values and return pt tensor
    input_values = processor(audio_input, sampling_rate=sample_rate, return_tensors="pt").input_values

    # INFERENCE
    # retrieve logits & take argmax
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)

    # transcribe
    transcription = processor.decode(predicted_ids[0], skip_special_tokens=True)
    print(transcription)

```


## Evaluation
The model can be evaluated as follows on the hindi test data of Common Voice. 

```python

import torch
import torchaudio
from datasets import load_dataset, load_metric
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import re

test_dataset = load_dataset("common_voice", "ta", split="test")
wer = load_metric("wer")

processor = Wav2Vec2Processor.from_pretrained("Harveenchadha/vakyansh-wav2vec2-tamil-tam-250")
model = Wav2Vec2ForCTC.from_pretrained("Harveenchadha/vakyansh-wav2vec2-tamil-tam-250")
model.to("cuda")

resampler = torchaudio.transforms.Resample(48_000, 16_000)

chars_to_ignore_regex = '[\,\?\.\!\-\;\:\"\“]'

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
      logits = model(inputs.input_values.to("cuda")).logits

      pred_ids = torch.argmax(logits, dim=-1)
      batch["pred_strings"] = processor.batch_decode(pred_ids, skip_special_tokens=True)
      return batch

result = test_dataset.map(evaluate, batched=True, batch_size=8)

print("WER: {:2f}".format(100 * wer.compute(predictions=result["pred_strings"], references=result["sentence"])))

```

**Test Result**: 53.64 %

[**Colab Evaluation**](https://github.com/harveenchadha/bol/blob/main/demos/hf/tamil/hf_vakyansh_tamil_tnm_4200_evaluation_common_voice.ipynb) 

## Credits
Thanks to Ekstep Foundation for making this possible. The vakyansh team will be open sourcing speech models in all the Indic Languages.