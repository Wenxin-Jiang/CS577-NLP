---
license: mit
tags:
- generated_from_trainer
datasets:
- pub_med_summarization_dataset
metrics:
- rouge
model-index:
- name: bart-large-cnn-finetuned-pubmed
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
      value: 40.4866
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-large-cnn-finetuned-pubmed

This model is a fine-tuned version of [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn) on the pub_med_summarization_dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8416
- Rouge1: 40.4866
- Rouge2: 16.7472
- Rougel: 24.9831
- Rougelsum: 36.4002
- Gen Len: 142.0

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

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len  |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:--------:|
| 1.932         | 1.0   | 4000  | 1.8110          | 38.1151 | 15.2255 | 23.4286 | 34.2521   | 141.8905 |
| 1.7001        | 2.0   | 8000  | 1.7790          | 39.8217 | 16.3042 | 24.649  | 35.831    | 142.0    |
| 1.5           | 3.0   | 12000 | 1.7971          | 40.6108 | 17.0446 | 25.1977 | 36.5556   | 141.9865 |
| 1.3316        | 4.0   | 16000 | 1.8106          | 40.0466 | 16.4851 | 24.7094 | 36.0998   | 141.9335 |
| 1.1996        | 5.0   | 20000 | 1.8416          | 40.4866 | 16.7472 | 24.9831 | 36.4002   | 142.0    |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.6
