---
language: ga-IE
datasets:
- common_voice
metrics:
- wer
tags:
- audio
- automatic-speech-recognition
- speech
license: apache-2.0
model-index:
- name: XLSR Wav2Vec2 Irish by Semih GULUM
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice gle
      type: common_voice
      args: ga-IE
    metrics:
       - name: Test WER
         type: wer
         
---
# wav2vec2-irish-lite Speech to Text
## Usage
The model can be used directly (without a language model) as follows:
```python
import torch
import torchaudio
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
test_dataset = load_dataset("common_voice", "ga-IE", split="test[:2%]") 
processor = Wav2Vec2Processor.from_pretrained("Semih/wav2vec2_Irish_Large")
model = Wav2Vec2ForCTC.from_pretrained("Semih/wav2vec2_Irish_Large")
resampler = torchaudio.transforms.Resample(48_000, 16_000)
```
Test Result: 55.11