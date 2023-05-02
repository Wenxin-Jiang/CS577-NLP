---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-large-xlsr-53-demo-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xlsr-53-demo-colab

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4170
- Wer: 0.4282

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 15
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 6.7049        | 0.8   | 200  | 3.0234          | 0.9683 |
| 2.9496        | 1.6   | 400  | 2.9348          | 0.9683 |
| 2.6582        | 2.4   | 600  | 1.2843          | 0.9818 |
| 1.0417        | 3.2   | 800  | 0.6061          | 0.5853 |
| 0.7853        | 4.0   | 1000 | 0.5113          | 0.5013 |
| 0.681         | 4.8   | 1200 | 0.4723          | 0.4695 |
| 0.6074        | 5.6   | 1400 | 0.4528          | 0.4491 |
| 0.5539        | 6.4   | 1600 | 0.4818          | 0.4555 |
| 0.5257        | 7.2   | 1800 | 0.4439          | 0.4298 |
| 0.5038        | 8.0   | 2000 | 0.4495          | 0.4398 |
| 0.4868        | 8.8   | 2200 | 0.4467          | 0.4392 |
| 0.4727        | 9.6   | 2400 | 0.4076          | 0.4045 |
| 0.4493        | 10.4  | 2600 | 0.4559          | 0.4452 |
| 0.4452        | 11.2  | 2800 | 0.4174          | 0.4124 |
| 0.4407        | 12.0  | 3000 | 0.4188          | 0.4098 |
| 0.4385        | 12.8  | 3200 | 0.4123          | 0.4098 |
| 0.4192        | 13.6  | 3400 | 0.4090          | 0.4199 |
| 0.4061        | 14.4  | 3600 | 0.4170          | 0.4282 |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.0+cu111
- Datasets 1.17.0
- Tokenizers 0.10.3
