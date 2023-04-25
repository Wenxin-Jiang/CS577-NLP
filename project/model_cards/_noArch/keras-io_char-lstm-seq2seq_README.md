---
language: 
- en
- fr

tags:
- seq2seq
- translation
 
license:
- cc0-1.0
---

## Keras Implementation of Character-level recurrent sequence-to-sequence model

This repo contains the model and the notebook [to this Keras example on Character-level recurrent sequence-to-sequence model](https://keras.io/examples/nlp/lstm_seq2seq/).

Full credits to: [fchollet](https://twitter.com/fchollet)

## Background Information 
This example demonstrates how to implement a basic character-level recurrent sequence-to-sequence model. We apply it to translating short English sentences into short French sentences, character-by-character. Note that it is fairly unusual to do character-level machine translation, as word-level models are more common in this domain.

## Limitations
It works on text of length <= 15 characters

## Parameters needed for using the model
```python
latent_dim = 256
num_encoder_tokens = 71
max_encoder_seq_length = 15
num_decoder_tokens = 92
max_decoder_seq_length = 59
```