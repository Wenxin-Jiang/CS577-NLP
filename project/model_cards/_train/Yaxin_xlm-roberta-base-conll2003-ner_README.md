---
license: mit
tags:
- generated_from_trainer
datasets:
- conll2003
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: test-conll2003-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: conll2003
      type: conll2003
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.9459188783174762
    - name: Recall
      type: recall
      value: 0.9537192864355436
    - name: F1
      type: f1
      value: 0.94980306712478
    - name: Accuracy
      type: accuracy
      value: 0.9911218410498034
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# test-conll2003-ner

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0470
- Precision: 0.9459
- Recall: 0.9537
- F1: 0.9498
- Accuracy: 0.9911

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
- num_epochs: 3.0

### Training results



### Framework versions

- Transformers 4.18.0.dev0
- Pytorch 1.10.0
- Datasets 1.18.3
- Tokenizers 0.11.0
