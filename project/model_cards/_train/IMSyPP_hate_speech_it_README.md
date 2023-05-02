---
widget:
- text: "Ciao, mi chiamo Marcantonio, sono di Roma. Studio informatica all'Università di Roma."
language: 
  - it
license: mit
---

# Hate Speech Classifier for Social Media Content in Italian Language

A monolingual model for hate speech classification of social media content in Italian language. The model was trained on 119,670 YouTube comments and tested on an independent test set of 21,072 YouTube comments. It is based on Italian ALBERTO pre-trained language model.

## Tokenizer

During training the text was preprocessed using the original Italian ALBERTO tokenizer. We suggest the same tokenizer is used for inference.

## Model output

The model classifies each input into one of four distinct classes:

* 0 - acceptable

* 1 - inappropriate

* 2 - offensive

* 3 - violent