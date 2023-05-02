---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- conll2003
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: funnel-transformer-xlarge_ner_conll2003
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: conll2003
      type: conll2003
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.9565363315992617
    - name: Recall
      type: recall
      value: 0.9592729720632783
    - name: F1
      type: f1
      value: 0.9579026972523318
    - name: Accuracy
      type: accuracy
      value: 0.9914528250457537
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# funnel-transformer-xlarge_ner_conll2003

This model is a fine-tuned version of [funnel-transformer/xlarge](https://huggingface.co/funnel-transformer/xlarge) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0436
- Precision: 0.9565
- Recall: 0.9593
- F1: 0.9579
- Accuracy: 0.9915

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
- lr_scheduler_type: cosine
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1349        | 1.0   | 878  | 0.0441          | 0.9328    | 0.9438 | 0.9383 | 0.9881   |
| 0.0308        | 2.0   | 1756 | 0.0377          | 0.9457    | 0.9561 | 0.9509 | 0.9901   |
| 0.0144        | 3.0   | 2634 | 0.0432          | 0.9512    | 0.9578 | 0.9545 | 0.9906   |
| 0.007         | 4.0   | 3512 | 0.0419          | 0.9551    | 0.9584 | 0.9567 | 0.9913   |
| 0.0041        | 5.0   | 4390 | 0.0436          | 0.9565    | 0.9593 | 0.9579 | 0.9915   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
