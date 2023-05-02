---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: squad-bn-mt5-base2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# squad-bn-mt5-base2

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5309
- Rouge1 Precision: 37.5039
- Rouge1 Recall: 30.4476
- Rouge1 Fmeasure: 32.6695
- Rouge2 Precision: 16.2843
- Rouge2 Recall: 12.9093
- Rouge2 Fmeasure: 13.9246
- Rougel Precision: 35.2648
- Rougel Recall: 28.6919
- Rougel Fmeasure: 30.7578
- Rougelsum Precision: 35.2646
- Rougelsum Recall: 28.6829
- Rougelsum Fmeasure: 30.7527
- Bleu-1: 23.9098
- Bleu-2: 14.7458
- Bleu-3: 9.684
- Bleu-4: 6.6217
- Meteor: 0.142

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1 Precision | Rouge1 Recall | Rouge1 Fmeasure | Rouge2 Precision | Rouge2 Recall | Rouge2 Fmeasure | Rougel Precision | Rougel Recall | Rougel Fmeasure | Rougelsum Precision | Rougelsum Recall | Rougelsum Fmeasure | Bleu-1  | Bleu-2  | Bleu-3 | Bleu-4 | Meteor |
|:-------------:|:-----:|:-----:|:---------------:|:----------------:|:-------------:|:---------------:|:----------------:|:-------------:|:---------------:|:----------------:|:-------------:|:---------------:|:-------------------:|:----------------:|:------------------:|:-------:|:-------:|:------:|:------:|:------:|
| 0.698         | 1.0   | 6769  | 0.5654          | 35.1173          | 28.5689       | 30.6164         | 14.7565          | 11.6885       | 12.6012         | 33.0241          | 26.9309       | 28.8245         | 33.0061             | 26.9075          | 28.807             | 22.6163 | 13.6841 | 8.8346 | 5.926  | 0.1314 |
| 0.6202        | 2.0   | 13538 | 0.5437          | 36.3795          | 29.5116       | 31.6675         | 15.5398          | 12.3022       | 13.2805         | 34.3036          | 27.8749       | 29.8881         | 34.2498             | 27.8384          | 29.8439            | 23.2744 | 14.1999 | 9.2715 | 6.2908 | 0.1364 |
| 0.5878        | 3.0   | 20307 | 0.5322          | 37.2522          | 30.1185       | 32.3701         | 16.0437          | 12.6396       | 13.6664         | 35.0062          | 28.3657       | 30.4487         | 34.9742             | 28.3319          | 30.4195            | 23.7569 | 14.5781 | 9.5429 | 6.52   | 0.1407 |
| 0.5761        | 4.0   | 27076 | 0.5309          | 37.5             | 30.4513       | 32.6723         | 16.2813          | 12.9079       | 13.9284         | 35.2662          | 28.6924       | 30.755          | 35.2509             | 28.6759          | 30.7444            | 23.9098 | 14.7458 | 9.684  | 6.6217 | 0.142  |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.2
