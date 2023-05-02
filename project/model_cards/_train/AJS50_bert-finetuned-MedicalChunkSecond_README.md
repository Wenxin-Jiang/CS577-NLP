---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-finetuned-MedicalChunkSecond
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-MedicalChunkSecond

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1804
- Precision: 0.2396
- Recall: 0.2613
- F1: 0.25
- Accuracy: 0.9541
- Pop Precision: 0.3889
- Pop Recall: 0.3818
- Pop F1: 0.3853
- Pop Number: 55
- Int Precision: 0.2065
- Int Recall: 0.2468
- Int F1: 0.2249
- Int Number: 77
- Out Precision: 0.1690
- Out Recall: 0.1791
- Out F1: 0.1739
- Out Number: 67
- Pop Count: 121
- Int Count: 254
- Out Count: 158

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy | Pop Precision | Pop Recall | Pop F1 | Pop Number | Int Precision | Int Recall | Int F1 | Int Number | Out Precision | Out Recall | Out F1 | Out Number | Pop Count | Int Count | Out Count |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|:-------------:|:----------:|:------:|:----------:|:-------------:|:----------:|:------:|:----------:|:-------------:|:----------:|:------:|:----------:|:---------:|:---------:|:---------:|
| No log        | 1.0   | 56   | 0.1626          | 0.0       | 0.0    | 0.0    | 0.9599   | 0.0           | 0.0        | 0.0    | 55         | 0.0           | 0.0        | 0.0    | 77         | 0.0           | 0.0        | 0.0    | 67         | 1         | 57        | 0         |
| No log        | 2.0   | 112  | 0.1420          | 0.0962    | 0.0503 | 0.0660 | 0.9575   | 0.0588        | 0.0182     | 0.0278 | 55         | 0.1084        | 0.1169     | 0.1125 | 77         | 0.0           | 0.0        | 0.0    | 67         | 24        | 193       | 4         |
| No log        | 3.0   | 168  | 0.1354          | 0.1604    | 0.1508 | 0.1554 | 0.9568   | 0.2449        | 0.2182     | 0.2308 | 55         | 0.1204        | 0.1688     | 0.1405 | 77         | 0.1667        | 0.0746     | 0.1031 | 67         | 107       | 261       | 49        |
| No log        | 4.0   | 224  | 0.1360          | 0.2701    | 0.1859 | 0.2202 | 0.9620   | 0.3478        | 0.2909     | 0.3168 | 55         | 0.1961        | 0.1299     | 0.1562 | 77         | 0.275         | 0.1642     | 0.2056 | 67         | 98        | 137       | 77        |
| No log        | 5.0   | 280  | 0.1443          | 0.2914    | 0.2563 | 0.2727 | 0.9603   | 0.4038        | 0.3818     | 0.3925 | 55         | 0.2289        | 0.2468     | 0.2375 | 77         | 0.275         | 0.1642     | 0.2056 | 67         | 121       | 199       | 85        |
| No log        | 6.0   | 336  | 0.1618          | 0.2988    | 0.2462 | 0.2700 | 0.9601   | 0.4865        | 0.3273     | 0.3913 | 55         | 0.2571        | 0.2338     | 0.2449 | 77         | 0.2281        | 0.1940     | 0.2097 | 67         | 85        | 187       | 121       |
| No log        | 7.0   | 392  | 0.1622          | 0.2417    | 0.2563 | 0.2488 | 0.9571   | 0.3333        | 0.3636     | 0.3478 | 55         | 0.2125        | 0.2208     | 0.2166 | 77         | 0.1972        | 0.2090     | 0.2029 | 67         | 126       | 213       | 142       |
| No log        | 8.0   | 448  | 0.1741          | 0.2356    | 0.2663 | 0.25   | 0.9544   | 0.3667        | 0.4        | 0.3826 | 55         | 0.1919        | 0.2468     | 0.2159 | 77         | 0.1818        | 0.1791     | 0.1805 | 67         | 132       | 258       | 147       |
| 0.1112        | 9.0   | 504  | 0.1796          | 0.2275    | 0.2663 | 0.2454 | 0.9527   | 0.3929        | 0.4        | 0.3964 | 55         | 0.1845        | 0.2468     | 0.2111 | 77         | 0.1622        | 0.1791     | 0.1702 | 67         | 129       | 278       | 158       |
| 0.1112        | 10.0  | 560  | 0.1804          | 0.2396    | 0.2613 | 0.25   | 0.9541   | 0.3889        | 0.3818     | 0.3853 | 55         | 0.2065        | 0.2468     | 0.2249 | 77         | 0.1690        | 0.1791     | 0.1739 | 67         | 121       | 254       | 158       |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
