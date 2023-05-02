---
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: BioBERT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BioBERT

This model is a fine-tuned version of [dmis-lab/biobert-v1.1](https://huggingface.co/dmis-lab/biobert-v1.1) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9310
- Accuracy: 0.79
- Precision: 0.8730
- Recall: 0.8088
- F1: 0.8397

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
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.6755        | 1.0   | 50   | 0.6608          | 0.47     | 0.9412    | 0.2353 | 0.3765 |
| 0.6097        | 2.0   | 100  | 0.5785          | 0.68     | 0.8214    | 0.6765 | 0.7419 |
| 0.5123        | 3.0   | 150  | 0.5240          | 0.7      | 0.9318    | 0.6029 | 0.7321 |
| 0.3547        | 4.0   | 200  | 0.4475          | 0.8      | 0.9138    | 0.7794 | 0.8413 |
| 0.2413        | 5.0   | 250  | 0.5033          | 0.81     | 0.9153    | 0.7941 | 0.8504 |
| 0.1398        | 6.0   | 300  | 0.6918          | 0.8      | 0.8636    | 0.8382 | 0.8507 |
| 0.0995        | 7.0   | 350  | 0.7694          | 0.79     | 0.8730    | 0.8088 | 0.8397 |
| 0.0636        | 8.0   | 400  | 0.8876          | 0.84     | 0.8824    | 0.8824 | 0.8824 |
| 0.0512        | 9.0   | 450  | 0.9019          | 0.8      | 0.875     | 0.8235 | 0.8485 |
| 0.0359        | 10.0  | 500  | 0.9310          | 0.79     | 0.8730    | 0.8088 | 0.8397 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
