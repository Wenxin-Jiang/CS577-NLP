---
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- matthews_correlation
model-index:
- name: bert-base-uncased-CoLA-finetuned-cola
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
      value: 0.5755298089385917
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-CoLA-finetuned-cola

This model is a fine-tuned version of [textattack/bert-base-uncased-CoLA](https://huggingface.co/textattack/bert-base-uncased-CoLA) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8318
- Matthews Correlation: 0.5755

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Matthews Correlation |
|:-------------:|:-----:|:----:|:---------------:|:--------------------:|
| 0.2949        | 1.0   | 535  | 0.5742          | 0.5219               |
| 0.1852        | 2.0   | 1070 | 0.7226          | 0.5573               |
| 0.1196        | 3.0   | 1605 | 0.8318          | 0.5755               |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0
