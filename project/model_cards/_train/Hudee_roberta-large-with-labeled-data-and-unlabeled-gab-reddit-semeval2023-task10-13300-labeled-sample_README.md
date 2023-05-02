---
license: mit
tags:
- generated_from_trainer
model-index:
- name: roberta-large-with-labeled-data-and-unlabeled-gab-reddit-semeval2023-task10-13300-labeled-sample
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-large-with-labeled-data-and-unlabeled-gab-reddit-semeval2023-task10-13300-labeled-sample

This model is a fine-tuned version of [HPL/roberta-large-unlabeled-gab-reddit-semeval2023-task10-57000sample](https://huggingface.co/HPL/roberta-large-unlabeled-gab-reddit-semeval2023-task10-57000sample) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7889

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
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.9921        | 1.0   | 832  | 1.9311          |
| 1.9284        | 2.0   | 1664 | 1.8428          |
| 1.8741        | 3.0   | 2496 | 1.8364          |
| 1.816         | 4.0   | 3328 | 1.7889          |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.0
- Tokenizers 0.10.3
