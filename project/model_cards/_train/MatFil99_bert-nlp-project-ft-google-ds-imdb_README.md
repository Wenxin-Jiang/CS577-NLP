---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bert-nlp-project-ft-google-ds-imdb
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-nlp-project-ft-google-ds-imdb

This model is a fine-tuned version of [jestemleon/bert-nlp-project-google](https://huggingface.co/jestemleon/bert-nlp-project-google) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2646
- Accuracy: 0.9455
- F1: 0.9446

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
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.2684        | 0.38  | 750  | 0.1850          | 0.9315   | 0.9295 |
| 0.2105        | 0.75  | 1500 | 0.1734          | 0.9407   | 0.9385 |
| 0.1767        | 1.12  | 2250 | 0.2229          | 0.9337   | 0.9346 |
| 0.1259        | 1.5   | 3000 | 0.2029          | 0.9423   | 0.9401 |
| 0.1187        | 1.88  | 3750 | 0.2554          | 0.9353   | 0.9359 |
| 0.0778        | 2.25  | 4500 | 0.2759          | 0.9433   | 0.9418 |
| 0.06          | 2.62  | 5250 | 0.2663          | 0.9443   | 0.9428 |
| 0.0551        | 3.0   | 6000 | 0.2646          | 0.9455   | 0.9446 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
