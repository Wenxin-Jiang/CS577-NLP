---
language: tr
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
- name: XLSR Wav2Vec2 Turkish by Davut Emre TASAR
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice tr
      type: common_voice
      args: tr 
    metrics:
       - name: Test WER
         type: wer
         
---

# wav2vec-tr-lite-AG

## Usage

The model can be used directly (without a language model) as follows:

```python
import torch
import torchaudio
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

test_dataset = load_dataset("common_voice", "tr", split="test[:2%]") 

processor = Wav2Vec2Processor.from_pretrained("emre/wav2vec-tr-lite-AG")
model = Wav2Vec2ForCTC.from_pretrained("emre/wav2vec-tr-lite-AG")

resampler = torchaudio.transforms.Resample(48_000, 16_000)

**Test Result**: 27.30 %


 [here](https://adresgezgini.com)

