---
tags:
- generated_from_trainer
datasets:
- orange_sum
metrics:
- rouge
model-index:
- name: bert2gpt2SUMM-finetuned-mlsum-finetuned-mlorange_sum
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: orange_sum
      type: orange_sum
      args: abstract
    metrics:
    - name: Rouge1
      type: rouge
      value: 24.949
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

<img src="https://huggingface.co/Chemsseddine/bert2gpt2_med_ml_orange_summ-finetuned_med_sum_new-finetuned_med_sum_new/resolve/main/logobert2gpt2.png" alt="Map of positive probabilities per country." width="200"/>

# bert2gpt2SUMM-finetuned-mlsum-finetuned-mlorange_sum

This model is a fine-tuned version of [Chemsseddine/bert2gpt2SUMM-finetuned-mlsum](https://huggingface.co/Chemsseddine/bert2gpt2SUMM-finetuned-mlsum) on the orange_sum dataset.
It achieves the following results on the evaluation set:
- Loss: 3.1773
- Rouge1: 24.949
- Rouge2: 7.851
- Rougel: 18.1575
- Rougelsum: 18.4114
- Gen Len: 39.7947

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

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:-------:|:---------:|:-------:|
| 3.5484        | 1.0   | 1338 | 3.1773          | 24.949 | 7.851  | 18.1575 | 18.4114   | 39.7947 |


### Framework versions

- Transformers 4.20.0
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
