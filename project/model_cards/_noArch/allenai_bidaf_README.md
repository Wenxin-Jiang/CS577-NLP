---
language: en
tags:
- allennlp
- question-answering
---

This is an implementation of the BiDAF model with GloVe embeddings. The basic layout is pretty simple: encode words as a combination of word embeddings and a character-level encoder, pass the word representations through a bi-LSTM/GRU, use a matrix of attentions to put question information into the passage word representations (this is the only part that is at all non-standard), pass this through another few layers of bi-LSTMs/GRUs, and do a softmax over span start and span end.