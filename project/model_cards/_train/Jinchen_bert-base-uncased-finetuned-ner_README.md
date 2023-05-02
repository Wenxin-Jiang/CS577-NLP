---
license: apache-2.0
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
- name: bert-base-uncased-finetuned-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-ner

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0712
- Precision: 0.8945
- Recall: 0.9182
- F1: 0.9062
- Accuracy: 0.9793

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: IPU
- gradient_accumulation_steps: 16
- total_train_batch_size: 64
- total_eval_batch_size: 20
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- training precision: Mixed Precision

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1318        | 1.0   | 219  | 0.0967          | 0.8371    | 0.8714 | 0.8539 | 0.9705   |
| 0.0597        | 2.0   | 438  | 0.0735          | 0.8912    | 0.9052 | 0.8981 | 0.9779   |
| 0.0523        | 3.0   | 657  | 0.0712          | 0.8945    | 0.9182 | 0.9062 | 0.9793   |


### Framework versions

- Transformers 4.20.0
- Pytorch 1.10.0+cpu
- Datasets 2.4.0
- Tokenizers 0.12.1
