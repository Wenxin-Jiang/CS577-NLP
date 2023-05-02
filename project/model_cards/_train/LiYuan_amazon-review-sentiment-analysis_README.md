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

This model is a fine-tuned version of [nlptown/bert-base-multilingual-uncased-sentiment](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment?text=I+like+you.+I+love+you) on an [Amazon US Customer Reviews Dataset](https://www.kaggle.com/datasets/cynthiarempel/amazon-us-customer-reviews-dataset). The code for the fine-tuning process can be found
[here](https://github.com/vanderbilt-data-science/bigdata/blob/main/06-fine-tune-BERT-on-our-dataset.ipynb). This model is uncased: it does
not make a difference between english and English.
It achieves the following results on the evaluation set:
- Loss: 0.5202942490577698
- Accuracy: 0.8

## Model description

This a bert-base-multilingual-uncased model finetuned for sentiment analysis on product reviews in six languages: English, Dutch, German, French, Spanish and Italian. It predicts the sentiment of the review as a number of stars (between 1 and 5).

This model is intended for direct use as a sentiment analysis model for product reviews in any of the six languages above, or for further finetuning on related sentiment analysis tasks.

We replaced its head with our customer reviews to fine-tune it on 17,280 rows of training set while validating it on 4,320 rows of dev set. Finally, we evaluated our model performance on a held-out test set: 2,400 rows.

## Intended uses & limitations

Bert-base is primarily aimed at being fine-tuned on tasks that use the whole sentence (potentially masked)
to make decisions, such as sequence classification, token classification, or question answering. This fine-tuned version of BERT-base is used to predict review rating star given the review.

The limitations are this trained model is focusing on reviews and products on Amazon. If you apply this model to other domains, it may perform poorly.

## How to use 

You can use this model directly by downloading the trained weights and configurations like the below code snippet:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("LiYuan/amazon-review-sentiment-analysis")

model = AutoModelForSequenceClassification.from_pretrained("LiYuan/amazon-review-sentiment-analysis")
```

## Training and evaluation data

Download all the raw [dataset](https://www.kaggle.com/datasets/cynthiarempel/amazon-us-customer-reviews-dataset) from the Kaggle website.



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
| 0.555400        | 1.0   | 1080 | 0.520294          | 0.800000   |
| 0.424300        | 2.0   | 1080 | 0.549649          | 0.798380   |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1