---
language: sv
license: mit
---

## Swedish BERT models for sentiment analysis, Sentiment targets. 
[Recorded Future](https://www.recordedfuture.com/) together with [AI Sweden](https://www.ai.se/en) releases a Named Entity Recognition(NER) model for entety detection in Swedish. The model is based on [KB/bert-base-swedish-cased](https://huggingface.co/KB/bert-base-swedish-cased) and finetuned on data collected from various internet sources and forums.

The model has been trained on Swedish data and only supports inference of Swedish input texts. The models inference metrics for all non-Swedish inputs are not defined, these inputs are considered as out of domain data.

The current models are supported at Transformers version >= 4.3.3 and Torch version 1.8.0, compatibility with older versions are not verified. 

### Available tags

* Location
* Organization
* Person
* Religion
* Title

### Evaluation metrics
The model had the following metrics when evaluated on test data originating from the same domain as the training data. 
#### F1-score
| Loc  | Org  | Per  | Nat  | Rel  | Tit  | Total |
|------|------|------|------|------|------|-------|
| 0.91 | 0.88 | 0.96 | 0.95 | 0.91 | 0.84 | 0.92  |
