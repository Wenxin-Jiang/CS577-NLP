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
      value: 0.9719066462260881
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-cola

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unkown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1037
- Matthews Correlation: 0.9719

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

| Training Loss | Epoch | Step | Validation Loss | Matthews Correlation |
|:-------------:|:-----:|:----:|:---------------:|:--------------------:|
| 0.2094        | 1.0   | 525  | 0.1069          | 0.9607               |
| 0.0483        | 2.0   | 1050 | 0.0878          | 0.9719               |
| 0.0296        | 3.0   | 1575 | 0.1263          | 0.9664               |
| 0.0108        | 4.0   | 2100 | 0.1037          | 0.9719               |
| 0.0096        | 5.0   | 2625 | 0.1065          | 0.9719               |


### Framework versions

- Transformers 4.9.2
- Pytorch 1.9.0+cu102
- Datasets 1.11.0
- Tokenizers 0.10.3
