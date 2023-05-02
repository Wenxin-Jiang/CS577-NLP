---
license: apache-2.0
tags:
- image-classification
- vision
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: pedestrian_age_recognition_local
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: imagefolder
      type: imagefolder
      config: default
      split: train
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8073394495412844
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pedestrian_age_recognition_local

This model is a fine-tuned version of [microsoft/beit-base-patch16-224-pt22k-ft22k](https://huggingface.co/microsoft/beit-base-patch16-224-pt22k-ft22k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5004
- Accuracy: 0.8073

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 1337
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.8849        | 1.0   | 2008  | 0.7939          | 0.6807   |
| 0.9836        | 2.0   | 4016  | 0.6694          | 0.7336   |
| 0.8128        | 3.0   | 6024  | 0.5768          | 0.7668   |
| 0.7611        | 4.0   | 8032  | 0.5541          | 0.7833   |
| 0.6441        | 5.0   | 10040 | 0.5473          | 0.7773   |
| 0.5696        | 6.0   | 12048 | 0.5187          | 0.7971   |
| 0.6925        | 7.0   | 14056 | 0.5082          | 0.8038   |
| 0.5711        | 8.0   | 16064 | 0.5092          | 0.8098   |
| 0.7741        | 9.0   | 18072 | 0.5026          | 0.8020   |
| 0.5269        | 10.0  | 20080 | 0.5004          | 0.8073   |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1

### Contact information
For personal communication related to this project, please contact Nha Nguyen Van (nha282@gmail.com).