---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-efficient-base-finetuned-1.2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-efficient-base-finetuned-1.2

This model is a fine-tuned version of [google/t5-efficient-base](https://huggingface.co/google/t5-efficient-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5294
- Rouge1: 62.691
- Rouge2: 55.9731
- Rougel: 60.9097
- Rougelsum: 61.4393

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.6e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 4662
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 16

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| 2.2424        | 1.0   | 1217  | 1.7042          | 34.2215 | 24.2754 | 31.7289 | 32.4237   |
| 1.7716        | 2.0   | 2434  | 1.6184          | 43.4774 | 34.0476 | 41.3691 | 41.9132   |
| 1.6324        | 3.0   | 3651  | 1.5811          | 49.1441 | 40.7935 | 47.0077 | 47.6388   |
| 1.5226        | 4.0   | 4868  | 1.5243          | 54.4769 | 46.3387 | 52.3289 | 52.9555   |
| 1.4121        | 5.0   | 6085  | 1.5040          | 56.8792 | 49.1963 | 54.7327 | 55.2805   |
| 1.331         | 6.0   | 7302  | 1.4930          | 58.6896 | 51.1683 | 56.7096 | 57.3605   |
| 1.2677        | 7.0   | 8519  | 1.4785          | 59.9285 | 52.4631 | 57.8575 | 58.4203   |
| 1.2175        | 8.0   | 9736  | 1.4839          | 60.0299 | 52.8806 | 58.0099 | 58.6348   |
| 1.1782        | 9.0   | 10953 | 1.4908          | 61.247  | 54.0887 | 59.2175 | 59.7658   |
| 1.1442        | 10.0  | 12170 | 1.4882          | 61.9895 | 54.9455 | 60.0728 | 60.5786   |
| 1.1118        | 11.0  | 13387 | 1.5061          | 62.1077 | 55.1276 | 60.2218 | 60.7475   |
| 1.081         | 12.0  | 14604 | 1.5078          | 61.6083 | 54.6805 | 59.7912 | 60.2489   |
| 1.0668        | 13.0  | 15821 | 1.5200          | 62.3075 | 55.5201 | 60.5192 | 60.9557   |
| 1.0488        | 14.0  | 17038 | 1.5344          | 62.5144 | 55.6332 | 60.6845 | 61.1715   |
| 1.0324        | 15.0  | 18255 | 1.5313          | 62.7697 | 56.0313 | 60.9298 | 61.4739   |
| 1.0302        | 16.0  | 19472 | 1.5294          | 62.691  | 55.9731 | 60.9097 | 61.4393   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.3
- Tokenizers 0.11.6
