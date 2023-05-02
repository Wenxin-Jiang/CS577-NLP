---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-base-gec-combine_data
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-gec-combine_data

This model is a fine-tuned version of [t5-base](https://huggingface.co/t5-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5624
- Rouge1: 76.0801
- Rouge2: 65.3291
- Rougel: 75.4097
- Rougelsum: 75.4189
- Gen Len: 16.8811

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
| 0.8413        | 0.45  | 500  | 0.6549          | 74.1413 | 62.083  | 73.4159 | 73.4206   | 16.9847 |
| 0.6945        | 0.9   | 1000 | 0.6147          | 75.0476 | 63.5645 | 74.3777 | 74.3726   | 16.926  |
| 0.6551        | 1.35  | 1500 | 0.5972          | 75.3742 | 64.1326 | 74.7249 | 74.7271   | 16.9048 |
| 0.6429        | 1.81  | 2000 | 0.5853          | 75.6    | 64.4944 | 74.9325 | 74.9335   | 16.9061 |
| 0.6142        | 2.26  | 2500 | 0.5783          | 75.7553 | 64.7554 | 75.0816 | 75.09     | 16.8953 |
| 0.6116        | 2.71  | 3000 | 0.5704          | 75.8622 | 64.9522 | 75.1886 | 75.1969   | 16.8863 |
| 0.5991        | 3.16  | 3500 | 0.5681          | 75.9079 | 65.0892 | 75.2619 | 75.2666   | 16.8887 |
| 0.5933        | 3.61  | 4000 | 0.5664          | 76.0166 | 65.2437 | 75.3563 | 75.3664   | 16.8842 |
| 0.5904        | 4.06  | 4500 | 0.5645          | 76.0398 | 65.2934 | 75.3759 | 75.3875   | 16.8849 |
| 0.5962        | 4.51  | 5000 | 0.5624          | 76.0458 | 65.2794 | 75.3762 | 75.3876   | 16.882  |
| 0.5749        | 4.96  | 5500 | 0.5624          | 76.0801 | 65.3291 | 75.4097 | 75.4189   | 16.8811 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
