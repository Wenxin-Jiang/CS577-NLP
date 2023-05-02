---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta-v3-large__sst2__train-16-9
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-large__sst2__train-16-9

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2598
- Accuracy: 0.7809

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.6887        | 1.0   | 7    | 0.7452          | 0.2857   |
| 0.6889        | 2.0   | 14   | 0.7988          | 0.2857   |
| 0.6501        | 3.0   | 21   | 0.8987          | 0.2857   |
| 0.4286        | 4.0   | 28   | 0.9186          | 0.4286   |
| 0.3591        | 5.0   | 35   | 0.5566          | 0.7143   |
| 0.0339        | 6.0   | 42   | 1.1130          | 0.5714   |
| 0.013         | 7.0   | 49   | 1.8296          | 0.7143   |
| 0.0041        | 8.0   | 56   | 1.7069          | 0.7143   |
| 0.0023        | 9.0   | 63   | 1.1942          | 0.7143   |
| 0.0022        | 10.0  | 70   | 0.6054          | 0.7143   |
| 0.0011        | 11.0  | 77   | 0.3872          | 0.7143   |
| 0.0006        | 12.0  | 84   | 0.3217          | 0.7143   |
| 0.0005        | 13.0  | 91   | 0.2879          | 0.8571   |
| 0.0005        | 14.0  | 98   | 0.2640          | 0.8571   |
| 0.0004        | 15.0  | 105  | 0.2531          | 0.8571   |
| 0.0003        | 16.0  | 112  | 0.2384          | 0.8571   |
| 0.0004        | 17.0  | 119  | 0.2338          | 0.8571   |
| 0.0003        | 18.0  | 126  | 0.2314          | 0.8571   |
| 0.0003        | 19.0  | 133  | 0.2276          | 0.8571   |
| 0.0003        | 20.0  | 140  | 0.2172          | 0.8571   |
| 0.0003        | 21.0  | 147  | 0.2069          | 0.8571   |
| 0.0002        | 22.0  | 154  | 0.2018          | 0.8571   |
| 0.0002        | 23.0  | 161  | 0.2005          | 0.8571   |
| 0.0002        | 24.0  | 168  | 0.1985          | 0.8571   |
| 0.0002        | 25.0  | 175  | 0.1985          | 1.0      |
| 0.0002        | 26.0  | 182  | 0.1955          | 1.0      |
| 0.0002        | 27.0  | 189  | 0.1967          | 1.0      |
| 0.0002        | 28.0  | 196  | 0.1918          | 1.0      |
| 0.0002        | 29.0  | 203  | 0.1888          | 1.0      |
| 0.0002        | 30.0  | 210  | 0.1864          | 1.0      |
| 0.0002        | 31.0  | 217  | 0.1870          | 1.0      |
| 0.0002        | 32.0  | 224  | 0.1892          | 1.0      |
| 0.0002        | 33.0  | 231  | 0.1917          | 1.0      |
| 0.0002        | 34.0  | 238  | 0.1869          | 1.0      |
| 0.0002        | 35.0  | 245  | 0.1812          | 1.0      |
| 0.0001        | 36.0  | 252  | 0.1777          | 1.0      |
| 0.0002        | 37.0  | 259  | 0.1798          | 1.0      |
| 0.0002        | 38.0  | 266  | 0.1824          | 0.8571   |
| 0.0002        | 39.0  | 273  | 0.1846          | 0.8571   |
| 0.0002        | 40.0  | 280  | 0.1839          | 0.8571   |
| 0.0001        | 41.0  | 287  | 0.1826          | 0.8571   |
| 0.0001        | 42.0  | 294  | 0.1779          | 0.8571   |
| 0.0002        | 43.0  | 301  | 0.1762          | 0.8571   |
| 0.0001        | 44.0  | 308  | 0.1742          | 1.0      |
| 0.0002        | 45.0  | 315  | 0.1708          | 1.0      |
| 0.0001        | 46.0  | 322  | 0.1702          | 1.0      |
| 0.0001        | 47.0  | 329  | 0.1699          | 1.0      |
| 0.0001        | 48.0  | 336  | 0.1695          | 1.0      |
| 0.0001        | 49.0  | 343  | 0.1683          | 1.0      |
| 0.0001        | 50.0  | 350  | 0.1681          | 1.0      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
