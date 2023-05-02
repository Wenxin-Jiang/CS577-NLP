---
license: cc-by-4.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: hing-mbert-ours-run-4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# hing-mbert-ours-run-4

This model is a fine-tuned version of [l3cube-pune/hing-mbert](https://huggingface.co/l3cube-pune/hing-mbert) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 3.0173
- Accuracy: 0.68
- Precision: 0.6330
- Recall: 0.6325
- F1: 0.6320

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
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.9781        | 1.0   | 100  | 0.8852          | 0.55     | 0.4044    | 0.5284 | 0.4211 |
| 0.7568        | 2.0   | 200  | 0.8110          | 0.655    | 0.5994    | 0.6013 | 0.5762 |
| 0.5121        | 3.0   | 300  | 0.9735          | 0.65     | 0.6145    | 0.6131 | 0.5965 |
| 0.314         | 4.0   | 400  | 1.1324          | 0.65     | 0.6305    | 0.6355 | 0.6266 |
| 0.1298        | 5.0   | 500  | 2.8247          | 0.61     | 0.5804    | 0.5087 | 0.5092 |
| 0.1013        | 6.0   | 600  | 2.8183          | 0.635    | 0.6212    | 0.5674 | 0.5667 |
| 0.0989        | 7.0   | 700  | 2.3235          | 0.635    | 0.5944    | 0.5922 | 0.5916 |
| 0.0481        | 8.0   | 800  | 2.5240          | 0.68     | 0.6334    | 0.6172 | 0.6221 |
| 0.018         | 9.0   | 900  | 2.6782          | 0.65     | 0.6123    | 0.6054 | 0.6062 |
| 0.0285        | 10.0  | 1000 | 2.3400          | 0.67     | 0.6206    | 0.6327 | 0.6189 |
| 0.014         | 11.0  | 1100 | 2.6558          | 0.66     | 0.6098    | 0.5992 | 0.6018 |
| 0.0085        | 12.0  | 1200 | 2.9366          | 0.66     | 0.6076    | 0.5961 | 0.5991 |
| 0.0106        | 13.0  | 1300 | 2.8567          | 0.665    | 0.6198    | 0.6193 | 0.6186 |
| 0.0097        | 14.0  | 1400 | 3.1526          | 0.64     | 0.6089    | 0.5975 | 0.5954 |
| 0.0022        | 15.0  | 1500 | 2.7305          | 0.69     | 0.6404    | 0.6404 | 0.6398 |
| 0.0016        | 16.0  | 1600 | 2.7670          | 0.69     | 0.6418    | 0.6434 | 0.6425 |
| 0.0017        | 17.0  | 1700 | 2.8193          | 0.7      | 0.6533    | 0.6566 | 0.6546 |
| 0.0009        | 18.0  | 1800 | 2.9959          | 0.685    | 0.6400    | 0.6389 | 0.6384 |
| 0.0006        | 19.0  | 1900 | 3.0153          | 0.68     | 0.6330    | 0.6325 | 0.6320 |
| 0.0005        | 20.0  | 2000 | 3.0173          | 0.68     | 0.6330    | 0.6325 | 0.6320 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Tokenizers 0.13.2
