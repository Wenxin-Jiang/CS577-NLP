---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- mnist
metrics:
- accuracy
model-index:
- name: beit-base-patch16-224-pt22k-ft22k-finetuned-mnist
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: mnist
      type: mnist
      config: mnist
      split: train
      args: mnist
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9935
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# beit-base-patch16-224-pt22k-ft22k-finetuned-mnist

This model is a fine-tuned version of [microsoft/beit-base-patch16-224-pt22k-ft22k](https://huggingface.co/microsoft/beit-base-patch16-224-pt22k-ft22k) on the mnist dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0202
- Accuracy: 0.9935

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
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.3376        | 1.0   | 937  | 0.0446          | 0.9855   |
| 0.318         | 2.0   | 1874 | 0.0262          | 0.9916   |
| 0.2374        | 3.0   | 2811 | 0.0202          | 0.9935   |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
