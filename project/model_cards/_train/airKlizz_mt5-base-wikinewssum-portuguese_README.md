---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mt5-base-wikinewssum-portuguese
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-base-wikinewssum-portuguese

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.0428
- Rouge1: 9.4966
- Rouge2: 4.2224
- Rougel: 7.9845
- Rougelsum: 8.8641

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

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|
| No log        | 1.0   | 334  | 2.2258          | 7.3686 | 2.9066 | 6.3167 | 6.8758    |
| No log        | 2.0   | 668  | 2.1389          | 9.0551 | 3.8395 | 7.6578 | 8.4641    |
| No log        | 3.0   | 1002 | 2.1030          | 9.2792 | 3.9352 | 7.8259 | 8.663     |
| No log        | 4.0   | 1336 | 2.0841          | 9.337  | 4.0647 | 7.8662 | 8.693     |
| 3.2831        | 5.0   | 1670 | 2.0487          | 9.4244 | 4.0821 | 7.8633 | 8.7111    |
| 3.2831        | 6.0   | 2004 | 2.0580          | 9.4598 | 4.1598 | 7.9511 | 8.8299    |
| 3.2831        | 7.0   | 2338 | 2.0426          | 9.501  | 4.1885 | 7.9803 | 8.8612    |
| 3.2831        | 8.0   | 2672 | 2.0428          | 9.4966 | 4.2224 | 7.9845 | 8.8641    |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.10.1
- Datasets 1.16.1
- Tokenizers 0.10.3
