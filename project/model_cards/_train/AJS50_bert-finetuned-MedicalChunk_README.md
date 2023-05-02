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
- name: bert-finetuned-MedicalChunk
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-MedicalChunk

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1762
- Precision: 0.2723
- Recall: 0.3065
- F1: 0.2884
- Accuracy: 0.9563

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 56   | 0.1631          | 0.0       | 0.0    | 0.0    | 0.9606   |
| No log        | 2.0   | 112  | 0.1416          | 0.0638    | 0.0302 | 0.0410 | 0.9592   |
| No log        | 3.0   | 168  | 0.1405          | 0.1982    | 0.2161 | 0.2067 | 0.9559   |
| No log        | 4.0   | 224  | 0.1356          | 0.2771    | 0.2312 | 0.2521 | 0.9633   |
| No log        | 5.0   | 280  | 0.1419          | 0.2928    | 0.2663 | 0.2789 | 0.9593   |
| No log        | 6.0   | 336  | 0.1550          | 0.2732    | 0.2513 | 0.2618 | 0.9602   |
| No log        | 7.0   | 392  | 0.1620          | 0.2732    | 0.2814 | 0.2772 | 0.9578   |
| No log        | 8.0   | 448  | 0.1670          | 0.2585    | 0.3065 | 0.2805 | 0.9554   |
| 0.1137        | 9.0   | 504  | 0.1728          | 0.2553    | 0.3015 | 0.2765 | 0.9552   |
| 0.1137        | 10.0  | 560  | 0.1762          | 0.2723    | 0.3065 | 0.2884 | 0.9563   |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
