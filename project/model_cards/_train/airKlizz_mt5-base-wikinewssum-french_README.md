---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mt5-base-wikinewssum-french
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-base-wikinewssum-french

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.0917
- Rouge1: 12.0984
- Rouge2: 5.7289
- Rougel: 9.9245
- Rougelsum: 11.0697

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.6e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:------:|:---------:|
| No log        | 1.0   | 549  | 2.3203          | 11.5172 | 4.9352 | 9.3617 | 10.4605   |
| No log        | 2.0   | 1098 | 2.2057          | 11.8469 | 5.2369 | 9.6452 | 10.8337   |
| No log        | 3.0   | 1647 | 2.1525          | 11.9096 | 5.4027 | 9.7648 | 10.9315   |
| 3.1825        | 4.0   | 2196 | 2.1307          | 12.0782 | 5.5848 | 9.9614 | 11.1081   |
| 3.1825        | 5.0   | 2745 | 2.1172          | 11.9821 | 5.6042 | 9.8216 | 11.0077   |
| 3.1825        | 6.0   | 3294 | 2.1012          | 12.0845 | 5.6834 | 9.9119 | 11.0741   |
| 3.1825        | 7.0   | 3843 | 2.0964          | 12.1296 | 5.7271 | 9.9495 | 11.1227   |
| 2.3376        | 8.0   | 4392 | 2.0917          | 12.0984 | 5.7289 | 9.9245 | 11.0697   |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.10.1
- Datasets 1.16.1
- Tokenizers 0.10.3
