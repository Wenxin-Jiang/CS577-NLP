---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- filipino_voice
model-index:
- name: english-filipino-wav2vec2-l-xls-r-test-08
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# english-filipino-wav2vec2-l-xls-r-test-08

This model is a fine-tuned version of [jonatasgrosman/wav2vec2-large-xlsr-53-english](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-english) on the filipino_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5968
- Wer: 0.4255

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
| 3.3434        | 2.09  | 400  | 2.2857          | 0.9625 |
| 1.6304        | 4.19  | 800  | 1.1547          | 0.7268 |
| 0.9231        | 6.28  | 1200 | 1.0252          | 0.6186 |
| 0.6098        | 8.38  | 1600 | 0.9371          | 0.5494 |
| 0.4922        | 10.47 | 2000 | 0.7092          | 0.5478 |
| 0.3652        | 12.57 | 2400 | 0.7358          | 0.5149 |
| 0.2735        | 14.66 | 2800 | 0.6270          | 0.4646 |
| 0.2038        | 16.75 | 3200 | 0.5717          | 0.4506 |
| 0.1552        | 18.85 | 3600 | 0.5968          | 0.4255 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3
