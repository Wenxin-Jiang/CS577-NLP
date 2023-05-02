---
license: mit
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: lfqa_covid
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# lfqa_covid

This model is a fine-tuned version of [vblagoje/bart_lfqa](https://huggingface.co/vblagoje/bart_lfqa) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1028
- Bleu: 0.0
- Gen Len: 19.8564

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:----:|:-------:|
| 1.5923        | 1.0   | 808  | 0.1028          | 0.0  | 19.8564 |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.0
- Tokenizers 0.13.2
