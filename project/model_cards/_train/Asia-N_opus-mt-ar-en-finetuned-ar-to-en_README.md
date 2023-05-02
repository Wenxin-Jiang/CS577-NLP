---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- news_commentary
metrics:
- bleu
model-index:
- name: opus-mt-ar-en-finetuned-ar-to-en
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: news_commentary
      type: news_commentary
      args: ar-en
    metrics:
    - name: Bleu
      type: bleu
      value: 32.5327
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# opus-mt-ar-en-finetuned-ar-to-en

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-ar-en](https://huggingface.co/Helsinki-NLP/opus-mt-ar-en) on the news_commentary dataset.
It achieves the following results on the evaluation set:
- Loss: 10.6102
- Bleu: 32.5327
- Gen Len: 56.234

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-09
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|
| No log        | 1.0   | 32   | 10.6112         | 32.5327 | 56.234  |
| No log        | 2.0   | 64   | 10.6103         | 32.5327 | 56.234  |
| No log        | 3.0   | 96   | 10.6102         | 32.5327 | 56.234  |


### Framework versions

- Transformers 4.20.0
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
