---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: BBC
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BBC

This model is a fine-tuned version of [t5-base](https://huggingface.co/t5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2824
- Rouge1: 18.46
- Rouge2: 17.0488
- Rougel: 18.3552
- Rougelsum: 18.3466

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| 0.7104        | 1.0   | 445  | 0.3218          | 17.4866 | 15.2567 | 17.0429 | 17.1216   |
| 0.3433        | 2.0   | 890  | 0.3039          | 17.7632 | 15.8878 | 17.4551 | 17.5161   |
| 0.3116        | 3.0   | 1335 | 0.2912          | 18.175  | 16.4391 | 17.9597 | 18.0081   |
| 0.2908        | 4.0   | 1780 | 0.2869          | 18.2832 | 16.6726 | 18.1187 | 18.1205   |
| 0.273         | 5.0   | 2225 | 0.2829          | 18.2807 | 16.7359 | 18.1496 | 18.1621   |
| 0.2625        | 6.0   | 2670 | 0.2819          | 18.3845 | 16.8793 | 18.2622 | 18.2561   |
| 0.2482        | 7.0   | 3115 | 0.2801          | 18.4748 | 17.0796 | 18.3792 | 18.3672   |
| 0.2454        | 8.0   | 3560 | 0.2824          | 18.46   | 17.0488 | 18.3552 | 18.3466   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
