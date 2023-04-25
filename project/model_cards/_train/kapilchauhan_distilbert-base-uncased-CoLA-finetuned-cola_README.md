---
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- matthews_correlation
model-index:
- name: distilbert-base-uncased-CoLA-finetuned-cola
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
      value: 0.5689051637185746
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-CoLA-finetuned-cola

This model is a fine-tuned version of [textattack/distilbert-base-uncased-CoLA](https://huggingface.co/textattack/distilbert-base-uncased-CoLA) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6996
- Matthews Correlation: 0.5689

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Matthews Correlation |
|:-------------:|:-----:|:----:|:---------------:|:--------------------:|
| No log        | 1.0   | 134  | 0.6061          | 0.5074               |
| No log        | 2.0   | 268  | 0.5808          | 0.5652               |
| No log        | 3.0   | 402  | 0.6996          | 0.5689               |
| 0.0952        | 4.0   | 536  | 0.8249          | 0.5385               |
| 0.0952        | 5.0   | 670  | 0.8714          | 0.5567               |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0