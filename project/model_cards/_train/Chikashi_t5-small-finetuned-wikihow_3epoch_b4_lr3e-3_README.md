---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wikihow
metrics:
- rouge
model-index:
- name: t5-small-finetuned-wikihow_3epoch_b4_lr3e-3
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
      value: 26.7383
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-wikihow_3epoch_b4_lr3e-3

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the wikihow dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3400
- Rouge1: 26.7383
- Rouge2: 10.1981
- Rougel: 22.8642
- Rougelsum: 26.0922
- Gen Len: 18.524

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.003
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
| 3.2548        | 0.13  | 5000   | 2.9708          | 22.0519 | 6.7142  | 18.7677 | 21.4627   | 17.9546 |
| 3.1153        | 0.25  | 10000  | 2.9099          | 20.2838 | 5.8365  | 17.5009 | 19.7112   | 18.4981 |
| 3.0478        | 0.38  | 15000  | 2.8763          | 22.8282 | 7.3649  | 19.6843 | 22.2312   | 18.1331 |
| 3.0146        | 0.51  | 20000  | 2.8484          | 23.2465 | 7.4295  | 19.621  | 22.6246   | 18.5115 |
| 2.9572        | 0.64  | 25000  | 2.7902          | 23.8681 | 7.9617  | 20.4984 | 23.2066   | 18.5544 |
| 2.9425        | 0.76  | 30000  | 2.7577          | 23.4402 | 7.5289  | 19.7382 | 22.7941   | 18.4613 |
| 2.9075        | 0.89  | 35000  | 2.7343          | 23.0082 | 7.5408  | 19.8426 | 22.3832   | 18.1218 |
| 2.8705        | 1.02  | 40000  | 2.7136          | 23.9492 | 7.8861  | 20.3675 | 23.3035   | 18.4869 |
| 2.7967        | 1.14  | 45000  | 2.6923          | 24.2394 | 8.2895  | 20.7275 | 23.6127   | 18.3486 |
| 2.7794        | 1.27  | 50000  | 2.6639          | 24.4062 | 8.2481  | 20.8957 | 23.8077   | 18.4258 |
| 2.7776        | 1.4   | 55000  | 2.6321          | 24.6213 | 8.4161  | 21.0528 | 23.968    | 18.351  |
| 2.7397        | 1.53  | 60000  | 2.6116          | 24.16   | 8.3605  | 20.618  | 23.5037   | 18.6049 |
| 2.7199        | 1.65  | 65000  | 2.5846          | 24.2606 | 8.3829  | 20.6274 | 23.6252   | 18.4742 |
| 2.7044        | 1.78  | 70000  | 2.5663          | 25.0452 | 8.896   | 21.4554 | 24.4748   | 18.3143 |
| 2.6928        | 1.91  | 75000  | 2.5365          | 25.1312 | 9.008   | 21.6376 | 24.4963   | 18.5605 |
| 2.6281        | 2.03  | 80000  | 2.5209          | 25.5311 | 9.1521  | 21.729  | 24.8864   | 18.2597 |
| 2.5333        | 2.16  | 85000  | 2.4860          | 25.4834 | 9.2969  | 21.7257 | 24.8802   | 18.3831 |
| 2.5308        | 2.29  | 90000  | 2.4619          | 26.0526 | 9.605   | 22.2178 | 25.4353   | 18.4235 |
| 2.5136        | 2.42  | 95000  | 2.4356          | 25.9434 | 9.6537  | 22.2957 | 25.312    | 18.4647 |
| 2.4801        | 2.54  | 100000 | 2.4098          | 26.1109 | 9.7637  | 22.3844 | 25.4771   | 18.5765 |
| 2.4494        | 2.67  | 105000 | 2.3835          | 26.332  | 9.9472  | 22.4243 | 25.6933   | 18.5985 |
| 2.4393        | 2.8   | 110000 | 2.3590          | 26.6896 | 10.2248 | 22.8743 | 26.0665   | 18.4883 |
| 2.4071        | 2.93  | 115000 | 2.3400          | 26.7383 | 10.1981 | 22.8642 | 26.0922   | 18.524  |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
