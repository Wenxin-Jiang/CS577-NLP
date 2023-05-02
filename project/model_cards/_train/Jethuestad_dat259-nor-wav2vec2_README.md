---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice_8_0
model-index:
- name: dat259-nor-wav2vec2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dat259-nor-wav2vec2

This model is a fine-tuned version of [NbAiLab/nb-wav2vec2-300m-nynorsk](https://huggingface.co/NbAiLab/nb-wav2vec2-300m-nynorsk) on the common_voice_8_0 dataset.
It achieves the following results on the evaluation set:
- Loss: 10.9446
- Wer: 1.1259

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
- lr_scheduler_warmup_steps: 5
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 84.8696       | 1.57  | 5    | 91.5942         | 1.0    |
| 62.5471       | 3.29  | 10   | 33.8515         | 1.0068 |
| 20.2215       | 4.86  | 15   | 17.4461         | 1.0017 |
| 15.2892       | 6.57  | 20   | 13.5454         | 1.0034 |
| 12.8086       | 8.29  | 25   | 12.0084         | 1.0408 |
| 11.0168       | 9.86  | 30   | 10.9446         | 1.1259 |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.10.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
