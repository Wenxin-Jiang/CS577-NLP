---
tags:
- text-to-speech
language:
- it
model-index:
- name: vits-commonvoice9.0
  results: []
datasets:
- mozilla-foundation/common_voice_9_0
---

# Common Voice it Vits

Train on [Mozzila Common voice](https://commonvoice.mozilla.org/) v9.0 it with [Coqui VITS](https://github.com/coqui-ai/TTS)
```
# Coqui tts sha commit coquitts: 0cf3265a4686d7e856bd472cdaf1572d61cab2b8

PYTORCH_CUDA_ALLOC_CONF="max_split_size_mb:25" CUDA_VISIBLE_DEVICES=1 python recipes/common_voice/vits/train_vits.py

CUDA_VISIBLE_DEVICES=0 tts-server --model_path "/run/media/opensuse/Barracuda/Models/TTS_new/trained_common_voice/vits_vctk-June-05-2022_03+45PM-0cf3265a/best_model.pth" --config_path "/run/media/opensuse/Barracuda/Models/TTS_new/trained_common_voice/vits_vctk-June-05-2022_03+45PM-0cf3265a/config.json"
```