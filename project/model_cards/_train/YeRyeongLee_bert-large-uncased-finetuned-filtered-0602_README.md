---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bert-large-uncased-finetuned-filtered-0602
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-large-uncased-finetuned-filtered-0602

This model is a fine-tuned version of [bert-large-uncased](https://huggingface.co/bert-large-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8409
- Accuracy: 0.1667
- F1: 0.0476

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
- lr_scheduler_warmup_steps: 1000
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:------:|
| 1.8331        | 1.0   | 3180  | 1.8054          | 0.1667   | 0.0476 |
| 1.8158        | 2.0   | 6360  | 1.8196          | 0.1667   | 0.0476 |
| 1.8088        | 3.0   | 9540  | 1.8059          | 0.1667   | 0.0476 |
| 1.8072        | 4.0   | 12720 | 1.7996          | 0.1667   | 0.0476 |
| 1.8182        | 5.0   | 15900 | 1.7962          | 0.1667   | 0.0476 |
| 1.7993        | 6.0   | 19080 | 1.8622          | 0.1667   | 0.0476 |
| 1.7963        | 7.0   | 22260 | 1.8378          | 0.1667   | 0.0476 |
| 1.7956        | 8.0   | 25440 | 1.8419          | 0.1667   | 0.0476 |
| 1.7913        | 9.0   | 28620 | 1.8406          | 0.1667   | 0.0476 |
| 1.7948        | 10.0  | 31800 | 1.8409          | 0.1667   | 0.0476 |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.9.0
- Datasets 1.16.1
- Tokenizers 0.12.1
