---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-finetuned-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6370
- Precision: 0.5313
- Recall: 0.4530
- F1: 0.4891
- Accuracy: 0.9290

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

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 125  | 0.5387          | 0.2190    | 0.0552 | 0.0882 | 0.8991   |
| No log        | 2.0   | 250  | 0.4241          | 0.3430    | 0.1750 | 0.2317 | 0.9117   |
| No log        | 3.0   | 375  | 0.4721          | 0.3502    | 0.1786 | 0.2366 | 0.9088   |
| 0.1529        | 4.0   | 500  | 0.6204          | 0.4300    | 0.2320 | 0.3014 | 0.9134   |
| 0.1529        | 5.0   | 625  | 0.6479          | 0.4470    | 0.2486 | 0.3195 | 0.9104   |
| 0.1529        | 6.0   | 750  | 0.4640          | 0.4532    | 0.4015 | 0.4258 | 0.9220   |
| 0.1529        | 7.0   | 875  | 0.5170          | 0.4288    | 0.4217 | 0.4253 | 0.9224   |
| 0.0229        | 8.0   | 1000 | 0.5846          | 0.5524    | 0.4273 | 0.4818 | 0.9233   |
| 0.0229        | 9.0   | 1125 | 0.5569          | 0.4644    | 0.4328 | 0.4480 | 0.9234   |
| 0.0229        | 10.0  | 1250 | 0.5818          | 0.5502    | 0.4438 | 0.4913 | 0.9258   |
| 0.0229        | 11.0  | 1375 | 0.6183          | 0.5607    | 0.4254 | 0.4838 | 0.9231   |
| 0.0048        | 12.0  | 1500 | 0.6148          | 0.5385    | 0.4254 | 0.4753 | 0.9250   |
| 0.0048        | 13.0  | 1625 | 0.6271          | 0.4896    | 0.4328 | 0.4594 | 0.9255   |
| 0.0048        | 14.0  | 1750 | 0.6475          | 0.5668    | 0.4217 | 0.4836 | 0.9267   |
| 0.0048        | 15.0  | 1875 | 0.6428          | 0.5704    | 0.4328 | 0.4921 | 0.9282   |
| 0.0016        | 16.0  | 2000 | 0.6577          | 0.5487    | 0.4254 | 0.4793 | 0.9270   |
| 0.0016        | 17.0  | 2125 | 0.6688          | 0.5556    | 0.4144 | 0.4747 | 0.9262   |
| 0.0016        | 18.0  | 2250 | 0.6481          | 0.5434    | 0.4383 | 0.4852 | 0.9282   |
| 0.0016        | 19.0  | 2375 | 0.6432          | 0.5428    | 0.4438 | 0.4883 | 0.9289   |
| 0.0007        | 20.0  | 2500 | 0.6370          | 0.5313    | 0.4530 | 0.4891 | 0.9290   |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.8.0
- Datasets 2.6.1
- Tokenizers 0.13.1
