---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- xsum
metrics:
- rouge
model-index:
- name: t5-small-finetuned-xsum-512
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: xsum
      type: xsum
      args: default
    metrics:
    - name: Rouge1
      type: rouge
      value: 28.8448
      
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-xsum-512

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the xsum dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4706
- Rouge1: 28.8448
- Rouge2: 7.9819
- Rougel: 22.8686
- Rougelsum: 22.8754
- Gen Len: 18.7654


T5, zero-shot on the same evaluation set:
`{'rouge1': 19.2304, 'rouge2': 2.5842, 'rougeL': 13.9683, 'rougeLsum': 15.516}`

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:-------:|:---------:|:-------:|
| 2.7057        | 1.0   | 7854 | 2.4706          | 28.8448 | 7.9819 | 22.8686 | 22.8754   | 18.7654 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.2
- Datasets 2.1.0
- Tokenizers 0.12.1
