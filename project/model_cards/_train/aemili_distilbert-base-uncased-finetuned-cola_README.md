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
      value: 0.5317477654019562
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-cola

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7578
- Matthews Correlation: 0.5317

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
| 0.5239        | 1.0   | 535  | 0.5219          | 0.4097               |
| 0.3483        | 2.0   | 1070 | 0.5775          | 0.4913               |
| 0.2296        | 3.0   | 1605 | 0.6440          | 0.4903               |
| 0.1734        | 4.0   | 2140 | 0.7578          | 0.5317               |
| 0.137         | 5.0   | 2675 | 0.8612          | 0.5192               |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.7.1+cu110
- Datasets 2.4.0
- Tokenizers 0.12.1
