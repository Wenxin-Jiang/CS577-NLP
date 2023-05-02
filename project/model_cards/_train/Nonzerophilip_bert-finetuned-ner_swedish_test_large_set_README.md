---
tags:
- generated_from_trainer
datasets:
- suc3
model-index:
- name: bert-finetuned-ner_swedish_test_large_set
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner_swedish_test_large_set

This model is a fine-tuned version of [KBLab/bert-base-swedish-cased-ner](https://huggingface.co/KBLab/bert-base-swedish-cased-ner) on the suc3 dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.0265
- eval_precision: 0.8542
- eval_recall: 0.8468
- eval_f1: 0.8505
- eval_accuracy: 0.9919
- eval_runtime: 1076.8307
- eval_samples_per_second: 10.685
- eval_steps_per_second: 1.336
- epoch: 1.0
- step: 5754

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
- num_epochs: 3

### Framework versions

- Transformers 4.19.3
- Pytorch 1.7.1
- Datasets 2.2.2
- Tokenizers 0.12.1
