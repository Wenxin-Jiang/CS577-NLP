---
tags:
- generated_from_trainer
model-index:
- name: NEW_DAT_10_8wangchanberta-base-att-spm-uncased
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# NEW_DAT_10_8wangchanberta-base-att-spm-uncased

This model is a fine-tuned version of [airesearch/wangchanberta-base-att-spm-uncased](https://huggingface.co/airesearch/wangchanberta-base-att-spm-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2286

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
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 0.7307        | 1.0   | 3953  | 1.1431          |
| 0.6442        | 2.0   | 7906  | 0.5108          |
| 0.402         | 3.0   | 11859 | 0.4406          |
| 0.2948        | 4.0   | 15812 | 0.3048          |
| 0.2758        | 5.0   | 19765 | 0.3484          |
| 0.2247        | 6.0   | 23718 | 0.2783          |
| 0.1418        | 7.0   | 27671 | 0.2137          |
| 0.1301        | 8.0   | 31624 | 0.2409          |
| 0.1257        | 9.0   | 35577 | 0.2431          |
| 0.1379        | 10.0  | 39530 | 0.2286          |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.13.0+cu116
- Datasets 1.17.0
- Tokenizers 0.10.3
