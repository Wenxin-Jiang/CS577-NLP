---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice_8_0
model-index:
- name: xls-r-ur-large
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xls-r-ur-large

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the common_voice_8_0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8056
- Wer: 0.4716

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 6.5282        | 3.25  | 1000 | 3.0650          | 0.9989 |
| 1.7351        | 6.49  | 2000 | 0.8798          | 0.6284 |
| 0.7662        | 9.74  | 3000 | 0.7720          | 0.5399 |
| 0.5675        | 12.99 | 4000 | 0.7661          | 0.5229 |
| 0.4591        | 16.23 | 5000 | 0.7849          | 0.5041 |
| 0.3881        | 19.48 | 6000 | 0.8065          | 0.4893 |
| 0.3522        | 22.73 | 7000 | 0.7915          | 0.4804 |
| 0.3127        | 25.97 | 8000 | 0.8119          | 0.4804 |
| 0.2932        | 29.22 | 9000 | 0.8056          | 0.4716 |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
