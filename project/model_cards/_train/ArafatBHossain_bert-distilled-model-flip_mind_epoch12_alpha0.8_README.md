---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: bert-distilled-model-flip_mind_epoch12_alpha0.8
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-distilled-model-flip_mind_epoch12_alpha0.8

This model is a fine-tuned version of [ArafatBHossain/distill_bert_fine_tuned_mind](https://huggingface.co/ArafatBHossain/distill_bert_fine_tuned_mind) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7953
- Accuracy: 0.914

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
- num_epochs: 12
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 1.8595        | 1.0   | 3054  | 1.8311          | 0.854    |
| 1.7769        | 2.0   | 6108  | 1.7204          | 0.847    |
| 1.7614        | 3.0   | 9162  | 1.7666          | 0.8666   |
| 1.7212        | 4.0   | 12216 | 1.8134          | 0.8716   |
| 1.7255        | 5.0   | 15270 | 1.7368          | 0.8812   |
| 1.6845        | 6.0   | 18324 | 1.7368          | 0.8898   |
| 1.7346        | 7.0   | 21378 | 1.6621          | 0.8936   |
| 1.7436        | 8.0   | 24432 | 1.7180          | 0.9008   |
| 1.7333        | 9.0   | 27486 | 1.7523          | 0.9048   |
| 1.7805        | 10.0  | 30540 | 1.7820          | 0.9078   |
| 1.792         | 11.0  | 33594 | 1.7329          | 0.9096   |
| 1.7463        | 12.0  | 36648 | 1.7953          | 0.914    |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.11.0
- Datasets 2.6.1
- Tokenizers 0.12.1
