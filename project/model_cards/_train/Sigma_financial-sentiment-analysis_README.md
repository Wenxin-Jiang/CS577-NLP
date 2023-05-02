---
tags:
- generated_from_trainer
datasets:
- financial_phrasebank
metrics:
- accuracy
- f1
model-index:
- name: financial-sentiment-analysis
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: financial_phrasebank
      type: financial_phrasebank
      args: sentences_allagree
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9924242424242424
    - name: F1
      type: f1
      value: 0.9924242424242424
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# financial-sentiment-analysis

This model is a fine-tuned version of [ahmedrachid/FinancialBERT](https://huggingface.co/ahmedrachid/FinancialBERT) on the financial_phrasebank dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0395
- Accuracy: 0.9924
- F1: 0.9924

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
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results



### Framework versions

- Transformers 4.19.1
- Pytorch 1.11.0+cu113
- Datasets 2.2.1
- Tokenizers 0.12.1
