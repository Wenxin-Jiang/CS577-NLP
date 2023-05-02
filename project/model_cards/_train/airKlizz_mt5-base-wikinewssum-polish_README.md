---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mt5-base-wikinewssum-polish
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-base-wikinewssum-polish

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3179
- Rouge1: 7.911
- Rouge2: 3.2189
- Rougel: 6.7856
- Rougelsum: 7.4485

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
| No log        | 1.0   | 315  | 2.5391          | 5.9874 | 2.3594 | 5.1303 | 5.6116    |
| No log        | 2.0   | 630  | 2.4446          | 7.7294 | 3.0152 | 6.6024 | 7.2757    |
| No log        | 3.0   | 945  | 2.3912          | 7.6451 | 2.9785 | 6.5714 | 7.2011    |
| 3.5311        | 4.0   | 1260 | 2.3720          | 7.8007 | 3.0913 | 6.7067 | 7.3451    |
| 3.5311        | 5.0   | 1575 | 2.3411          | 7.8374 | 3.1208 | 6.7288 | 7.3459    |
| 3.5311        | 6.0   | 1890 | 2.3354          | 7.8664 | 3.1655 | 6.762  | 7.4364    |
| 3.5311        | 7.0   | 2205 | 2.3175          | 7.9529 | 3.2225 | 6.8438 | 7.4904    |
| 2.692         | 8.0   | 2520 | 2.3179          | 7.911  | 3.2189 | 6.7856 | 7.4485    |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.10.1
- Datasets 1.16.1
- Tokenizers 0.10.3
