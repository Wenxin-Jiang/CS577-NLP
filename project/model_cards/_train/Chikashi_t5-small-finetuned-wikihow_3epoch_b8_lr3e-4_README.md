---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wikihow
metrics:
- rouge
model-index:
- name: t5-small-finetuned-wikihow_3epoch_b8_lr3e-4
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
      value: 27.3718
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-wikihow_3epoch_b8_lr3e-4

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the wikihow dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3136
- Rouge1: 27.3718
- Rouge2: 10.6235
- Rougel: 23.3396
- Rougelsum: 26.6889
- Gen Len: 18.5194

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 2.8029        | 0.25  | 5000  | 2.5368          | 25.2267 | 8.9048  | 21.2588 | 24.5804   | 18.4303 |
| 2.6924        | 0.51  | 10000 | 2.4725          | 25.6553 | 9.1904  | 21.7633 | 24.9807   | 18.5549 |
| 2.6369        | 0.76  | 15000 | 2.4332          | 26.2895 | 9.7203  | 22.3286 | 25.6009   | 18.4185 |
| 2.5994        | 1.02  | 20000 | 2.4051          | 26.1779 | 9.5708  | 22.3531 | 25.5357   | 18.561  |
| 2.521         | 1.27  | 25000 | 2.3805          | 26.7558 | 10.0411 | 22.7252 | 26.0476   | 18.304  |
| 2.5091        | 1.53  | 30000 | 2.3625          | 26.6439 | 10.0698 | 22.6662 | 25.9537   | 18.5437 |
| 2.4941        | 1.78  | 35000 | 2.3498          | 26.9322 | 10.2817 | 23.0002 | 26.2604   | 18.4953 |
| 2.4848        | 2.03  | 40000 | 2.3424          | 27.0381 | 10.3452 | 22.9749 | 26.3407   | 18.5749 |
| 2.4268        | 2.29  | 45000 | 2.3272          | 27.2386 | 10.4595 | 23.1866 | 26.5541   | 18.4954 |
| 2.4263        | 2.54  | 50000 | 2.3226          | 27.1489 | 10.532  | 23.1428 | 26.4657   | 18.5583 |
| 2.4161        | 2.8   | 55000 | 2.3136          | 27.3718 | 10.6235 | 23.3396 | 26.6889   | 18.5194 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
