---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice_1_0
model-index:
- name: dat259-cv_en-wav2vec2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dat259-cv_en-wav2vec2

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the common_voice_1_0 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4286
- Wer: 0.5339

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
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 200
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 4.383         | 1.32  | 200  | 3.0312          | 1.0    |
| 2.7346        | 2.63  | 400  | 2.0207          | 0.9413 |
| 0.8772        | 3.95  | 600  | 1.3528          | 0.6911 |
| 0.4718        | 5.26  | 800  | 1.1830          | 0.6135 |
| 0.3209        | 6.58  | 1000 | 1.2242          | 0.5856 |
| 0.2556        | 7.89  | 1200 | 1.3165          | 0.5894 |
| 0.2055        | 9.21  | 1400 | 1.3716          | 0.5708 |
| 0.18          | 10.53 | 1600 | 1.2709          | 0.5702 |
| 0.1497        | 11.84 | 1800 | 1.4300          | 0.5526 |
| 0.126         | 13.16 | 2000 | 1.3852          | 0.5507 |
| 0.1145        | 14.47 | 2200 | 1.3893          | 0.5489 |
| 0.101         | 15.79 | 2400 | 1.4051          | 0.5431 |
| 0.091         | 17.11 | 2600 | 1.4103          | 0.5399 |
| 0.0793        | 18.42 | 2800 | 1.3968          | 0.5324 |
| 0.0746        | 19.74 | 3000 | 1.4286          | 0.5339 |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1+cu102
- Datasets 2.4.0
- Tokenizers 0.12.1
