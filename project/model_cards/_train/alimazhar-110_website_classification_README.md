---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: website_classification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# website_classification

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2292
- Accuracy: 0.9504
- F1: 0.9489
- Precision: 0.9510
- Recall: 0.9504

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
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 2.404         | 1.0   | 71   | 1.7840          | 0.8865   | 0.8776 | 0.8785    | 0.8865 |
| 1.295         | 2.0   | 142  | 0.8539          | 0.8972   | 0.8871 | 0.8803    | 0.8972 |
| 0.6186        | 3.0   | 213  | 0.4818          | 0.9326   | 0.9263 | 0.9266    | 0.9326 |
| 0.3103        | 4.0   | 284  | 0.3101          | 0.9397   | 0.9343 | 0.9324    | 0.9397 |
| 0.1618        | 5.0   | 355  | 0.3001          | 0.9291   | 0.9251 | 0.9278    | 0.9291 |
| 0.0893        | 6.0   | 426  | 0.2743          | 0.9291   | 0.9251 | 0.9276    | 0.9291 |
| 0.0547        | 7.0   | 497  | 0.2605          | 0.9255   | 0.9236 | 0.9334    | 0.9255 |
| 0.028         | 8.0   | 568  | 0.2167          | 0.9397   | 0.9375 | 0.9403    | 0.9397 |
| 0.0186        | 9.0   | 639  | 0.2096          | 0.9468   | 0.9467 | 0.9499    | 0.9468 |
| 0.0134        | 10.0  | 710  | 0.2219          | 0.9362   | 0.9354 | 0.9402    | 0.9362 |
| 0.0107        | 11.0  | 781  | 0.2124          | 0.9468   | 0.9466 | 0.9507    | 0.9468 |
| 0.0087        | 12.0  | 852  | 0.2119          | 0.9504   | 0.9497 | 0.9534    | 0.9504 |
| 0.0075        | 13.0  | 923  | 0.2141          | 0.9504   | 0.9497 | 0.9534    | 0.9504 |
| 0.0066        | 14.0  | 994  | 0.2198          | 0.9433   | 0.9415 | 0.9442    | 0.9433 |
| 0.0058        | 15.0  | 1065 | 0.2188          | 0.9468   | 0.9454 | 0.9474    | 0.9468 |
| 0.0052        | 16.0  | 1136 | 0.2181          | 0.9468   | 0.9454 | 0.9474    | 0.9468 |
| 0.0047        | 17.0  | 1207 | 0.2220          | 0.9504   | 0.9489 | 0.9510    | 0.9504 |
| 0.0044        | 18.0  | 1278 | 0.2232          | 0.9504   | 0.9489 | 0.9510    | 0.9504 |
| 0.004         | 19.0  | 1349 | 0.2216          | 0.9539   | 0.9535 | 0.9565    | 0.9539 |
| 0.0037        | 20.0  | 1420 | 0.2251          | 0.9504   | 0.9489 | 0.9510    | 0.9504 |
| 0.0036        | 21.0  | 1491 | 0.2275          | 0.9468   | 0.9451 | 0.9470    | 0.9468 |
| 0.0034        | 22.0  | 1562 | 0.2264          | 0.9539   | 0.9535 | 0.9565    | 0.9539 |
| 0.0032        | 23.0  | 1633 | 0.2283          | 0.9504   | 0.9489 | 0.9510    | 0.9504 |
| 0.003         | 24.0  | 1704 | 0.2299          | 0.9504   | 0.9489 | 0.9510    | 0.9504 |
| 0.0029        | 25.0  | 1775 | 0.2282          | 0.9468   | 0.9451 | 0.9470    | 0.9468 |
| 0.0029        | 26.0  | 1846 | 0.2288          | 0.9468   | 0.9451 | 0.9470    | 0.9468 |
| 0.0028        | 27.0  | 1917 | 0.2286          | 0.9504   | 0.9489 | 0.9510    | 0.9504 |
| 0.0027        | 28.0  | 1988 | 0.2293          | 0.9504   | 0.9489 | 0.9510    | 0.9504 |
| 0.0026        | 29.0  | 2059 | 0.2291          | 0.9504   | 0.9489 | 0.9510    | 0.9504 |
| 0.0026        | 30.0  | 2130 | 0.2292          | 0.9504   | 0.9489 | 0.9510    | 0.9504 |


### Framework versions

- Transformers 4.26.0
- Pytorch 1.13.1+cu116
- Datasets 2.9.0
- Tokenizers 0.13.2
