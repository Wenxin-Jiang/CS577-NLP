---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: Xegho.30.4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Xegho.30.4

This model is a fine-tuned version of [t5-base](https://huggingface.co/t5-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1814
- Bleu: 87.4768

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
- eval_batch_size: 4
- seed: 121
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| No log        | 1.19  | 100  | 1.2331          | 23.9598 |
| No log        | 2.38  | 200  | 0.7943          | 39.0191 |
| No log        | 3.57  | 300  | 0.5889          | 42.0816 |
| No log        | 4.76  | 400  | 0.4595          | 47.6986 |
| 1.0058        | 5.95  | 500  | 0.3801          | 49.9630 |
| 1.0058        | 7.14  | 600  | 0.3209          | 50.4290 |
| 1.0058        | 8.33  | 700  | 0.2848          | 51.1531 |
| 1.0058        | 9.52  | 800  | 0.2544          | 54.0631 |
| 1.0058        | 10.71 | 900  | 0.2338          | 56.3553 |
| 0.3559        | 11.9  | 1000 | 0.2224          | 59.7317 |
| 0.3559        | 13.1  | 1100 | 0.2110          | 62.2114 |
| 0.3559        | 14.29 | 1200 | 0.2060          | 63.4936 |
| 0.3559        | 15.48 | 1300 | 0.1994          | 63.7621 |
| 0.3559        | 16.67 | 1400 | 0.1959          | 63.3415 |
| 0.2423        | 17.86 | 1500 | 0.1932          | 63.7683 |
| 0.2423        | 19.05 | 1600 | 0.1898          | 64.2757 |
| 0.2423        | 20.24 | 1700 | 0.1901          | 64.2757 |
| 0.2423        | 21.43 | 1800 | 0.1875          | 64.1890 |
| 0.2423        | 22.62 | 1900 | 0.1852          | 63.8513 |
| 0.2051        | 23.81 | 2000 | 0.1837          | 64.4531 |
| 0.2051        | 25.0  | 2100 | 0.1829          | 64.4531 |
| 0.2051        | 26.19 | 2200 | 0.1818          | 64.6303 |
| 0.2051        | 27.38 | 2300 | 0.1817          | 64.6303 |
| 0.2051        | 28.57 | 2400 | 0.1816          | 65.0213 |
| 0.186         | 29.76 | 2500 | 0.1814          | 65.0213 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0a0+17540c5
- Datasets 2.1.0
- Tokenizers 0.12.1
