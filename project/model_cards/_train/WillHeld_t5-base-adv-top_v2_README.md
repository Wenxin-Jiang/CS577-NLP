---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- top_v2
model-index:
- name: t5-base-adv-top_v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-adv-top_v2

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on the top_v2 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0336
- Exact Match: 0.8540

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 64
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 3000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Exact Match |
|:-------------:|:-----:|:----:|:---------------:|:-----------:|
| 1.4252        | 0.21  | 200  | 0.3381          | 0.1505      |
| 0.4478        | 0.41  | 400  | 0.0673          | 0.3914      |
| 0.38          | 0.62  | 600  | 0.0533          | 0.4060      |
| 0.3603        | 0.82  | 800  | 0.0490          | 0.4132      |
| 0.3539        | 1.03  | 1000 | 0.0420          | 0.4186      |
| 0.3425        | 1.23  | 1200 | 0.0396          | 0.4219      |
| 0.3373        | 1.44  | 1400 | 0.0384          | 0.4233      |
| 0.3345        | 1.64  | 1600 | 0.0361          | 0.4247      |
| 0.3334        | 1.85  | 1800 | 0.0357          | 0.4255      |
| 0.33          | 2.05  | 2000 | 0.0361          | 0.4277      |
| 0.3269        | 2.26  | 2200 | 0.0349          | 0.4278      |
| 0.3262        | 2.46  | 2400 | 0.0345          | 0.4288      |
| 0.324         | 2.67  | 2600 | 0.0342          | 0.4285      |
| 0.3212        | 2.87  | 2800 | 0.0337          | 0.4295      |
| 0.3257        | 3.08  | 3000 | 0.0336          | 0.4293      |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.0
- Tokenizers 0.13.2
