---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: run-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# run-5

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.2694
- Accuracy: 0.745
- Precision: 0.7091
- Recall: 0.7017
- F1: 0.7043

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.9558        | 1.0   | 50   | 0.8587          | 0.665    | 0.6541    | 0.6084 | 0.5787 |
| 0.7752        | 2.0   | 100  | 0.8892          | 0.655    | 0.6416    | 0.5835 | 0.5790 |
| 0.5771        | 3.0   | 150  | 0.7066          | 0.715    | 0.6884    | 0.7026 | 0.6915 |
| 0.3738        | 4.0   | 200  | 1.0130          | 0.705    | 0.6578    | 0.6409 | 0.6455 |
| 0.253         | 5.0   | 250  | 1.1405          | 0.74     | 0.7132    | 0.7018 | 0.7059 |
| 0.1604        | 6.0   | 300  | 1.1993          | 0.69     | 0.6334    | 0.6244 | 0.6261 |
| 0.1265        | 7.0   | 350  | 1.5984          | 0.705    | 0.6875    | 0.6775 | 0.6764 |
| 0.0741        | 8.0   | 400  | 1.4755          | 0.745    | 0.7116    | 0.7132 | 0.7114 |
| 0.0505        | 9.0   | 450  | 2.2514          | 0.71     | 0.6791    | 0.6427 | 0.6524 |
| 0.0372        | 10.0  | 500  | 2.2234          | 0.71     | 0.6675    | 0.6503 | 0.6488 |
| 0.0161        | 11.0  | 550  | 2.1070          | 0.72     | 0.6783    | 0.6712 | 0.6718 |
| 0.016         | 12.0  | 600  | 2.0232          | 0.72     | 0.6737    | 0.6659 | 0.6688 |
| 0.0197        | 13.0  | 650  | 2.0224          | 0.74     | 0.7065    | 0.6954 | 0.6895 |
| 0.01          | 14.0  | 700  | 2.1777          | 0.74     | 0.7023    | 0.6904 | 0.6936 |
| 0.0173        | 15.0  | 750  | 2.3227          | 0.72     | 0.6761    | 0.6590 | 0.6638 |
| 0.0066        | 16.0  | 800  | 2.2131          | 0.735    | 0.6983    | 0.6912 | 0.6923 |
| 0.0043        | 17.0  | 850  | 2.1196          | 0.76     | 0.7278    | 0.7207 | 0.7191 |
| 0.0039        | 18.0  | 900  | 2.4087          | 0.72     | 0.6791    | 0.6590 | 0.6650 |
| 0.0041        | 19.0  | 950  | 2.1487          | 0.73     | 0.6889    | 0.6860 | 0.6873 |
| 0.0024        | 20.0  | 1000 | 2.2694          | 0.745    | 0.7091    | 0.7017 | 0.7043 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Tokenizers 0.13.2
