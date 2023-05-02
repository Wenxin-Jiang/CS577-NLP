---
license: apache-2.0
tags:
- multilingual model
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mt5-small-finetuned-multilingual-xlsum-new
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-small-finetuned-multilingual-xlsum-new

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.7673
- Rouge1: 9.1368
- Rouge2: 2.3893
- Rougel: 7.6599
- Rougelsum: 7.6873

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|
| 3.7827        | 1.0   | 1687 | 2.8911          | 8.1314 | 1.9569 | 6.7927 | 6.8179    |
| 3.6518        | 2.0   | 3374 | 2.8338          | 8.6621 | 2.1437 | 7.2171 | 7.246     |
| 3.3691        | 3.0   | 5061 | 2.8015          | 8.9402 | 2.2733 | 7.4744 | 7.497     |
| 3.4435        | 4.0   | 6748 | 2.7746          | 9.0514 | 2.3627 | 7.6144 | 7.6358    |
| 3.5139        | 5.0   | 8435 | 2.7673          | 9.1368 | 2.3893 | 7.6599 | 7.6873    |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
