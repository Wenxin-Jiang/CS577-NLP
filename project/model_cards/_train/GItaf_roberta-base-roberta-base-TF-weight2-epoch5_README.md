---
tags:
- generated_from_trainer
model-index:
- name: roberta-base-roberta-base-TF-weight2-epoch5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-roberta-base-TF-weight2-epoch5

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 5.5174
- Cls loss: 0.6899
- Lm loss: 4.1376
- Cls Accuracy: 0.5401
- Cls F1: 0.3788
- Cls Precision: 0.2917
- Cls Recall: 0.5401
- Perplexity: 62.65

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
| 6.023         | 1.0   | 3470  | 5.6863          | 0.6910   | 4.3046  | 0.5401       | 0.3788 | 0.2917        | 0.5401     | 74.04      |
| 5.6871        | 2.0   | 6940  | 5.5897          | 0.6926   | 4.2045  | 0.5401       | 0.3788 | 0.2917        | 0.5401     | 66.99      |
| 5.5587        | 3.0   | 10410 | 5.5414          | 0.6905   | 4.1604  | 0.5401       | 0.3788 | 0.2917        | 0.5401     | 64.10      |
| 5.481         | 4.0   | 13880 | 5.5208          | 0.6900   | 4.1409  | 0.5401       | 0.3788 | 0.2917        | 0.5401     | 62.86      |
| 5.4338        | 5.0   | 17350 | 5.5174          | 0.6899   | 4.1376  | 0.5401       | 0.3788 | 0.2917        | 0.5401     | 62.65      |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
