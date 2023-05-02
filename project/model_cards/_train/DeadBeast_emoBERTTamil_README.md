---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tamilmixsentiment
metrics:
- accuracy
model_index:
- name: emoBERTTamil
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: tamilmixsentiment
      type: tamilmixsentiment
      args: default
    metric:
      name: Accuracy
      type: accuracy
      value: 0.671
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# emoBERTTamil

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the tamilmixsentiment dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9666
- Accuracy: 0.671

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.1128        | 1.0   | 250  | 1.0290          | 0.672    |
| 1.0226        | 2.0   | 500  | 1.0172          | 0.686    |
| 0.9137        | 3.0   | 750  | 0.9666          | 0.671    |


### Framework versions

- Transformers 4.9.2
- Pytorch 1.9.0+cu102
- Datasets 1.11.0
- Tokenizers 0.10.3
