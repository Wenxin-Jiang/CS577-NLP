---
language: en
tags:
- exbert
license: apache-2.0
datasets:
- Confidential
---
# BERT base model (uncased)

Pretrained model on English language using a masked language modeling (MLM) objective. It was introduced in
[this paper](https://arxiv.org/abs/1810.04805) and first released in
[this repository](https://github.com/google-research/bert). This model is uncased: it does not make a difference
between english and English.

## Model description

BERT is a transformers model pretrained on a large corpus of English data in a self-supervised fashion. This means it
was pretrained on the raw texts only, with no humans labelling them in any way (which is why it can use lots of
publicly available data) with an automatic process to generate inputs and labels from those texts. More precisely, it
was pretrained with two objectives:

- Masked language modeling (MLM): taking a sentence, the model randomly masks 15% of the words in the input then run
  the entire masked sentence through the model and has to predict the masked words. This is different from traditional
  recurrent neural networks (RNNs) that usually see the words one after the other, or from autoregressive models like
  GPT which internally mask the future tokens. It allows the model to learn a bidirectional representation of the
  sentence.
- Next sentence prediction (NSP): the models concatenates two masked sentences as inputs during pretraining. Sometimes
  they correspond to sentences that were next to each other in the original text, sometimes not. The model then has to
  predict if the two sentences were following each other or not.

This way, the model learns an inner representation of the English language that can then be used to extract features
useful for downstream tasks: if you have a dataset of labeled sentences for instance, you can train a standard
classifier using the features produced by the BERT model as inputs.

## Model description [sbcBI/sentiment_analysis]

This is a fine-tuned downstream version of the bert-base-uncased model for sentiment analysis, this model is not intended for
further downstream fine-tuning for any other tasks. This model is trained on a classified dataset for text-classification.

## Model description [CK42/sbcBI/sentiment_analysis]
This is clone of "https://huggingface.co/sbcBI/sentiment_analysis"
