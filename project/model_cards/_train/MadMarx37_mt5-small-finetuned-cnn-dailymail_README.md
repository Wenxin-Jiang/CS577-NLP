---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- cnn_dailymail
metrics:
- rouge
model-index:
- name: mt5-small-finetuned-cnn-dailymail
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: summarization
    dataset:
      name: cnn_dailymail
      type: cnn_dailymail
      config: 3.0.0
      split: train
      args: 3.0.0
    metrics:
    - name: Rouge1
      type: rouge
      value: 32.8352
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-small-finetuned-cnn-dailymail

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on the cnn_dailymail dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7294
- Rouge1: 32.8352
- Rouge2: 17.0633
- Rougel: 29.0888
- Rougelsum: 30.8226

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.6e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| No log        | 1.0   | 8973  | 1.9272          | 31.6634 | 16.1653 | 28.1624 | 29.7819   |
| No log        | 2.0   | 17946 | 1.8282          | 32.1032 | 16.4388 | 28.4914 | 30.1856   |
| No log        | 3.0   | 26919 | 1.7967          | 32.5721 | 16.8392 | 28.8483 | 30.5764   |
| 2.1615        | 4.0   | 35892 | 1.7640          | 32.6788 | 16.94   | 28.994  | 30.6883   |
| 2.1615        | 5.0   | 44865 | 1.7450          | 32.8129 | 17.048  | 29.0788 | 30.8106   |
| 2.1615        | 6.0   | 53838 | 1.7379          | 32.7074 | 16.9641 | 28.9745 | 30.7043   |
| 2.1615        | 7.0   | 62811 | 1.7317          | 32.7692 | 17.0116 | 29.0395 | 30.7685   |
| 2.0886        | 8.0   | 71784 | 1.7294          | 32.8352 | 17.0633 | 29.0888 | 30.8226   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.11.0+cu102
- Datasets 2.7.1
- Tokenizers 0.13.2
