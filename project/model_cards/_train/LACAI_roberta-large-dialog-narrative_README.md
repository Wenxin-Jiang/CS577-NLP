---
license: mit
tags:
- generated_from_trainer
model-index:
- name: output_mlm
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output_mlm

This model is a fine-tuned version of [roberta-large](https://huggingface.co/roberta-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2024

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step   | Validation Loss |
|:-------------:|:-----:|:------:|:---------------:|
| 1.5832        | 0.19  | 15000  | 1.4992          |
| 1.5325        | 0.39  | 30000  | 1.4653          |
| 1.4979        | 0.58  | 45000  | 1.4359          |
| 1.4715        | 0.77  | 60000  | 1.4039          |
| 1.4448        | 0.97  | 75000  | 1.3877          |
| 1.4191        | 1.16  | 90000  | 1.3603          |
| 1.3988        | 1.35  | 105000 | 1.3425          |
| 1.3699        | 1.54  | 120000 | 1.3230          |
| 1.3493        | 1.74  | 135000 | 1.3012          |
| 1.3201        | 1.93  | 150000 | 1.2773          |
| 1.2993        | 2.12  | 165000 | 1.2617          |
| 1.2745        | 2.32  | 180000 | 1.2490          |
| 1.2614        | 2.51  | 195000 | 1.2283          |
| 1.2424        | 2.7   | 210000 | 1.2152          |
| 1.2296        | 2.9   | 225000 | 1.2052          |


### Framework versions

- Transformers 4.11.2
- Pytorch 1.9.0
- Datasets 1.12.1
- Tokenizers 0.10.3
