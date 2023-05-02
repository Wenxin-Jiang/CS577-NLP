---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: bert-distilled-single_teacher_mind_epoch07_alpha0.8
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-distilled-single_teacher_mind_epoch07_alpha0.8

This model is a fine-tuned version of [ArafatBHossain/distill_bert_fine_tuned_mind](https://huggingface.co/ArafatBHossain/distill_bert_fine_tuned_mind) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1023
- Accuracy: 0.9208

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 7
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.2937        | 1.0   | 3054  | 0.2652          | 0.8802   |
| 0.2339        | 2.0   | 6108  | 0.2510          | 0.8822   |
| 0.1721        | 3.0   | 9162  | 0.1781          | 0.9038   |
| 0.1284        | 4.0   | 12216 | 0.1450          | 0.9108   |
| 0.0993        | 5.0   | 15270 | 0.1195          | 0.9182   |
| 0.0765        | 6.0   | 18324 | 0.1115          | 0.9172   |
| 0.063         | 7.0   | 21378 | 0.1023          | 0.9208   |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.11.0
- Datasets 2.6.1
- Tokenizers 0.12.1
