---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: VaccinChatSentenceClassifierDutch_fromBERTjeDIAL
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# VaccinChatSentenceClassifierDutch_fromBERTjeDIAL

This model is a fine-tuned version of [Jeska/BertjeWDialDataQA20k](https://huggingface.co/Jeska/BertjeWDialDataQA20k) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8355
- Accuracy: 0.6322

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 3.4418        | 1.0   | 1457 | 2.3866          | 0.5406   |
| 1.7742        | 2.0   | 2914 | 1.9365          | 0.6069   |
| 1.1313        | 3.0   | 4371 | 1.8355          | 0.6322   |


### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.10.0
- Datasets 1.16.1
- Tokenizers 0.10.3
