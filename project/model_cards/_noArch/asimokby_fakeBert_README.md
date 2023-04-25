---
license: mit
tags:
- text-classification
- PyTorch
- Transformers
---


# fakeBert

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on a [news dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset) from Kaggle.

## Model description

Fine-tuning Bert for text classification.

## Training and evaluation data

Training & Validation: [Fake and real news dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
Testing: [Fake News Detection Challenge KDD 2020](https://www.kaggle.com/competitions/fakenewskdd2020/overview)

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-5
- train_batch_size: 16
- eval_batch_size: 16
- optimizer: AdamW
