---
tags:
- generated_from_trainer
model-index:
- name: DistilBERT-POWO_Scratch
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# DistilBERT-POWO_Scratch

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.9068

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
| 7.104         | 0.18  | 200  | 5.9641          |
| 5.6973        | 0.36  | 400  | 5.5992          |
| 5.5464        | 0.54  | 600  | 5.4564          |
| 5.377         | 0.72  | 800  | 5.3606          |
| 5.2162        | 0.9   | 1000 | 5.2674          |
| 5.1499        | 1.08  | 1200 | 5.2080          |
| 5.1313        | 1.26  | 1400 | 5.1447          |
| 5.0138        | 1.44  | 1600 | 5.1041          |
| 4.9509        | 1.62  | 1800 | 5.0572          |
| 4.9598        | 1.8   | 2000 | 5.0185          |
| 4.9581        | 1.98  | 2200 | 5.0109          |
| 4.8458        | 2.16  | 2400 | 4.9608          |
| 4.953         | 2.34  | 2600 | 4.9482          |
| 4.7448        | 2.52  | 2800 | 4.9211          |
| 4.8574        | 2.71  | 3000 | 4.9093          |
| 4.8402        | 2.89  | 3200 | 4.8980          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
