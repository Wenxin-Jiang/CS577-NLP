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
- name: roberta-large-finetuned-ours-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-large-finetuned-ours-DS

This model is a fine-tuned version of [roberta-large](https://huggingface.co/roberta-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3369
- Accuracy: 0.75
- Precision: 0.7054
- Recall: 0.6949
- F1: 0.6974

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
- eval_batch_size: 16
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.0561        | 0.99  | 99   | 0.8773          | 0.615    | 0.4054    | 0.5584 | 0.4591 |
| 0.762         | 1.98  | 198  | 0.6514          | 0.715    | 0.6735    | 0.6672 | 0.6588 |
| 0.5661        | 2.97  | 297  | 0.6806          | 0.71     | 0.6764    | 0.6608 | 0.6435 |
| 0.3699        | 3.96  | 396  | 0.8358          | 0.71     | 0.6611    | 0.6691 | 0.6570 |
| 0.2184        | 4.95  | 495  | 1.1627          | 0.7      | 0.6597    | 0.6337 | 0.6414 |
| 0.1743        | 5.94  | 594  | 1.0544          | 0.725    | 0.6831    | 0.6949 | 0.6831 |
| 0.098         | 6.93  | 693  | 1.4757          | 0.73     | 0.6885    | 0.6902 | 0.6892 |
| 0.0813        | 7.92  | 792  | 1.8146          | 0.73     | 0.6840    | 0.6772 | 0.6800 |
| 0.0435        | 8.91  | 891  | 1.6697          | 0.755    | 0.7141    | 0.7127 | 0.7132 |
| 0.0209        | 9.9   | 990  | 1.8931          | 0.755    | 0.7102    | 0.7070 | 0.7082 |
| 0.0201        | 10.89 | 1089 | 2.1934          | 0.74     | 0.6971    | 0.6866 | 0.6907 |
| 0.0095        | 11.88 | 1188 | 2.1389          | 0.75     | 0.7014    | 0.6915 | 0.6932 |
| 0.0141        | 12.87 | 1287 | 2.1902          | 0.74     | 0.6942    | 0.6943 | 0.6936 |
| 0.0112        | 13.86 | 1386 | 2.5021          | 0.73     | 0.6889    | 0.6669 | 0.6741 |
| 0.0054        | 14.85 | 1485 | 2.3840          | 0.73     | 0.6819    | 0.6715 | 0.6746 |
| 0.0088        | 15.84 | 1584 | 2.3224          | 0.74     | 0.6909    | 0.6825 | 0.6787 |
| 0.003         | 16.83 | 1683 | 2.2641          | 0.75     | 0.7054    | 0.6949 | 0.6974 |
| 0.0017        | 17.82 | 1782 | 2.3361          | 0.75     | 0.7077    | 0.6968 | 0.7012 |
| 0.0014        | 18.81 | 1881 | 2.3041          | 0.755    | 0.7131    | 0.7009 | 0.7051 |
| 0.0083        | 19.8  | 1980 | 2.3369          | 0.75     | 0.7054    | 0.6949 | 0.6974 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1
