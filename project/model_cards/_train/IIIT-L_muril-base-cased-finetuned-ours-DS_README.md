---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: muril-base-cased-finetuned-ours-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# muril-base-cased-finetuned-ours-DS

This model is a fine-tuned version of [google/muril-base-cased](https://huggingface.co/google/muril-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8885
- Accuracy: 0.625
- Precision: 0.5563
- Recall: 0.5570
- F1: 0.5412

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 25

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.0904        | 1.98  | 99   | 1.0762          | 0.245    | 0.0817    | 0.3333 | 0.1312 |
| 1.0535        | 3.96  | 198  | 1.0206          | 0.595    | 0.3940    | 0.5312 | 0.4410 |
| 0.9936        | 5.94  | 297  | 1.0099          | 0.58     | 0.3582    | 0.4833 | 0.4115 |
| 0.9371        | 7.92  | 396  | 0.9645          | 0.615    | 0.3918    | 0.5378 | 0.4507 |
| 0.8931        | 9.9   | 495  | 0.9333          | 0.615    | 0.3969    | 0.5447 | 0.4535 |
| 0.8237        | 11.88 | 594  | 0.9273          | 0.595    | 0.5451    | 0.5171 | 0.4439 |
| 0.7772        | 13.86 | 693  | 0.8890          | 0.61     | 0.5186    | 0.5512 | 0.4661 |
| 0.7365        | 15.84 | 792  | 0.8834          | 0.625    | 0.5661    | 0.5666 | 0.5112 |
| 0.6987        | 17.82 | 891  | 0.9026          | 0.615    | 0.5532    | 0.5507 | 0.5314 |
| 0.679         | 19.8  | 990  | 0.9018          | 0.63     | 0.5631    | 0.5596 | 0.5501 |
| 0.6572        | 21.78 | 1089 | 0.8737          | 0.635    | 0.5782    | 0.5806 | 0.5614 |
| 0.644         | 23.76 | 1188 | 0.8885          | 0.625    | 0.5563    | 0.5570 | 0.5412 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1
