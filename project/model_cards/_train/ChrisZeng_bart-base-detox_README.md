---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: bart-base-detox
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-base-detox

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1819

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.5633        | 1.0   | 135  | 0.2524          |
| 0.2589        | 2.0   | 270  | 0.2193          |
| 0.2307        | 3.0   | 405  | 0.1993          |
| 0.2171        | 4.0   | 540  | 0.2002          |
| 0.2027        | 5.0   | 675  | 0.1937          |
| 0.1946        | 6.0   | 810  | 0.1972          |
| 0.1874        | 7.0   | 945  | 0.1917          |
| 0.1853        | 8.0   | 1080 | 0.1868          |
| 0.1811        | 9.0   | 1215 | 0.1890          |
| 0.1776        | 10.0  | 1350 | 0.1871          |
| 0.1798        | 11.0  | 1485 | 0.1858          |
| 0.1745        | 12.0  | 1620 | 0.1820          |
| 0.1689        | 13.0  | 1755 | 0.1827          |
| 0.1707        | 14.0  | 1890 | 0.1843          |
| 0.1658        | 15.0  | 2025 | 0.1834          |
| 0.1647        | 16.0  | 2160 | 0.1820          |
| 0.1645        | 17.0  | 2295 | 0.1837          |
| 0.1633        | 18.0  | 2430 | 0.1814          |
| 0.1612        | 19.0  | 2565 | 0.1815          |
| 0.1603        | 20.0  | 2700 | 0.1819          |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.12.0.dev20220429
- Datasets 2.1.0
- Tokenizers 0.10.3
