---
license: mit
tags:
- generated_from_trainer
datasets:
- pawsx
metrics:
- accuracy
- f1
model-index:
- name: camembert-base-finetuned-paraphrase
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: pawsx
      type: pawsx
      args: fr
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9085
    - name: F1
      type: f1
      value: 0.9088724090678741
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# camembert-base-finetuned-paraphrase

This model is a fine-tuned version of [camembert-base](https://huggingface.co/camembert-base) on the pawsx dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2708
- Accuracy: 0.9085
- F1: 0.9089

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.3918        | 1.0   | 772  | 0.3211          | 0.869    | 0.8696 |
| 0.2103        | 2.0   | 1544 | 0.2448          | 0.9075   | 0.9077 |
| 0.1622        | 3.0   | 2316 | 0.2577          | 0.9055   | 0.9059 |
| 0.1344        | 4.0   | 3088 | 0.2708          | 0.9085   | 0.9089 |


### Framework versions

- Transformers 4.19.3
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
