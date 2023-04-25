---
language: sv-SE
datasets:
- common_voice
- NST Swedish ASR Database
metrics:
- wer
- cer
tags:
- audio
- automatic-speech-recognition
- speech
- voxpopuli
license: cc-by-nc-4.0
model-index:
- name: Wav2vec 2.0 large VoxPopuli-sv swedish
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice
      type: common_voice
      args: sv-SE
    metrics:
       - name: Test WER
         type: wer
         value: 10.994764
       - name: Test CER
         type: cer
         value: 3.946846
---
# Wav2vec 2.0 large-voxpopuli-sv-swedish

**PLEASE NOTE that [this](https://huggingface.co/KBLab/wav2vec2-large-voxrex-swedish) model performs better and has a less restrictive license.**


Additionally pretrained and finetuned version of Facebooks [VoxPopuli-sv large](https://huggingface.co/facebook/wav2vec2-large-sv-voxpopuli) model using Swedish radio broadcasts, NST and Common Voice data. Evalutation without a language model gives the following: WER for NST + Common Voice test set (2% of total sentences) is **3.95%**. WER for Common Voice test set is **10.99%** directly and **7.82%** with a 4-gram language model.

When using this model, make sure that your speech input is sampled at 16kHz.

## Training
This model has additionally pretrained on 1000h of Swedish local radio broadcasts, fine-tuned for 120000 updates on NST + CommonVoice and then for an additional 20000 updates on CommonVoice only. The additional fine-tuning on CommonVoice hurts performance on the NST+CommonVoice test set somewhat and, unsurprisingly, improves it on the CommonVoice test set. It seems to perform generally better though [citation needed].

## Usage
The model can be used directly (without a language model) as follows:
```python
import torch
import torchaudio
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
test_dataset = load_dataset("common_voice", "sv-SE", split="test[:2%]").
processor = Wav2Vec2Processor.from_pretrained("KBLab/wav2vec2-large-voxpopuli-sv-swedish")
model = Wav2Vec2ForCTC.from_pretrained("KBLab/wav2vec2-large-voxpopuli-sv-swedish")
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