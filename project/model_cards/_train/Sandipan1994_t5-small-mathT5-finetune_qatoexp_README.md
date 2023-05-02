---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- math_qa
metrics:
- rouge
model-index:
- name: t5-small-mathT5-finetune_qatoexp
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: math_qa
      type: math_qa
      config: default
      split: train
      args: default
    metrics:
    - name: Rouge1
      type: rouge
      value: 21.9174
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-mathT5-finetune_qatoexp

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the math_qa dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8677
- Rouge1: 21.9174
- Rouge2: 8.4401
- Rougel: 19.1645
- Rougelsum: 19.8239
- Gen Len: 18.9765

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

We have trained T5-small on MathQA dataset for sequence to sequence generation of explanations from given math problem.
## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 10
- eval_batch_size: 10
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:------:|:-------:|:---------:|:-------:|
| 2.4496        | 1.0   | 2984  | 2.2096          | 19.6477 | 6.508  | 16.9295 | 17.5212   | 18.9064 |
| 2.2893        | 2.0   | 5968  | 2.0837          | 20.4879 | 7.2528 | 17.7778 | 18.4085   | 18.968  |
| 2.1869        | 3.0   | 8952  | 2.0125          | 20.8462 | 7.6105 | 18.1516 | 18.8343   | 18.9837 |
| 2.1456        | 4.0   | 11936 | 1.9633          | 20.7623 | 7.7113 | 18.1274 | 18.783    | 18.9886 |
| 2.1171        | 5.0   | 14920 | 1.9321          | 21.0648 | 7.8897 | 18.4162 | 19.0551   | 18.9844 |
| 2.0854        | 6.0   | 17904 | 1.9061          | 21.4445 | 8.0883 | 18.8038 | 19.4176   | 18.9812 |
| 2.0592        | 7.0   | 20888 | 1.8902          | 21.5714 | 8.2751 | 18.8864 | 19.537    | 18.9772 |
| 2.0609        | 8.0   | 23872 | 1.8770          | 21.7737 | 8.3297 | 19.022  | 19.6897   | 18.9763 |
| 2.0285        | 9.0   | 26856 | 1.8701          | 21.964  | 8.4358 | 19.1701 | 19.845    | 18.9747 |
| 2.0165        | 10.0  | 29840 | 1.8677          | 21.9174 | 8.4401 | 19.1645 | 19.8239   | 18.9765 |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu113
- Datasets 2.5.2
- Tokenizers 0.12.1
