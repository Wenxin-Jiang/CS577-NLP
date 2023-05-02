---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- pub_med_summarization_dataset
metrics:
- rouge
model-index:
- name: bart-large-finetuned-pubmed
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
      value: 10.946
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-large-finetuned-pubmed

This model is a fine-tuned version of [facebook/bart-large](https://huggingface.co/facebook/bart-large) on the pub_med_summarization_dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8135
- Rouge1: 10.946
- Rouge2: 5.0933
- Rougel: 9.5608
- Rougelsum: 10.4259
- Gen Len: 19.0495

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
| 2.0861        | 1.0   | 4000  | 1.8909          | 8.7344  | 3.6919 | 7.8804 | 8.3305    | 20.0    |
| 1.8996        | 2.0   | 8000  | 1.8261          | 10.2124 | 4.6212 | 8.9842 | 9.7417    | 17.632  |
| 1.7459        | 3.0   | 12000 | 1.8160          | 9.4933  | 4.4117 | 8.3977 | 9.0758    | 16.4775 |
| 1.6258        | 4.0   | 16000 | 1.8136          | 10.8248 | 5.0335 | 9.4286 | 10.3123   | 18.724  |
| 1.5214        | 5.0   | 20000 | 1.8135          | 10.946  | 5.0933 | 9.5608 | 10.4259   | 19.0495 |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.6
