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
- name: albert-base-ours-run-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# albert-base-ours-run-5

This model is a fine-tuned version of [albert-base-v2](https://huggingface.co/albert-base-v2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.6151
- Accuracy: 0.675
- Precision: 0.6356
- Recall: 0.6360
- F1: 0.6356

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
| 0.9766        | 1.0   | 200  | 0.8865          | 0.645    | 0.5935    | 0.5872 | 0.5881 |
| 0.7725        | 2.0   | 400  | 1.0650          | 0.665    | 0.7143    | 0.5936 | 0.5556 |
| 0.6018        | 3.0   | 600  | 0.8558          | 0.7      | 0.6637    | 0.6444 | 0.6456 |
| 0.3838        | 4.0   | 800  | 0.9796          | 0.67     | 0.6220    | 0.6219 | 0.6218 |
| 0.2135        | 5.0   | 1000 | 1.4533          | 0.675    | 0.6611    | 0.5955 | 0.6055 |
| 0.1209        | 6.0   | 1200 | 1.4688          | 0.67     | 0.6392    | 0.6474 | 0.6398 |
| 0.072         | 7.0   | 1400 | 1.8395          | 0.695    | 0.6574    | 0.6540 | 0.6514 |
| 0.0211        | 8.0   | 1600 | 2.0849          | 0.7      | 0.6691    | 0.6607 | 0.6603 |
| 0.0102        | 9.0   | 1800 | 2.3042          | 0.695    | 0.6675    | 0.6482 | 0.6533 |
| 0.0132        | 10.0  | 2000 | 2.2390          | 0.685    | 0.6472    | 0.6423 | 0.6439 |
| 0.004         | 11.0  | 2200 | 2.3779          | 0.68     | 0.6435    | 0.6481 | 0.6443 |
| 0.0004        | 12.0  | 2400 | 2.4575          | 0.675    | 0.6397    | 0.6352 | 0.6357 |
| 0.0003        | 13.0  | 2600 | 2.4676          | 0.675    | 0.6356    | 0.6360 | 0.6356 |
| 0.0003        | 14.0  | 2800 | 2.5109          | 0.68     | 0.6427    | 0.6424 | 0.6422 |
| 0.0002        | 15.0  | 3000 | 2.5470          | 0.675    | 0.6356    | 0.6360 | 0.6356 |
| 0.0002        | 16.0  | 3200 | 2.5674          | 0.675    | 0.6356    | 0.6360 | 0.6356 |
| 0.0001        | 17.0  | 3400 | 2.5889          | 0.685    | 0.6471    | 0.6488 | 0.6474 |
| 0.0001        | 18.0  | 3600 | 2.6016          | 0.675    | 0.6356    | 0.6360 | 0.6356 |
| 0.0001        | 19.0  | 3800 | 2.6108          | 0.675    | 0.6356    | 0.6360 | 0.6356 |
| 0.0001        | 20.0  | 4000 | 2.6151          | 0.675    | 0.6356    | 0.6360 | 0.6356 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Tokenizers 0.13.2
