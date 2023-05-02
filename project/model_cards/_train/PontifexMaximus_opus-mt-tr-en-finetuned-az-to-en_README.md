---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- turkic_xwmt
metrics:
- bleu
model-index:
- name: opus-mt-tr-en-finetuned-az-to-en
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: turkic_xwmt
      type: turkic_xwmt
      args: az-en
    metrics:
    - name: Bleu
      type: bleu
      value: 0.0002
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# opus-mt-tr-en-finetuned-az-to-en

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-tr-en](https://huggingface.co/Helsinki-NLP/opus-mt-tr-en) on the turkic_xwmt dataset.
It achieves the following results on the evaluation set:
- Loss: nan
- Bleu: 0.0002
- Gen Len: 511.0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.2
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu   | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:------:|:-------:|
| No log        | 1.0   | 38   | nan             | 0.0002 | 511.0   |
| No log        | 2.0   | 76   | nan             | 0.0002 | 511.0   |
| No log        | 3.0   | 114  | nan             | 0.0002 | 511.0   |
| No log        | 4.0   | 152  | nan             | 0.0002 | 511.0   |
| No log        | 5.0   | 190  | nan             | 0.0002 | 511.0   |
| No log        | 6.0   | 228  | nan             | 0.0002 | 511.0   |
| No log        | 7.0   | 266  | nan             | 0.0002 | 511.0   |
| No log        | 8.0   | 304  | nan             | 0.0002 | 511.0   |
| No log        | 9.0   | 342  | nan             | 0.0002 | 511.0   |
| No log        | 10.0  | 380  | nan             | 0.0002 | 511.0   |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.1
- Tokenizers 0.12.1
