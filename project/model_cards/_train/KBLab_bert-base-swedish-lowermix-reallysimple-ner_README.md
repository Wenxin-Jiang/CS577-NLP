---
model:
- KB/bert-base-swedish-cased
tags:
- token-classification
- sequence-tagger-model
- bert
language: sv
datasets:
- KBLab/sucx3_ner
widget:
- text: "Emil bor i Lönneberga"
---

# KB-BERT for NER

## Mixed cased and uncased data

This model is based on [KB-BERT](https://huggingface.co/KB/bert-base-swedish-cased) and was fine-tuned on the [SUCX 3.0 - NER](https://huggingface.co/datasets/KBLab/sucx3_ner) corpus, using the _simple_ tags and partially lowercased data.
For this model we used a variation of the data that did **not** use BIO-encoding to differentiate between the beginnings (B), and insides (I) of named entity tags.

The model was trained on the training data only, with the best model chosen by its performance on the validation data.
You find more information about the model and the performance on our blog: https://kb-labb.github.io/posts/2022-02-07-sucx3_ner