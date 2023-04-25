---
tags:
- text-to-speech
language:
- it
model-index:
- name: vits-male-it
  results: []
datasets:
- z-uo/female-LJSpeech-italian
---

# Coqui Model for TTS
```
pip install TTS
git clone https://huggingface.co/z-uo/vits-male-it
# predict one
tts --text "ciao pluto" --model_path "vits-male-it/best_model.pth.tar" --config_path "vits-male-it/config.json"
# predict server
tts-server --model_path "vits-male-it/best_model.pth.tar" --config_path "vits-male-it/config.json"
firefox localhost:5002
```
More information about training script in [this repo](https://github.com/nicolalandro/train_coqui_tts_ita).