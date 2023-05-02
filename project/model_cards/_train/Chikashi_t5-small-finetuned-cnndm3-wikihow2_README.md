---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- cnn_dailymail
metrics:
- rouge
model-index:
- name: t5-small-finetuned-cnndm3-wikihow2
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: cnn_dailymail
      type: cnn_dailymail
      args: 3.0.0
    metrics:
    - name: Rouge1
      type: rouge
      value: 24.6704
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-cnndm3-wikihow2

This model is a fine-tuned version of [Chikashi/t5-small-finetuned-cnndm2-wikihow2](https://huggingface.co/Chikashi/t5-small-finetuned-cnndm2-wikihow2) on the cnn_dailymail dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6265
- Rouge1: 24.6704
- Rouge2: 11.9038
- Rougel: 20.3622
- Rougelsum: 23.2612
- Gen Len: 18.9997

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 1.8071        | 1.0   | 71779 | 1.6265          | 24.6704 | 11.9038 | 20.3622 | 23.2612   | 18.9997 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.1.0
- Tokenizers 0.12.1
