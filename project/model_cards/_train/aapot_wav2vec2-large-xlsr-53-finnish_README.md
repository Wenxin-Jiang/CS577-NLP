---
language: fi
datasets:
- common_voice
metrics:
- wer
tags:
- audio
- automatic-speech-recognition
- speech
- xlsr-fine-tuning-week
license: apache-2.0
model-index:
- name: XLSR Wav2Vec2 Finnish by Aapo Tanskanen
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice fi
      type: common_voice
      args: fi
    metrics:
       - name: Test WER
         type: wer
         value: 32.378771
---

# NOTE: this is an old model and should not be used anymore!! There are a lot better newer models available at our orgnization hub: [Finnish-NLP/wav2vec2-xlsr-1b-finnish-lm-v2](https://huggingface.co/Finnish-NLP/wav2vec2-xlsr-1b-finnish-lm-v2) and [Finnish-NLP/wav2vec2-xlsr-300m-finnish-lm](https://huggingface.co/Finnish-NLP/wav2vec2-xlsr-300m-finnish-lm)

# Wav2Vec2-Large-XLSR-53-Finnish

Fine-tuned [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on Finnish using the [Common Voice](https://huggingface.co/datasets/common_voice), [CSS10 Finnish](https://www.kaggle.com/bryanpark/finnish-single-speaker-speech-dataset) and [Finnish parliament session 2](https://b2share.eudat.eu/records/4df422d631544ce682d6af1d4714b2d4) datasets.
When using this model, make sure that your speech input is sampled at 16kHz.

## Usage

The model can be used directly (without a language model) as follows:

```python
import librosa
import torch
import torchaudio
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

test_dataset = load_dataset("common_voice", "fi", split="test[:2%]")

processor = Wav2Vec2Processor.from_pretrained("aapot/wav2vec2-large-xlsr-53-finnish")
model = Wav2Vec2ForCTC.from_pretrained("aapot/wav2vec2-large-xlsr-53-finnish")

resampler = lambda sr, y: librosa.resample(y.numpy().squeeze(), sr, 16_000)

# Preprocessing the datasets.
# We need to read the audio files as arrays
def speech_file_to_array_fn(batch):
    speech_array, sampling_rate = torchaudio.load(batch["path"])
    batch["speech"] = resampler(sampling_rate, speech_array).squeeze()
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

The model can be evaluated as follows on the Finnish test data of Common Voice.  


```python
import librosa
import torch
import torchaudio
from datasets import load_dataset, load_metric
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import re

test_dataset = load_dataset("common_voice", "fi", split="test")
wer = load_metric("wer")

processor = Wav2Vec2Processor.from_pretrained("aapot/wav2vec2-large-xlsr-53-finnish")
model = Wav2Vec2ForCTC.from_pretrained("aapot/wav2vec2-large-xlsr-53-finnish")
model.to("cuda")

chars_to_ignore_regex = '[\,\?\.\!\-\;\:\"\“\%\‘\”\�\'\...\…\–\é]'
resampler = lambda sr, y: librosa.resample(y.numpy().squeeze(), sr, 16_000)

# Preprocessing the datasets.
# We need to read the audio files as arrays
def speech_file_to_array_fn(batch):
  batch["sentence"] = re.sub(chars_to_ignore_regex, '', batch["sentence"]).lower()
  speech_array, sampling_rate = torchaudio.load(batch["path"])
  batch["speech"] = resampler(sampling_rate, speech_array).squeeze()
  return batch

test_dataset = test_dataset.map(speech_file_to_array_fn)

# Preprocessing the datasets.
# We need to read the audio files as arrays
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

**Test Result**: 32.378771 %


## Training

The Common Voice `train`, `validation` and `other` datasets were used for training as well as `CSS10 Finnish` and `Finnish parliament session 2` datasets.

The script used for training can be found from [Google Colab](https://colab.research.google.com/drive/1vnEGC9BnNRmVyIHj-0UsVulh_cUYSGWA?usp=sharing)