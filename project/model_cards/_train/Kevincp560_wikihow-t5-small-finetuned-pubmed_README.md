---
tags:
- generated_from_trainer
datasets:
- pub_med_summarization_dataset
metrics:
- rouge
model-index:
- name: wikihow-t5-small-finetuned-pubmed
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
      value: 8.9619
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wikihow-t5-small-finetuned-pubmed

This model is a fine-tuned version of [deep-learning-analytics/wikihow-t5-small](https://huggingface.co/deep-learning-analytics/wikihow-t5-small) on the pub_med_summarization_dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 2.2702
- Rouge1: 8.9619
- Rouge2: 3.2719
- Rougel: 8.1558
- Rougelsum: 8.5714
- Gen Len: 19.0

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
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|:------:|:---------:|:-------:|
| 2.5984        | 1.0   | 4000  | 2.3696          | 10.237 | 3.8609 | 8.9776 | 9.677     | 19.0    |
| 2.5677        | 2.0   | 8000  | 2.3132          | 9.302  | 3.4499 | 8.3816 | 8.8831    | 19.0    |
| 2.5038        | 3.0   | 12000 | 2.2884          | 9.0578 | 3.3103 | 8.23   | 8.6723    | 19.0    |
| 2.4762        | 4.0   | 16000 | 2.2758          | 9.0001 | 3.2882 | 8.1845 | 8.6084    | 19.0    |
| 2.4393        | 5.0   | 20000 | 2.2702          | 8.9619 | 3.2719 | 8.1558 | 8.5714    | 19.0    |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.6
