---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
datasets:
- mlsum
metrics:
- rouge
model-index:
- name: mt5-small-mlsum_training_sample
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: mlsum
      type: mlsum
      config: de
      split: train
      args: de
    metrics:
    - name: Rouge1
      type: rouge
      value: 28.2078
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-small-mlsum_training_sample

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on the mlsum dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9727
- Rouge1: 28.2078
- Rouge2: 19.0712
- Rougel: 26.2267
- Rougelsum: 26.9462

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| 1.3193        | 1.0   | 6875  | 2.1352          | 25.8941 | 17.4672 | 24.2858 | 24.924    |
| 1.2413        | 2.0   | 13750 | 2.0528          | 26.6221 | 18.1166 | 24.8233 | 25.5111   |
| 1.1844        | 3.0   | 20625 | 1.9783          | 27.0518 | 18.3457 | 25.2288 | 25.8919   |
| 1.0403        | 4.0   | 27500 | 1.9487          | 27.8154 | 18.9701 | 25.9435 | 26.6578   |
| 0.9582        | 5.0   | 34375 | 1.9374          | 27.6863 | 18.7723 | 25.7667 | 26.4694   |
| 0.8992        | 6.0   | 41250 | 1.9353          | 27.8959 | 18.919  | 26.0434 | 26.7262   |
| 0.8109        | 7.0   | 48125 | 1.9492          | 28.0644 | 18.8873 | 26.0628 | 26.757    |
| 0.7705        | 8.0   | 55000 | 1.9727          | 28.2078 | 19.0712 | 26.2267 | 26.9462   |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
