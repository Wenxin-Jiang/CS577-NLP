---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bart-JES-cnn_dailymail
  results:
  - task:
      name: Summarization
      type: summarization
    metrics:
    - name: Rouge1
      type: rouge
      value: 43.9753
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-JES-cnn_dailymail

This model is a fine-tuned version of [facebook/bart-large](https://huggingface.co/facebook/bart-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1452
- Rouge1: 43.9753
- Rouge2: 19.7191
- Rougel: 33.6236
- Rougelsum: 41.1683
- Gen Len: 80.1767

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step   | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:------:|:---------------:|:-------:|:------:|:-------:|:---------:|:-------:|
| 1.2949        | 1.0   | 71779  | 1.2080          | 11.7171 | 3.3284 | 11.3209 | 11.4022   | 20.0    |
| 1.191         | 2.0   | 143558 | 1.1615          | 11.8484 | 3.363  | 11.4175 | 11.5037   | 20.0    |
| 1.0907        | 3.0   | 215337 | 1.1452          | 12.6221 | 3.773  | 12.1226 | 12.2359   | 20.0    |
| 0.9798        | 4.0   | 287116 | 1.1670          | 12.4306 | 3.7329 | 11.9497 | 12.0617   | 20.0    |
| 0.9112        | 5.0   | 358895 | 1.1667          | 12.5404 | 3.7842 | 12.0541 | 12.1643   | 20.0    |
| 0.8358        | 6.0   | 430674 | 1.1997          | 12.5153 | 3.778  | 12.0382 | 12.1332   | 20.0    |


### Framework versions

- Transformers 4.10.2
- Pytorch 1.7.1+cu110
- Datasets 1.11.0
- Tokenizers 0.10.3
