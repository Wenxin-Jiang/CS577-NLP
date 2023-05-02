---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- filipino_voice
model-index:
- name: english-filipino-wav2vec2-l-xls-r-test-02
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# english-filipino-wav2vec2-l-xls-r-test-02

This model is a fine-tuned version of [jonatasgrosman/wav2vec2-large-xlsr-53-english](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-english) on the filipino_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4561
- Wer: 0.2632

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
- num_epochs: 40
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 3.1707        | 2.09  | 400  | 0.8006          | 0.8224 |
| 0.4801        | 4.19  | 800  | 0.3363          | 0.4329 |
| 0.2541        | 6.28  | 1200 | 0.3365          | 0.3676 |
| 0.1851        | 8.38  | 1600 | 0.3485          | 0.3739 |
| 0.1408        | 10.47 | 2000 | 0.3628          | 0.3420 |
| 0.1098        | 12.57 | 2400 | 0.3979          | 0.3277 |
| 0.1019        | 14.66 | 2800 | 0.4031          | 0.2896 |
| 0.0887        | 16.75 | 3200 | 0.3977          | 0.3024 |
| 0.0798        | 18.85 | 3600 | 0.3959          | 0.3129 |
| 0.0671        | 20.94 | 4000 | 0.4489          | 0.3241 |
| 0.0633        | 23.04 | 4400 | 0.4455          | 0.3026 |
| 0.055         | 25.13 | 4800 | 0.4668          | 0.2910 |
| 0.0523        | 27.23 | 5200 | 0.4670          | 0.2960 |
| 0.0468        | 29.32 | 5600 | 0.4536          | 0.2781 |
| 0.0392        | 31.41 | 6000 | 0.4612          | 0.2860 |
| 0.0381        | 33.51 | 6400 | 0.4651          | 0.2841 |
| 0.034         | 35.6  | 6800 | 0.4723          | 0.2716 |
| 0.0315        | 37.7  | 7200 | 0.4546          | 0.2642 |
| 0.0294        | 39.79 | 7600 | 0.4561          | 0.2632 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3
