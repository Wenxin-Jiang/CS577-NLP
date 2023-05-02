---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- mtop
model-index:
- name: t5-small-adv-mtop
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-adv-mtop

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on the mtop dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1058
- Exact Match: 0.7749

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 32
- total_train_batch_size: 512
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 3000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Exact Match |
|:-------------:|:-----:|:----:|:---------------:|:-----------:|
| 2.4477        | 1.09  | 200  | 0.3427          | 0.2555      |
| 0.7447        | 2.17  | 400  | 0.1441          | 0.5123      |
| 0.4016        | 3.26  | 600  | 0.1122          | 0.5808      |
| 0.4824        | 4.35  | 800  | 0.1117          | 0.5955      |
| 0.4124        | 5.43  | 1000 | 0.1075          | 0.6089      |
| 0.4651        | 6.52  | 1200 | 0.1058          | 0.6094      |
| 0.3521        | 7.61  | 1400 | 0.1114          | 0.6139      |
| 0.3476        | 8.69  | 1600 | 0.1171          | 0.6125      |
| 0.2324        | 9.78  | 1800 | 0.1174          | 0.6161      |
| 0.2406        | 10.87 | 2000 | 0.1227          | 0.6157      |
| 0.1002        | 11.96 | 2200 | 0.1198          | 0.6170      |
| 0.0922        | 13.04 | 2400 | 0.1226          | 0.6134      |
| -0.0436       | 14.13 | 2600 | 0.1182          | 0.6183      |
| -0.1447       | 15.22 | 2800 | 0.1202          | 0.6215      |
| -0.2379       | 16.3  | 3000 | 0.1212          | 0.6206      |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.0
- Tokenizers 0.13.2
