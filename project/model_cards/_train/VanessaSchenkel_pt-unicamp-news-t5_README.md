---
tags:
- translation
- generated_from_trainer
datasets:
- news_commentary
metrics:
- bleu
model-index:
- name: pt-unicamp-news
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: news_commentary
      type: news_commentary
      config: en-pt
      split: train
      args: en-pt
    metrics:
    - name: Bleu
      type: bleu
      value: 39.16010441514751
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pt-unicamp-news

This model is a fine-tuned version of [unicamp-dl/translation-en-pt-t5](https://huggingface.co/unicamp-dl/translation-en-pt-t5) on the news_commentary dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2849
- Bleu: 39.1601

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
- train_batch_size: 32
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- Transformers 4.22.0
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
