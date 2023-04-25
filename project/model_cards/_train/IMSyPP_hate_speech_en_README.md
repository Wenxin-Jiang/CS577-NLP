---
widget:

- text: "My name is Mark and I live in London. I am a postgraduate student at Queen Mary University."
language: 
  - en
license: mit
---

# Hate Speech Classifier for Social Media Content in English Language

A monolingual model for hate speech classification of social media content in English language. The model was trained on 103190 YouTube comments and tested on an independent test set of 20554 YouTube comments. It is based on English BERT base pre-trained language model.

## Tokenizer

During training the text was preprocessed using the original English BERT base tokenizer. We suggest the same tokenizer is used for inference.

## Model output

The model classifies each input into one of four distinct classes:
* 0 - acceptable
* 1 - inappropriate
* 2 - offensive
* 3 - violent