---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-base-gec-new_data
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-gec-new_data

This model is a fine-tuned version of [t5-base](https://huggingface.co/t5-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2636
- Rouge1: 80.9191
- Rouge2: 72.1033
- Rougel: 80.7135
- Rougelsum: 80.702
- Gen Len: 17.1547

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 0.9218        | 0.2   | 50   | 0.6153          | 57.6131 | 46.0349 | 57.1409 | 57.2367   | 17.6527 |
| 0.6706        | 0.4   | 100  | 0.5047          | 71.4161 | 58.032  | 71.0641 | 71.0333   | 17.3962 |
| 0.5469        | 0.6   | 150  | 0.4484          | 74.5881 | 61.5423 | 74.311  | 74.2835   | 17.3643 |
| 0.4922        | 0.8   | 200  | 0.4105          | 76.2609 | 63.8102 | 76.0237 | 75.9821   | 17.3253 |
| 0.4641        | 1.0   | 250  | 0.3812          | 77.1152 | 65.3254 | 76.8848 | 76.8505   | 17.2954 |
| 0.4303        | 1.2   | 300  | 0.3585          | 78.0321 | 66.8786 | 77.8416 | 77.8145   | 17.2455 |
| 0.4088        | 1.39  | 350  | 0.3431          | 78.4136 | 67.5929 | 78.2166 | 78.1909   | 17.2325 |
| 0.3817        | 1.59  | 400  | 0.3299          | 78.8418 | 68.3354 | 78.6253 | 78.6123   | 17.2226 |
| 0.3898        | 1.79  | 450  | 0.3183          | 79.1565 | 68.9491 | 78.9458 | 78.9413   | 17.2246 |
| 0.3729        | 1.99  | 500  | 0.3098          | 79.4178 | 69.4412 | 79.1888 | 79.1712   | 17.2166 |
| 0.364         | 2.19  | 550  | 0.3008          | 79.6774 | 69.8938 | 79.4064 | 79.3861   | 17.1936 |
| 0.3411        | 2.39  | 600  | 0.2960          | 79.8587 | 70.2089 | 79.6081 | 79.592    | 17.2006 |
| 0.3134        | 2.59  | 650  | 0.2901          | 80.0283 | 70.589  | 79.7871 | 79.7862   | 17.1906 |
| 0.3449        | 2.79  | 700  | 0.2856          | 80.1987 | 70.8695 | 79.9722 | 79.9612   | 17.1856 |
| 0.3298        | 2.99  | 750  | 0.2801          | 80.3158 | 71.1125 | 80.0688 | 80.0581   | 17.1647 |
| 0.3235        | 3.19  | 800  | 0.2769          | 80.4603 | 71.3189 | 80.2226 | 80.1989   | 17.1557 |
| 0.3138        | 3.39  | 850  | 0.2749          | 80.4406 | 71.302  | 80.2032 | 80.1828   | 17.1587 |
| 0.3152        | 3.59  | 900  | 0.2716          | 80.5545 | 71.5128 | 80.3174 | 80.2989   | 17.1577 |
| 0.309         | 3.78  | 950  | 0.2692          | 80.5711 | 71.5881 | 80.3434 | 80.321    | 17.1577 |
| 0.3029        | 3.98  | 1000 | 0.2672          | 80.6339 | 71.691  | 80.4081 | 80.3889   | 17.1607 |
| 0.3012        | 4.18  | 1050 | 0.2662          | 80.8062 | 71.9093 | 80.5751 | 80.5748   | 17.1517 |
| 0.3034        | 4.38  | 1100 | 0.2655          | 80.8201 | 71.9581 | 80.5943 | 80.5971   | 17.1517 |
| 0.2972        | 4.58  | 1150 | 0.2644          | 80.8875 | 72.0671 | 80.6642 | 80.6618   | 17.1517 |
| 0.2978        | 4.78  | 1200 | 0.2638          | 80.9266 | 72.0925 | 80.7175 | 80.7107   | 17.1537 |
| 0.3052        | 4.98  | 1250 | 0.2636          | 80.9191 | 72.1033 | 80.7135 | 80.702    | 17.1547 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
