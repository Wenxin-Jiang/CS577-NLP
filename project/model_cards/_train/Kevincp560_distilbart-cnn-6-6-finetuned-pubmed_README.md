---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- pub_med_summarization_dataset
metrics:
- rouge
model-index:
- name: distilbart-cnn-6-6-finetuned-pubmed
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
      value: 39.2769
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbart-cnn-6-6-finetuned-pubmed

This model is a fine-tuned version of [sshleifer/distilbart-cnn-6-6](https://huggingface.co/sshleifer/distilbart-cnn-6-6) on the pub_med_summarization_dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 2.0648
- Rouge1: 39.2769
- Rouge2: 15.876
- Rougel: 24.2306
- Rougelsum: 35.267
- Gen Len: 141.8565

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
| 2.2215        | 1.0   | 4000  | 2.0781          | 37.2476 | 14.2852 | 22.6875 | 33.1607   | 141.97   |
| 2.0105        | 2.0   | 8000  | 2.0217          | 37.8038 | 14.7869 | 23.2025 | 33.7069   | 141.918  |
| 1.8331        | 3.0   | 12000 | 2.0243          | 39.0497 | 15.8077 | 24.2237 | 34.9371   | 141.822  |
| 1.6936        | 4.0   | 16000 | 2.0487          | 38.7059 | 15.4364 | 23.8514 | 34.7771   | 141.878  |
| 1.5817        | 5.0   | 20000 | 2.0648          | 39.2769 | 15.876  | 24.2306 | 35.267    | 141.8565 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.6
