---
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: rubert-base-cased-sentence-finetuned-sent_in_news_sents
  results:
  - task:
      name: Text Classification
      type: text-classification
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.7224199288256228
    - name: F1
      type: f1
      value: 0.5137303178348194
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# rubert-base-cased-sentence-finetuned-sent_in_news_sents

This model is a fine-tuned version of [DeepPavlov/rubert-base-cased-sentence](https://huggingface.co/DeepPavlov/rubert-base-cased-sentence) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9506
- Accuracy: 0.7224
- F1: 0.5137

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 14
- eval_batch_size: 14
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| No log        | 1.0   | 81   | 1.0045          | 0.6690   | 0.1388 |
| No log        | 2.0   | 162  | 0.9574          | 0.6228   | 0.2980 |
| No log        | 3.0   | 243  | 1.0259          | 0.6477   | 0.3208 |
| No log        | 4.0   | 324  | 1.1262          | 0.6619   | 0.4033 |
| No log        | 5.0   | 405  | 1.3377          | 0.6299   | 0.3909 |
| No log        | 6.0   | 486  | 1.5716          | 0.6868   | 0.3624 |
| 0.6085        | 7.0   | 567  | 1.6286          | 0.6762   | 0.4130 |
| 0.6085        | 8.0   | 648  | 1.6450          | 0.6940   | 0.4775 |
| 0.6085        | 9.0   | 729  | 1.7108          | 0.7224   | 0.4920 |
| 0.6085        | 10.0  | 810  | 1.8792          | 0.7046   | 0.5028 |
| 0.6085        | 11.0  | 891  | 1.8670          | 0.7153   | 0.4992 |
| 0.6085        | 12.0  | 972  | 1.8856          | 0.7153   | 0.4934 |
| 0.0922        | 13.0  | 1053 | 1.9506          | 0.7224   | 0.5137 |
| 0.0922        | 14.0  | 1134 | 2.0363          | 0.7189   | 0.4761 |
| 0.0922        | 15.0  | 1215 | 2.0601          | 0.7224   | 0.5053 |
| 0.0922        | 16.0  | 1296 | 2.0813          | 0.7153   | 0.5038 |
| 0.0922        | 17.0  | 1377 | 2.0960          | 0.7189   | 0.5065 |
| 0.0922        | 18.0  | 1458 | 2.1060          | 0.7224   | 0.5098 |
| 0.0101        | 19.0  | 1539 | 2.1153          | 0.7260   | 0.5086 |
| 0.0101        | 20.0  | 1620 | 2.1187          | 0.7260   | 0.5086 |


### Framework versions

- Transformers 4.10.3
- Pytorch 1.9.0+cu102
- Datasets 1.12.1
- Tokenizers 0.10.3
