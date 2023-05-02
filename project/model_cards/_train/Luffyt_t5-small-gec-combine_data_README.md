---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-small-gec-combine_data
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-gec-combine_data

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7615
- Rouge1: 73.8239
- Rouge2: 61.2831
- Rougel: 73.1307
- Rougelsum: 73.115
- Gen Len: 17.0115

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
| 1.0791        | 0.45  | 500  | 0.8889          | 69.9014 | 56.7405 | 69.0756 | 69.0665   | 17.0912 |
| 0.9384        | 0.9   | 1000 | 0.8330          | 72.6531 | 59.6086 | 71.9311 | 71.9097   | 17.039  |
| 0.8906        | 1.35  | 1500 | 0.8059          | 73.2731 | 60.3578 | 72.5712 | 72.5505   | 17.0334 |
| 0.8764        | 1.81  | 2000 | 0.7895          | 73.552  | 60.7708 | 72.8445 | 72.8303   | 17.0228 |
| 0.852         | 2.26  | 2500 | 0.7821          | 73.6316 | 60.9269 | 72.9263 | 72.9124   | 17.0172 |
| 0.852         | 2.71  | 3000 | 0.7731          | 73.7115 | 61.0532 | 72.9932 | 72.9805   | 17.0144 |
| 0.8327        | 3.16  | 3500 | 0.7700          | 73.7518 | 61.1167 | 73.0386 | 73.0282   | 17.0169 |
| 0.8334        | 3.61  | 4000 | 0.7669          | 73.7976 | 61.2103 | 73.0951 | 73.0796   | 17.0142 |
| 0.8262        | 4.06  | 4500 | 0.7640          | 73.8157 | 61.2515 | 73.1183 | 73.1043   | 17.0126 |
| 0.8348        | 4.51  | 5000 | 0.7622          | 73.8202 | 61.2773 | 73.1264 | 73.1103   | 17.0111 |
| 0.8147        | 4.96  | 5500 | 0.7615          | 73.8239 | 61.2831 | 73.1307 | 73.115    | 17.0115 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
