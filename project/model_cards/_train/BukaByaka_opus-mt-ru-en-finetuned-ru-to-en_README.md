---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wmt16
metrics:
- bleu
model-index:
- name: opus-mt-ru-en-finetuned-ru-to-en
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: wmt16
      type: wmt16
      args: ru-en
    metrics:
    - name: Bleu
      type: bleu
      value: 30.4049
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# opus-mt-ru-en-finetuned-ru-to-en

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-ru-en](https://huggingface.co/Helsinki-NLP/opus-mt-ru-en) on the wmt16 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4092
- Bleu: 30.4049
- Gen Len: 26.3911

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|
| 2.2606        | 1.0   | 94761 | 1.4092          | 30.4049 | 26.3911 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0.post202
- Datasets 2.3.2
- Tokenizers 0.12.1
