---
tags:
- generated_from_trainer
datasets:
- wmt16
metrics:
- bleu
model_index:
- name: opus-mt-en-ro-finetuned-en-to-ro
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: wmt16
      type: wmt16
      args: ro-en
    metric:
      name: Bleu
      type: bleu
      value: 28.1641
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# opus-mt-en-ro-finetuned-en-to-ro

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-en-ro](https://huggingface.co/Helsinki-NLP/opus-mt-en-ro) on the wmt16 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2886
- Bleu: 28.1641
- Gen Len: 34.1071

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

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|
| 0.7436        | 1.0   | 38145 | 1.2886          | 28.1641 | 34.1071 |


### Framework versions

- Transformers 4.9.1
- Pytorch 1.9.0+cu102
- Datasets 1.10.2
- Tokenizers 0.10.3
