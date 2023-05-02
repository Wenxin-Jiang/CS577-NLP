---
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: twitter-prosusai-finbert-sentiment-finetuned-memes-final
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# twitter-prosusai-finbert-sentiment-finetuned-memes-final

This model is a fine-tuned version of [jayantapaul888/twitter-data-prosusai-finbert-sentiment-finetuned-memes](https://huggingface.co/jayantapaul888/twitter-data-prosusai-finbert-sentiment-finetuned-memes) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9363
- Accuracy: 0.8163
- Precision: 0.8166
- Recall: 0.8163
- F1: 0.8164

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
| No log        | 1.0   | 294  | 0.3954          | 0.8198   | 0.8215    | 0.8198 | 0.8200 |
| 0.4754        | 2.0   | 588  | 0.4318          | 0.8203   | 0.8270    | 0.8203 | 0.8204 |
| 0.4754        | 3.0   | 882  | 0.5372          | 0.8230   | 0.8230    | 0.8230 | 0.8230 |
| 0.192         | 4.0   | 1176 | 0.7378          | 0.8196   | 0.8198    | 0.8196 | 0.8195 |
| 0.192         | 5.0   | 1470 | 0.8747          | 0.8168   | 0.8176    | 0.8168 | 0.8170 |
| 0.0726        | 6.0   | 1764 | 0.9363          | 0.8163   | 0.8166    | 0.8163 | 0.8164 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
