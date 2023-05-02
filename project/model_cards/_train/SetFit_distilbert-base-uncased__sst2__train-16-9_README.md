---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__sst2__train-16-9
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__sst2__train-16-9

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6915
- Accuracy: 0.5157

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
| 0.6868        | 1.0   | 7    | 0.7121          | 0.1429   |
| 0.6755        | 2.0   | 14   | 0.7234          | 0.1429   |
| 0.6389        | 3.0   | 21   | 0.7384          | 0.2857   |
| 0.5575        | 4.0   | 28   | 0.7884          | 0.2857   |
| 0.4972        | 5.0   | 35   | 0.7767          | 0.4286   |
| 0.2821        | 6.0   | 42   | 0.8275          | 0.4286   |
| 0.1859        | 7.0   | 49   | 0.9283          | 0.2857   |
| 0.1388        | 8.0   | 56   | 0.9384          | 0.4286   |
| 0.078         | 9.0   | 63   | 1.1973          | 0.4286   |
| 0.0462        | 10.0  | 70   | 1.4016          | 0.4286   |
| 0.0319        | 11.0  | 77   | 1.4087          | 0.4286   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
