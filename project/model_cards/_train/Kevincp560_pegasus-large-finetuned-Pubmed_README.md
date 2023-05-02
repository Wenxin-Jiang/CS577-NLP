---
tags:
- generated_from_trainer
datasets:
- pub_med_summarization_dataset
metrics:
- rouge
model-index:
- name: pegasus-large-finetuned-Pubmed
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
      value: 39.1107
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pegasus-large-finetuned-Pubmed

This model is a fine-tuned version of [google/pegasus-large](https://huggingface.co/google/pegasus-large) on the pub_med_summarization_dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7669
- Rouge1: 39.1107
- Rouge2: 15.4127
- Rougel: 24.3729
- Rougelsum: 35.1236
- Gen Len: 226.594

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
| 2.065         | 1.0   | 1000 | 1.8262          | 37.1986 | 14.3685 | 23.7153 | 33.0713   | 218.902 |
| 1.9552        | 2.0   | 2000 | 1.7933          | 38.0663 | 14.7813 | 23.8412 | 33.9574   | 217.488 |
| 1.8983        | 3.0   | 3000 | 1.7768          | 38.3975 | 15.0983 | 24.0247 | 34.314    | 222.32  |
| 1.882         | 4.0   | 4000 | 1.7687          | 39.1311 | 15.4167 | 24.2978 | 35.078    | 222.564 |
| 1.8456        | 5.0   | 5000 | 1.7669          | 39.1107 | 15.4127 | 24.3729 | 35.1236   | 226.594 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.9.1
- Datasets 1.18.4
- Tokenizers 0.11.6
