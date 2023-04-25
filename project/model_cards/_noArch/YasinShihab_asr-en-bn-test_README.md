---
language: Bengali
datasets:
- OpenSLR
metrics:
- wer
tags:
- bn
- audio
- automatic-speech-recognition
- speech
license: cc-by-sa-4.0
model-index:
- name: XLSR Wav2Vec2 Bengali by Arijit
  results:
  - task:
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: OpenSLR
      type: OpenSLR
      args: ben
    metrics:
    - name: Test WER
      type: wer
      value: 32.45
---
# Wav2Vec2-Large-XLSR-Bengali
Fine-tuned [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) Bengali using a subset of 40,000 utterances from [Bengali ASR training data set containing ~196K utterances](https://www.openslr.org/53/). Tested WER using ~4200 held out from training.
When using this model, make sure that your speech input is sampled at 16kHz.
Train Script can be Found at : train.py 
    Data Prep Notebook : https://colab.research.google.com/drive/1JMlZPU-DrezXjZ2t7sOVqn7CJjZhdK2q?usp=sharing
    Inference Notebook : https://colab.research.google.com/drive/1uKC2cK9JfUPDTUHbrNdOYqKtNozhxqgZ?usp=sharing
## Usage

The model can be used directly (without a language model) as follows:
```python
import torch
import torchaudio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
processor = Wav2Vec2Processor.from_pretrained("arijitx/wav2vec2-large-xlsr-bengali")
model = Wav2Vec2ForCTC.from_pretrained("arijitx/wav2vec2-large-xlsr-bengali")
# model = model.to("cuda")
resampler = torchaudio.transforms.Resample(TEST_AUDIO_SR, 16_000)
def speech_file_to_array_fn(batch):
    speech_array, sampling_rate = torchaudio.load(batch)
    speech =  resampler(speech_array).squeeze().numpy()
    return speech
speech_array = speech_file_to_array_fn("test_file.wav")
inputs = processor(speech_array, sampling_rate=16_000, return_tensors="pt", padding=True)
with torch.no_grad():
    logits = model(inputs.input_values).logits
    
predicted_ids = torch.argmax(logits, dim=-1)
preds = processor.batch_decode(predicted_ids)[0]
print(preds.replace("[PAD]",""))
```
**Test Result**: WER on ~4200 utterance : 32.45 %