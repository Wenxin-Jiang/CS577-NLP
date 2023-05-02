---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bert-nlp-project-ft-imdb
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-nlp-project-ft-imdb

This model is a fine-tuned version of [jestemleon/bert-nlp-project-imdb](https://huggingface.co/jestemleon/bert-nlp-project-imdb) on the [steciuk/imdb](https://huggingface.co/datasets/steciuk/imdb) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2429
- Accuracy: 0.9477
- F1: 0.9468

and flowing results on the testing set:
- Accuracy: 0.9467
- F1: 0.9480

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
| 0.2603        | 0.38  | 750  | 0.1922          | 0.9293   | 0.9293 |
| 0.2021        | 0.75  | 1500 | 0.1633          | 0.9463   | 0.9446 |
| 0.1706        | 1.12  | 2250 | 0.1957          | 0.944    | 0.9425 |
| 0.1195        | 1.5   | 3000 | 0.2054          | 0.9455   | 0.9452 |
| 0.1106        | 1.88  | 3750 | 0.2417          | 0.9383   | 0.9391 |
| 0.0747        | 2.25  | 4500 | 0.2562          | 0.945    | 0.9441 |
| 0.0566        | 2.62  | 5250 | 0.2544          | 0.946    | 0.9443 |
| 0.0511        | 3.0   | 6000 | 0.2429          | 0.9477   | 0.9468 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
