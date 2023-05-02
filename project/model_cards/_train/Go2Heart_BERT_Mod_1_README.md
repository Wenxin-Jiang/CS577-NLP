---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- matthews_correlation
model-index:
- name: BERT_Mod_1
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
      value: 0.541934635424655
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BERT_Mod_1

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1787
- Matthews Correlation: 0.5419

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
| 0.1616        | 1.0   | 535  | 0.9278          | 0.4979               |
| 0.1128        | 2.0   | 1070 | 1.0487          | 0.5046               |
| 0.0712        | 3.0   | 1605 | 1.0155          | 0.5306               |
| 0.0952        | 4.0   | 2140 | 1.1860          | 0.5147               |
| 0.0698        | 5.0   | 2675 | 1.1787          | 0.5419               |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0
- Datasets 2.4.0
- Tokenizers 0.12.1
