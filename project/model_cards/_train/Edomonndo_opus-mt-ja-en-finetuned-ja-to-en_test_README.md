---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- bleu
model_index:
- name: opus-mt-ja-en-finetuned-ja-to-en_test
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    metric:
      name: Bleu
      type: bleu
      value: 80.2723
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# opus-mt-ja-en-finetuned-ja-to-en_test

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-ja-en](https://huggingface.co/Helsinki-NLP/opus-mt-ja-en) on an unkown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4737
- Bleu: 80.2723
- Gen Len: 16.5492

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|
| 1.1237        | 1.0   | 247  | 0.6131          | 60.9383 | 16.4152 |
| 0.5395        | 2.0   | 494  | 0.5274          | 67.5705 | 16.2883 |
| 0.3584        | 3.0   | 741  | 0.5122          | 71.3098 | 16.3777 |
| 0.2563        | 4.0   | 988  | 0.4887          | 73.6639 | 16.401  |
| 0.138         | 5.0   | 1235 | 0.4796          | 76.7942 | 16.4873 |
| 0.0979        | 6.0   | 1482 | 0.4849          | 76.9404 | 16.6162 |
| 0.0792        | 7.0   | 1729 | 0.4806          | 78.9831 | 16.5442 |
| 0.0569        | 8.0   | 1976 | 0.4765          | 79.3461 | 16.4873 |
| 0.0299        | 9.0   | 2223 | 0.4751          | 79.7901 | 16.4863 |
| 0.0204        | 10.0  | 2470 | 0.4737          | 80.2723 | 16.5492 |


### Framework versions

- Transformers 4.9.1
- Pytorch 1.9.0+cu111
- Datasets 1.10.2
- Tokenizers 0.10.3
