---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: VaccinChatSentenceClassifierDutch_fromBERTje2_DAdialogQonly
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# VaccinChatSentenceClassifierDutch_fromBERTje2_DAdialogQonly

This model is a fine-tuned version of [outputDAQonly/checkpoint-8710](https://huggingface.co/outputDAQonly/checkpoint-8710) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5008
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
| 4.0751        | 1.0   | 1320  | 3.1674          | 0.4086   |
| 2.5619        | 2.0   | 2640  | 2.0335          | 0.6426   |
| 1.8549        | 3.0   | 3960  | 1.3537          | 0.7861   |
| 1.106         | 4.0   | 5280  | 0.9515          | 0.8519   |
| 0.6698        | 5.0   | 6600  | 0.7152          | 0.8757   |
| 0.4497        | 6.0   | 7920  | 0.5838          | 0.8921   |
| 0.2626        | 7.0   | 9240  | 0.5300          | 0.8940   |
| 0.1762        | 8.0   | 10560 | 0.4984          | 0.8958   |
| 0.119         | 9.0   | 11880 | 0.4906          | 0.9059   |
| 0.0919        | 10.0  | 13200 | 0.4896          | 0.8995   |
| 0.0722        | 11.0  | 14520 | 0.5012          | 0.9022   |
| 0.0517        | 12.0  | 15840 | 0.4951          | 0.9040   |
| 0.0353        | 13.0  | 17160 | 0.4988          | 0.9040   |
| 0.0334        | 14.0  | 18480 | 0.5035          | 0.9049   |
| 0.0304        | 15.0  | 19800 | 0.5008          | 0.9068   |


### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.10.0
- Datasets 1.16.1
- Tokenizers 0.10.3
