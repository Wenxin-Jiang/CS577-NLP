---
tags:
- generated_from_trainer
datasets:
- pub_med_summarization_dataset
metrics:
- rouge
model-index:
- name: pegasus-arxiv-finetuned-pubmed
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
      value: 44.286
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pegasus-arxiv-finetuned-pubmed

This model is a fine-tuned version of [google/pegasus-arxiv](https://huggingface.co/google/pegasus-arxiv) on the pub_med_summarization_dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8118
- Rouge1: 44.286
- Rouge2: 19.0477
- Rougel: 27.1122
- Rougelsum: 40.2609
- Gen Len: 230.586

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
| 2.65          | 1.0   | 1000 | 1.9848          | 40.6984 | 16.387  | 25.0097 | 36.4831   | 215.294 |
| 2.1317        | 2.0   | 2000 | 1.8524          | 43.6431 | 18.6794 | 26.7571 | 39.6642   | 224.646 |
| 2.0591        | 3.0   | 3000 | 1.8254          | 43.6707 | 18.5176 | 26.6015 | 39.6325   | 225.894 |
| 2.0109        | 4.0   | 4000 | 1.8138          | 44.1244 | 18.8866 | 26.8313 | 40.0913   | 229.656 |
| 1.9894        | 5.0   | 5000 | 1.8118          | 44.286  | 19.0477 | 27.1122 | 40.2609   | 230.586 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.9.1
- Datasets 1.18.4
- Tokenizers 0.11.6
