---
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bert2gpt2_med_v4
  results: []
---
<img src="https://huggingface.co/Chemsseddine/bert2gpt2_med_ml_orange_summ-finetuned_med_sum_new-finetuned_med_sum_new/resolve/main/logobert2gpt2.png" alt="Map of positive probabilities per country." width="200"/>

# bert2gpt2_med_v4

This model is a fine-tuned version of [Chemsseddine/bert2gpt2_med_v3](https://huggingface.co/Chemsseddine/bert2gpt2_med_v3) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4780
- Rouge1: 36.7502
- Rouge2: 18.5992
- Rougel: 36.2566
- Rougelsum: 36.161
- Gen Len: 22.96

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| No log        | 1.0   | 169  | 1.4796          | 33.9893 | 16.2462 | 33.5685 | 33.4738   | 22.42   |
| No log        | 2.0   | 338  | 1.4404          | 34.0811 | 16.219  | 34.0206 | 33.9139   | 22.76   |
| 1.0815        | 3.0   | 507  | 1.4078          | 35.2755 | 18.2266 | 34.9186 | 34.9052   | 22.63   |
| 1.0815        | 4.0   | 676  | 1.4207          | 34.0146 | 17.4167 | 33.9904 | 33.9735   | 22.92   |
| 1.0815        | 5.0   | 845  | 1.4285          | 35.2093 | 17.3269 | 35.1023 | 35.222    | 22.75   |
| 0.4699        | 6.0   | 1014 | 1.4607          | 34.5503 | 16.9067 | 34.6404 | 34.5957   | 22.8    |
| 0.4699        | 7.0   | 1183 | 1.4469          | 35.0539 | 17.0677 | 34.7607 | 34.8734   | 22.73   |
| 0.4699        | 8.0   | 1352 | 1.4632          | 35.2308 | 17.9663 | 35.1657 | 35.1012   | 22.9    |
| 0.2522        | 9.0   | 1521 | 1.4734          | 35.5699 | 18.53   | 35.4927 | 35.3747   | 22.84   |
| 0.2522        | 10.0  | 1690 | 1.4780          | 36.7502 | 18.5992 | 36.2566 | 36.161    | 22.96   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
