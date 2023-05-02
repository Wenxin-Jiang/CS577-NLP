---
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: mbart-large-50-many-to-many-mmt-finetuned-acw-to-en
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mbart-large-50-many-to-many-mmt-finetuned-ar-to-en

This model is a fine-tuned version of [facebook/mbart-large-50-many-to-many-mmt](https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5204
- Bleu: 34.8213
- Gen Len: 33.544

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
- gradient_accumulation_steps: 4
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|
| 1.4657        | 1.0   | 816  | 1.1739          | 30.1212 | 32.868  |
| 0.8541        | 2.0   | 1632 | 1.1190          | 33.0098 | 32.808  |
| 0.6176        | 3.0   | 2448 | 1.1681          | 33.3634 | 32.756  |
| 0.3397        | 4.0   | 3264 | 1.3327          | 33.2941 | 33.6    |
| 0.2227        | 5.0   | 4080 | 1.4211          | 33.9298 | 33.128  |
| 0.1597        | 6.0   | 4896 | 1.5157          | 34.7405 | 33.496  |
| 0.1426        | 6.13  | 5000 | 1.5204          | 34.8213 | 33.544  |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
