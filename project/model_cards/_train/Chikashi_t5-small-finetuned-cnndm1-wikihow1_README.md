---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wikihow
metrics:
- rouge
model-index:
- name: t5-small-finetuned-cnndm1-wikihow1
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: wikihow
      type: wikihow
      args: all
    metrics:
    - name: Rouge1
      type: rouge
      value: 26.6881
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-cnndm1-wikihow1

This model is a fine-tuned version of [Chikashi/t5-small-finetuned-cnndm1-wikihow0](https://huggingface.co/Chikashi/t5-small-finetuned-cnndm1-wikihow0) on the wikihow dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3727
- Rouge1: 26.6881
- Rouge2: 9.9589
- Rougel: 22.6828
- Rougelsum: 26.0203
- Gen Len: 18.4813

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

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:------:|:-------:|:---------:|:-------:|
| 2.56          | 1.0   | 39313 | 2.3727          | 26.6881 | 9.9589 | 22.6828 | 26.0203   | 18.4813 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.1.0
- Tokenizers 0.12.1
