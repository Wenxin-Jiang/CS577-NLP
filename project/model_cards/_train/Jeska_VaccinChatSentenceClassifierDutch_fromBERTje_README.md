---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: VaccinChatSentenceClassifierDutch_fromBERTje
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# VaccinChatSentenceClassifierDutch_fromBERTje

This model is a fine-tuned version of [GroNLP/bert-base-dutch-cased](https://huggingface.co/GroNLP/bert-base-dutch-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6223
- Accuracy: 0.9068

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
- num_epochs: 15.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 3.4666        | 1.0   | 1320  | 2.3355          | 0.5768   |
| 1.5293        | 2.0   | 2640  | 1.1118          | 0.8144   |
| 0.8031        | 3.0   | 3960  | 0.6362          | 0.8803   |
| 0.2985        | 4.0   | 5280  | 0.5119          | 0.8958   |
| 0.1284        | 5.0   | 6600  | 0.5023          | 0.8931   |
| 0.0842        | 6.0   | 7920  | 0.5246          | 0.9022   |
| 0.0414        | 7.0   | 9240  | 0.5581          | 0.9013   |
| 0.0372        | 8.0   | 10560 | 0.5721          | 0.9004   |
| 0.0292        | 9.0   | 11880 | 0.5469          | 0.9141   |
| 0.0257        | 10.0  | 13200 | 0.5871          | 0.9059   |
| 0.0189        | 11.0  | 14520 | 0.6181          | 0.9049   |
| 0.0104        | 12.0  | 15840 | 0.6184          | 0.9068   |
| 0.009         | 13.0  | 17160 | 0.6013          | 0.9049   |
| 0.0051        | 14.0  | 18480 | 0.6205          | 0.9059   |
| 0.0035        | 15.0  | 19800 | 0.6223          | 0.9068   |


### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.10.0
- Datasets 1.16.1
- Tokenizers 0.10.3
