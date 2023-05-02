---
tags:
- generated_from_trainer
model-index:
- name: sciBERT-case-finetuned-breastcancer
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sciBERT-case-finetuned-breastcancer

This model is a fine-tuned version of [allenai/scibert_scivocab_uncased](https://huggingface.co/allenai/scibert_scivocab_uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0058

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
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 53   | 0.0126          |
| No log        | 2.0   | 106  | 0.0097          |
| No log        | 3.0   | 159  | 0.0113          |
| No log        | 4.0   | 212  | 0.0094          |
| No log        | 5.0   | 265  | 0.0080          |
| No log        | 6.0   | 318  | 0.0091          |
| No log        | 7.0   | 371  | 0.0078          |
| No log        | 8.0   | 424  | 0.0087          |
| No log        | 9.0   | 477  | 0.0077          |
| 0.0037        | 10.0  | 530  | 0.0074          |
| 0.0037        | 11.0  | 583  | 0.0072          |
| 0.0037        | 12.0  | 636  | 0.0066          |
| 0.0037        | 13.0  | 689  | 0.0069          |
| 0.0037        | 14.0  | 742  | 0.0064          |
| 0.0037        | 15.0  | 795  | 0.0063          |
| 0.0037        | 16.0  | 848  | 0.0063          |
| 0.0037        | 17.0  | 901  | 0.0058          |
| 0.0037        | 18.0  | 954  | 0.0060          |
| 0.0011        | 19.0  | 1007 | 0.0059          |
| 0.0011        | 20.0  | 1060 | 0.0058          |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
