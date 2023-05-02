---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: robertuito-base-cased
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# robertuito-base-cased

This model was trained from scratch on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3006
- Accuracy: 0.9738

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.2557        | 1.0   | 3611  | 0.2650          | 0.9383   |
| 0.1543        | 2.0   | 7222  | 0.1762          | 0.9632   |
| 0.0792        | 3.0   | 10833 | 0.1959          | 0.9601   |
| 0.0565        | 4.0   | 14444 | 0.2106          | 0.9670   |
| 0.0507        | 5.0   | 18055 | 0.2597          | 0.9664   |
| 0.0297        | 6.0   | 21666 | 0.2761          | 0.9688   |
| 0.0531        | 7.0   | 25277 | 0.2336          | 0.9514   |
| 0.166         | 8.0   | 28888 | 0.2249          | 0.9688   |
| 0.0112        | 9.0   | 32499 | 0.2416          | 0.9720   |
| 0.0129        | 10.0  | 36110 | 0.2840          | 0.9713   |
| 0.0041        | 11.0  | 39721 | 0.2673          | 0.9695   |
| 0.0023        | 12.0  | 43332 | 0.3371          | 0.9664   |
| 0.0022        | 13.0  | 46943 | 0.3109          | 0.9688   |
| 0.0023        | 14.0  | 50554 | 0.2464          | 0.9757   |
| 0.0042        | 15.0  | 54165 | 0.3368          | 0.9688   |
| 0.001         | 16.0  | 57776 | 0.2903          | 0.9726   |
| 0.001         | 17.0  | 61387 | 0.3165          | 0.9707   |
| 0.0006        | 18.0  | 64998 | 0.2619          | 0.9769   |
| 0.0           | 19.0  | 68609 | 0.3053          | 0.9732   |
| 0.0           | 20.0  | 72220 | 0.3001          | 0.9745   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
