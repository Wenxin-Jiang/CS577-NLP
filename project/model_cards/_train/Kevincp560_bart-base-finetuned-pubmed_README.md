---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- pub_med_summarization_dataset
metrics:
- rouge
model-index:
- name: bart-base-finetuned-pubmed
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
      value: 9.3963
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-base-finetuned-pubmed

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on the pub_med_summarization_dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 2.0277
- Rouge1: 9.3963
- Rouge2: 4.0473
- Rougel: 8.4526
- Rougelsum: 8.9659
- Gen Len: 20.0

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
| 2.3706        | 1.0   | 4000  | 2.1245          | 9.1644 | 3.8264 | 8.2223 | 8.718     | 20.0    |
| 2.2246        | 2.0   | 8000  | 2.0811          | 9.023  | 3.7716 | 8.1453 | 8.5998    | 20.0    |
| 2.1034        | 3.0   | 12000 | 2.0469          | 9.4412 | 4.0783 | 8.4949 | 8.9977    | 20.0    |
| 2.0137        | 4.0   | 16000 | 2.0390          | 9.2261 | 3.9307 | 8.3154 | 8.7937    | 20.0    |
| 1.9288        | 5.0   | 20000 | 2.0277          | 9.3963 | 4.0473 | 8.4526 | 8.9659    | 20.0    |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.6
