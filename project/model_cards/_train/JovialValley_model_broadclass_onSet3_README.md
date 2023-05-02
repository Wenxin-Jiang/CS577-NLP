---
tags:
- generated_from_trainer
model-index:
- name: model_broadclass_onSet3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# model_broadclass_onSet3

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.1389
- eval_0_precision: 1.0
- eval_0_recall: 1.0
- eval_0_f1-score: 1.0
- eval_0_support: 23
- eval_1_precision: 0.9697
- eval_1_recall: 0.9697
- eval_1_f1-score: 0.9697
- eval_1_support: 33
- eval_2_precision: 1.0
- eval_2_recall: 1.0
- eval_2_f1-score: 1.0
- eval_2_support: 26
- eval_3_precision: 0.9333
- eval_3_recall: 0.9333
- eval_3_f1-score: 0.9333
- eval_3_support: 15
- eval_accuracy: 0.9794
- eval_macro avg_precision: 0.9758
- eval_macro avg_recall: 0.9758
- eval_macro avg_f1-score: 0.9758
- eval_macro avg_support: 97
- eval_weighted avg_precision: 0.9794
- eval_weighted avg_recall: 0.9794
- eval_weighted avg_f1-score: 0.9794
- eval_weighted avg_support: 97
- eval_wer: 0.1037
- eval_mtrix: [[0, 1, 2, 3], [0, 23, 0, 0, 0], [1, 0, 32, 0, 1], [2, 0, 0, 26, 0], [3, 0, 1, 0, 14]]
- eval_runtime: 5.6481
- eval_samples_per_second: 17.174
- eval_steps_per_second: 2.302
- step: 0

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
- lr_scheduler_warmup_steps: 200
- num_epochs: 80
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
