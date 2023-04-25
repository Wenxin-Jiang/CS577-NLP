---
license: gpl-3.0
tags:
- generated_from_trainer
datasets:
- mim_gold_ner
metrics:
- precision
- recall
- f1
- accuracy
widget:
- text: Systurnar Guðrún og Monique átu einar á McDonalds og horfðu á Stöð 2, þar glitti í Bruce Willis leika í Die Hard 2.
model-index:
- name: IceBERT-finetuned-ner
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
      value: 0.89397115028973
    - name: Recall
      type: recall
      value: 0.8664117576771418
    - name: F1
      type: f1
      value: 0.8799757281553399
    - name: Accuracy
      type: accuracy
      value: 0.9854156499755994
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# IceBERT-finetuned-ner

This model is a fine-tuned version of [vesteinn/IceBERT](https://huggingface.co/vesteinn/IceBERT) on the mim_gold_ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0802
- Precision: 0.8940
- Recall: 0.8664
- F1: 0.8800
- Accuracy: 0.9854

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
| 0.0528        | 1.0   | 2904 | 0.0779          | 0.8829    | 0.8504 | 0.8663 | 0.9831   |
| 0.0274        | 2.0   | 5808 | 0.0784          | 0.8802    | 0.8585 | 0.8692 | 0.9839   |
| 0.0162        | 3.0   | 8712 | 0.0802          | 0.8940    | 0.8664 | 0.8800 | 0.9854   |


### Framework versions

- Transformers 4.11.1
- Pytorch 1.9.0+cu102
- Datasets 1.12.1
- Tokenizers 0.10.3
