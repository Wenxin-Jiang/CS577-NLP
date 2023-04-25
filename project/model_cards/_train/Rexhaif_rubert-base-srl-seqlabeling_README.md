---
tags:
- generated_from_trainer
model-index:
- name: rubert-base-srl-seqlabeling
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# rubert-base-srl-seqlabeling

This model is a fine-tuned version of [./ruBert-base/](https://huggingface.co/./ruBert-base/) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1723
- Causator Precision: 0.8539
- Causator Recall: 0.8352
- Causator F1: 0.8444
- Causator Number: 91
- Expiriencer Precision: 0.9259
- Expiriencer Recall: 0.9740
- Expiriencer F1: 0.9494
- Expiriencer Number: 77
- Instrument Precision: 0.375
- Instrument Recall: 1.0
- Instrument F1: 0.5455
- Instrument Number: 3
- Other Precision: 0.0
- Other Recall: 0.0
- Other F1: 0.0
- Other Number: 1
- Predicate Precision: 0.9352
- Predicate Recall: 0.9902
- Predicate F1: 0.9619
- Predicate Number: 102
- Overall Precision: 0.8916
- Overall Recall: 0.9307
- Overall F1: 0.9107
- Overall Accuracy: 0.9667

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.98) and epsilon=1e-06
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 10.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Causator Precision | Causator Recall | Causator F1 | Causator Number | Expiriencer Precision | Expiriencer Recall | Expiriencer F1 | Expiriencer Number | Instrument Precision | Instrument Recall | Instrument F1 | Instrument Number | Other Precision | Other Recall | Other F1 | Other Number | Predicate Precision | Predicate Recall | Predicate F1 | Predicate Number | Overall Precision | Overall Recall | Overall F1 | Overall Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:------------------:|:---------------:|:-----------:|:---------------:|:---------------------:|:------------------:|:--------------:|:------------------:|:--------------------:|:-----------------:|:-------------:|:-----------------:|:---------------:|:------------:|:--------:|:------------:|:-------------------:|:----------------:|:------------:|:----------------:|:-----------------:|:--------------:|:----------:|:----------------:|
| 0.2552        | 1.0   | 56   | 0.3471          | 0.8841             | 0.6703          | 0.7625      | 91              | 0.8421                | 0.8312             | 0.8366         | 77                 | 0.0                  | 0.0               | 0.0           | 3                 | 0.0             | 0.0          | 0.0      | 1            | 0.9259              | 0.9804           | 0.9524       | 102              | 0.8893            | 0.8212         | 0.8539     | 0.9203           |
| 0.2385        | 2.0   | 112  | 0.1608          | 0.9103             | 0.7802          | 0.8402      | 91              | 0.9375                | 0.9740             | 0.9554         | 77                 | 0.2857               | 0.6667            | 0.4           | 3                 | 0.0             | 0.0          | 0.0      | 1            | 0.9519              | 0.9706           | 0.9612       | 102              | 0.9182            | 0.9015         | 0.9098     | 0.9554           |
| 0.0367        | 3.0   | 168  | 0.1311          | 0.8902             | 0.8022          | 0.8439      | 91              | 0.9375                | 0.9740             | 0.9554         | 77                 | 0.4286               | 1.0               | 0.6           | 3                 | 0.0             | 0.0          | 0.0      | 1            | 0.9709              | 0.9804           | 0.9756       | 102              | 0.9228            | 0.9161         | 0.9194     | 0.9673           |
| 0.0494        | 4.0   | 224  | 0.1507          | 0.7812             | 0.8242          | 0.8021      | 91              | 0.9241                | 0.9481             | 0.9359         | 77                 | 0.4286               | 1.0               | 0.6           | 3                 | 0.0             | 0.0          | 0.0      | 1            | 0.9524              | 0.9804           | 0.9662       | 102              | 0.8746            | 0.9161         | 0.8948     | 0.9637           |
| 0.0699        | 5.0   | 280  | 0.1830          | 0.8276             | 0.7912          | 0.8090      | 91              | 0.8941                | 0.9870             | 0.9383         | 77                 | 0.375                | 1.0               | 0.5455        | 3                 | 0.0             | 0.0          | 0.0      | 1            | 0.9352              | 0.9902           | 0.9619       | 102              | 0.875             | 0.9197         | 0.8968     | 0.9560           |
| 0.0352        | 6.0   | 336  | 0.1994          | 0.7857             | 0.8462          | 0.8148      | 91              | 0.9048                | 0.9870             | 0.9441         | 77                 | 0.375                | 1.0               | 0.5455        | 3                 | 0.0             | 0.0          | 0.0      | 1            | 0.9266              | 0.9902           | 0.9573       | 102              | 0.8595            | 0.9380         | 0.8970     | 0.9572           |
| 0.0186        | 7.0   | 392  | 0.1657          | 0.8652             | 0.8462          | 0.8556      | 91              | 0.9146                | 0.9740             | 0.9434         | 77                 | 0.375                | 1.0               | 0.5455        | 3                 | 0.0             | 0.0          | 0.0      | 1            | 0.9352              | 0.9902           | 0.9619       | 102              | 0.8920            | 0.9343         | 0.9127     | 0.9673           |
| 0.0052        | 8.0   | 448  | 0.1716          | 0.8556             | 0.8462          | 0.8508      | 91              | 0.9259                | 0.9740             | 0.9494         | 77                 | 0.375                | 1.0               | 0.5455        | 3                 | 0.0             | 0.0          | 0.0      | 1            | 0.9352              | 0.9902           | 0.9619       | 102              | 0.8920            | 0.9343         | 0.9127     | 0.9673           |
| 0.0094        | 9.0   | 504  | 0.1715          | 0.8444             | 0.8352          | 0.8398      | 91              | 0.9259                | 0.9740             | 0.9494         | 77                 | 0.4286               | 1.0               | 0.6           | 3                 | 0.0             | 0.0          | 0.0      | 1            | 0.9352              | 0.9902           | 0.9619       | 102              | 0.8916            | 0.9307         | 0.9107     | 0.9667           |
| 0.0078        | 10.0  | 560  | 0.1723          | 0.8539             | 0.8352          | 0.8444      | 91              | 0.9259                | 0.9740             | 0.9494         | 77                 | 0.375                | 1.0               | 0.5455        | 3                 | 0.0             | 0.0          | 0.0      | 1            | 0.9352              | 0.9902           | 0.9619       | 102              | 0.8916            | 0.9307         | 0.9107     | 0.9667           |


### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.10.0+cu102
- Datasets 1.15.1
- Tokenizers 0.10.3
