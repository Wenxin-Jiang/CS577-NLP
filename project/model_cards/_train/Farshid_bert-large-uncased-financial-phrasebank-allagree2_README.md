---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- financial_phrasebank
metrics:
- accuracy
- f1
model-index:
- name: bert-large-uncased-financial-phrasebank-allagree2
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: financial_phrasebank
      type: financial_phrasebank
      config: sentences_allagree
      split: train
      args: sentences_allagree
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9911504424778761
    - name: F1
      type: f1
      value: 0.9910704012566471
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-large-uncased-financial-phrasebank-allagree2

This model is a fine-tuned version of [bert-large-uncased](https://huggingface.co/bert-large-uncased) on the financial_phrasebank dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0734
- Accuracy: 0.9912
- F1: 0.9911

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.3209        | 1.0   | 227  | 0.1929          | 0.9558   | 0.9551 |
| 0.0821        | 2.0   | 454  | 0.0994          | 0.9867   | 0.9867 |
| 0.04          | 3.0   | 681  | 0.0685          | 0.9867   | 0.9866 |
| 0.0098        | 4.0   | 908  | 0.0980          | 0.9867   | 0.9867 |
| 0.0003        | 5.0   | 1135 | 0.0734          | 0.9912   | 0.9911 |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
