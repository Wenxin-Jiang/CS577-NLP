---
language: sv
datasets:
- common_voice
- NST Swedish ASR Database
- P4
metrics:
- wer
tags:
- audio
- automatic-speech-recognition
- speech
- hf-asr-leaderboard
license: cc0-1.0
model-index:
- name: Wav2vec 2.0 large VoxRex Swedish
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
      value: 8.49
---
# Wav2vec 2.0 large VoxRex Swedish (C)

**Disclaimer:** This is a work in progress. See [VoxRex](https://huggingface.co/KBLab/wav2vec2-large-voxrex) for more details.

**Update 2022-01-10:** Updated to VoxRex-C version.

**Update 2022-05-16:** Paper is is [here](https://arxiv.org/abs/2205.03026).

Finetuned version of KBs [VoxRex large](https://huggingface.co/KBLab/wav2vec2-large-voxrex) model using Swedish radio broadcasts, NST and Common Voice data. Evalutation without a language model gives the following: WER for NST + Common Voice test set (2% of total sentences) is **2.5%**. WER for Common Voice test set is **8.49%** directly and **7.37%** with a 4-gram language model.

When using this model, make sure that your speech input is sampled at 16kHz.

# Performance\*

![Comparison](comparison.png "Comparison")
<center><del>*<i>Chart shows performance without the additional 20k steps of Common Voice fine-tuning</i></del></center>

## Training
This model has been fine-tuned for 120000 updates on NST + CommonVoice<del> and then for an additional 20000 updates on CommonVoice only. The additional fine-tuning on CommonVoice hurts performance on the NST+CommonVoice test set somewhat and, unsurprisingly, improves it on the CommonVoice test set. It seems to perform generally better though [citation needed]</del>.

![WER during training](chart_1.svg "WER")

## Usage
The model can be used directly (without a language model) as follows:
```python
import torch
import torchaudio
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
test_dataset = load_dataset("common_voice", "sv-SE", split="test[:2%]").
processor = Wav2Vec2Processor.from_pretrained("KBLab/wav2vec2-large-voxrex-swedish")
model = Wav2Vec2ForCTC.from_pretrained("KBLab/wav2vec2-large-voxrex-swedish")
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

