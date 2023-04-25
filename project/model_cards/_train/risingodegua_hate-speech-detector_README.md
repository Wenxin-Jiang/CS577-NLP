---
language: en
tag: text-classification
datasets:
- twitter
- movies subtitles
---

# Hate Speech Detector 
This model is a fork of the [bert-based-uncased-hatespeech-movies](https://huggingface.co/uhhlt/bert-based-uncased-hatespeech-movies) model. It is used to classify text as **normal**, **offensive**, **hatespeech**. The model is initially a pre-trained transformer model(bert-based-uncased) which is further trained on Twitter comments which can be normal, offensive and hate to learn the context from social media data. It is then fine-tuned using the movie subtitles dataset.

## Test it out
You can test this model live on [Spaces](https://huggingface.co/spaces/risingodegua/hate-speech-detector)
