---
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: CV_bn_trained_on_Validation
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CV_bn_trained_on_Validation

This model is a fine-tuned version of [./content/CV_bn_trained_on_Validation/checkpoint-6000](https://huggingface.co/./content/CV_bn_trained_on_Validation/checkpoint-6000) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2181
- Wer: 0.3385

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7.5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 1.1104        | 1.25  | 2000 | 0.2535          | 0.3705 |
| 1.1069        | 2.49  | 4000 | 0.2369          | 0.3545 |
| 1.0344        | 3.74  | 6000 | 0.2181          | 0.3385 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
