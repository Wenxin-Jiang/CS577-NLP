---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: twitter-data-xlm-roberta-base-sentiment-finetuned-memes-final
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# twitter-data-xlm-roberta-base-sentiment-finetuned-memes-final

This model is a fine-tuned version of [jayantapaul888/twitter-data-xlm-roberta-base-sentiment-finetuned-memes](https://huggingface.co/jayantapaul888/twitter-data-xlm-roberta-base-sentiment-finetuned-memes) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5884
- Accuracy: 0.8310
- Precision: 0.8314
- Recall: 0.8310
- F1: 0.8311

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
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| No log        | 1.0   | 294  | 0.3981          | 0.8136   | 0.8185    | 0.8136 | 0.8132 |
| 0.4388        | 2.0   | 588  | 0.4114          | 0.8220   | 0.8275    | 0.8220 | 0.8221 |
| 0.4388        | 3.0   | 882  | 0.4203          | 0.8263   | 0.8285    | 0.8263 | 0.8266 |
| 0.2731        | 4.0   | 1176 | 0.4815          | 0.8235   | 0.8276    | 0.8235 | 0.8221 |
| 0.2731        | 5.0   | 1470 | 0.5090          | 0.8330   | 0.8335    | 0.8330 | 0.8332 |
| 0.1883        | 6.0   | 1764 | 0.5884          | 0.8310   | 0.8314    | 0.8310 | 0.8311 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
