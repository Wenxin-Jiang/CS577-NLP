---
license: apache-2.0
language: ta
tags:
- audio
- automatic-speech-recognition
- speech
- xlsr-fine-tuning-week
- hf-asr-leaderboard
- tamil language
model-index:
- name: XLSR Wav2Vec2 Tamil by Manan Dey
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
         value: 57.004356
---

# Wav2Vec2-Large-XLSR-Tamil

When using this model, make sure that your speech input is sampled at 16kHz.

## Inference

The model can be used directly as follows:

```python
!pip install datasets 
!pip install transformers 

from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

import torch
import librosa
from datasets import load_dataset

test_dataset = load_dataset("common_voice", "ta", split="test[:2%]").

processor = Wav2Vec2Processor.from_pretrained("Gobee/Wav2vec2-Large-XLSR-Tamil")
model = Wav2Vec2ForCTC.from_pretrained("Gobee/Wav2vec2-Large-XLSR-Tamil")

resampler = torchaudio.transforms.Resample(48_000, 16_000)

# Preprocessing the datasets.
# We need to read the audio files as arrays
def speech_file_to_array_fn(batch):
    speech_array, sampling_rate = librosa.load(batch["path"], sr=16_000)
    batch["speech"] = speech_array
    batch["sentence"] = batch["sentence"].upper()
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

The model can be evaluated as follows on the {language} test data of Common Voice.


```python
!pip install datasets 
!pip install transformers 
!pip install jiwer

from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

import torch
import librosa
from datasets import load_dataset, load_metric
import re

test_dataset = load_dataset("common_voice", "ta", split="test")
wer = load_metric("wer")

processor = Wav2Vec2Processor.from_pretrained("Gobee/Wav2vec2-Large-XLSR-Tamil")
model = Wav2Vec2ForCTC.from_pretrained("Gobee/Wav2vec2-Large-XLSR-Tamil")
model.to("cuda")

chars_to_ignore_regex = '[\,\?\.\!\-\;\:\"\“\%\‘\”\ \’\–\(\)]'

# Preprocessing the datasets.
# We need to read the aduio files as arrays
def speech_file_to_array_fn(batch):
    batch["sentence"] = re.sub(chars_to_ignore_regex, '', batch["sentence"]).lower()
    speech_array, sampling_rate = librosa.load(batch["path"], sr=16_000)
    batch["speech"] = speech_array
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

**Test Result**: 57.004356 %

## Usage and Evaluation script

The script used for usage and evaluation can be found [here](https://colab.research.google.com/drive/1dyDe14iOmoNoVHDJTkg-hAgLnrGdI-Dk?usp=share_link)

## Training

The Common Voice `train`, `validation` datasets were used for training.

The script used for training can be found [here](https://colab.research.google.com/drive/1-Klkgr4f-C9SanHfVC5RhP0ELUH6TYlN?usp=sharing)
