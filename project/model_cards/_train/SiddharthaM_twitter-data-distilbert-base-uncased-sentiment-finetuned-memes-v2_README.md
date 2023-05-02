---
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: twitter-data-distilbert-base-uncased-sentiment-finetuned-memes-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# twitter-data-distilbert-base-uncased-sentiment-finetuned-memes-v2

This model is a fine-tuned version of [jayantapaul888/twitter-data-distilbert-base-uncased-sentiment-finetuned-memes](https://huggingface.co/jayantapaul888/twitter-data-distilbert-base-uncased-sentiment-finetuned-memes) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3345
- Accuracy: 0.6527
- Precision: 0.6528
- Recall: 0.6527
- F1: 0.6527

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
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.859         | 1.0   | 663  | 0.7251          | 0.6635   | 0.6722    | 0.6635 | 0.6620 |
| 0.6619        | 2.0   | 1326 | 0.7307          | 0.6723   | 0.6737    | 0.6723 | 0.6720 |
| 0.5684        | 3.0   | 1989 | 0.8724          | 0.6629   | 0.6645    | 0.6629 | 0.6626 |
| 0.3338        | 4.0   | 2652 | 1.0549          | 0.6551   | 0.6571    | 0.6551 | 0.6548 |
| 0.2512        | 5.0   | 3315 | 1.2275          | 0.6554   | 0.6555    | 0.6554 | 0.6553 |
| 0.1945        | 6.0   | 3978 | 1.3345          | 0.6527   | 0.6528    | 0.6527 | 0.6527 |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
