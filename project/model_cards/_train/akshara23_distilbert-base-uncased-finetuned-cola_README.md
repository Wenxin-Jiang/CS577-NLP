---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- matthews_correlation
model_index:
- name: distilbert-base-uncased-finetuned-cola
  results:
  - task:
      name: Text Classification
      type: text-classification
    metric:
      name: Matthews Correlation
      type: matthews_correlation
      value: 0.6290322580645161
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-cola

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unkown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0475
- Matthews Correlation: 0.6290

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
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Matthews Correlation |
|:-------------:|:-----:|:----:|:---------------:|:--------------------:|
| No log        | 1.0   | 16   | 1.3863          | 0.0                  |
| No log        | 2.0   | 32   | 1.2695          | 0.4503               |
| No log        | 3.0   | 48   | 1.1563          | 0.6110               |
| No log        | 4.0   | 64   | 1.0757          | 0.6290               |
| No log        | 5.0   | 80   | 1.0475          | 0.6290               |


### Framework versions

- Transformers 4.9.2
- Pytorch 1.9.0+cu102
- Datasets 1.11.0
- Tokenizers 0.10.3
