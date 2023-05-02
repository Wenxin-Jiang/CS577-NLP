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
      config: cola
      split: train
      args: cola
    metrics:
    - name: Matthews Correlation
      type: matthews_correlation
      value: 0.5340667882909217
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-cola

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8130
- Matthews Correlation: 0.5341

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
| 0.5214        | 1.0   | 535  | 0.5266          | 0.4239               |
| 0.3449        | 2.0   | 1070 | 0.5079          | 0.5052               |
| 0.2347        | 3.0   | 1605 | 0.5736          | 0.5185               |
| 0.1764        | 4.0   | 2140 | 0.7526          | 0.5305               |
| 0.1324        | 5.0   | 2675 | 0.8130          | 0.5341               |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
