---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mt5-small-finetuned-amazon-en-es
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-small-finetuned-amazon-en-es

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.0282
- Rouge1: 17.629
- Rouge2: 8.5256
- Rougel: 17.1329
- Rougelsum: 17.1403

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

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| 6.6665        | 1.0   | 1209 | 3.2917          | 13.9446 | 5.4878  | 13.3696 | 13.3884   |
| 3.9091        | 2.0   | 2418 | 3.1575          | 16.5515 | 8.4045  | 15.734  | 15.8858   |
| 3.5987        | 3.0   | 3627 | 3.0803          | 18.4586 | 10.0134 | 17.6448 | 17.8592   |
| 3.4269        | 4.0   | 4836 | 3.0492          | 17.9493 | 8.9283  | 17.0803 | 17.1683   |
| 3.3213        | 5.0   | 6045 | 3.0466          | 18.124  | 8.967   | 17.4472 | 17.4445   |
| 3.2368        | 6.0   | 7254 | 3.0405          | 17.5527 | 8.4814  | 16.9722 | 17.0104   |
| 3.2039        | 7.0   | 8463 | 3.0335          | 17.5116 | 8.2969  | 17.006  | 17.0084   |
| 3.1834        | 8.0   | 9672 | 3.0282          | 17.629  | 8.5256  | 17.1329 | 17.1403   |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1
