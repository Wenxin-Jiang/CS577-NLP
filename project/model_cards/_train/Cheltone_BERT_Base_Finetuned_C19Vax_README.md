---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- accuracy
- f1
model-index:
- name: Bert_Test
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Bert_Test

This model is a fine-tuned version of [bert-large-uncased](https://huggingface.co/bert-large-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1965
- Precision: 0.9332
- Accuracy: 0.9223
- F1: 0.9223

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
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 7

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:--------:|:------:|
| 0.6717        | 0.4   | 500  | 0.6049          | 0.7711    | 0.6743   | 0.6112 |
| 0.5704        | 0.8   | 1000 | 0.5299          | 0.7664    | 0.7187   | 0.6964 |
| 0.52          | 1.2   | 1500 | 0.4866          | 0.7698    | 0.7537   | 0.7503 |
| 0.4792        | 1.6   | 2000 | 0.4292          | 0.8031    | 0.793    | 0.7927 |
| 0.4332        | 2.0   | 2500 | 0.3920          | 0.8318    | 0.8203   | 0.8198 |
| 0.381         | 2.4   | 3000 | 0.3723          | 0.9023    | 0.8267   | 0.8113 |
| 0.3625        | 2.8   | 3500 | 0.3134          | 0.8736    | 0.8607   | 0.8601 |
| 0.3325        | 3.2   | 4000 | 0.2924          | 0.8973    | 0.871    | 0.8683 |
| 0.3069        | 3.6   | 4500 | 0.2671          | 0.8916    | 0.8847   | 0.8851 |
| 0.2866        | 4.0   | 5000 | 0.2571          | 0.8920    | 0.8913   | 0.8926 |
| 0.2595        | 4.4   | 5500 | 0.2450          | 0.8980    | 0.9      | 0.9015 |
| 0.2567        | 4.8   | 6000 | 0.2246          | 0.9057    | 0.9043   | 0.9054 |
| 0.2255        | 5.2   | 6500 | 0.2263          | 0.9332    | 0.905    | 0.9030 |
| 0.2237        | 5.6   | 7000 | 0.2083          | 0.9265    | 0.9157   | 0.9156 |
| 0.2248        | 6.0   | 7500 | 0.2039          | 0.9387    | 0.9193   | 0.9185 |
| 0.2086        | 6.4   | 8000 | 0.2038          | 0.9436    | 0.9193   | 0.9181 |
| 0.2029        | 6.8   | 8500 | 0.1965          | 0.9332    | 0.9223   | 0.9223 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
