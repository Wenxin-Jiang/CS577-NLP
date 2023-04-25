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
- name: distilbert-base-cased-finetuned-chunk
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-cased-finetuned-chunk

This model is a fine-tuned version of [distilbert-base-cased](https://huggingface.co/distilbert-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5180
- Precision: 0.8615
- Recall: 0.9088
- F1: 0.8845
- Accuracy: 0.8239

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

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.8391        | 1.0   | 878  | 0.5871          | 0.8453    | 0.9035 | 0.8734 | 0.8054   |
| 0.6134        | 2.0   | 1756 | 0.5447          | 0.8555    | 0.8983 | 0.8764 | 0.8142   |
| 0.5565        | 3.0   | 2634 | 0.5180          | 0.8615    | 0.9088 | 0.8845 | 0.8239   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.9.1
- Tokenizers 0.10.3
