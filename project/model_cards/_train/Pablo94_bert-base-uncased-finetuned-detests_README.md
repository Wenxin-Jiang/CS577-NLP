---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: bert-base-uncased-finetuned-detests
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-detests

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0660
- Accuracy: 0.8232

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.4677        | 1.0   | 153  | 0.4412          | 0.8101   |
| 0.468         | 2.0   | 306  | 0.4210          | 0.8167   |
| 0.2216        | 3.0   | 459  | 0.4649          | 0.8183   |
| 0.1552        | 4.0   | 612  | 0.5008          | 0.8069   |
| 0.0962        | 5.0   | 765  | 0.7498          | 0.8347   |
| 0.0379        | 6.0   | 918  | 0.8682          | 0.8282   |
| 0.0026        | 7.0   | 1071 | 0.9450          | 0.8249   |
| 0.0202        | 8.0   | 1224 | 1.0202          | 0.8282   |
| 0.0011        | 9.0   | 1377 | 1.0601          | 0.8282   |
| 0.0305        | 10.0  | 1530 | 1.0660          | 0.8232   |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
