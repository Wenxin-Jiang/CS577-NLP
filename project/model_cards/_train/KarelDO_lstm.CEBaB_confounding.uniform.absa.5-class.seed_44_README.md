---
language:
- en
tags:
- generated_from_trainer
datasets:
- OpenTable
metrics:
- accuracy
model-index:
- name: lstm.CEBaB_confounding.uniform.absa.5-class.seed_44
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: OpenTable OPENTABLE-ABSA
      type: OpenTable
      args: opentable-absa
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.7060383516931864
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# lstm.CEBaB_confounding.uniform.absa.5-class.seed_44

This model is a fine-tuned version of [lstm](https://huggingface.co/lstm) on the OpenTable OPENTABLE-ABSA dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6849
- Accuracy: 0.7060
- Macro-f1: 0.7017
- Weighted-macro-f1: 0.7077

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 32
- eval_batch_size: 32
- seed: 44
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5.0

### Training results



### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.2+cu102
- Datasets 2.5.2
- Tokenizers 0.12.1
