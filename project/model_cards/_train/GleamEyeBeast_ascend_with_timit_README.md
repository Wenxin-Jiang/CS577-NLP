---
tags:
- generated_from_trainer
model-index:
- name: ascend_with_timit
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ascend_with_timit

This model is a fine-tuned version of [GleamEyeBeast/ascend_with_timit](https://huggingface.co/GleamEyeBeast/ascend_with_timit) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8013
- Wer: 0.4781
- Cer: 0.1727

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    | Cer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|
| 2.4026        | 1.0   | 890  | 1.3419          | 0.9083 | 0.3670 |
| 1.1926        | 2.0   | 1780 | 0.9730          | 0.6491 | 0.2585 |
| 0.9104        | 3.0   | 2670 | 0.8483          | 0.5368 | 0.1963 |
| 0.7718        | 4.0   | 3560 | 0.8122          | 0.4913 | 0.1791 |
| 0.7013        | 5.0   | 4450 | 0.8013          | 0.4781 | 0.1727 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
