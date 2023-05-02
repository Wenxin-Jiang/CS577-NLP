---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased-finetuned-mnli-amazon-query-shopping
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-mnli-amazon-query-shopping

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an [Amazon shopping query dataset](https://www.aicrowd.com/challenges/esci-challenge-for-improving-product-search). The code for the fine-tuning process can be found
[here](https://github.com/vanderbilt-data-science/sna). This model is uncased: it does
not make a difference between english and English.
It achieves the following results on the evaluation set:
- Loss: 0.8244
- Accuracy: 0.6617

## Model description

DistilBERT is a transformers model, smaller and faster than BERT, which was pretrained on the same corpus in a
self-supervised fashion, using the BERT base model as a teacher. This means it was pretrained on the raw texts only,
with no humans labelling them in any way (which is why it can use lots of publicly available data) with an automatic
process to generate inputs and labels from those texts using the BERT base model. We replaced its head with our shopping relevance category to fine-tune it on 571,223 rows of training set while validate it on 142,806 rows of dev set. Finally, we evaluated our model performance on a held-out test set: 79,337 rows.

## Intended uses & limitations

DistilBERT is primarily aimed at being fine-tuned on tasks that use the whole sentence (potentially masked)
to make decisions, such as sequence classification, token classification, or question answering. This fine-tuned version of DistilBERT is used to predict the relevance between one query and one product description. It also can be used to rerank the relevance order of products given one query for the amazon platform or other e-commerce platforms.

The limitations are this trained model is focusing on queries and products on Amazon. If you apply this model to other domains, it may perform poorly.

## How to use 

You can use this model directly by downloading the trained weights and configurations like the below code snippet:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("LiYuan/amazon-query-product-ranking")

model = AutoModelForSequenceClassification.from_pretrained("LiYuan/amazon-query-product-ranking")
```

## Training and evaluation data

Download all the raw [dataset](https://www.aicrowd.com/challenges/esci-challenge-for-improving-product-search/dataset_files) from the Amazon KDD Cup website.

1. Concatenate the all product attributes from the product dataset
2. Join it with a training query dataset
3. Stratified Split the merged data into 571,223-row training, 142,806-row validation, 79,337-row test set
4. Train on the full training set


## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.8981        | 1.0   | 35702 | 0.8662          | 0.6371   |
| 0.7837        | 2.0   | 71404 | 0.8244          | 0.6617   |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1
