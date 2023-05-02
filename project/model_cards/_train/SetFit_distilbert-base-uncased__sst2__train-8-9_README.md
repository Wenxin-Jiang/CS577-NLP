---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__sst2__train-8-9
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__sst2__train-8-9

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6925
- Accuracy: 0.5140

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.7204        | 1.0   | 3    | 0.7025          | 0.5      |
| 0.6885        | 2.0   | 6    | 0.7145          | 0.5      |
| 0.6662        | 3.0   | 9    | 0.7222          | 0.5      |
| 0.6182        | 4.0   | 12   | 0.7427          | 0.25     |
| 0.5707        | 5.0   | 15   | 0.7773          | 0.25     |
| 0.5247        | 6.0   | 18   | 0.8137          | 0.25     |
| 0.5003        | 7.0   | 21   | 0.8556          | 0.25     |
| 0.4195        | 8.0   | 24   | 0.9089          | 0.5      |
| 0.387         | 9.0   | 27   | 0.9316          | 0.25     |
| 0.2971        | 10.0  | 30   | 0.9558          | 0.25     |
| 0.2581        | 11.0  | 33   | 0.9420          | 0.25     |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
