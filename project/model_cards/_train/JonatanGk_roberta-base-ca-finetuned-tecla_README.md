---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tecla
metrics:
- accuracy
model-index:
- name: roberta-base-ca-finetuned-mnli
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: tecla
      type: tecla
      args: tecla
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.7361816335412737
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-ca-finetuned-mnli

This model is a fine-tuned version of [BSC-TeMU/roberta-base-ca](https://huggingface.co/BSC-TeMU/roberta-base-ca) on the tecla dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9354
- Accuracy: 0.7362

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.8465        | 1.0   | 6888  | 0.8222          | 0.6990   |
| 0.6966        | 2.0   | 13776 | 0.7872          | 0.7157   |
| 0.5643        | 3.0   | 20664 | 0.8060          | 0.7268   |
| 0.4435        | 4.0   | 27552 | 0.8470          | 0.7333   |
| 0.3206        | 5.0   | 34440 | 0.9354          | 0.7362   |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.0+cu111
- Datasets 1.12.1
- Tokenizers 0.10.3
