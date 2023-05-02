---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: wav2vec2-base-intent-classification-ori-f1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-intent-classification-ori-f1

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4353
- F1: 0.875

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 45

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 2.19          | 1.0   | 28   | 2.1733          | 0.2708 |
| 2.1205        | 2.0   | 56   | 2.1125          | 0.2708 |
| 2.0965        | 3.0   | 84   | 2.0543          | 0.2708 |
| 1.9694        | 4.0   | 112  | 1.9125          | 0.2917 |
| 1.9091        | 5.0   | 140  | 1.8455          | 0.3542 |
| 1.8399        | 6.0   | 168  | 1.7895          | 0.3958 |
| 1.8424        | 7.0   | 196  | 1.8828          | 0.3125 |
| 1.5475        | 8.0   | 224  | 1.4255          | 0.5208 |
| 1.2653        | 9.0   | 252  | 1.3953          | 0.5417 |
| 1.1465        | 10.0  | 280  | 1.3501          | 0.5417 |
| 1.281         | 11.0  | 308  | 1.2800          | 0.5417 |
| 1.0996        | 12.0  | 336  | 1.2797          | 0.6042 |
| 1.1288        | 13.0  | 364  | 1.1341          | 0.6667 |
| 0.8577        | 14.0  | 392  | 1.0104          | 0.7083 |
| 0.8047        | 15.0  | 420  | 1.0906          | 0.6667 |
| 0.7098        | 16.0  | 448  | 0.9710          | 0.7917 |
| 0.5407        | 17.0  | 476  | 0.9363          | 0.7708 |
| 0.4634        | 18.0  | 504  | 0.8283          | 0.75   |
| 0.4368        | 19.0  | 532  | 0.7587          | 0.7708 |
| 0.2818        | 20.0  | 560  | 0.6551          | 0.8333 |
| 0.1951        | 21.0  | 588  | 0.5865          | 0.8333 |
| 0.1456        | 22.0  | 616  | 0.7378          | 0.7917 |
| 0.1269        | 23.0  | 644  | 0.6327          | 0.8333 |
| 0.0801        | 24.0  | 672  | 0.6896          | 0.8333 |
| 0.0723        | 25.0  | 700  | 0.7179          | 0.8333 |
| 0.0626        | 26.0  | 728  | 1.0643          | 0.7708 |
| 0.0434        | 27.0  | 756  | 0.4353          | 0.875  |
| 0.0499        | 28.0  | 784  | 0.6656          | 0.8333 |
| 0.0396        | 29.0  | 812  | 0.6788          | 0.8333 |
| 0.0352        | 30.0  | 840  | 0.8139          | 0.8333 |
| 0.0348        | 31.0  | 868  | 0.8745          | 0.8125 |
| 0.0313        | 32.0  | 896  | 0.8693          | 0.8125 |
| 0.0269        | 33.0  | 924  | 0.9393          | 0.8125 |
| 0.0242        | 34.0  | 952  | 0.9351          | 0.8333 |
| 0.0217        | 35.0  | 980  | 0.9406          | 0.8333 |
| 0.0234        | 36.0  | 1008 | 0.9464          | 0.8333 |
| 0.0219        | 37.0  | 1036 | 0.9507          | 0.8333 |
| 0.0215        | 38.0  | 1064 | 0.9471          | 0.8333 |
| 0.0206        | 39.0  | 1092 | 0.9260          | 0.8333 |
| 0.0229        | 40.0  | 1120 | 0.9420          | 0.8333 |
| 0.0216        | 41.0  | 1148 | 0.9570          | 0.8333 |
| 0.0227        | 42.0  | 1176 | 0.9573          | 0.8333 |
| 0.0208        | 43.0  | 1204 | 0.9609          | 0.8333 |
| 0.0201        | 44.0  | 1232 | 0.9617          | 0.8333 |
| 0.0208        | 45.0  | 1260 | 0.9620          | 0.8333 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
