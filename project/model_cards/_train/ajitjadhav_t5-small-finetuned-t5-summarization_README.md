---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- cnn_dailymail
metrics:
- rouge
model-index:
- name: t5-small-finetuned-t5-summarization
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: cnn_dailymail
      type: cnn_dailymail
      config: 3.0.0
      split: train
      args: 3.0.0
    metrics:
    - name: Rouge1
      type: rouge
      value: 24.5755
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-t5-summarization

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the cnn_dailymail dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7613
- Rouge1: 24.5755
- Rouge2: 11.8424
- Rougel: 20.3031
- Rougelsum: 23.1867
- Gen Len: 18.9999

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 6e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step   | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:------:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 1.9891        | 1.0   | 17945  | 1.7981          | 24.382  | 11.7099 | 20.1707 | 23.0021   | 18.9998 |
| 1.9527        | 2.0   | 35890  | 1.7816          | 24.4884 | 11.7673 | 20.2698 | 23.1233   | 19.0    |
| 1.9421        | 3.0   | 53835  | 1.7728          | 24.5782 | 11.8401 | 20.3343 | 23.2033   | 18.9997 |
| 1.9298        | 4.0   | 71780  | 1.7677          | 24.566  | 11.8723 | 20.3296 | 23.1943   | 18.9999 |
| 1.9256        | 5.0   | 89725  | 1.7619          | 24.5662 | 11.8385 | 20.3265 | 23.2016   | 18.9999 |
| 1.9056        | 6.0   | 107670 | 1.7613          | 24.5755 | 11.8424 | 20.3031 | 23.1867   | 18.9999 |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
