---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- matthews_correlation
model-index:
- name: distilbert-base-uncased-finetuned-cola
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: glue
      type: glue
      args: cola
    metrics:
    - name: Matthews Correlation
      type: matthews_correlation
      value: 0.5474713423103301
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-cola

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8663
- Matthews Correlation: 0.5475

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
| 0.5248        | 1.0   | 535  | 0.5171          | 0.4210               |
| 0.3418        | 2.0   | 1070 | 0.4971          | 0.5236               |
| 0.2289        | 3.0   | 1605 | 0.6874          | 0.5023               |
| 0.1722        | 4.0   | 2140 | 0.7680          | 0.5392               |
| 0.118         | 5.0   | 2675 | 0.8663          | 0.5475               |


### Framework versions

- Transformers 4.12.3
- Pytorch 1.8.1+cu102
- Datasets 1.18.3
- Tokenizers 0.10.3
