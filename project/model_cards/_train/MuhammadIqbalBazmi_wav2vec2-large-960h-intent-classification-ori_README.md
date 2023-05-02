---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: wav2vec2-large-960h-intent-classification-ori
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-960h-intent-classification-ori

This model is a fine-tuned version of [facebook/wav2vec2-large-960h](https://huggingface.co/facebook/wav2vec2-large-960h) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6013
- Accuracy: 0.7708

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 45

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.1937        | 1.0   | 14   | 2.1715          | 0.3333   |
| 2.1764        | 2.0   | 28   | 2.1317          | 0.3333   |
| 2.1358        | 3.0   | 42   | 2.0794          | 0.3333   |
| 2.1227        | 4.0   | 56   | 2.0367          | 0.3333   |
| 2.1157        | 5.0   | 70   | 1.9845          | 0.3333   |
| 2.0776        | 6.0   | 84   | 1.9369          | 0.3333   |
| 2.0126        | 7.0   | 98   | 1.8021          | 0.375    |
| 1.88          | 8.0   | 112  | 1.6825          | 0.4167   |
| 1.8818        | 9.0   | 126  | 1.4638          | 0.5      |
| 1.7044        | 10.0  | 140  | 1.4188          | 0.5208   |
| 1.5442        | 11.0  | 154  | 1.3421          | 0.5625   |
| 1.5045        | 12.0  | 168  | 1.3971          | 0.5      |
| 1.3369        | 13.0  | 182  | 1.1602          | 0.5833   |
| 1.4017        | 14.0  | 196  | 1.3510          | 0.5417   |
| 1.2565        | 15.0  | 210  | 1.0978          | 0.5625   |
| 1.1056        | 16.0  | 224  | 1.0847          | 0.5833   |
| 1.2006        | 17.0  | 238  | 1.0262          | 0.625    |
| 0.9235        | 18.0  | 252  | 0.9532          | 0.7083   |
| 0.9528        | 19.0  | 266  | 1.0212          | 0.6042   |
| 0.8195        | 20.0  | 280  | 0.8442          | 0.7083   |
| 0.7518        | 21.0  | 294  | 0.8379          | 0.6875   |
| 0.6017        | 22.0  | 308  | 0.9422          | 0.7292   |
| 0.7697        | 23.0  | 322  | 0.7353          | 0.75     |
| 0.5367        | 24.0  | 336  | 0.8685          | 0.6875   |
| 0.5655        | 25.0  | 350  | 0.7440          | 0.7708   |
| 0.5116        | 26.0  | 364  | 0.7572          | 0.75     |
| 0.4297        | 27.0  | 378  | 0.7518          | 0.75     |
| 0.4928        | 28.0  | 392  | 0.5988          | 0.7917   |
| 0.4424        | 29.0  | 406  | 0.7240          | 0.75     |
| 0.3313        | 30.0  | 420  | 0.6173          | 0.7708   |
| 0.3854        | 31.0  | 434  | 0.7375          | 0.75     |
| 0.4131        | 32.0  | 448  | 0.7026          | 0.7708   |
| 0.2899        | 33.0  | 462  | 0.6516          | 0.7708   |
| 0.3644        | 34.0  | 476  | 0.6201          | 0.7917   |
| 0.2316        | 35.0  | 490  | 0.6111          | 0.7708   |
| 0.2589        | 36.0  | 504  | 0.5518          | 0.7917   |
| 0.3778        | 37.0  | 518  | 0.5512          | 0.7708   |
| 0.2426        | 38.0  | 532  | 0.5779          | 0.7917   |
| 0.304         | 39.0  | 546  | 0.7771          | 0.75     |
| 0.1833        | 40.0  | 560  | 0.5839          | 0.7708   |
| 0.1649        | 41.0  | 574  | 0.5699          | 0.7708   |
| 0.2529        | 42.0  | 588  | 0.6190          | 0.75     |
| 0.2121        | 43.0  | 602  | 0.5992          | 0.75     |
| 0.2736        | 44.0  | 616  | 0.6011          | 0.7917   |
| 0.2446        | 45.0  | 630  | 0.6013          | 0.7708   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
