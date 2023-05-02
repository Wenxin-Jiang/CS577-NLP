---
tags:
- generated_from_trainer
datasets:
- pub_med_summarization_dataset
metrics:
- rouge
model-index:
- name: pegasus-cnn_dailymail-finetuned-pubmed
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: pub_med_summarization_dataset
      type: pub_med_summarization_dataset
      args: document
    metrics:
    - name: Rouge1
      type: rouge
      value: 37.2569
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pegasus-cnn_dailymail-finetuned-pubmed

This model is a fine-tuned version of [google/pegasus-cnn_dailymail](https://huggingface.co/google/pegasus-cnn_dailymail) on the pub_med_summarization_dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8050
- Rouge1: 37.2569
- Rouge2: 15.8205
- Rougel: 24.1969
- Rougelsum: 34.0331
- Gen Len: 125.892

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 2.2449        | 1.0   | 1000 | 1.8942          | 36.4494 | 14.9948 | 23.8279 | 33.3081   | 124.482 |
| 2.0803        | 2.0   | 2000 | 1.8440          | 36.998  | 15.4992 | 24.091  | 33.6614   | 125.678 |
| 2.0166        | 3.0   | 3000 | 1.8176          | 37.4703 | 16.0358 | 24.5735 | 34.1789   | 125.094 |
| 1.9911        | 4.0   | 4000 | 1.8055          | 37.1338 | 15.7921 | 24.1412 | 33.8293   | 125.874 |
| 1.9419        | 5.0   | 5000 | 1.8050          | 37.2569 | 15.8205 | 24.1969 | 34.0331   | 125.892 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.9.1
- Datasets 1.18.4
- Tokenizers 0.11.6
