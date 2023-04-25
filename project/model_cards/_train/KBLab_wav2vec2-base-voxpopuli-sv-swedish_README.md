---
language: sv-SE
datasets:
- common_voice
- NST Swedish ASR Database
metrics:
- wer
#- cer
tags:
- audio
- automatic-speech-recognition
- speech
- voxpopuli
license: cc-by-nc-4.0
model-index:
- name: Wav2vec 2.0 base VoxPopuli-sv swedish
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: NST Swedish ASR Database
    metrics:
       - name: Test WER
         type: wer
         value: 5.619804368919309
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
         value: 19.145252414798616
---
# Wav2vec 2.0 base-voxpopuli-sv-swedish
Finetuned version of Facebooks [VoxPopuli-sv base](https://huggingface.co/facebook/wav2vec2-base-sv-voxpopuli) model using NST and Common Voice data. Evalutation without a language model gives the following: WER for NST + Common Voice test set (2% of total sentences) is **5.62%**, WER for Common Voice test set is **19.15%**.

When using this model, make sure that your speech input is sampled at 16kHz.

## Usage
The model can be used directly (without a language model) as follows:
```python
import torch
import torchaudio
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
test_dataset = load_dataset("common_voice", "sv-SE", split="test[:2%]").
processor = Wav2Vec2Processor.from_pretrained("KBLab/wav2vec2-base-voxpopuli-sv-swedish")
model = Wav2Vec2ForCTC.from_pretrained("KBLab/wav2vec2-base-voxpopuli-sv-swedish")
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