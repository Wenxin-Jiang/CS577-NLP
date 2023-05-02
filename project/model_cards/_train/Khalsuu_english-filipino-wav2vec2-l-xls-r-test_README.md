---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- filipino_voice
model-index:
- name: english-filipino-wav2vec2-l-xls-r-test
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# english-filipino-wav2vec2-l-xls-r-test

This model is a fine-tuned version of [jonatasgrosman/wav2vec2-large-xlsr-53-english](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-english) on the filipino_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5795
- Wer: 0.3996

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 3.0751        | 2.09  | 400  | 2.4744          | 0.9804 |
| 0.7852        | 4.19  | 800  | 0.5836          | 0.5620 |
| 0.3751        | 6.28  | 1200 | 0.4873          | 0.4658 |
| 0.2578        | 8.38  | 1600 | 0.5725          | 0.5289 |
| 0.1897        | 10.47 | 2000 | 0.5342          | 0.4856 |
| 0.1394        | 12.57 | 2400 | 0.5677          | 0.4761 |
| 0.1048        | 14.66 | 2800 | 0.5708          | 0.4415 |
| 0.0848        | 16.75 | 3200 | 0.5908          | 0.4374 |
| 0.0652        | 18.85 | 3600 | 0.5795          | 0.3996 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3
