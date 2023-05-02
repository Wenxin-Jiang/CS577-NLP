---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: finetuned_sentence_itr0_2e-05_webDiscourse_01_03_2022-13_17_55
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_sentence_itr0_2e-05_webDiscourse_01_03_2022-13_17_55

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7224
- Accuracy: 0.6979
- F1: 0.4736
- Precision: 0.5074
- Recall: 0.4440

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
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| No log        | 1.0   | 95   | 0.6009          | 0.65     | 0.2222 | 0.625     | 0.1351 |
| No log        | 2.0   | 190  | 0.6140          | 0.675    | 0.3689 | 0.6552    | 0.2568 |
| No log        | 3.0   | 285  | 0.6580          | 0.67     | 0.4590 | 0.5833    | 0.3784 |
| No log        | 4.0   | 380  | 0.7560          | 0.665    | 0.4806 | 0.5636    | 0.4189 |
| No log        | 5.0   | 475  | 0.8226          | 0.665    | 0.464  | 0.5686    | 0.3919 |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
