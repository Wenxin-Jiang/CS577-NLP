---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- top_v2
model-index:
- name: t5-base-pointer-adv-top_v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-pointer-adv-top_v2

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on the top_v2 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0255
- Exact Match: 0.8472

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 64
- total_train_batch_size: 512
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 3000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Exact Match |
|:-------------:|:-----:|:----:|:---------------:|:-----------:|
| 2.2938        | 0.41  | 200  | 0.5532          | 0.0012      |
| 0.671         | 0.82  | 400  | 0.1624          | 0.1610      |
| 0.5276        | 1.23  | 600  | 0.0692          | 0.2157      |
| 0.4196        | 1.64  | 800  | 0.0491          | 0.2259      |
| 0.3593        | 2.05  | 1000 | 0.0400          | 0.2291      |
| 0.3471        | 2.46  | 1200 | 0.0335          | 0.2297      |
| 0.3416        | 2.87  | 1400 | 0.0307          | 0.2318      |
| 0.3351        | 3.29  | 1600 | 0.0307          | 0.2334      |
| 0.3316        | 3.7   | 1800 | 0.0297          | 0.2343      |
| 0.3312        | 4.11  | 2000 | 0.0282          | 0.2344      |
| 0.3271        | 4.52  | 2200 | 0.0262          | 0.2365      |
| 0.3241        | 4.93  | 2400 | 0.0263          | 0.2365      |
| 0.3227        | 5.34  | 2600 | 0.0259          | 0.2368      |
| 0.3201        | 5.75  | 2800 | 0.0257          | 0.2365      |
| 0.3227        | 6.16  | 3000 | 0.0255          | 0.2365      |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.0
- Tokenizers 0.13.2
