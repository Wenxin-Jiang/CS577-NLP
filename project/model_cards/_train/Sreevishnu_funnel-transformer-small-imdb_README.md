---
license: apache-2.0
language: en
widget:
- text: "In the garden of wonderment that is the body of work by the animation master Hayao Miyazaki, his 2001 gem 'Spirited Away' is at once one of his most accessible films to a Western audience and the one most distinctly rooted in Japanese culture and lore. The tale of Chihiro, a 10 year old girl who resents being moved away from all her friends, only to find herself working in a bathhouse for the gods, doesn't just use its home country's fraught relationship with deities as a backdrop. Never remotely didactic, the film is ultimately a self-fulfilment drama that touches on religious, ethical, ecological and psychological issues.

It's also a fine children's film, the kind that elicits a deepening bond across repeat viewings and the passage of time, mostly because Miyazaki refuses to talk down to younger viewers. That's been a constant in all of his filmography, but it's particularly conspicuous here because the stakes for its young protagonist are bigger than in most of his previous features aimed at younger viewers. It involves conquering fears and finding oneself in situations where safety is not a given.

There are so many moving parts in Spirited Away, from both a thematic and technical point of view, that pinpointing what makes Spirited Away stand out from an already outstanding body of work becomes as challenging as a meeting with Yubaba. But I think it comes down to an ability to deal with heady, complex subject matter from a young girl's perspective without diluting or lessening its resonance. Miyazaki has made a loopy, demanding work of art that asks your inner child to come out and play. There are few high-wire acts in all of movie-dom as satisfying as that."
datasets:
- imdb
tags:
- sentiment-analysis
---

# Funnel Transformer small (B4-4-4 with decoder) fine-tuned on IMDB for Sentiment Analysis

These are the model weights for the Funnel Transformer small model fine-tuned on the IMDB dataset for performing Sentiment Analysis with `max_position_embeddings=1024`.

The original model weights for English language are from [funnel-transformer/small](https://huggingface.co/funnel-transformer/small) and it uses a similar objective objective as [ELECTRA](https://huggingface.co/transformers/model_doc/electra.html). It was introduced in [this paper](https://arxiv.org/pdf/2006.03236.pdf) and first released in [this repository](https://github.com/laiguokun/Funnel-Transformer). This model is uncased: it does not make a difference between english and English.

## Fine-tuning Results

|                               | Accuracy | Precision | Recall   | F1       |
|-------------------------------|----------|-----------|----------|----------|
| funnel-transformer-small-imdb | 0.956530 | 0.952286  | 0.961075 | 0.956661 |


## Model description (from [funnel-transformer/small](https://huggingface.co/funnel-transformer/small))

Funnel Transformer is a transformers model pretrained on a large corpus of English data in a self-supervised fashion. This means it was pretrained on the raw texts only, with no humans labelling them in any way (which is why it can use lots of publicly available data) with an automatic process to generate inputs and labels from those texts.

More precisely, a small language model corrupts the input texts and serves as a generator of inputs for this model, and the pretraining objective is to predict which token is an original and which one has been replaced, a bit like a GAN training.

This way, the model learns an inner representation of the English language that can then be used to extract features useful for downstream tasks: if you have a dataset of labeled sentences for instance, you can train a standard classifier using the features produced by the BERT model as inputs.

# How to use

Here is how to use this model to get the features of a given text in PyTorch:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizer = AutoTokenizer.from_pretrained(
    "Sreevishnu/funnel-transformer-small-imdb",
    use_fast=True)
model = AutoModelForSequenceClassification.from_pretrained(
    "Sreevishnu/funnel-transformer-small-imdb",
    num_labels=2,
    max_position_embeddings=1024)
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
```

# Example App

https://lazy-film-reviews-7gif2bz4sa-ew.a.run.app/

Project repo: https://github.com/akshaydevml/lazy-film-reviews