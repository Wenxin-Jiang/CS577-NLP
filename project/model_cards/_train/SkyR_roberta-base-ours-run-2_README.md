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
- name: run-2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# run-2

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1449
- Accuracy: 0.75
- Precision: 0.7115
- Recall: 0.7093
- F1: 0.7103

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
| 0.9838        | 1.0   | 50   | 0.8621          | 0.645    | 0.6536    | 0.6130 | 0.6124 |
| 0.7134        | 2.0   | 100  | 0.8124          | 0.7      | 0.6628    | 0.6421 | 0.6483 |
| 0.4911        | 3.0   | 150  | 0.8571          | 0.7      | 0.6726    | 0.6314 | 0.6361 |
| 0.3104        | 4.0   | 200  | 0.8228          | 0.76     | 0.7298    | 0.7367 | 0.7294 |
| 0.1942        | 5.0   | 250  | 1.1132          | 0.76     | 0.7282    | 0.7031 | 0.7119 |
| 0.1409        | 6.0   | 300  | 1.2218          | 0.685    | 0.6516    | 0.6560 | 0.6524 |
| 0.0976        | 7.0   | 350  | 1.3648          | 0.715    | 0.6984    | 0.7044 | 0.6946 |
| 0.0791        | 8.0   | 400  | 1.5985          | 0.745    | 0.7183    | 0.7113 | 0.7124 |
| 0.0647        | 9.0   | 450  | 1.8884          | 0.725    | 0.6818    | 0.6761 | 0.6785 |
| 0.0275        | 10.0  | 500  | 1.8639          | 0.725    | 0.6979    | 0.7008 | 0.6958 |
| 0.0329        | 11.0  | 550  | 1.8831          | 0.72     | 0.6816    | 0.6869 | 0.6838 |
| 0.0169        | 12.0  | 600  | 2.1426          | 0.73     | 0.6864    | 0.6776 | 0.6794 |
| 0.0072        | 13.0  | 650  | 2.2483          | 0.725    | 0.7187    | 0.7054 | 0.6968 |
| 0.0203        | 14.0  | 700  | 2.2901          | 0.735    | 0.6986    | 0.6885 | 0.6921 |
| 0.0093        | 15.0  | 750  | 2.3134          | 0.725    | 0.6830    | 0.6666 | 0.6723 |
| 0.0089        | 16.0  | 800  | 2.1598          | 0.73     | 0.6919    | 0.6860 | 0.6885 |
| 0.0061        | 17.0  | 850  | 2.0879          | 0.75     | 0.7129    | 0.7132 | 0.7125 |
| 0.0024        | 18.0  | 900  | 2.1285          | 0.745    | 0.7062    | 0.7071 | 0.7049 |
| 0.0043        | 19.0  | 950  | 2.1386          | 0.74     | 0.7001    | 0.7003 | 0.6985 |
| 0.0028        | 20.0  | 1000 | 2.1449          | 0.75     | 0.7115    | 0.7093 | 0.7103 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Tokenizers 0.13.2
