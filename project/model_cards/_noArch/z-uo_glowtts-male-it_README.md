---
tags:
- text-to-speech
language:
- it
model-index:
- name: glowtts-male-it
  results: []
datasets:
- z-uo/male-LJSpeech-italian
---

# Coqui Model for TTS
```
pip install TTS
git clone https://huggingface.co/z-uo/glowtts-male-it
# predict one
server --text "ciao pluto" --model_path "glowtts-male-it/GOOD_best_model_3840.pth.tar" --config_path "glowtts-male-it/config.json"
# predict server
tts-server --model_path "glowtts-male-it/GOOD_best_model_3840.pth.tar" --config_path "glowtts-male-it/config.json"
firefox localhost:5002
```
More information about training script in [this repo](https://github.com/nicolalandro/train_coqui_tts_ita).