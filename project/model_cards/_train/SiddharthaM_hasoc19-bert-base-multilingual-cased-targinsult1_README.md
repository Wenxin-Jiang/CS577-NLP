---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: hasoc19-bert-base-multilingual-cased-targinsult1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# hasoc19-bert-base-multilingual-cased-targinsult1

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1105
- Accuracy: 0.6920
- Precision: 0.6630
- Recall: 0.6523
- F1: 0.6559

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| No log        | 1.0   | 263  | 0.5820          | 0.6820   | 0.6704    | 0.5890 | 0.5768 |
| 0.5841        | 2.0   | 526  | 0.5826          | 0.7025   | 0.6972    | 0.6196 | 0.6179 |
| 0.5841        | 3.0   | 789  | 0.5732          | 0.7029   | 0.6810    | 0.6863 | 0.6831 |
| 0.4583        | 4.0   | 1052 | 0.6151          | 0.7063   | 0.6797    | 0.6712 | 0.6744 |
| 0.4583        | 5.0   | 1315 | 0.6998          | 0.7034   | 0.6773    | 0.6732 | 0.6750 |
| 0.3201        | 6.0   | 1578 | 0.7943          | 0.6892   | 0.6679    | 0.6744 | 0.6701 |
| 0.3201        | 7.0   | 1841 | 0.9488          | 0.6873   | 0.6565    | 0.6386 | 0.6428 |
| 0.207         | 8.0   | 2104 | 1.0036          | 0.6844   | 0.6563    | 0.6529 | 0.6544 |
| 0.207         | 9.0   | 2367 | 1.0690          | 0.6906   | 0.6617    | 0.6532 | 0.6562 |
| 0.1517        | 10.0  | 2630 | 1.1105          | 0.6920   | 0.6630    | 0.6523 | 0.6559 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
