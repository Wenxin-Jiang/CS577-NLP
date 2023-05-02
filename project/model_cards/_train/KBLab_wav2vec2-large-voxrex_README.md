---
language: sv
tags:
- audio
- automatic-speech-recognition
- voxrex
license: cc0-1.0
---

# Wav2vec 2.0 large VoxRex (C)

**Please note:** The model hosted in this repository is a pretrained wav2vec2 without a CTC head, as such it cannot do speech-to-text. If you are interested in speech-to-text, see our finetuned version of this model, which can be found at [KBLab/wav2vec2-large-voxrex-swedish](https://huggingface.co/KBLab/wav2vec2-large-voxrex-swedish). The weights found in this repository are from the pure acoustic model after unsupervised pretraining. This model is suitable for anyone interested in i) continued wav2vec2-pretraining with your own unsupervised data, ii) a feature extractor for finetuning your own downstream tasks (e.g. if you want to train your own CTC head, or an audio classifier). 

**Disclaimer:** This is a work in progress.<br>
**Update 2022-01-08:** Updated to VoxRex-C version, use git to get the older (B) version.<br>
**Update 2022-05-16:** Paper is is [here](https://arxiv.org/abs/2205.03026).

This model has been pretrained for 400,000 updates on the P4-10k corpus which contains 10 000 hours of swedish local public service radio as well as 1500 hours of audio books and other speech from KBs collections.

![Accuracy during training](accuracy.svg "Accuracy")
