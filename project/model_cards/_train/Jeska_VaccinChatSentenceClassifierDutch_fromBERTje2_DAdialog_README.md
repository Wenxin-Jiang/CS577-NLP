---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: VaccinChatSentenceClassifierDutch_fromBERTje2_DAdialog
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# VaccinChatSentenceClassifierDutch_fromBERTje2_DAdialog

This model is a fine-tuned version of [outputDA/checkpoint-7710](https://huggingface.co/outputDA/checkpoint-7710) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5025
- Accuracy: 0.9077

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-06
- lr_scheduler_type: linear
- num_epochs: 15.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 3.9925        | 1.0   | 1320  | 3.0954          | 0.4223   |
| 2.5041        | 2.0   | 2640  | 1.9762          | 0.6563   |
| 1.8061        | 3.0   | 3960  | 1.3196          | 0.7952   |
| 1.0694        | 4.0   | 5280  | 0.9304          | 0.8510   |
| 0.6479        | 5.0   | 6600  | 0.6875          | 0.8821   |
| 0.4408        | 6.0   | 7920  | 0.5692          | 0.8976   |
| 0.2542        | 7.0   | 9240  | 0.5291          | 0.8949   |
| 0.1709        | 8.0   | 10560 | 0.5038          | 0.9059   |
| 0.1181        | 9.0   | 11880 | 0.4885          | 0.9049   |
| 0.0878        | 10.0  | 13200 | 0.4900          | 0.9049   |
| 0.0702        | 11.0  | 14520 | 0.4930          | 0.9086   |
| 0.0528        | 12.0  | 15840 | 0.4987          | 0.9113   |
| 0.0406        | 13.0  | 17160 | 0.5009          | 0.9113   |
| 0.0321        | 14.0  | 18480 | 0.5017          | 0.9104   |
| 0.0308        | 15.0  | 19800 | 0.5025          | 0.9077   |


### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.10.0
- Datasets 1.16.1
- Tokenizers 0.10.3
