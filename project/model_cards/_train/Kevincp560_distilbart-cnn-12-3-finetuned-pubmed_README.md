---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- pub_med_summarization_dataset
metrics:
- rouge
model-index:
- name: distilbart-cnn-12-3-finetuned-pubmed
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
      value: 40.5642
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbart-cnn-12-3-finetuned-pubmed

This model is a fine-tuned version of [sshleifer/distilbart-cnn-12-3](https://huggingface.co/sshleifer/distilbart-cnn-12-3) on the pub_med_summarization_dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1743
- Rouge1: 40.5642
- Rouge2: 16.9812
- Rougel: 25.3449
- Rougelsum: 36.46
- Gen Len: 141.95

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
| 2.469         | 1.0   | 4000  | 2.2956          | 38.3713 | 15.2594 | 23.6734 | 34.1634   | 141.707  |
| 2.2527        | 2.0   | 8000  | 2.1994          | 39.5939 | 16.2376 | 24.6363 | 35.5106   | 141.831  |
| 2.0669        | 3.0   | 12000 | 2.1780          | 40.078  | 16.6705 | 25.1119 | 35.9605   | 141.8475 |
| 1.9275        | 4.0   | 16000 | 2.1669          | 40.0825 | 16.6169 | 24.9702 | 36.0191   | 141.928  |
| 1.8102        | 5.0   | 20000 | 2.1743          | 40.5642 | 16.9812 | 25.3449 | 36.46     | 141.95   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.6
