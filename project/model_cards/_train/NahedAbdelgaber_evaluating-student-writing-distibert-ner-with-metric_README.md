---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: evaluating-student-writing-distibert-ner-with-metric
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# evaluating-student-writing-distibert-ner-with-metric

This model is a fine-tuned version of [NahedAbdelgaber/evaluating-student-writing-distibert-ner](https://huggingface.co/NahedAbdelgaber/evaluating-student-writing-distibert-ner) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7535
- Precision: 0.0614
- Recall: 0.2590
- F1: 0.0993
- Accuracy: 0.6188

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.7145        | 1.0   | 1755 | 0.7683          | 0.0546    | 0.2194 | 0.0875 | 0.6191   |
| 0.6608        | 2.0   | 3510 | 0.7504          | 0.0570    | 0.2583 | 0.0934 | 0.6136   |
| 0.5912        | 3.0   | 5265 | 0.7535          | 0.0614    | 0.2590 | 0.0993 | 0.6188   |


### Framework versions

- Transformers 4.12.5
- Pytorch 1.9.1
- Datasets 1.16.1
- Tokenizers 0.10.3
