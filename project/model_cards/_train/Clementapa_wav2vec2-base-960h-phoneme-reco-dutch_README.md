---
language: nl
datasets:
- common_voice
tags:
- audio
- automatic-speech-recognition
- phoneme-recognition
model-index:
- name: wav2vec2-base-960h-phoneme-reco-dutch
  results:
  - task:
      name: Automatic Phoneme Recognition
      type: automatic-phoneme-recognition
    dataset:
      name: CommonVoice (clean)
      type: librispeech_asr
      config: clean
      split: test
      args: 
        language: nl
    metrics:
    - name: Test PER
      type: per
      value: 20.83
    - name: Val PER
      type: per
      value: 16.18
---

# Model Description

The Wav2vec2 base model [facebook/wav2vec2-base-960h](https://huggingface.co/facebook/wav2vec2-base-960h) fine tuned on phoneme recognition task for the dutch language.

# Usage

To transcribe in phonemes audio files the model can be used as a standalone acoustic model as follows:

```python
 from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
 from datasets import load_dataset
 import torch
 
 # load model and tokenizer
 processor = Wav2Vec2Processor.from_pretrained("Clementapa/wav2vec2-base-960h-phoneme-reco-dutch")
 model = Wav2Vec2ForCTC.from_pretrained("Clementapa/wav2vec2-base-960h-phoneme-reco-dutch")
     
 # load dummy dataset and read soundfiles
 ds = load_dataset("common_voice", "nl", split="validation")
 
 # tokenize
 input_values = processor(ds[0]["audio"]["array"], return_tensors="pt", padding="longest").input_values  # Batch size 1
 
 # retrieve logits
 logits = model(input_values).logits
 
 # take argmax and decode
 predicted_ids = torch.argmax(logits, dim=-1)
 transcription = processor.batch_decode(predicted_ids)
 ```