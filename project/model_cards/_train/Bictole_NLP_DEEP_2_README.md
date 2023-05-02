---
language: en
license: mit
datasets:
- imdb
---

# NLP Deep 2

Fine Tuned model from [distilbert-base](https://huggingface.co/distilbert-base-uncased?text=The+goal+of+life+is+%5BMASK%5D.) on the IMDB dataset.

## Model description

DistilBERT is a transformers model, smaller and faster than BERT, which was pretrained on the same corpus in a self-supervised fashion, using the BERT base model as a teacher. This means it was pretrained on the raw texts only, with no humans labelling them in any way (which is why it can use lots of publicly available data) with an automatic process to generate inputs and labels from those texts using the BERT base model. 


## Training data

The NLP Deep 2 model was pretrained on [BookCorpus](https://yknzhu.wixsite.com/mbweb), a dataset consisting of 11,038
unpublished books and [English Wikipedia](https://en.wikipedia.org/wiki/English_Wikipedia) (excluding lists, tables and
headers).

It was fine tuned on [IMDB](https://arxiv.org/abs/2005.14147) dataset. This is a dataset for binary sentiment classification containing substantially more data than previous benchmark datasets. It provides a set of 25,000 highly polar movie reviews for training, and 25,000 for testing. There is additional unlabeled data for use as well. Raw text and already processed bag of words formats are provided. See the README file contained in the release for more details.

## Training procedure

### Preprocessing

The texts are tokenized using **DistilBertTokenizerFast**. The inputs of the model are then of the form:

```
[CLS] Sentence A [SEP] Sentence B [SEP]
```



## Evaluation results


// TODO