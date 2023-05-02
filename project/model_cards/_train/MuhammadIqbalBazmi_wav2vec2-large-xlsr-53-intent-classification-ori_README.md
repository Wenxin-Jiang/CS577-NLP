---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: wav2vec2-large-xlsr-53-intent-classification-ori
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xlsr-53-intent-classification-ori

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7682
- Accuracy: 0.4167

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
| 2.2017        | 1.0   | 14   | 2.2113          | 0.1042   |
| 2.2013        | 2.0   | 28   | 2.2078          | 0.0625   |
| 2.197         | 3.0   | 42   | 2.1981          | 0.0625   |
| 2.1917        | 4.0   | 56   | 2.1760          | 0.3125   |
| 2.1759        | 5.0   | 70   | 2.1534          | 0.3333   |
| 2.1713        | 6.0   | 84   | 2.1305          | 0.3333   |
| 2.1431        | 7.0   | 98   | 2.1044          | 0.3333   |
| 2.1366        | 8.0   | 112  | 2.0838          | 0.3333   |
| 2.1482        | 9.0   | 126  | 2.0649          | 0.3333   |
| 2.1074        | 10.0  | 140  | 2.0532          | 0.3333   |
| 2.1066        | 11.0  | 154  | 2.0506          | 0.3333   |
| 2.089         | 12.0  | 168  | 2.0624          | 0.3333   |
| 2.0625        | 13.0  | 182  | 2.0580          | 0.3333   |
| 2.1106        | 14.0  | 196  | 2.0419          | 0.3333   |
| 2.0714        | 15.0  | 210  | 2.0350          | 0.3333   |
| 2.0256        | 16.0  | 224  | 2.0333          | 0.3333   |
| 2.1226        | 17.0  | 238  | 2.0286          | 0.3333   |
| 2.0451        | 18.0  | 252  | 2.0195          | 0.3333   |
| 2.0822        | 19.0  | 266  | 1.9968          | 0.3333   |
| 2.0991        | 20.0  | 280  | 1.9883          | 0.3333   |
| 2.0537        | 21.0  | 294  | 1.9767          | 0.3333   |
| 1.973         | 22.0  | 308  | 1.9524          | 0.3333   |
| 2.0429        | 23.0  | 322  | 1.9432          | 0.3333   |
| 2.0091        | 24.0  | 336  | 1.9402          | 0.3333   |
| 2.0309        | 25.0  | 350  | 1.9295          | 0.3333   |
| 2.0261        | 26.0  | 364  | 1.9167          | 0.3333   |
| 2.0081        | 27.0  | 378  | 1.9083          | 0.3333   |
| 2.023         | 28.0  | 392  | 1.9013          | 0.3333   |
| 2.0           | 29.0  | 406  | 1.8623          | 0.375    |
| 1.936         | 30.0  | 420  | 1.8483          | 0.3958   |
| 1.9809        | 31.0  | 434  | 1.8344          | 0.3958   |
| 1.9645        | 32.0  | 448  | 1.8428          | 0.4167   |
| 1.9788        | 33.0  | 462  | 1.8372          | 0.3958   |
| 1.9484        | 34.0  | 476  | 1.8246          | 0.3958   |
| 1.9553        | 35.0  | 490  | 1.7941          | 0.4167   |
| 1.9321        | 36.0  | 504  | 1.7824          | 0.4167   |
| 1.9759        | 37.0  | 518  | 1.7884          | 0.3958   |
| 1.9424        | 38.0  | 532  | 1.7875          | 0.3958   |
| 1.9592        | 39.0  | 546  | 1.7901          | 0.3958   |
| 1.9425        | 40.0  | 560  | 1.7812          | 0.3958   |
| 1.8899        | 41.0  | 574  | 1.7736          | 0.3958   |
| 1.9361        | 42.0  | 588  | 1.7711          | 0.4167   |
| 1.9023        | 43.0  | 602  | 1.7711          | 0.4167   |
| 1.9203        | 44.0  | 616  | 1.7688          | 0.4167   |
| 1.8921        | 45.0  | 630  | 1.7682          | 0.4167   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
