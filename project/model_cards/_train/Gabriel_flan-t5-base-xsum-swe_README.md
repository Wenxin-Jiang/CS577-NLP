---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: flan-t5-base-xsum-swe
  results: []

inference:
  parameters:
    temperature: 0.7
    min_length: 30
    max_length: 120

---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# flan-t5-base-xsum-swe

This model is a fine-tuned version of [google/flan-t5-base](https://huggingface.co/google/flan-t5-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4174
- Rouge1: 20.3004
- Rouge2: 6.2309
- Rougel: 17.5863
- Rougelsum: 17.5827
- Gen Len: 18.9998

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:------:|:-------:|:---------:|:-------:|
| 1.8384        | 1.0   | 12751 | 1.6491          | 19.0409 | 5.1339 | 16.3642 | 16.3725   | 19.0    |
| 1.6806        | 2.0   | 25502 | 1.5189          | 19.882  | 5.7451 | 17.1187 | 17.1233   | 19.0    |
| 1.5961        | 3.0   | 38253 | 1.4575          | 20.237  | 6.1009 | 17.4642 | 17.4647   | 18.9998 |
| 1.5556        | 4.0   | 51004 | 1.4268          | 20.2998 | 6.2217 | 17.5423 | 17.541    | 18.9998 |
| 1.5429        | 5.0   | 63755 | 1.4174          | 20.3004 | 6.2309 | 17.5863 | 17.5827   | 18.9998 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
