---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- pub_med_summarization_dataset
metrics:
- rouge
model-index:
- name: t5-small-finetuned-pubmed
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
      value: 8.8295
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-pubmed

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the pub_med_summarization_dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 2.2635
- Rouge1: 8.8295
- Rouge2: 3.2594
- Rougel: 7.9975
- Rougelsum: 8.4483
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

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2 | Rougel | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:------:|:------:|:---------:|:-------:|
| 2.5892        | 1.0   | 4000  | 2.3616          | 10.1169 | 3.9666 | 8.8854 | 9.5836    | 19.0    |
| 2.559         | 2.0   | 8000  | 2.3045          | 9.4321  | 3.5398 | 8.424  | 8.984     | 19.0    |
| 2.5029        | 3.0   | 12000 | 2.2820          | 9.1658  | 3.3686 | 8.2222 | 8.7311    | 19.0    |
| 2.4673        | 4.0   | 16000 | 2.2692          | 8.8973  | 3.2617 | 8.0395 | 8.5046    | 19.0    |
| 2.4331        | 5.0   | 20000 | 2.2635          | 8.8295  | 3.2594 | 7.9975 | 8.4483    | 19.0    |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.6
