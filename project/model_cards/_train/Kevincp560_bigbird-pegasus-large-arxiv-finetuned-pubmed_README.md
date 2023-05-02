---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- pub_med_summarization_dataset
metrics:
- rouge
model-index:
- name: bigbird-pegasus-large-arxiv-finetuned-pubmed
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
      value: 45.4807
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bigbird-pegasus-large-arxiv-finetuned-pubmed

This model is a fine-tuned version of [google/bigbird-pegasus-large-arxiv](https://huggingface.co/google/bigbird-pegasus-large-arxiv) on the pub_med_summarization_dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6049
- Rouge1: 45.4807
- Rouge2: 20.0199
- Rougel: 28.3621
- Rougelsum: 41.4618
- Gen Len: 219.144

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 2.594         | 1.0   | 500  | 1.9879          | 33.6364 | 13.5074 | 21.4286 | 29.7158   | 189.014 |
| 1.9146        | 2.0   | 1000 | 1.6494          | 44.0056 | 19.0069 | 27.5142 | 40.0492   | 210.528 |
| 1.7378        | 3.0   | 1500 | 1.6213          | 44.7071 | 19.3559 | 27.6806 | 40.6124   | 213.596 |
| 1.692         | 4.0   | 2000 | 1.6081          | 45.1505 | 19.7355 | 28.06   | 41.0108   | 213.674 |
| 1.6656        | 5.0   | 2500 | 1.6049          | 45.4807 | 20.0199 | 28.3621 | 41.4618   | 219.144 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.9.1
- Datasets 1.18.4
- Tokenizers 0.11.6
