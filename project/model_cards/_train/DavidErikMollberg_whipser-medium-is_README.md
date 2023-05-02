---
language:
- is
license: apache-2.0
tags:
- whisper-event
- hf-asr-leaderboard
datasets:
- language-and-voice-lab/samromur_asr
- language-and-voice-lab/althingi_asr
- language-and-voice-lab/malromur_asr
- language-and-voice-lab/samromur_children
- language-and-voice-lab/raddromur_asr
metrics:
- wer
pinned: false
model-index:
- name: Whisper medium is
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: samromur
      type: language-and-voice-lab/samromur_asr
      config: samromur_asr
      split: test
    metrics:
    - type: wer
      value: 10.08%
      name: WER
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: google/fleurs
      type: google/fleurs
      config: is_is
      split: test
    metrics:
    - type: wer
      value: 13.94
      name: WER
---
# openai/whisper-medium

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the samromur, malromur, raddromur and althingi datasets.
It achieves the following results on the evaluation set, the output is lowercased and punctuation is removed:
- Google Fleurs 13.94% WER
- Samrómur 10.08% WER

### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
