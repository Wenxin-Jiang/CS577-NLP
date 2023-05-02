---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- pub_med_summarization_dataset
metrics:
- rouge
model-index:
- name: distilbart-cnn-12-6-finetuned-pubmed
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
      value: 40.0985
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbart-cnn-12-6-finetuned-pubmed

This model is a fine-tuned version of [sshleifer/distilbart-cnn-12-6](https://huggingface.co/sshleifer/distilbart-cnn-12-6) on the pub_med_summarization_dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9895
- Rouge1: 40.0985
- Rouge2: 16.5016
- Rougel: 24.8319
- Rougelsum: 36.0775
- Gen Len: 141.884

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
| 2.1709        | 1.0   | 4000  | 2.0257          | 38.1012 | 15.112  | 23.4064 | 33.9373   | 141.9195 |
| 1.9495        | 2.0   | 8000  | 1.9593          | 39.529  | 16.1693 | 24.487  | 35.5238   | 141.9785 |
| 1.756         | 3.0   | 12000 | 1.9488          | 39.9623 | 16.5799 | 24.949  | 35.9194   | 141.8855 |
| 1.6032        | 4.0   | 16000 | 1.9732          | 39.672  | 16.1994 | 24.5996 | 35.7021   | 141.921  |
| 1.4817        | 5.0   | 20000 | 1.9895          | 40.0985 | 16.5016 | 24.8319 | 36.0775   | 141.884  |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.6
