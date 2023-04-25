---
tags:
- text-to-speech
language:
- it
model-index:
- name: vits-female-it
  results: []
datasets:
- z-uo/female-LJSpeech-italian
---

# Coqui Model for TTS
```
pip install TTS
git clone https://huggingface.co/z-uo/vits-female-it
# predict one
tts --text "ciao pluto" --model_path "vits-female-it/best_model.pth.tar" --config_path "vits-female-it/config.json"
# predict server
tts-server --model_path "vits-female-it/best_model.pth.tar" --config_path "vits-female-it/config.json"
firefox localhost:5002
```
More information about training script in [this repo](https://github.com/nicolalandro/train_coqui_tts_ita).