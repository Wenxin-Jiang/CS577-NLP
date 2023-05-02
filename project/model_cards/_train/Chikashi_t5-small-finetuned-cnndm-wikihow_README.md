---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wikihow
metrics:
- rouge
model-index:
- name: t5-small-finetuned-cnndm-wikihow
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
      value: 27.5037
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-cnndm-wikihow

This model is a fine-tuned version of [Sevil/t5-small-finetuned-cnndm_3epoch_v2](https://huggingface.co/Sevil/t5-small-finetuned-cnndm_3epoch_v2) on the wikihow dataset.
It achieves the following results on the evaluation set:
- Loss: 2.2653
- Rouge1: 27.5037
- Rouge2: 10.8442
- Rougel: 23.4674
- Rougelsum: 26.7997
- Gen Len: 18.5558

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
| 2.8459        | 0.13  | 5000   | 2.5755          | 25.2929 | 8.7852  | 21.2379 | 24.5649   | 18.4758 |
| 2.7251        | 0.25  | 10000  | 2.5189          | 25.33   | 9.0505  | 21.4892 | 24.6523   | 18.4513 |
| 2.6696        | 0.38  | 15000  | 2.4805          | 26.3909 | 9.6858  | 22.3589 | 25.7297   | 18.4649 |
| 2.647         | 0.51  | 20000  | 2.4491          | 25.9234 | 9.3936  | 22.0086 | 25.2342   | 18.5558 |
| 2.5973        | 0.64  | 25000  | 2.4251          | 26.4988 | 9.8197  | 22.6201 | 25.8407   | 18.3438 |
| 2.5916        | 0.76  | 30000  | 2.4022          | 26.3149 | 9.8432  | 22.3695 | 25.6581   | 18.4506 |
| 2.5691        | 0.89  | 35000  | 2.3801          | 26.4198 | 9.8848  | 22.4856 | 25.7847   | 18.5381 |
| 2.5365        | 1.02  | 40000  | 2.3755          | 26.5846 | 10.0287 | 22.667  | 25.9606   | 18.5608 |
| 2.4649        | 1.14  | 45000  | 2.3663          | 26.5925 | 10.0569 | 22.6191 | 25.9247   | 18.5803 |
| 2.4539        | 1.27  | 50000  | 2.3490          | 26.9735 | 10.2389 | 22.9536 | 26.282    | 18.5126 |
| 2.4578        | 1.4   | 55000  | 2.3374          | 26.7878 | 10.2275 | 22.849  | 26.1188   | 18.6162 |
| 2.4365        | 1.53  | 60000  | 2.3266          | 27.1171 | 10.403  | 23.0596 | 26.4284   | 18.6128 |
| 2.428         | 1.65  | 65000  | 2.3209          | 27.1762 | 10.578  | 23.1577 | 26.5007   | 18.5246 |
| 2.4293        | 1.78  | 70000  | 2.3145          | 27.0896 | 10.5146 | 23.1502 | 26.4338   | 18.4604 |
| 2.4335        | 1.91  | 75000  | 2.2979          | 27.3373 | 10.6273 | 23.2944 | 26.6725   | 18.5403 |
| 2.3981        | 2.03  | 80000  | 2.3008          | 27.1857 | 10.6455 | 23.1333 | 26.5203   | 18.5412 |
| 2.3395        | 2.16  | 85000  | 2.2908          | 27.3123 | 10.7063 | 23.3126 | 26.626    | 18.4265 |
| 2.3463        | 2.29  | 90000  | 2.2869          | 27.5328 | 10.7662 | 23.4527 | 26.8613   | 18.5664 |
| 2.3481        | 2.42  | 95000  | 2.2802          | 27.4799 | 10.7826 | 23.4538 | 26.7912   | 18.5449 |
| 2.3345        | 2.54  | 100000 | 2.2774          | 27.3182 | 10.724  | 23.3276 | 26.669    | 18.5908 |
| 2.3254        | 2.67  | 105000 | 2.2713          | 27.3942 | 10.777  | 23.3918 | 26.7036   | 18.5681 |
| 2.3369        | 2.8   | 110000 | 2.2666          | 27.5976 | 10.9144 | 23.5832 | 26.9147   | 18.5471 |
| 2.3269        | 2.93  | 115000 | 2.2653          | 27.5037 | 10.8442 | 23.4674 | 26.7997   | 18.5558 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
