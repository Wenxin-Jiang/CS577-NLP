---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-xls-r-300m-ar-10
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xls-r-300m-ar-10

This model is a fine-tuned version of [MeshalAlamr/wav2vec2-xls-r-300m-ar-9](https://huggingface.co/MeshalAlamr/wav2vec2-xls-r-300m-ar-9) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 87.0172
- Wer: 0.2017

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
- train_batch_size: 64
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 56.409        | 4.71  | 400  | 81.8407         | 0.2151 |
| 84.2726       | 9.41  | 800  | 82.6777         | 0.2237 |
| 80.3604       | 14.12 | 1200 | 85.3856         | 0.2226 |
| 70.7446       | 18.82 | 1600 | 87.9551         | 0.2180 |
| 61.3713       | 23.53 | 2000 | 88.0419         | 0.2096 |
| 54.5011       | 28.24 | 2400 | 87.0172         | 0.2017 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0
- Datasets 1.18.4
- Tokenizers 0.11.6
