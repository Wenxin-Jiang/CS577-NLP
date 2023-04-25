---
language: en
tags:
- allennlp
- question-answering
---

A reading comprehension model patterned after the proposed model in Devlin et al, with improvements borrowed from the SQuAD model in the transformers project
The model implements a reading comprehension model patterned after the proposed model in BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (Devlin et al, 2018), with improvements borrowed from the SQuAD model in the transformers project. It predicts start tokens and end tokens with a linear layer on top of word piece embeddings.