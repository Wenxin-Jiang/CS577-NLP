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

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on the Xlsum dataset.
It achieves the following results on the evaluation set:
- Loss: 2.7436
- Rouge1: 9.3908
- Rouge2: 2.5077
- RougeL: 7.8615
- Rougelsum: 7.8745

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|:------:|:---------:|
| 3.8301        | 1.0   | 3375  | 2.8828          | 8.1957 | 1.9439 | 6.8031 | 6.8206    |
| 3.4032        | 2.0   | 6750  | 2.8049          | 8.9533 | 2.2919 | 7.4137 | 7.4244    |
| 3.3697        | 3.0   | 10125 | 2.7743          | 9.3366 | 2.4531 | 7.8129 | 7.8276    |
| 3.3862        | 4.0   | 13500 | 2.7500          | 9.4377 | 2.542  | 7.9123 | 7.9268    |
| 3.1704        | 5.0   | 16875 | 2.7436          | 9.3908 | 2.5077 | 7.8615 | 7.8745    |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.1
- Tokenizers 0.12.1
