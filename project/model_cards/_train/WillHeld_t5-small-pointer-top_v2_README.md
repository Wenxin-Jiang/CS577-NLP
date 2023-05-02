---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- top_v2
model-index:
- name: t5-small-pointer-top_v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-pointer-top_v2

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on the top_v2 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0306
- Exact Match: 0.8264

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
| 1.9316        | 0.82  | 200  | 0.4566          | 0.0084      |
| 0.3713        | 1.65  | 400  | 0.1473          | 0.1230      |
| 0.1747        | 2.47  | 600  | 0.0788          | 0.1984      |
| 0.1104        | 3.29  | 800  | 0.0568          | 0.2149      |
| 0.0842        | 4.12  | 1000 | 0.0473          | 0.2217      |
| 0.0694        | 4.94  | 1200 | 0.0426          | 0.2260      |
| 0.0603        | 5.76  | 1400 | 0.0383          | 0.2279      |
| 0.0534        | 6.58  | 1600 | 0.0367          | 0.2281      |
| 0.0477        | 7.41  | 1800 | 0.0347          | 0.2301      |
| 0.0441        | 8.23  | 2000 | 0.0334          | 0.2314      |
| 0.0413        | 9.05  | 2200 | 0.0323          | 0.2315      |
| 0.0387        | 9.88  | 2400 | 0.0316          | 0.2316      |
| 0.0366        | 10.7  | 2600 | 0.0311          | 0.2324      |
| 0.0358        | 11.52 | 2800 | 0.0307          | 0.2324      |
| 0.0343        | 12.35 | 3000 | 0.0306          | 0.2327      |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu117
- Datasets 2.7.1
- Tokenizers 0.13.2
