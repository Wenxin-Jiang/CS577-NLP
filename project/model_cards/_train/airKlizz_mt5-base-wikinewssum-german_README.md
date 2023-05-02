---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mt5-base-wikinewssum-german
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-base-wikinewssum-german

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.5135
- Rouge1: 8.0553
- Rouge2: 2.7846
- Rougel: 6.2182
- Rougelsum: 7.6203

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
| No log        | 1.0   | 723  | 2.7112          | 7.3681 | 2.3679 | 5.5705 | 6.7588    |
| No log        | 2.0   | 1446 | 2.6178          | 7.8539 | 2.7551 | 6.2081 | 7.4139    |
| No log        | 3.0   | 2169 | 2.5756          | 7.8401 | 2.6075 | 6.0135 | 7.4303    |
| No log        | 4.0   | 2892 | 2.5465          | 8.1097 | 2.8525 | 6.268  | 7.6482    |
| 3.4589        | 5.0   | 3615 | 2.5315          | 8.0192 | 2.7848 | 6.2484 | 7.5859    |
| 3.4589        | 6.0   | 4338 | 2.5222          | 8.1063 | 2.8986 | 6.337  | 7.6564    |
| 3.4589        | 7.0   | 5061 | 2.5136          | 8.0565 | 2.8707 | 6.2732 | 7.6105    |
| 3.4589        | 8.0   | 5784 | 2.5135          | 8.0553 | 2.7846 | 6.2182 | 7.6203    |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.10.1
- Datasets 1.16.1
- Tokenizers 0.10.3
