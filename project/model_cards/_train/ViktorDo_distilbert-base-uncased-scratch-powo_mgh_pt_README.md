---
tags:
- generated_from_trainer
model-index:
- name: distilbert-base-uncased-scratch-powo_mgh_pt
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-scratch-powo_mgh_pt

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.0408

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
- train_batch_size: 5
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 40
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 6.4584        | 0.2   | 200  | 4.7806          |
| 4.6385        | 0.41  | 400  | 4.3704          |
| 4.2219        | 0.61  | 600  | 4.0727          |
| 3.994         | 0.81  | 800  | 3.8772          |
| 3.8048        | 1.01  | 1000 | 3.6894          |
| 3.6722        | 1.22  | 1200 | 3.5732          |
| 3.4828        | 1.42  | 1400 | 3.4203          |
| 3.3648        | 1.62  | 1600 | 3.3634          |
| 3.3918        | 1.83  | 1800 | 3.2685          |
| 3.3919        | 2.03  | 2000 | 3.2027          |
| 3.1715        | 2.23  | 2200 | 3.1365          |
| 3.0635        | 2.43  | 2400 | 3.1228          |
| 3.0804        | 2.64  | 2600 | 3.0595          |
| 3.0468        | 2.84  | 2800 | 3.0318          |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
