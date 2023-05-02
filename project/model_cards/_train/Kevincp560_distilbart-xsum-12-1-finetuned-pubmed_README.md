---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- pub_med_summarization_dataset
metrics:
- rouge
model-index:
- name: distilbart-xsum-12-1-finetuned-pubmed
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
      value: 27.0012
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbart-xsum-12-1-finetuned-pubmed

This model is a fine-tuned version of [sshleifer/distilbart-xsum-12-1](https://huggingface.co/sshleifer/distilbart-xsum-12-1) on the pub_med_summarization_dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 2.8236
- Rouge1: 27.0012
- Rouge2: 12.728
- Rougel: 19.8685
- Rougelsum: 25.0485
- Gen Len: 59.969

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

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 3.3604        | 1.0   | 4000  | 3.1575          | 25.0078 | 11.5381 | 18.4246 | 23.1605   | 54.8935 |
| 3.0697        | 2.0   | 8000  | 2.9478          | 26.4947 | 12.5411 | 19.4328 | 24.6123   | 57.948  |
| 2.8638        | 3.0   | 12000 | 2.8672          | 26.8856 | 12.7568 | 19.8949 | 24.8745   | 59.6245 |
| 2.7243        | 4.0   | 16000 | 2.8347          | 26.7347 | 12.5152 | 19.6516 | 24.7756   | 60.439  |
| 2.6072        | 5.0   | 20000 | 2.8236          | 27.0012 | 12.728  | 19.8685 | 25.0485   | 59.969  |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.6
