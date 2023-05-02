---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: wav2vec2-conformer-rel-pos-large-960h-ft-intent-classification-ori
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-conformer-rel-pos-large-960h-ft-intent-classification-ori

This model is a fine-tuned version of [facebook/wav2vec2-conformer-rel-pos-large-960h-ft](https://huggingface.co/facebook/wav2vec2-conformer-rel-pos-large-960h-ft) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2518
- Accuracy: 0.5833

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
| 2.2018        | 1.0   | 28   | 2.1963          | 0.125    |
| 2.1871        | 2.0   | 56   | 2.1715          | 0.3333   |
| 2.1499        | 3.0   | 84   | 2.1349          | 0.3333   |
| 2.1236        | 4.0   | 112  | 2.0749          | 0.3333   |
| 2.0814        | 5.0   | 140  | 2.0232          | 0.3333   |
| 2.0905        | 6.0   | 168  | 1.9028          | 0.375    |
| 1.9167        | 7.0   | 196  | 1.8469          | 0.3958   |
| 1.7048        | 8.0   | 224  | 1.6481          | 0.4583   |
| 1.4723        | 9.0   | 252  | 1.5350          | 0.4583   |
| 1.5265        | 10.0  | 280  | 1.4526          | 0.5      |
| 1.2621        | 11.0  | 308  | 1.4451          | 0.4583   |
| 1.5083        | 12.0  | 336  | 1.3296          | 0.4792   |
| 1.1857        | 13.0  | 364  | 1.2983          | 0.4792   |
| 1.3449        | 14.0  | 392  | 1.3026          | 0.4792   |
| 1.2061        | 15.0  | 420  | 1.3181          | 0.4792   |
| 1.2544        | 16.0  | 448  | 1.2603          | 0.4792   |
| 1.0731        | 17.0  | 476  | 1.2607          | 0.4792   |
| 0.8836        | 18.0  | 504  | 1.2644          | 0.4792   |
| 1.0917        | 19.0  | 532  | 1.2345          | 0.4792   |
| 1.0786        | 20.0  | 560  | 1.2791          | 0.4792   |
| 1.1616        | 21.0  | 588  | 1.2238          | 0.4792   |
| 1.0614        | 22.0  | 616  | 1.2305          | 0.4583   |
| 0.9617        | 23.0  | 644  | 1.2315          | 0.4792   |
| 0.9652        | 24.0  | 672  | 1.2931          | 0.4792   |
| 0.9042        | 25.0  | 700  | 1.1246          | 0.5      |
| 1.0865        | 26.0  | 728  | 1.1490          | 0.4792   |
| 0.9653        | 27.0  | 756  | 1.1713          | 0.5      |
| 0.858         | 28.0  | 784  | 1.1726          | 0.5208   |
| 0.8364        | 29.0  | 812  | 1.2142          | 0.5      |
| 0.6798        | 30.0  | 840  | 1.2163          | 0.5208   |
| 0.9284        | 31.0  | 868  | 1.1398          | 0.4792   |
| 0.7383        | 32.0  | 896  | 1.2418          | 0.5208   |
| 0.651         | 33.0  | 924  | 1.1734          | 0.5      |
| 0.7416        | 34.0  | 952  | 1.2285          | 0.5      |
| 0.6287        | 35.0  | 980  | 1.1467          | 0.5833   |
| 0.6806        | 36.0  | 1008 | 1.1589          | 0.5625   |
| 0.6148        | 37.0  | 1036 | 1.1373          | 0.5833   |
| 0.7174        | 38.0  | 1064 | 1.2118          | 0.5625   |
| 0.6056        | 39.0  | 1092 | 1.2205          | 0.5833   |
| 0.7041        | 40.0  | 1120 | 1.2408          | 0.5833   |
| 0.631         | 41.0  | 1148 | 1.2350          | 0.5833   |
| 0.6028        | 42.0  | 1176 | 1.2787          | 0.5833   |
| 0.5942        | 43.0  | 1204 | 1.2463          | 0.5833   |
| 0.5441        | 44.0  | 1232 | 1.2496          | 0.5833   |
| 0.5042        | 45.0  | 1260 | 1.2518          | 0.5833   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
