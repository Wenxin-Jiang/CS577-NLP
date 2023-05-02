---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- opus_infopankki
metrics:
- bleu
model-index:
- name: opus-mt-tr-en-finetuned-tr-to-en
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: opus_infopankki
      type: opus_infopankki
      args: en-tr
    metrics:
    - name: Bleu
      type: bleu
      value: 54.7617
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# opus-mt-tr-en-finetuned-tr-to-en

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-tr-en](https://huggingface.co/Helsinki-NLP/opus-mt-tr-en) on the opus_infopankki dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6924
- Bleu: 54.7617
- Gen Len: 13.5501

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-06
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 16
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|
| No log        | 1.0   | 412  | 1.1776          | 43.3104 | 12.9297 |
| 1.4032        | 2.0   | 824  | 1.0750          | 45.7912 | 12.9155 |
| 1.2268        | 3.0   | 1236 | 1.0019          | 47.6255 | 12.9251 |
| 1.141         | 4.0   | 1648 | 0.9411          | 49.0649 | 12.9302 |
| 1.0651        | 5.0   | 2060 | 0.8929          | 50.4894 | 12.9066 |
| 1.0651        | 6.0   | 2472 | 0.8519          | 51.5072 | 12.9067 |
| 1.0025        | 7.0   | 2884 | 0.8180          | 52.5035 | 12.8875 |
| 0.9582        | 8.0   | 3296 | 0.7893          | 51.7587 | 13.5338 |
| 0.9173        | 9.0   | 3708 | 0.7655          | 52.3566 | 13.5376 |
| 0.8892        | 10.0  | 4120 | 0.7449          | 53.0488 | 13.5545 |
| 0.8639        | 11.0  | 4532 | 0.7285          | 53.5965 | 13.5539 |
| 0.8639        | 12.0  | 4944 | 0.7152          | 53.9433 | 13.5547 |
| 0.8424        | 13.0  | 5356 | 0.7053          | 54.2509 | 13.5502 |
| 0.8317        | 14.0  | 5768 | 0.6981          | 54.5339 | 13.5502 |
| 0.817         | 15.0  | 6180 | 0.6938          | 54.7068 | 13.5448 |
| 0.8155        | 16.0  | 6592 | 0.6924          | 54.7617 | 13.5501 |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.7.1+cu110
- Datasets 2.2.2
- Tokenizers 0.12.1
