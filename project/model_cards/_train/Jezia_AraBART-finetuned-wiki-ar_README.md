---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: AraBART-finetuned-wiki-ar
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# AraBART-finetuned-wiki-ar

This model is a fine-tuned version of [moussaKam/AraBART](https://huggingface.co/moussaKam/AraBART) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4030
- Rouge1: 0.9862
- Rouge2: 0.2292
- Rougel: 0.9902
- Rougelsum: 0.9847
- Gen Len: 19.3511

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|:------:|:---------:|:-------:|
| 2.8633        | 1.0   | 2556  | 2.5599          | 0.7861 | 0.1289 | 0.7656 | 0.7721    | 19.2354 |
| 2.6525        | 2.0   | 5112  | 2.4824          | 0.7315 | 0.2374 | 0.7224 | 0.7357    | 19.261  |
| 2.5068        | 3.0   | 7668  | 2.4404          | 0.7772 | 0.2114 | 0.7671 | 0.7861    | 19.3035 |
| 2.4251        | 4.0   | 10224 | 2.4269          | 0.7464 | 0.2156 | 0.745  | 0.7504    | 19.2929 |
| 2.3739        | 5.0   | 12780 | 2.4119          | 0.7642 | 0.1879 | 0.7729 | 0.7774    | 19.3573 |
| 2.275         | 6.0   | 15336 | 2.4039          | 0.9048 | 0.1952 | 0.9198 | 0.9189    | 19.37   |
| 2.2787        | 7.0   | 17892 | 2.4007          | 0.9913 | 0.2278 | 0.9951 | 1.0038    | 19.335  |
| 2.2142        | 8.0   | 20448 | 2.4073          | 0.9736 | 0.238  | 0.9697 | 0.9773    | 19.3556 |
| 2.1852        | 9.0   | 23004 | 2.4007          | 0.9825 | 0.2322 | 0.9891 | 0.9962    | 19.3213 |
| 2.1597        | 10.0  | 25560 | 2.4030          | 0.9862 | 0.2292 | 0.9902 | 0.9847    | 19.3511 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
