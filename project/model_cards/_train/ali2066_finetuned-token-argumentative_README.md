---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: finetuned-token-argumentative
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned-token-argumentative

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1573
- Precision: 0.3777
- Recall: 0.3919
- F1: 0.3847
- Accuracy: 0.9497

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 75   | 0.3241          | 0.1109    | 0.2178 | 0.1470 | 0.8488   |
| No log        | 2.0   | 150  | 0.3145          | 0.1615    | 0.2462 | 0.1950 | 0.8606   |
| No log        | 3.0   | 225  | 0.3035          | 0.1913    | 0.3258 | 0.2411 | 0.8590   |
| No log        | 4.0   | 300  | 0.3080          | 0.2199    | 0.3220 | 0.2613 | 0.8612   |
| No log        | 5.0   | 375  | 0.3038          | 0.2209    | 0.3277 | 0.2639 | 0.8630   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
