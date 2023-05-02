---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mt5-small_summarization
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-small_summarization

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 3.1774
- Rouge1: 18.2118
- Rouge2: 6.6244
- Rougel: 15.4682
- Rougelsum: 15.3942

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:-------:|:---------:|
| 17.7253       | 1.0   | 50   | 7.6921          | 6.677   | 1.1111 | 6.5586  | 6.6861    |
| 9.8457        | 2.0   | 100  | 4.5604          | 12.8991 | 1.9103 | 11.2559 | 10.9036   |
| 6.2403        | 3.0   | 150  | 3.9071          | 16.463  | 4.0695 | 14.3098 | 14.4065   |
| 5.2032        | 4.0   | 200  | 3.4869          | 17.6601 | 4.0878 | 14.2931 | 14.2743   |
| 4.8331        | 5.0   | 250  | 3.3472          | 18.5241 | 5.3312 | 15.8993 | 16.0559   |
| 4.526         | 6.0   | 300  | 3.2346          | 19.0264 | 5.7839 | 15.8013 | 16.1208   |
| 4.5378        | 7.0   | 350  | 3.1927          | 18.9843 | 6.992  | 16.3787 | 16.3574   |
| 4.3278        | 8.0   | 400  | 3.1774          | 18.2118 | 6.6244 | 15.4682 | 15.3942   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0
- Datasets 2.3.2
- Tokenizers 0.12.1
