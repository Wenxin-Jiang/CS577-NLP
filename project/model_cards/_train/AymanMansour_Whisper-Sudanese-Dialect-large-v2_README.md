---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: openai/whisper-large-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# openai/whisper-large-v2

This model is a fine-tuned version of [openai/whisper-large-v2](https://huggingface.co/openai/whisper-large-v2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9317
- Wer: 41.0267

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 8
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.5167        | 1.08  | 1000 | 0.7033          | 67.2465 |
| 0.0886        | 3.04  | 2000 | 0.7730          | 51.1880 |
| 0.0808        | 4.12  | 3000 | 0.7812          | 52.5880 |
| 0.0232        | 6.08  | 4000 | 0.8798          | 40.8570 |
| 0.001         | 8.04  | 5000 | 0.9317          | 41.0267 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
