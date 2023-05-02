---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
model-index:
- name: bert-base-uncased-finetuned-sst2
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: glue
      type: glue
      args: sst2
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9346330275229358
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-sst2

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2745
- Accuracy: 0.9346

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
| 0.1778        | 1.0   | 4210  | 0.3553          | 0.9060   |
| 0.1257        | 2.0   | 8420  | 0.2745          | 0.9346   |
| 0.0779        | 3.0   | 12630 | 0.3272          | 0.9300   |
| 0.0655        | 4.0   | 16840 | 0.3412          | 0.9323   |
| 0.0338        | 5.0   | 21050 | 0.3994          | 0.9300   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.4
- Tokenizers 0.11.6
