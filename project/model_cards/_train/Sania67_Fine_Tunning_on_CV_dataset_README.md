---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice_8_0
model-index:
- name: Fine_Tunning_on_CV_dataset
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Fine_Tunning_on_CV_dataset

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the common_voice_8_0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7892
- Wer: 0.4734

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
| 6.8618        | 3.25  | 1000 | 3.0765          | 0.9989 |
| 1.6825        | 6.49  | 2000 | 0.8932          | 0.6292 |
| 0.7813        | 9.74  | 3000 | 0.7750          | 0.5454 |
| 0.5859        | 12.99 | 4000 | 0.7413          | 0.5151 |
| 0.472         | 16.23 | 5000 | 0.7559          | 0.4952 |
| 0.404         | 19.48 | 6000 | 0.7677          | 0.4915 |
| 0.3637        | 22.73 | 7000 | 0.7788          | 0.4863 |
| 0.3238        | 25.97 | 8000 | 0.7920          | 0.4738 |
| 0.3038        | 29.22 | 9000 | 0.7892          | 0.4734 |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
