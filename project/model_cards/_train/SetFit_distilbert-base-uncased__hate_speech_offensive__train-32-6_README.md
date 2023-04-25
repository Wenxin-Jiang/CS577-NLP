---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-32-6
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-32-6

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0523
- Accuracy: 0.663

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.0957        | 1.0   | 19   | 1.0696          | 0.6      |
| 1.0107        | 2.0   | 38   | 1.0047          | 0.55     |
| 0.8257        | 3.0   | 57   | 0.8358          | 0.8      |
| 0.6006        | 4.0   | 76   | 0.7641          | 0.6      |
| 0.4172        | 5.0   | 95   | 0.5931          | 0.8      |
| 0.2639        | 6.0   | 114  | 0.5570          | 0.7      |
| 0.1314        | 7.0   | 133  | 0.5017          | 0.65     |
| 0.0503        | 8.0   | 152  | 0.3115          | 0.75     |
| 0.023         | 9.0   | 171  | 0.4353          | 0.85     |
| 0.0128        | 10.0  | 190  | 0.5461          | 0.75     |
| 0.0092        | 11.0  | 209  | 0.5045          | 0.8      |
| 0.007         | 12.0  | 228  | 0.5014          | 0.8      |
| 0.0064        | 13.0  | 247  | 0.5070          | 0.8      |
| 0.0049        | 14.0  | 266  | 0.4681          | 0.8      |
| 0.0044        | 15.0  | 285  | 0.4701          | 0.8      |
| 0.0039        | 16.0  | 304  | 0.4862          | 0.8      |
| 0.0036        | 17.0  | 323  | 0.4742          | 0.8      |
| 0.0035        | 18.0  | 342  | 0.4652          | 0.8      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
