---
language: nl
tags:
- speech
---

# Wav2Vec2-Dutch-Large-ft-CGN

A Dutch Wav2Vec2 model. This model is created by further pre-training the original English [`facebook/wav2vec2-large`](https://huggingface.co/facebook/wav2vec2-large) model on Dutch speech from [Het Corpus Gesproken Nederlands](https://taalmaterialen.ivdnt.org/download/tstc-corpus-gesproken-nederlands/). Subsequently, the model is fine-tuned on the same Dutch speech using CTC.