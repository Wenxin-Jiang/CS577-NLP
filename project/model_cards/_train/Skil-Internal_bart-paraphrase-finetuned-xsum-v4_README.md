---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bart-paraphrase-finetuned-xsum-v4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-paraphrase-finetuned-xsum-v4

This model is a fine-tuned version of [eugenesiow/bart-paraphrase](https://huggingface.co/eugenesiow/bart-paraphrase) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1765
- Rouge1: 49.972
- Rouge2: 49.85
- Rougel: 49.9165
- Rougelsum: 49.7819
- Gen Len: 8.3061

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| No log        | 1.0   | 263  | 0.5050          | 47.9628 | 47.7085 | 47.8625 | 47.772    | 6.9639  |
| 0.676         | 2.0   | 526  | 0.5793          | 49.6085 | 49.3495 | 49.5196 | 49.4173   | 7.4715  |
| 0.676         | 3.0   | 789  | 0.7011          | 49.8635 | 49.6937 | 49.8155 | 49.6604   | 7.576   |
| 0.322         | 4.0   | 1052 | 0.7585          | 49.8851 | 49.7578 | 49.8526 | 49.6977   | 7.6654  |
| 0.322         | 5.0   | 1315 | 0.6615          | 49.861  | 49.7185 | 49.7978 | 49.6669   | 8.3023  |
| 0.2828        | 6.0   | 1578 | 0.6233          | 49.916  | 49.7819 | 49.8861 | 49.7384   | 7.6084  |
| 0.2828        | 7.0   | 1841 | 0.9380          | 49.916  | 49.7819 | 49.8861 | 49.7384   | 8.2433  |
| 0.2073        | 8.0   | 2104 | 0.8497          | 49.9624 | 49.8355 | 49.91   | 49.7666   | 7.6331  |
| 0.2073        | 9.0   | 2367 | 0.7715          | 49.972  | 49.85   | 49.9165 | 49.7819   | 7.9772  |
| 0.1744        | 10.0  | 2630 | 1.1765          | 49.972  | 49.85   | 49.9165 | 49.7819   | 8.3061  |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
