---
inference: true
pipeline_tag: text-classification
tags:
- feature-extraction
- text-classification
library: pytorch
---

<div style="clear: both;">
  <div style="float: left; margin-right 1em;">
    <h1><strong>FReE (Financial Relation Extraction)</strong></h1>
  </div>
  <div>
    <h2><img src="https://pbs.twimg.com/profile_images/1333760924914753538/fQL4zLUw_400x400.png" alt="" width="25" height="25"></h2>
  </div>
  </div>

We present FReE, a [DistilBERT](https://huggingface.co/distilbert-base-uncased) base model fine-tuned on a custom financial dataset for financial relation type detection and classification.

## Process

Detecting the presence of a relationship between financial terms and qualifying the relationship in case of its presence. Example use cases:

* An A-B trust is a joint trust created by a married couple for the purpose of minimizing estate taxes. (<em>Relationship **exists**, type: **is**</em>)
* There are no withdrawal penalties. (<em>Relationship **does not exist**, type: **x**</em>)

## Data
The data consists of financial definitions collected from different sources (Wikimedia, IFRS, Investopedia) for financial indicators. Each definition has been split up into sentences, and term relationships in a sentence have been extracted using the [Stanford Open Information Extraction](https://nlp.stanford.edu/software/openie.html) module.
A typical row in the dataset consists of a definition sentence and its corresponding relationship label. 
The labels were restricted to the 5 most-widely identified relationships, namely: **x** (no relationship), **has**, **is in**, **is** and **are**.


## Model
The model used is a standard DistilBERT-base transformer model from the Hugging Face library. See [HUGGING FACE DistilBERT base model](https://huggingface.co/distilbert-base-uncased) for more details about the model.
In addition, the model has been pretrained to initializa weigths that would otherwise be unused if loaded from an existing pretrained stock model.

## Metrics
The evaluation metrics used are: Precision, Recall and F1-score. The following is the classification report on the test set.

| relation  | precision        | recall           | f1-score  | support  |
| ------------- |:-------------:|:-------------:|:-------------:| -----:|
| has | 0.7416      | 0.9674 | 0.8396 | 2362 |
| is in | 0.7813      | 0.7925 | 0.7869 | 2362 |
| is | 0.8650     | 0.6863 | 0.7653 | 2362 |
| are | 0.8365     | 0.8493 | 0.8429 | 2362 |
| x | 0.9515     | 0.8302 | 0.8867 | 2362 |
|  |      |  |  |  |
| macro avg | 0.8352     | 0.8251 | 0.8243 | 11810 |
| weighted avg | 0.8352     | 0.8251 | 0.8243 | 11810 |