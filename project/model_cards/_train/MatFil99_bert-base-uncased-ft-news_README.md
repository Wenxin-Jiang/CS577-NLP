---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bert-base-uncased-ft-news
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-ft-news

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the [news](https://huggingface.co/datasets/steciuk/news) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4300
- Accuracy: 0.9
- F1: 0.8783

and flowing results on the testing set:
- Accuracy: 0.8954
- F1: 0.8784

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.4196        | 0.37  | 120  | 0.3051          | 0.8875   | 0.8566 |
| 0.3101        | 0.75  | 240  | 0.2979          | 0.8953   | 0.8743 |
| 0.2693        | 1.12  | 360  | 0.3162          | 0.9016   | 0.8831 |
| 0.2078        | 1.5   | 480  | 0.3298          | 0.8984   | 0.8767 |
| 0.1725        | 1.87  | 600  | 0.3801          | 0.9047   | 0.8851 |
| 0.1369        | 2.24  | 720  | 0.3901          | 0.8938   | 0.8677 |
| 0.1101        | 2.62  | 840  | 0.4160          | 0.9016   | 0.8805 |
| 0.1019        | 2.99  | 960  | 0.4300          | 0.9      | 0.8783 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
