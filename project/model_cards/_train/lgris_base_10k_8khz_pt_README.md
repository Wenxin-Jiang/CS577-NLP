---
language: pt
datasets:
- common_voice 
- mls
- cetuc
- lapsbm
- voxforge
- tedx
- sid
metrics:
- wer
tags:
- audio
- speech
- wav2vec2
- pt
- portuguese-speech-corpus
- automatic-speech-recognition
- speech
- PyTorch
license: apache-2.0
---

# Wav2vec 2.0 for Portuguese in 8kHz

This is a fine-tuned model from [facebook/wav2vec2-base-10k-voxpopuli](https://huggingface.co/facebook/wav2vec2-base-10k-voxpopuli)

Datasets used to fine-tune the model:
CETUC: contains approximately 145 hours of Brazilian Portuguese speech distributed among 50 male and 50 female speakers, each pronouncing approximately 1,000 phonetically balanced sentences selected from the CETEN-Folha corpus.
Common Voice 7.0: is a project proposed by Mozilla Foundation with the goal to create a wide open dataset in different languages. In this project, volunteers donate and validate speech using the oficial site.
Lapsbm: "Falabrasil - UFPA" is a dataset used by the Fala Brasil group to benchmark ASR systems in Brazilian Portuguese. Contains 35 speakers (10 females), each one pronouncing 20 unique sentences, totalling 700 utterances in Brazilian Portuguese. The audios were recorded in 22.05 kHz without environment control.
Multilingual Librispeech (MLS): a massive dataset available in many languages. The MLS is based on audiobook recordings in public domain like LibriVox. The dataset contains a total of 6k hours of transcribed data in many languages. The set in Portuguese used in this work (mostly Brazilian variant) has approximately 284 hours of speech, obtained from 55 audiobooks read by 62 speakers.
Multilingual TEDx: a collection of audio recordings from TEDx talks in 8 source languages. The Portuguese set (mostly Brazilian Portuguese variant) contains 164 hours of transcribed speech.
Sidney (SID): contains 5,777 utterances recorded by 72 speakers (20 women) from 17 to 59 years old with fields such as place of birth, age, gender, education, and occupation;
VoxForge: is a project with the goal to build open datasets for acoustic models. The corpus contains approximately 100 speakers and 4,130 utterances of Brazilian Portuguese, with sample rates varying from 16kHz to 44.1kHz
VoxPopuli