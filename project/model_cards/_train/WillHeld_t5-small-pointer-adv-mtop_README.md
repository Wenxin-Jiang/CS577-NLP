---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- mtop
model-index:
- name: t5-small-pointer-adv-mtop
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-pointer-adv-mtop

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on the mtop dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1341
- Exact Match: 0.5817

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
| 2.1628        | 1.09  | 200  | 0.7205          | 0.0022      |
| 1.1208        | 2.17  | 400  | 0.6393          | 0.0013      |
| 0.8675        | 3.26  | 600  | 0.5905          | 0.0027      |
| 1.8729        | 4.35  | 800  | 0.5726          | 0.0031      |
| 3.5417        | 5.43  | 1000 | 0.5371          | 0.0067      |
| 0.9087        | 6.52  | 1200 | 0.3512          | 0.1119      |
| 1.2224        | 7.61  | 1400 | 0.2739          | 0.1911      |
| 0.7597        | 8.69  | 1600 | 0.2151          | 0.3016      |
| 0.6981        | 9.78  | 1800 | 0.1736          | 0.3749      |
| 0.4779        | 10.87 | 2000 | 0.1548          | 0.4166      |
| 0.4397        | 11.96 | 2200 | 0.1377          | 0.4510      |
| 0.4101        | 13.04 | 2400 | 0.1480          | 0.4197      |
| 0.3323        | 14.13 | 2600 | 0.1396          | 0.4398      |
| 0.2565        | 15.22 | 2800 | 0.1351          | 0.4523      |
| 0.2108        | 16.3  | 3000 | 0.1341          | 0.4541      |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.0
- Tokenizers 0.13.2
