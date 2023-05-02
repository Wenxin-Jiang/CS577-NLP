---
tags:
- generated_from_trainer
datasets:
- timit_asr
model-index:
- name: ascend_with_english
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ascend_with_english

This model is a fine-tuned version of [GleamEyeBeast/ascend](https://huggingface.co/GleamEyeBeast/ascend) on the timit_asr dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3049
- Wer: 0.2251

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

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| No log        | 1.0   | 289  | 0.3524          | 0.3016 |
| 0.4246        | 2.0   | 578  | 0.3132          | 0.2607 |
| 0.4246        | 3.0   | 867  | 0.3044          | 0.2373 |
| 0.2008        | 4.0   | 1156 | 0.3075          | 0.2302 |
| 0.2008        | 5.0   | 1445 | 0.3049          | 0.2251 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
