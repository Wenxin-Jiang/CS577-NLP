---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bert-nlp-project-ft-news
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-nlp-project-ft-news

This model is a fine-tuned version of [jestemleon/bert-nlp-project-news](https://huggingface.co/jestemleon/bert-nlp-project-news) on the [news](https://huggingface.co/datasets/steciuk/news) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4362
- Accuracy: 0.9078
- F1: 0.8872

and flowing results on the testing set:
- Accuracy: 0.9001
- F1: 0.8827

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
| 0.4106        | 0.37  | 120  | 0.3049          | 0.8797   | 0.8444 |
| 0.3078        | 0.75  | 240  | 0.3038          | 0.8891   | 0.8683 |
| 0.2642        | 1.12  | 360  | 0.3363          | 0.8969   | 0.8769 |
| 0.2114        | 1.5   | 480  | 0.3460          | 0.8922   | 0.8671 |
| 0.1661        | 1.87  | 600  | 0.3894          | 0.9031   | 0.8826 |
| 0.156         | 2.24  | 720  | 0.3946          | 0.8953   | 0.8714 |
| 0.1079        | 2.62  | 840  | 0.4340          | 0.9016   | 0.8795 |
| 0.1083        | 2.99  | 960  | 0.4362          | 0.9078   | 0.8872 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
