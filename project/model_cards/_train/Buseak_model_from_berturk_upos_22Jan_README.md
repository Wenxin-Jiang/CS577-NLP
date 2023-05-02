---
license: mit
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: model_from_berturk_upos_22Jan
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# model_from_berturk_upos_22Jan

This model is a fine-tuned version of [dbmdz/bert-base-turkish-cased](https://huggingface.co/dbmdz/bert-base-turkish-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0130
- Precision: 0.9961
- Recall: 0.9953
- F1: 0.9957
- Accuracy: 0.9967

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 170  | 0.2285          | 0.9100    | 0.9079 | 0.9089 | 0.9352   |
| No log        | 2.0   | 340  | 0.1694          | 0.9303    | 0.9316 | 0.9310 | 0.9510   |
| 0.3728        | 3.0   | 510  | 0.1396          | 0.9420    | 0.9420 | 0.9420 | 0.9589   |
| 0.3728        | 4.0   | 680  | 0.1114          | 0.9561    | 0.9547 | 0.9554 | 0.9681   |
| 0.3728        | 5.0   | 850  | 0.0880          | 0.9657    | 0.9653 | 0.9655 | 0.9754   |
| 0.1318        | 6.0   | 1020 | 0.0670          | 0.9752    | 0.9730 | 0.9741 | 0.9814   |
| 0.1318        | 7.0   | 1190 | 0.0535          | 0.9801    | 0.9790 | 0.9795 | 0.9850   |
| 0.1318        | 8.0   | 1360 | 0.0407          | 0.9867    | 0.9842 | 0.9854 | 0.9894   |
| 0.0764        | 9.0   | 1530 | 0.0312          | 0.9902    | 0.9881 | 0.9892 | 0.9920   |
| 0.0764        | 10.0  | 1700 | 0.0254          | 0.9919    | 0.9903 | 0.9911 | 0.9935   |
| 0.0764        | 11.0  | 1870 | 0.0203          | 0.9939    | 0.9925 | 0.9932 | 0.9948   |
| 0.0466        | 12.0  | 2040 | 0.0169          | 0.9949    | 0.9939 | 0.9944 | 0.9958   |
| 0.0466        | 13.0  | 2210 | 0.0148          | 0.9955    | 0.9947 | 0.9951 | 0.9961   |
| 0.0466        | 14.0  | 2380 | 0.0135          | 0.9959    | 0.9949 | 0.9954 | 0.9966   |
| 0.0329        | 15.0  | 2550 | 0.0130          | 0.9961    | 0.9953 | 0.9957 | 0.9967   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
