---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- mtop
model-index:
- name: t5-base-adv-mtop
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-adv-mtop

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on the mtop dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1009
- Exact Match: 0.7937

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
| 4.2521        | 1.09  | 200  | 0.1367          | 0.5418      |
| 6.2586        | 2.17  | 400  | 0.1020          | 0.6004      |
| 4.0003        | 3.26  | 600  | 0.1009          | 0.6179      |
| 2.7191        | 4.35  | 800  | 0.1066          | 0.6251      |
| 1.5031        | 5.43  | 1000 | 0.1215          | 0.6286      |
| 0.703         | 6.52  | 1200 | 0.1238          | 0.6215      |
| 0.6371        | 7.61  | 1400 | 0.1365          | 0.6286      |
| 0.3712        | 8.69  | 1600 | 0.1450          | 0.6300      |
| 0.5666        | 9.78  | 1800 | 0.1500          | 0.6295      |
| 0.5237        | 10.87 | 2000 | 0.1416          | 0.6251      |
| 0.4562        | 11.96 | 2200 | 0.1464          | 0.6313      |
| 0.3421        | 13.04 | 2400 | 0.1635          | 0.6277      |
| 0.3686        | 14.13 | 2600 | 0.1643          | 0.6322      |
| 0.218         | 15.22 | 2800 | 0.1800          | 0.6277      |
| 0.2371        | 16.3  | 3000 | 0.1742          | 0.6268      |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.0
- Tokenizers 0.13.2
