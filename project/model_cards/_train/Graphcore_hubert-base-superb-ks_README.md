---
license: apache-2.0
tags:
- audio-classification
- generated_from_trainer
datasets:
- superb
metrics:
- accuracy
model-index:
- name: hubert-base-superb-ks
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# hubert-base-superb-ks

This model is a fine-tuned version of [facebook/hubert-base-ls960](https://huggingface.co/facebook/hubert-base-ls960) on the superb dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0848
- Accuracy: 0.9822

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
- train_batch_size: 2
- eval_batch_size: 8
- seed: 0
- distributed_type: IPU
- gradient_accumulation_steps: 16
- total_train_batch_size: 128
- total_eval_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 5.0
- training precision: Mixed Precision

### Training results



### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cpu
- Datasets 2.1.0
- Tokenizers 0.12.1
