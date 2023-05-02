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
- name: bert-finetuned-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0997
- Proteinmutation F1: 0.1309
- Snp F1: 0.1953
- Dnamutation F1: 0.3778
- Precision: 0.2380
- Recall: 0.2416
- F1: 0.2398
- Accuracy: 0.9703

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Proteinmutation F1 | Snp F1 | Dnamutation F1 | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:------------------:|:------:|:--------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 324  | 0.0533          | 0.0396             | 0.2830 | 0.4667         | 0.2334    | 0.3221 | 0.2707 | 0.9788   |
| 0.1072        | 2.0   | 648  | 0.0437          | 0.6065             | 0.4906 | 0.5009         | 0.4802    | 0.6348 | 0.5468 | 0.9868   |
| 0.1072        | 3.0   | 972  | 0.0592          | 0.1379             | 0.2485 | 0.2005         | 0.1639    | 0.2228 | 0.1889 | 0.9731   |
| 0.0573        | 4.0   | 1296 | 0.0722          | 0.0749             | 0.2530 | 0.4692         | 0.2705    | 0.2959 | 0.2826 | 0.9749   |
| 0.0431        | 5.0   | 1620 | 0.0766          | 0.1574             | 0.1847 | 0.2540         | 0.1766    | 0.2285 | 0.1992 | 0.9723   |
| 0.0431        | 6.0   | 1944 | 0.0805          | 0.1099             | 0.2202 | 0.2383         | 0.1657    | 0.2097 | 0.1851 | 0.9715   |
| 0.0396        | 7.0   | 2268 | 0.0886          | 0.1337             | 0.2138 | 0.4318         | 0.2683    | 0.2678 | 0.2680 | 0.9724   |
| 0.0354        | 8.0   | 2592 | 0.0927          | 0.1535             | 0.2113 | 0.3769         | 0.2505    | 0.2528 | 0.2516 | 0.9714   |
| 0.0354        | 9.0   | 2916 | 0.0978          | 0.1011             | 0.2540 | 0.3812         | 0.2495    | 0.2528 | 0.2512 | 0.9705   |
| 0.0312        | 10.0  | 3240 | 0.0997          | 0.1309             | 0.1953 | 0.3778         | 0.2380    | 0.2416 | 0.2398 | 0.9703   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.2
- Datasets 2.0.0
- Tokenizers 0.12.1
