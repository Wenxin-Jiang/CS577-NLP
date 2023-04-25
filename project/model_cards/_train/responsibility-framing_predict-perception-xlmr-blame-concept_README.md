---
license: mit
tags:
- generated_from_trainer
model-index:
- name: predict-perception-xlmr-blame-concept
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# predict-perception-xlmr-blame-concept

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9414
- Rmse: 0.7875
- Rmse Blame::a Un concetto astratto o un'emozione: 0.7875
- Mae: 0.6165
- Mae Blame::a Un concetto astratto o un'emozione: 0.6165
- R2: 0.2291
- R2 Blame::a Un concetto astratto o un'emozione: 0.2291
- Cos: 0.1304
- Pair: 0.0
- Rank: 0.5
- Neighbors: 0.3509
- Rsa: nan

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 20
- eval_batch_size: 8
- seed: 1996
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rmse   | Rmse Blame::a Un concetto astratto o un'emozione | Mae    | Mae Blame::a Un concetto astratto o un'emozione | R2     | R2 Blame::a Un concetto astratto o un'emozione | Cos     | Pair | Rank | Neighbors | Rsa |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------------------------------------------------:|:------:|:-----------------------------------------------:|:------:|:----------------------------------------------:|:-------:|:----:|:----:|:---------:|:---:|
| 1.0549        | 1.0   | 15   | 1.2093          | 0.8925 | 0.8925                                           | 0.6659 | 0.6659                                          | 0.0097 | 0.0097                                         | -0.3043 | 0.0  | 0.5  | 0.4013    | nan |
| 1.0085        | 2.0   | 30   | 1.2199          | 0.8964 | 0.8964                                           | 0.6494 | 0.6494                                          | 0.0010 | 0.0010                                         | -0.1304 | 0.0  | 0.5  | 0.4515    | nan |
| 1.0131        | 3.0   | 45   | 1.1798          | 0.8815 | 0.8815                                           | 0.6412 | 0.6412                                          | 0.0339 | 0.0339                                         | -0.2174 | 0.0  | 0.5  | 0.2402    | nan |
| 0.9931        | 4.0   | 60   | 1.1726          | 0.8788 | 0.8788                                           | 0.6370 | 0.6370                                          | 0.0397 | 0.0397                                         | -0.1304 | 0.0  | 0.5  | 0.2911    | nan |
| 0.9668        | 5.0   | 75   | 1.1194          | 0.8587 | 0.8587                                           | 0.5925 | 0.5925                                          | 0.0833 | 0.0833                                         | 0.2174  | 0.0  | 0.5  | 0.3303    | nan |
| 0.8759        | 6.0   | 90   | 1.0776          | 0.8425 | 0.8425                                           | 0.6265 | 0.6265                                          | 0.1175 | 0.1175                                         | 0.3043  | 0.0  | 0.5  | 0.4190    | nan |
| 0.8787        | 7.0   | 105  | 1.0513          | 0.8321 | 0.8321                                           | 0.6087 | 0.6087                                          | 0.1391 | 0.1391                                         | 0.2174  | 0.0  | 0.5  | 0.3303    | nan |
| 0.7637        | 8.0   | 120  | 1.0537          | 0.8331 | 0.8331                                           | 0.6265 | 0.6265                                          | 0.1372 | 0.1372                                         | 0.2174  | 0.0  | 0.5  | 0.3303    | nan |
| 0.6568        | 9.0   | 135  | 0.9104          | 0.7744 | 0.7744                                           | 0.5887 | 0.5887                                          | 0.2544 | 0.2544                                         | 0.3043  | 0.0  | 0.5  | 0.3680    | nan |
| 0.6354        | 10.0  | 150  | 0.9055          | 0.7723 | 0.7723                                           | 0.6222 | 0.6222                                          | 0.2585 | 0.2585                                         | 0.1304  | 0.0  | 0.5  | 0.3987    | nan |
| 0.5107        | 11.0  | 165  | 1.0173          | 0.8186 | 0.8186                                           | 0.6168 | 0.6168                                          | 0.1669 | 0.1669                                         | 0.2174  | 0.0  | 0.5  | 0.3303    | nan |
| 0.4598        | 12.0  | 180  | 0.9155          | 0.7765 | 0.7765                                           | 0.6284 | 0.6284                                          | 0.2503 | 0.2503                                         | 0.1304  | 0.0  | 0.5  | 0.3987    | nan |
| 0.3815        | 13.0  | 195  | 0.9255          | 0.7808 | 0.7808                                           | 0.6140 | 0.6140                                          | 0.2421 | 0.2421                                         | 0.1304  | 0.0  | 0.5  | 0.3987    | nan |
| 0.3303        | 14.0  | 210  | 0.8506          | 0.7485 | 0.7485                                           | 0.6076 | 0.6076                                          | 0.3035 | 0.3035                                         | 0.0435  | 0.0  | 0.5  | 0.2862    | nan |
| 0.2799        | 15.0  | 225  | 1.0272          | 0.8226 | 0.8226                                           | 0.6699 | 0.6699                                          | 0.1588 | 0.1588                                         | 0.0435  | 0.0  | 0.5  | 0.2862    | nan |
| 0.2998        | 16.0  | 240  | 0.9969          | 0.8103 | 0.8103                                           | 0.6461 | 0.6461                                          | 0.1836 | 0.1836                                         | 0.0435  | 0.0  | 0.5  | 0.2862    | nan |
| 0.3131        | 17.0  | 255  | 0.9066          | 0.7727 | 0.7727                                           | 0.5849 | 0.5849                                          | 0.2576 | 0.2576                                         | 0.2174  | 0.0  | 0.5  | 0.3303    | nan |
| 0.2234        | 18.0  | 270  | 0.8741          | 0.7588 | 0.7588                                           | 0.5953 | 0.5953                                          | 0.2842 | 0.2842                                         | 0.2174  | 0.0  | 0.5  | 0.3303    | nan |
| 0.2481        | 19.0  | 285  | 1.0022          | 0.8125 | 0.8125                                           | 0.6549 | 0.6549                                          | 0.1793 | 0.1793                                         | 0.0435  | 0.0  | 0.5  | 0.2862    | nan |
| 0.2333        | 20.0  | 300  | 0.9238          | 0.7801 | 0.7801                                           | 0.6180 | 0.6180                                          | 0.2435 | 0.2435                                         | 0.0435  | 0.0  | 0.5  | 0.2862    | nan |
| 0.2407        | 21.0  | 315  | 0.9868          | 0.8062 | 0.8062                                           | 0.6457 | 0.6457                                          | 0.1919 | 0.1919                                         | 0.0435  | 0.0  | 0.5  | 0.2862    | nan |
| 0.2122        | 22.0  | 330  | 0.9514          | 0.7916 | 0.7916                                           | 0.6204 | 0.6204                                          | 0.2209 | 0.2209                                         | 0.0435  | 0.0  | 0.5  | 0.2862    | nan |
| 0.2162        | 23.0  | 345  | 0.9227          | 0.7796 | 0.7796                                           | 0.6053 | 0.6053                                          | 0.2444 | 0.2444                                         | 0.1304  | 0.0  | 0.5  | 0.3509    | nan |
| 0.1739        | 24.0  | 360  | 0.9147          | 0.7762 | 0.7762                                           | 0.5979 | 0.5979                                          | 0.2510 | 0.2510                                         | 0.1304  | 0.0  | 0.5  | 0.3509    | nan |
| 0.2084        | 25.0  | 375  | 0.9645          | 0.7970 | 0.7970                                           | 0.6296 | 0.6296                                          | 0.2102 | 0.2102                                         | 0.0435  | 0.0  | 0.5  | 0.2862    | nan |
| 0.1702        | 26.0  | 390  | 0.9587          | 0.7946 | 0.7946                                           | 0.6279 | 0.6279                                          | 0.2149 | 0.2149                                         | 0.0435  | 0.0  | 0.5  | 0.2862    | nan |
| 0.2146        | 27.0  | 405  | 0.9519          | 0.7918 | 0.7918                                           | 0.6273 | 0.6273                                          | 0.2205 | 0.2205                                         | 0.0435  | 0.0  | 0.5  | 0.2862    | nan |
| 0.1645        | 28.0  | 420  | 0.9398          | 0.7868 | 0.7868                                           | 0.6181 | 0.6181                                          | 0.2304 | 0.2304                                         | 0.0435  | 0.0  | 0.5  | 0.2862    | nan |
| 0.2052        | 29.0  | 435  | 0.9492          | 0.7907 | 0.7907                                           | 0.6228 | 0.6228                                          | 0.2227 | 0.2227                                         | 0.0435  | 0.0  | 0.5  | 0.2862    | nan |
| 0.147         | 30.0  | 450  | 0.9414          | 0.7875 | 0.7875                                           | 0.6165 | 0.6165                                          | 0.2291 | 0.2291                                         | 0.1304  | 0.0  | 0.5  | 0.3509    | nan |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.2+cu113
- Datasets 1.18.3
- Tokenizers 0.11.0