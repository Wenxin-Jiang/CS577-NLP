---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- syssr_en_ar
metrics:
- bleu
model-index:
- name: opus-mt-en-ar-finetuned-dummyData-10-10-ar-to-en
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: syssr_en_ar
      type: syssr_en_ar
      args: default
    metrics:
    - name: Bleu
      type: bleu
      value: 7.9946
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# opus-mt-en-ar-finetuned-dummyData-10-10-ar-to-en

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-en-ar](https://huggingface.co/Helsinki-NLP/opus-mt-en-ar) on the syssr_en_ar dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2046
- Bleu: 7.9946
- Gen Len: 20.0

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
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu   | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:------:|:-------:|
| No log        | 1.0   | 1    | 1.2038          | 7.9946 | 20.0    |
| No log        | 2.0   | 2    | 1.2038          | 7.9946 | 20.0    |
| No log        | 3.0   | 3    | 1.2038          | 7.9946 | 20.0    |
| No log        | 4.0   | 4    | 1.2036          | 7.9946 | 20.0    |
| No log        | 5.0   | 5    | 1.2046          | 7.9946 | 20.0    |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.0+cu111
- Datasets 1.12.1
- Tokenizers 0.10.3
