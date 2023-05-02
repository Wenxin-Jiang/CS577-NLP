---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- mtop
model-index:
- name: t5-base-pointer-mtop
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-pointer-mtop

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on the mtop dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1131
- Exact Match: 0.7199

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 64
- total_train_batch_size: 512
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 3000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Exact Match |
|:-------------:|:-----:|:----:|:---------------:|:-----------:|
| 1.7749        | 6.65  | 200  | 0.5892          | 0.0031      |
| 0.6021        | 13.33 | 400  | 0.5160          | 0.0139      |
| 0.6044        | 19.98 | 600  | 0.4080          | 0.0532      |
| 0.3302        | 26.65 | 800  | 0.1865          | 0.3620      |
| 0.1483        | 33.33 | 1000 | 0.1267          | 0.5105      |
| 0.0768        | 39.98 | 1200 | 0.1131          | 0.5298      |
| 0.0525        | 46.65 | 1400 | 0.1219          | 0.5414      |
| 0.0801        | 53.33 | 1600 | 0.1186          | 0.5275      |
| 0.0331        | 59.98 | 1800 | 0.1306          | 0.5423      |
| 0.0254        | 66.65 | 2000 | 0.1396          | 0.5396      |
| 0.0168        | 73.33 | 2200 | 0.1560          | 0.5436      |
| 0.0129        | 79.98 | 2400 | 0.1659          | 0.5494      |
| 0.0105        | 86.65 | 2600 | 0.1699          | 0.5423      |
| 0.0088        | 93.33 | 2800 | 0.1742          | 0.5472      |
| 0.0077        | 99.98 | 3000 | 0.1775          | 0.5468      |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu117
- Datasets 2.7.1
- Tokenizers 0.13.2
