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
- name: roberta-large-finetuned-non-code-mixed-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-large-finetuned-non-code-mixed-DS

This model is a fine-tuned version of [roberta-large](https://huggingface.co/roberta-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 3.1265
- Accuracy: 0.6936
- Precision: 0.6794
- Recall: 0.6782
- F1: 0.6784

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
- train_batch_size: 16
- eval_batch_size: 32
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.0688        | 1.0   | 463  | 0.8847          | 0.6127   | 0.6038    | 0.6032 | 0.6014 |
| 0.8226        | 2.0   | 926  | 0.7622          | 0.6796   | 0.6769    | 0.6822 | 0.6716 |
| 0.6844        | 2.99  | 1389 | 0.8391          | 0.6828   | 0.6718    | 0.6563 | 0.6602 |
| 0.536         | 3.99  | 1852 | 0.8218          | 0.6990   | 0.6950    | 0.6807 | 0.6844 |
| 0.3938        | 4.99  | 2315 | 0.9616          | 0.6958   | 0.6967    | 0.7056 | 0.6880 |
| 0.2674        | 5.99  | 2778 | 1.1389          | 0.7033   | 0.6868    | 0.6895 | 0.6879 |
| 0.2073        | 6.98  | 3241 | 1.5578          | 0.6915   | 0.6786    | 0.6807 | 0.6792 |
| 0.1641        | 7.98  | 3704 | 1.9538          | 0.6850   | 0.6734    | 0.6715 | 0.6717 |
| 0.1394        | 8.98  | 4167 | 2.3230          | 0.6893   | 0.6733    | 0.6742 | 0.6736 |
| 0.1248        | 9.98  | 4630 | 2.4050          | 0.6936   | 0.6824    | 0.6819 | 0.6815 |
| 0.1002        | 10.98 | 5093 | 2.4227          | 0.6947   | 0.6832    | 0.6932 | 0.6795 |
| 0.0776        | 11.97 | 5556 | 2.5782          | 0.7012   | 0.6876    | 0.6923 | 0.6887 |
| 0.0685        | 12.97 | 6019 | 2.7967          | 0.6915   | 0.6836    | 0.6930 | 0.6820 |
| 0.045         | 13.97 | 6482 | 2.8884          | 0.7044   | 0.6873    | 0.6855 | 0.6863 |
| 0.0462        | 14.97 | 6945 | 2.9528          | 0.6947   | 0.6754    | 0.6749 | 0.6751 |
| 0.0444        | 15.97 | 7408 | 3.0356          | 0.6904   | 0.6778    | 0.6805 | 0.6778 |
| 0.0343        | 16.96 | 7871 | 3.0123          | 0.6936   | 0.6784    | 0.6762 | 0.6771 |
| 0.0245        | 17.96 | 8334 | 3.0160          | 0.6893   | 0.6720    | 0.6735 | 0.6727 |
| 0.0198        | 18.96 | 8797 | 3.1597          | 0.6904   | 0.6741    | 0.6727 | 0.6732 |
| 0.0189        | 19.96 | 9260 | 3.1265          | 0.6936   | 0.6794    | 0.6782 | 0.6784 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1
