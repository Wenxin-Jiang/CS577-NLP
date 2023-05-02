---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: domlm-finetuned-cleaneval
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# domlm-finetuned-cleaneval

This model is a fine-tuned version of [albertus-casm/dom-lm-epoch-3](https://huggingface.co/albertus-casm/dom-lm-epoch-3) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2098
- Precision: 0.9438
- Recall: 0.9559
- F1: 0.9498
- Accuracy: 0.9412

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 111  | 0.2472          | 0.9163    | 0.9636 | 0.9394 | 0.9276   |
| No log        | 2.0   | 222  | 0.1798          | 0.9313    | 0.9671 | 0.9489 | 0.9393   |
| No log        | 3.0   | 333  | 0.2098          | 0.9438    | 0.9559 | 0.9498 | 0.9412   |


### Framework versions

- Transformers 4.19.0.dev0
- Pytorch 1.10.0+cu111
- Datasets 2.1.1.dev0
- Tokenizers 0.12.1
