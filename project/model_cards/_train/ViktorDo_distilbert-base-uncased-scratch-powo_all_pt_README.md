---
tags:
- generated_from_trainer
model-index:
- name: distilbert-base-uncased-scratch-powo_all_pt
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-scratch-powo_all_pt

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.7109

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 5
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 40
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 6.9629        | 0.23  | 200  | 5.9718          |
| 5.5956        | 0.45  | 400  | 5.5355          |
| 5.2972        | 0.68  | 600  | 5.3399          |
| 5.124         | 0.9   | 800  | 5.1975          |
| 5.0191        | 1.13  | 1000 | 5.1085          |
| 4.947         | 1.35  | 1200 | 5.0121          |
| 4.8239        | 1.58  | 1400 | 4.9461          |
| 4.7335        | 1.8   | 1600 | 4.8962          |
| 4.7165        | 2.03  | 1800 | 4.8210          |
| 4.6413        | 2.25  | 2000 | 4.7934          |
| 4.5922        | 2.48  | 2200 | 4.7665          |
| 4.6042        | 2.7   | 2400 | 4.7354          |
| 4.5841        | 2.93  | 2600 | 4.7370          |


### Framework versions

- Transformers 4.20.0
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
