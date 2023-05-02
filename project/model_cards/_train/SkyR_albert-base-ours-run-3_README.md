---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: albert-base-ours-run-3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# albert-base-ours-run-3

This model is a fine-tuned version of [albert-base-v2](https://huggingface.co/albert-base-v2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4381
- Accuracy: 0.7
- Precision: 0.6579
- Recall: 0.6558
- F1: 0.6568

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.9876        | 1.0   | 200  | 0.9367          | 0.64     | 0.6707    | 0.5623 | 0.5425 |
| 0.7553        | 2.0   | 400  | 0.7936          | 0.66     | 0.6269    | 0.6298 | 0.6105 |
| 0.556         | 3.0   | 600  | 0.9257          | 0.71     | 0.6759    | 0.6504 | 0.6563 |
| 0.3871        | 4.0   | 800  | 0.9893          | 0.63     | 0.5882    | 0.5985 | 0.5876 |
| 0.2446        | 5.0   | 1000 | 1.1867          | 0.695    | 0.6582    | 0.6563 | 0.6566 |
| 0.1502        | 6.0   | 1200 | 1.6108          | 0.71     | 0.6708    | 0.6523 | 0.6585 |
| 0.1049        | 7.0   | 1400 | 2.4882          | 0.645    | 0.6030    | 0.5597 | 0.5649 |
| 0.0764        | 8.0   | 1600 | 2.0064          | 0.715    | 0.6798    | 0.6602 | 0.6651 |
| 0.032         | 9.0   | 1800 | 2.6447          | 0.655    | 0.5913    | 0.5774 | 0.5727 |
| 0.0177        | 10.0  | 2000 | 2.2460          | 0.675    | 0.6290    | 0.6287 | 0.6287 |
| 0.0153        | 11.0  | 2200 | 2.3537          | 0.69     | 0.6524    | 0.6407 | 0.6408 |
| 0.006         | 12.0  | 2400 | 2.4205          | 0.695    | 0.6582    | 0.6448 | 0.6486 |
| 0.0045        | 13.0  | 2600 | 2.3032          | 0.68     | 0.6394    | 0.6314 | 0.6287 |
| 0.0038        | 14.0  | 2800 | 2.3506          | 0.685    | 0.6388    | 0.6370 | 0.6367 |
| 0.0034        | 15.0  | 3000 | 2.3750          | 0.7      | 0.6590    | 0.6558 | 0.6573 |
| 0.0019        | 16.0  | 3200 | 2.4289          | 0.72     | 0.6819    | 0.6723 | 0.6763 |
| 0.0016        | 17.0  | 3400 | 2.4470          | 0.725    | 0.6892    | 0.6788 | 0.6830 |
| 0.0002        | 18.0  | 3600 | 2.4374          | 0.71     | 0.6700    | 0.6626 | 0.6657 |
| 0.0002        | 19.0  | 3800 | 2.4353          | 0.7      | 0.6579    | 0.6558 | 0.6568 |
| 0.0002        | 20.0  | 4000 | 2.4381          | 0.7      | 0.6579    | 0.6558 | 0.6568 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Tokenizers 0.13.2
