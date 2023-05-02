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
- name: xlm-roberta-large-finetuned-TRAC-DS-new
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-large-finetuned-TRAC-DS-new

This model is a fine-tuned version of [xlm-roberta-large](https://huggingface.co/xlm-roberta-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2229
- Accuracy: 0.6724
- Precision: 0.6503
- Recall: 0.6556
- F1: 0.6513

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
- train_batch_size: 4
- eval_batch_size: 8
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.0895        | 0.25  | 612   | 1.0893          | 0.4453   | 0.3220    | 0.4654 | 0.3554 |
| 1.0788        | 0.5   | 1224  | 1.1051          | 0.4436   | 0.1479    | 0.3333 | 0.2049 |
| 1.0567        | 0.75  | 1836  | 0.9507          | 0.5637   | 0.4176    | 0.4948 | 0.4279 |
| 1.0052        | 1.0   | 2448  | 0.9716          | 0.4665   | 0.4913    | 0.5106 | 0.4324 |
| 0.9862        | 1.25  | 3060  | 0.9160          | 0.5719   | 0.5824    | 0.5851 | 0.5517 |
| 0.9428        | 1.5   | 3672  | 0.9251          | 0.5645   | 0.5838    | 0.5903 | 0.5386 |
| 0.9381        | 1.75  | 4284  | 0.9212          | 0.6307   | 0.6031    | 0.6091 | 0.6053 |
| 0.9124        | 2.0   | 4896  | 0.8897          | 0.6054   | 0.6078    | 0.6169 | 0.5895 |
| 0.9558        | 2.25  | 5508  | 0.8576          | 0.6283   | 0.6330    | 0.6077 | 0.6094 |
| 0.8814        | 2.5   | 6120  | 0.9458          | 0.6520   | 0.6357    | 0.6270 | 0.6286 |
| 0.8697        | 2.75  | 6732  | 0.8928          | 0.6381   | 0.6304    | 0.6259 | 0.6228 |
| 0.9142        | 3.0   | 7344  | 0.8542          | 0.6225   | 0.6227    | 0.6272 | 0.6124 |
| 0.825         | 3.25  | 7956  | 0.9639          | 0.6577   | 0.6491    | 0.6089 | 0.6093 |
| 0.84          | 3.5   | 8568  | 0.8980          | 0.6266   | 0.6309    | 0.6169 | 0.6130 |
| 0.8505        | 3.75  | 9180  | 0.9127          | 0.6503   | 0.6197    | 0.6130 | 0.6154 |
| 0.8287        | 4.0   | 9792  | 0.9343          | 0.6683   | 0.6515    | 0.6527 | 0.6488 |
| 0.7772        | 4.25  | 10404 | 1.0434          | 0.6650   | 0.6461    | 0.6454 | 0.6437 |
| 0.8217        | 4.5   | 11016 | 0.9760          | 0.6724   | 0.6574    | 0.6550 | 0.6533 |
| 0.7543        | 4.75  | 11628 | 1.0790          | 0.6454   | 0.6522    | 0.6342 | 0.6327 |
| 0.7868        | 5.0   | 12240 | 1.1457          | 0.6708   | 0.6519    | 0.6445 | 0.6463 |
| 0.8093        | 5.25  | 12852 | 1.1714          | 0.6716   | 0.6517    | 0.6525 | 0.6509 |
| 0.8032        | 5.5   | 13464 | 1.1882          | 0.6691   | 0.6480    | 0.6542 | 0.6489 |
| 0.7511        | 5.75  | 14076 | 1.2113          | 0.6650   | 0.6413    | 0.6458 | 0.6429 |
| 0.7698        | 6.0   | 14688 | 1.2229          | 0.6724   | 0.6503    | 0.6556 | 0.6513 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1
