---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mt5-base-wikinewssum-spanish
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-base-wikinewssum-spanish

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.2394
- Rouge1: 7.9732
- Rouge2: 3.5041
- Rougel: 6.6713
- Rougelsum: 7.5229

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
| No log        | 1.0   | 528  | 2.3707          | 6.687  | 2.9169 | 5.6793 | 6.2978    |
| No log        | 2.0   | 1056 | 2.3140          | 7.9518 | 3.4529 | 6.7265 | 7.4984    |
| No log        | 3.0   | 1584 | 2.2848          | 7.9708 | 3.5344 | 6.7272 | 7.534     |
| No log        | 4.0   | 2112 | 2.2668          | 8.0252 | 3.5323 | 6.7319 | 7.5819    |
| 3.2944        | 5.0   | 2640 | 2.2532          | 8.0143 | 3.534  | 6.7155 | 7.582     |
| 3.2944        | 6.0   | 3168 | 2.2399          | 7.9525 | 3.4849 | 6.6716 | 7.5155    |
| 3.2944        | 7.0   | 3696 | 2.2376          | 7.9405 | 3.4661 | 6.6559 | 7.5043    |
| 3.2944        | 8.0   | 4224 | 2.2394          | 7.9732 | 3.5041 | 6.6713 | 7.5229    |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.10.1
- Datasets 1.16.1
- Tokenizers 0.10.3
