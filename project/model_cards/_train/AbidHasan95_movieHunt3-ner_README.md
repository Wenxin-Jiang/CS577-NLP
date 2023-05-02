---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: movieHunt3-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# movieHunt3-ner

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0009

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 95   | 0.0462          |
| No log        | 2.0   | 190  | 0.0067          |
| No log        | 3.0   | 285  | 0.0028          |
| No log        | 4.0   | 380  | 0.0018          |
| No log        | 5.0   | 475  | 0.0014          |
| 0.1098        | 6.0   | 570  | 0.0012          |
| 0.1098        | 7.0   | 665  | 0.0011          |
| 0.1098        | 8.0   | 760  | 0.0010          |
| 0.1098        | 9.0   | 855  | 0.0010          |
| 0.1098        | 10.0  | 950  | 0.0009          |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
