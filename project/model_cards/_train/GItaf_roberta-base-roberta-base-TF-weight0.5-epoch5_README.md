---
tags:
- generated_from_trainer
model-index:
- name: roberta-base-roberta-base-TF-weight0.5-epoch5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-roberta-base-TF-weight0.5-epoch5

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.4274
- Cls loss: 0.5846
- Lm loss: 4.1354
- Cls Accuracy: 0.7533
- Cls F1: 0.7495
- Cls Precision: 0.7581
- Cls Recall: 0.7533
- Perplexity: 62.51

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Cls loss | Lm loss | Cls Accuracy | Cls F1 | Cls Precision | Cls Recall | Perplexity |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:-------:|:------------:|:------:|:-------------:|:----------:|:----------:|
| 4.9675        | 1.0   | 3470  | 4.6427          | 0.6907   | 4.2975  | 0.5401       | 0.3788 | 0.2917        | 0.5401     | 73.51      |
| 4.6381        | 2.0   | 6940  | 4.5451          | 0.6935   | 4.1983  | 0.4599       | 0.2898 | 0.2115        | 0.4599     | 66.58      |
| 4.5086        | 3.0   | 10410 | 4.5036          | 0.6902   | 4.1585  | 0.5401       | 0.3788 | 0.2917        | 0.5401     | 63.98      |
| 4.4302        | 4.0   | 13880 | 4.4818          | 0.6877   | 4.1379  | 0.5447       | 0.3910 | 0.6764        | 0.5447     | 62.67      |
| 4.3315        | 5.0   | 17350 | 4.4274          | 0.5846   | 4.1354  | 0.7533       | 0.7495 | 0.7581        | 0.7533     | 62.51      |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1