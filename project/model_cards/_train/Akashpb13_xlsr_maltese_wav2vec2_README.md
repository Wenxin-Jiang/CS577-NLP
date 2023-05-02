---
language: mt
datasets:
- common_voice
tags:
- audio
- automatic-speech-recognition
- speech
- xlsr-fine-tuning-week
license: apache-2.0
model-index:
- name: XLSR Wav2Vec2 Maltese by Akash PB
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice mt
      type: common_voice
      args: {lang_id}  
    metrics:
       - name: Test WER
         type: wer
         value: 29.42
---
# Wav2Vec2-Large-XLSR-53-Maltese
Fine-tuned [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) in Maltese using the [Common Voice](https://huggingface.co/datasets/common_voice)
When using this model, make sure that your speech input is sampled at 16kHz.
## Usage
The model can be used directly (without a language model) as follows:
```python
import torchaudio
from datasets import load_dataset, load_metric
from transformers import (
    Wav2Vec2ForCTC,
    Wav2Vec2Processor,
)
import torch
import re
import sys

model_name = "Akashpb13/xlsr_maltese_wav2vec2"
device = "cuda"
chars_to_ignore_regex = '[\\,\\?\\.\\!\\-\\;\\:\\"\\“\\%\\‘\\”\\�\\)\\(\\*)]'

model = Wav2Vec2ForCTC.from_pretrained(model_name).to(device)
processor = Wav2Vec2Processor.from_pretrained(model_name)

ds = load_dataset("common_voice", "mt", split="test", data_dir="./cv-corpus-6.1-2020-12-11")

resampler = torchaudio.transforms.Resample(orig_freq=48_000, new_freq=16_000)

def map_to_array(batch):
    speech, _ = torchaudio.load(batch["path"])
    batch["speech"] = resampler.forward(speech.squeeze(0)).numpy()
    batch["sampling_rate"] = resampler.new_freq
    batch["sentence"] = re.sub(chars_to_ignore_regex, '', batch["sentence"]).lower() + " "
    return batch

ds = ds.map(map_to_array)

def map_to_pred(batch):
    features = processor(batch["speech"], sampling_rate=batch["sampling_rate"][0], padding=True, return_tensors="pt")
    input_values = features.input_values.to(device)
    attention_mask = features.attention_mask.to(device)
    with torch.no_grad():
        logits = model(input_values, attention_mask=attention_mask).logits
    pred_ids = torch.argmax(logits, dim=-1)
    batch["predicted"] = processor.batch_decode(pred_ids)
    batch["target"] = batch["sentence"]
    return batch

result = ds.map(map_to_pred, batched=True, batch_size=1, remove_columns=list(ds.features.keys()))

wer = load_metric("wer")
print(wer.compute(predictions=result["predicted"], references=result["target"]))

```
**Test Result**: 29.42 %
