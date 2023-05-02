---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice_8_0
model-index:
- name: Fine_Tunning_on_CV_Urdu_dataset
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Fine_Tunning_on_CV_Urdu_dataset

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the common_voice_8_0 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2389
- Wer: 0.7380

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
- lr_scheduler_warmup_steps: 100
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 15.2352       | 1.69  | 100  | 4.0555          | 1.0    |
| 3.3873        | 3.39  | 200  | 3.2521          | 1.0    |
| 3.2387        | 5.08  | 300  | 3.2304          | 1.0    |
| 3.1983        | 6.78  | 400  | 3.1712          | 1.0    |
| 3.1224        | 8.47  | 500  | 3.0883          | 1.0    |
| 3.0782        | 10.17 | 600  | 3.0767          | 0.9996 |
| 3.0618        | 11.86 | 700  | 3.0280          | 1.0    |
| 2.9929        | 13.56 | 800  | 2.8994          | 1.0    |
| 2.785         | 15.25 | 900  | 2.4330          | 1.0    |
| 2.1276        | 16.95 | 1000 | 1.7795          | 0.9517 |
| 1.5544        | 18.64 | 1100 | 1.5101          | 0.8266 |
| 1.2651        | 20.34 | 1200 | 1.4037          | 0.7993 |
| 1.0816        | 22.03 | 1300 | 1.3101          | 0.7638 |
| 0.9817        | 23.73 | 1400 | 1.2855          | 0.7542 |
| 0.9019        | 25.42 | 1500 | 1.2737          | 0.7421 |
| 0.8688        | 27.12 | 1600 | 1.2457          | 0.7435 |
| 0.8293        | 28.81 | 1700 | 1.2389          | 0.7380 |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
