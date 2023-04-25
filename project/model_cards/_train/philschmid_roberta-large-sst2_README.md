---
license: mit
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
model-index:
- name: roberta-large-sst2
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE SST2
      type: glue
      args: sst2
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9644495412844036
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-large-sst2

This model is a fine-tuned version of [roberta-large](https://huggingface.co/roberta-large) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1400
- Accuracy: 0.9644

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- distributed_type: sagemaker_data_parallel
- num_devices: 8
- total_train_batch_size: 256
- total_eval_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.3688        | 1.0   | 264  | 0.1444          | 0.9564   |
| 0.1529        | 2.0   | 528  | 0.1502          | 0.9518   |
| 0.107         | 3.0   | 792  | 0.1388          | 0.9530   |
| 0.0666        | 4.0   | 1056 | 0.1400          | 0.9644   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.2+cu113
- Datasets 1.18.4
- Tokenizers 0.11.6
