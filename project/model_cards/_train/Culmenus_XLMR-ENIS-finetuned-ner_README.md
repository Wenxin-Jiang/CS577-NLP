---
license: agpl-3.0
tags:
- generated_from_trainer
datasets:
- mim_gold_ner
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: XLMR-ENIS-finetuned-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: mim_gold_ner
      type: mim_gold_ner
      args: mim-gold-ner
    metrics:
    - name: Precision
      type: precision
      value: 0.8803619696791632
    - name: Recall
      type: recall
      value: 0.8517339397384878
    - name: F1
      type: f1
      value: 0.8658113730929264
    - name: Accuracy
      type: accuracy
      value: 0.9837103244207861
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# XLMR-ENIS-finetuned-ner

This model is a fine-tuned version of [vesteinn/XLMR-ENIS](https://huggingface.co/vesteinn/XLMR-ENIS) on the mim_gold_ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0891
- Precision: 0.8804
- Recall: 0.8517
- F1: 0.8658
- Accuracy: 0.9837

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0573        | 1.0   | 2904 | 0.1024          | 0.8608    | 0.8003 | 0.8295 | 0.9799   |
| 0.0307        | 2.0   | 5808 | 0.0899          | 0.8707    | 0.8380 | 0.8540 | 0.9825   |
| 0.0198        | 3.0   | 8712 | 0.0891          | 0.8804    | 0.8517 | 0.8658 | 0.9837   |


### Framework versions

- Transformers 4.11.2
- Pytorch 1.9.0+cu102
- Datasets 1.12.1
- Tokenizers 0.10.3
