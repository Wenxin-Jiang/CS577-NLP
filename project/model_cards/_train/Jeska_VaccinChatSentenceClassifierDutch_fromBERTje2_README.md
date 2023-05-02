---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: VaccinChatSentenceClassifierDutch_fromBERTje2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# VaccinChatSentenceClassifierDutch_fromBERTje2

This model is a fine-tuned version of [GroNLP/bert-base-dutch-cased](https://huggingface.co/GroNLP/bert-base-dutch-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5112
- Accuracy: 0.9004

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
| 4.1505        | 1.0   | 1320  | 3.3293          | 0.3793   |
| 2.7333        | 2.0   | 2640  | 2.2295          | 0.6133   |
| 2.0189        | 3.0   | 3960  | 1.5134          | 0.7587   |
| 1.2504        | 4.0   | 5280  | 1.0765          | 0.8282   |
| 0.7733        | 5.0   | 6600  | 0.7937          | 0.8629   |
| 0.5217        | 6.0   | 7920  | 0.6438          | 0.8784   |
| 0.3148        | 7.0   | 9240  | 0.5733          | 0.8857   |
| 0.2067        | 8.0   | 10560 | 0.5362          | 0.8912   |
| 0.1507        | 9.0   | 11880 | 0.5098          | 0.8903   |
| 0.1024        | 10.0  | 13200 | 0.5078          | 0.8976   |
| 0.0837        | 11.0  | 14520 | 0.5054          | 0.8967   |
| 0.0608        | 12.0  | 15840 | 0.5062          | 0.8958   |
| 0.0426        | 13.0  | 17160 | 0.5072          | 0.9013   |
| 0.0374        | 14.0  | 18480 | 0.5110          | 0.9040   |
| 0.0346        | 15.0  | 19800 | 0.5112          | 0.9004   |


### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.10.0
- Datasets 1.16.1
- Tokenizers 0.10.3
