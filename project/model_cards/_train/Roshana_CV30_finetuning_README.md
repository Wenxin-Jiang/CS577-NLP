---
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: CV30_finetuning
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CV30_finetuning

This model is a fine-tuned version of [Roshana/CV11_finetuning1](https://huggingface.co/Roshana/CV11_finetuning1) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7956
- Wer: 0.3677
- Cer: 0.1436

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    | Cer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|
| 0.1203        | 0.86  | 400  | 0.7747          | 0.4192 | 0.1656 |
| 0.2191        | 1.72  | 800  | 0.7546          | 0.4356 | 0.1771 |
| 0.213         | 2.59  | 1200 | 0.6965          | 0.4276 | 0.1709 |
| 0.1858        | 3.45  | 1600 | 0.7189          | 0.4156 | 0.1673 |
| 0.1597        | 4.31  | 2000 | 0.7462          | 0.4031 | 0.1606 |
| 0.1398        | 5.17  | 2400 | 0.7622          | 0.3944 | 0.1584 |
| 0.1245        | 6.03  | 2800 | 0.7527          | 0.3917 | 0.1553 |
| 0.1035        | 6.9   | 3200 | 0.7347          | 0.3819 | 0.1532 |
| 0.0918        | 7.76  | 3600 | 0.7825          | 0.3786 | 0.1497 |
| 0.0767        | 8.62  | 4000 | 0.7909          | 0.3724 | 0.1444 |
| 0.0722        | 9.48  | 4400 | 0.7956          | 0.3677 | 0.1436 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
