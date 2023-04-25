---
language: 
  - nl
license: mit
---

# Hate Speech Classifier for Social Media Content in Dutch

A monolingual model for hate speech classification of social media content in Dutch. The model was trained on 20000 social media posts (youtube, twitter, facebook) and tested on an independent test set of 2000 posts. It is based on thepre-trained language model [BERTje](https://huggingface.co/wietsedv/bert-base-dutch-cased).

## Tokenizer

During training the text was preprocessed using the BERTje tokenizer. We suggest the same tokenizer is used for inference.

## Model output

The model classifies each input into one of four distinct classes:
* 0 - acceptable
* 1 - inappropriate
* 2 - offensive
* 3 - violent