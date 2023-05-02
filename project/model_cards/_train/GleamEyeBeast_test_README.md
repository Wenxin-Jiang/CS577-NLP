---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: test
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# test

This model is a fine-tuned version of [facebook/wav2vec2-base-960h](https://huggingface.co/facebook/wav2vec2-base-960h) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1761
- Wer: 0.2161

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
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 5.5828        | 4.0   | 500  | 3.0263          | 1.0    |
| 1.8657        | 8.0   | 1000 | 0.2213          | 0.2650 |
| 0.332         | 12.0  | 1500 | 0.2095          | 0.2413 |
| 0.2037        | 16.0  | 2000 | 0.1906          | 0.2222 |
| 0.1282        | 20.0  | 2500 | 0.1761          | 0.2161 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu111
- Datasets 1.13.3
- Tokenizers 0.10.3
