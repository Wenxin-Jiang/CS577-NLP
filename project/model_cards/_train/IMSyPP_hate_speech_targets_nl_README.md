---
language: 
  - nl
license: mit
---

# Hate Speech Target Classifier for Social Media Content in Dutch

A monolingual model for hate speech target classification of social media content in Dutch. The model was trained on 20000 social media posts (youtube, twitter, facebook) and tested on an independent test set of 2000 posts. It is based on the pre-trained language model [distilbert-base-multilingual-cased](https://huggingface.co/distilbert-base-multilingual-cased).

## Tokenizer

During training the text was preprocessed using the Distilbert tokenizer. We suggest the same tokenizer is used for inference.

## Model output

The model classifies each input into one of four distinct classes:
* 0 - HOMOPHOBIA
* 1 - OTHER
* 2 - RELIGION
* 3 - ANTISEMITISM
* 4 - IDEOLOGY
* 5 - MIGRANTS
* 6 - POLITICS
* 7 - RACISM
* 8 - MEDIA
* 9 - ISLAMOPHOBIA
* 10 - INDIVIDUAL
* 11 - SEXISM