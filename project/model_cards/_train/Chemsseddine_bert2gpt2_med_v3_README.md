---
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bert2gpt2_med_v3
  results: []
---

<img src="https://huggingface.co/Chemsseddine/bert2gpt2_med_fr/resolve/main/logobert2gpt2.png" alt="Map of positive probabilities per country." width="200"/>

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert2gpt2_med_v3

This model is a fine-tuned version of [Chemsseddine/bert2gpt2_med_v2](https://huggingface.co/Chemsseddine/bert2gpt2_med_v2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.5474
- Rouge1: 31.8871
- Rouge2: 14.4411
- Rougel: 31.6716
- Rougelsum: 31.579
- Gen Len: 22.8412

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 2.5621        | 1.0   | 900  | 1.9724          | 30.3731 | 13.8412 | 29.9606 | 29.9716   | 22.6353 |
| 1.3692        | 2.0   | 1800 | 1.9634          | 29.6409 | 13.7674 | 29.5202 | 29.5207   | 22.5059 |
| 0.8308        | 3.0   | 2700 | 2.1431          | 30.9317 | 14.5594 | 30.8021 | 30.7287   | 22.6118 |
| 0.4689        | 4.0   | 3600 | 2.2970          | 30.1132 | 14.6407 | 29.9657 | 30.0182   | 23.3235 |
| 0.2875        | 5.0   | 4500 | 2.3787          | 30.9378 | 14.7108 | 30.861  | 30.9097   | 22.7529 |
| 0.1564        | 6.0   | 5400 | 2.4137          | 30.5338 | 13.9702 | 30.1252 | 30.1975   | 23.1588 |
| 0.1007        | 7.0   | 6300 | 2.4822          | 30.872  | 14.9353 | 30.835  | 30.7694   | 23.0529 |
| 0.0783        | 8.0   | 7200 | 2.4974          | 29.9825 | 14.1702 | 29.7507 | 29.7271   | 23.1882 |
| 0.0504        | 9.0   | 8100 | 2.5175          | 31.96   | 15.0705 | 31.9669 | 31.9839   | 23.0588 |
| 0.0339        | 10.0  | 9000 | 2.5474          | 31.8871 | 14.4411 | 31.6716 | 31.579    | 22.8412 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
