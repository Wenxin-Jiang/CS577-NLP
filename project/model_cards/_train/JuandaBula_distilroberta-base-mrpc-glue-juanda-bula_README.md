---
license: apache-2.0
tags:
- text-classification
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
- f1
widget:
  - text:
      - >-
        Yucaipa owned Dominick 's before selling the chain to Safeway in 1998
        for $ 2.5 billion.
      - >-
        Yucaipa bought Dominick's in 1995 for $ 693 million and sold it to
        Safeway for $ 1.8 billion in 1998.
    example_title: Not Equivalent
  - text:
      - >-
        Revenue in the first quarter of the year dropped 15 percent from the
        same period a year earlier.
      - >-
        With the scandal hanging over Stewart's company revenue the first
        quarter of the year dropped 15 percent from the same period a year
        earlier.
    example_title: Equivalent
model-index:
- name: distilroberta-base-mrpc-glue-juanda-bula
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: datasetX
      type: glue
      config: mrpc
      split: train
      args: mrpc
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8333333333333334
    - name: F1
      type: f1
      value: 0.870722433460076
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilroberta-base-mrpc-glue-juanda-bula

This model is a fine-tuned version of [distilroberta-base](https://huggingface.co/distilroberta-base) on the datasetX dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5684
- Accuracy: 0.8333
- F1: 0.8707

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.5239        | 1.09  | 500  | 0.6723          | 0.7990   | 0.8610 |
| 0.3692        | 2.18  | 1000 | 0.5684          | 0.8333   | 0.8707 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cpu
- Datasets 2.7.1
- Tokenizers 0.13.2
