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
- name: albert-base-ours-run-1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# albert-base-ours-run-1

This model is a fine-tuned version of [albert-base-v2](https://huggingface.co/albert-base-v2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3970
- Accuracy: 0.735
- Precision: 0.7033
- Recall: 0.6790
- F1: 0.6873

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
| 0.9719        | 1.0   | 200  | 0.8460          | 0.635    | 0.6534    | 0.5920 | 0.5547 |
| 0.7793        | 2.0   | 400  | 0.7762          | 0.675    | 0.6965    | 0.6323 | 0.5936 |
| 0.5734        | 3.0   | 600  | 0.8149          | 0.67     | 0.6200    | 0.6192 | 0.6196 |
| 0.3877        | 4.0   | 800  | 0.9555          | 0.7      | 0.6724    | 0.6482 | 0.6549 |
| 0.2426        | 5.0   | 1000 | 1.1248          | 0.695    | 0.6529    | 0.6437 | 0.6452 |
| 0.183         | 6.0   | 1200 | 1.3497          | 0.705    | 0.6717    | 0.6489 | 0.6563 |
| 0.1011        | 7.0   | 1400 | 1.6369          | 0.7      | 0.6620    | 0.6532 | 0.6560 |
| 0.0602        | 8.0   | 1600 | 1.8171          | 0.7      | 0.6763    | 0.6615 | 0.6654 |
| 0.0335        | 9.0   | 1800 | 1.9601          | 0.695    | 0.6640    | 0.6490 | 0.6545 |
| 0.0158        | 10.0  | 2000 | 2.0206          | 0.71     | 0.6802    | 0.6751 | 0.6768 |
| 0.0148        | 11.0  | 2200 | 2.0881          | 0.675    | 0.6252    | 0.6242 | 0.6232 |
| 0.0057        | 12.0  | 2400 | 2.2708          | 0.735    | 0.7146    | 0.6790 | 0.6904 |
| 0.0079        | 13.0  | 2600 | 2.2348          | 0.72     | 0.6917    | 0.6659 | 0.6746 |
| 0.0018        | 14.0  | 2800 | 2.2978          | 0.725    | 0.6968    | 0.6662 | 0.6761 |
| 0.0025        | 15.0  | 3000 | 2.3180          | 0.735    | 0.7067    | 0.6790 | 0.6883 |
| 0.0028        | 16.0  | 3200 | 2.3910          | 0.74     | 0.7153    | 0.6854 | 0.6953 |
| 0.0002        | 17.0  | 3400 | 2.3830          | 0.735    | 0.7033    | 0.6790 | 0.6873 |
| 0.0002        | 18.0  | 3600 | 2.3899          | 0.735    | 0.7033    | 0.6790 | 0.6873 |
| 0.0001        | 19.0  | 3800 | 2.3922          | 0.735    | 0.7033    | 0.6790 | 0.6873 |
| 0.0001        | 20.0  | 4000 | 2.3970          | 0.735    | 0.7033    | 0.6790 | 0.6873 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Tokenizers 0.13.2
