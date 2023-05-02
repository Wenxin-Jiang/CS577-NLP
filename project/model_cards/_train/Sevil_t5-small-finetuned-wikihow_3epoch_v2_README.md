---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wikihow
metrics:
- rouge
model-index:
- name: t5-small-finetuned-wikihow_3epoch_v2
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: wikihow
      type: wikihow
      args: all
    metrics:
    - name: Rouge1
      type: rouge
      value: 27.48
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-wikihow_3epoch_v2

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the wikihow dataset.
It achieves the following results on the evaluation set:
- Loss: 2.2758
- Rouge1: 27.48
- Rouge2: 10.7621
- Rougel: 23.4136
- Rougelsum: 26.7923
- Gen Len: 18.5424

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step   | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:------:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 2.8423        | 0.13  | 5000   | 2.5715          | 25.2685 | 8.6964  | 21.229  | 24.5773   | 18.4479 |
| 2.7345        | 0.25  | 10000  | 2.5236          | 24.982  | 8.7823  | 21.1609 | 24.3066   | 18.3631 |
| 2.6811        | 0.38  | 15000  | 2.4911          | 25.7585 | 9.3372  | 21.8388 | 25.1052   | 18.3997 |
| 2.6611        | 0.51  | 20000  | 2.4510          | 26.022  | 9.4708  | 22.0899 | 25.3236   | 18.5472 |
| 2.6133        | 0.64  | 25000  | 2.4272          | 26.3481 | 9.6769  | 22.4484 | 25.7046   | 18.3863 |
| 2.6083        | 0.76  | 30000  | 2.4108          | 26.4131 | 9.6643  | 22.4021 | 25.6958   | 18.5585 |
| 2.5842        | 0.89  | 35000  | 2.3866          | 26.2852 | 9.7505  | 22.4525 | 25.5908   | 18.5485 |
| 2.5554        | 1.02  | 40000  | 2.3816          | 26.3018 | 9.7218  | 22.3673 | 25.6515   | 18.4912 |
| 2.4895        | 1.14  | 45000  | 2.3730          | 26.6439 | 9.9665  | 22.6593 | 25.9521   | 18.5635 |
| 2.4781        | 1.27  | 50000  | 2.3541          | 26.8488 | 10.0364 | 22.8202 | 26.1598   | 18.4254 |
| 2.4821        | 1.4   | 55000  | 2.3440          | 26.9511 | 10.2079 | 23.0133 | 26.2821   | 18.5712 |
| 2.4593        | 1.53  | 60000  | 2.3370          | 26.945  | 10.3123 | 22.9245 | 26.2493   | 18.5978 |
| 2.4521        | 1.65  | 65000  | 2.3309          | 26.9652 | 10.314  | 22.9657 | 26.298    | 18.4837 |
| 2.4523        | 1.78  | 70000  | 2.3249          | 27.0548 | 10.4204 | 23.1286 | 26.379    | 18.4717 |
| 2.4563        | 1.91  | 75000  | 2.3079          | 27.4563 | 10.6452 | 23.3985 | 26.7812   | 18.5642 |
| 2.4229        | 2.03  | 80000  | 2.3115          | 27.0538 | 10.44   | 22.9957 | 26.349    | 18.5914 |
| 2.3694        | 2.16  | 85000  | 2.3017          | 27.332  | 10.6556 | 23.3135 | 26.629    | 18.459  |
| 2.3749        | 2.29  | 90000  | 2.2941          | 27.3294 | 10.5967 | 23.2039 | 26.6411   | 18.5179 |
| 2.3779        | 2.42  | 95000  | 2.2891          | 27.3725 | 10.6539 | 23.3455 | 26.707    | 18.5367 |
| 2.3638        | 2.54  | 100000 | 2.2895          | 27.3487 | 10.6738 | 23.2894 | 26.681    | 18.6128 |
| 2.3549        | 2.67  | 105000 | 2.2833          | 27.408  | 10.6903 | 23.3575 | 26.7137   | 18.6035 |
| 2.3652        | 2.8   | 110000 | 2.2788          | 27.561  | 10.8202 | 23.4672 | 26.8584   | 18.5565 |
| 2.3553        | 2.93  | 115000 | 2.2758          | 27.48   | 10.7621 | 23.4136 | 26.7923   | 18.5424 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6