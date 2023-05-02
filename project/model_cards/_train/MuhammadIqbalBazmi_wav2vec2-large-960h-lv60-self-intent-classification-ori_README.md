---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: wav2vec2-large-960h-lv60-self-intent-classification-ori
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-960h-lv60-self-intent-classification-ori

This model is a fine-tuned version of [facebook/wav2vec2-large-960h-lv60-self](https://huggingface.co/facebook/wav2vec2-large-960h-lv60-self) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1985
- Accuracy: 0.5417

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 45

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.2033        | 1.0   | 14   | 2.2126          | 0.0833   |
| 2.2006        | 2.0   | 28   | 2.2026          | 0.0833   |
| 2.1786        | 3.0   | 42   | 2.1758          | 0.3333   |
| 2.1712        | 4.0   | 56   | 2.1436          | 0.3333   |
| 2.1495        | 5.0   | 70   | 2.1120          | 0.3333   |
| 2.1326        | 6.0   | 84   | 2.0909          | 0.3333   |
| 2.1039        | 7.0   | 98   | 2.0966          | 0.3333   |
| 2.0931        | 8.0   | 112  | 2.0355          | 0.3333   |
| 2.1144        | 9.0   | 126  | 2.0082          | 0.3333   |
| 2.0258        | 10.0  | 140  | 1.9901          | 0.375    |
| 2.0028        | 11.0  | 154  | 1.9429          | 0.3958   |
| 1.9737        | 12.0  | 168  | 1.9538          | 0.3958   |
| 1.9023        | 13.0  | 182  | 1.8824          | 0.375    |
| 1.9226        | 14.0  | 196  | 1.8607          | 0.3958   |
| 1.8521        | 15.0  | 210  | 1.8065          | 0.3958   |
| 1.7752        | 16.0  | 224  | 1.8153          | 0.4167   |
| 1.8391        | 17.0  | 238  | 1.7470          | 0.4375   |
| 1.7041        | 18.0  | 252  | 1.7419          | 0.4167   |
| 1.7075        | 19.0  | 266  | 1.6644          | 0.4375   |
| 1.6845        | 20.0  | 280  | 1.6340          | 0.4375   |
| 1.6275        | 21.0  | 294  | 1.6271          | 0.4167   |
| 1.4586        | 22.0  | 308  | 1.5640          | 0.4375   |
| 1.4987        | 23.0  | 322  | 1.5279          | 0.4583   |
| 1.5513        | 24.0  | 336  | 1.4873          | 0.4792   |
| 1.4828        | 25.0  | 350  | 1.4887          | 0.4583   |
| 1.4711        | 26.0  | 364  | 1.4613          | 0.4583   |
| 1.371         | 27.0  | 378  | 1.4062          | 0.4792   |
| 1.3789        | 28.0  | 392  | 1.4038          | 0.4792   |
| 1.3579        | 29.0  | 406  | 1.4031          | 0.4792   |
| 1.2771        | 30.0  | 420  | 1.3637          | 0.5      |
| 1.3417        | 31.0  | 434  | 1.3655          | 0.5      |
| 1.231         | 32.0  | 448  | 1.3698          | 0.5      |
| 1.2367        | 33.0  | 462  | 1.3394          | 0.5      |
| 1.2933        | 34.0  | 476  | 1.3448          | 0.4792   |
| 1.1631        | 35.0  | 490  | 1.2867          | 0.5417   |
| 1.165         | 36.0  | 504  | 1.2624          | 0.5417   |
| 1.2431        | 37.0  | 518  | 1.2252          | 0.5625   |
| 1.1731        | 38.0  | 532  | 1.2082          | 0.5625   |
| 1.1734        | 39.0  | 546  | 1.2062          | 0.5417   |
| 1.1631        | 40.0  | 560  | 1.2034          | 0.5417   |
| 1.0963        | 41.0  | 574  | 1.1973          | 0.5417   |
| 1.2157        | 42.0  | 588  | 1.1988          | 0.5625   |
| 1.1467        | 43.0  | 602  | 1.2018          | 0.5417   |
| 1.1503        | 44.0  | 616  | 1.1986          | 0.5417   |
| 1.0945        | 45.0  | 630  | 1.1985          | 0.5417   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
