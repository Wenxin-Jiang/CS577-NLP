---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: wav2vec2-base-intent-classification-ori
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-intent-classification-ori

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the [intent-dataset](https://huggingface.co/datasets/MuhammadIqbalBazmi/intent-dataset) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4928
- Accuracy: 0.9167

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.1867        | 1.0   | 28   | 2.1745          | 0.2708   |
| 2.1177        | 2.0   | 56   | 2.1165          | 0.2708   |
| 2.1012        | 3.0   | 84   | 2.0553          | 0.2708   |
| 1.9851        | 4.0   | 112  | 1.9551          | 0.375    |
| 1.9092        | 5.0   | 140  | 1.9765          | 0.2917   |
| 1.6848        | 6.0   | 168  | 1.8461          | 0.2917   |
| 1.6576        | 7.0   | 196  | 1.5223          | 0.5      |
| 1.4492        | 8.0   | 224  | 1.4500          | 0.4792   |
| 1.2193        | 9.0   | 252  | 1.5349          | 0.4792   |
| 1.1149        | 10.0  | 280  | 1.2159          | 0.5833   |
| 1.0615        | 11.0  | 308  | 1.1469          | 0.6875   |
| 1.0584        | 12.0  | 336  | 1.2778          | 0.6042   |
| 0.8237        | 13.0  | 364  | 1.1774          | 0.5625   |
| 0.6699        | 14.0  | 392  | 0.9661          | 0.6875   |
| 0.7414        | 15.0  | 420  | 1.2787          | 0.5208   |
| 0.5324        | 16.0  | 448  | 0.8592          | 0.7292   |
| 0.3753        | 17.0  | 476  | 0.6860          | 0.7917   |
| 0.3274        | 18.0  | 504  | 0.6210          | 0.8333   |
| 0.3667        | 19.0  | 532  | 0.7310          | 0.75     |
| 0.2347        | 20.0  | 560  | 0.6801          | 0.7292   |
| 0.2036        | 21.0  | 588  | 0.9876          | 0.6875   |
| 0.1711        | 22.0  | 616  | 0.6323          | 0.7917   |
| 0.205         | 23.0  | 644  | 0.4414          | 0.8958   |
| 0.0892        | 24.0  | 672  | 0.4253          | 0.8958   |
| 0.0777        | 25.0  | 700  | 0.4703          | 0.8958   |
| 0.0717        | 26.0  | 728  | 0.4883          | 0.8958   |
| 0.041         | 27.0  | 756  | 0.6224          | 0.8542   |
| 0.0493        | 28.0  | 784  | 0.5839          | 0.875    |
| 0.0405        | 29.0  | 812  | 0.6454          | 0.8542   |
| 0.04          | 30.0  | 840  | 0.6102          | 0.875    |
| 0.0333        | 31.0  | 868  | 0.6080          | 0.875    |
| 0.0303        | 32.0  | 896  | 0.5539          | 0.875    |
| 0.025         | 33.0  | 924  | 0.5799          | 0.8958   |
| 0.0246        | 34.0  | 952  | 0.5766          | 0.8958   |
| 0.0209        | 35.0  | 980  | 0.5700          | 0.8958   |
| 0.0225        | 36.0  | 1008 | 0.5709          | 0.8958   |
| 0.0225        | 37.0  | 1036 | 0.5582          | 0.8958   |
| 0.0217        | 38.0  | 1064 | 0.5258          | 0.875    |
| 0.0207        | 39.0  | 1092 | 0.5058          | 0.8958   |
| 0.0234        | 40.0  | 1120 | 0.4981          | 0.8958   |
| 0.021         | 41.0  | 1148 | 0.4928          | 0.9167   |
| 0.0224        | 42.0  | 1176 | 0.4962          | 0.9167   |
| 0.0212        | 43.0  | 1204 | 0.5329          | 0.8958   |
| 0.0208        | 44.0  | 1232 | 0.5727          | 0.8958   |
| 0.0206        | 45.0  | 1260 | 0.5733          | 0.8958   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
