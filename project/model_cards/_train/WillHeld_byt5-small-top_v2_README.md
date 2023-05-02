---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- top_v2
model-index:
- name: byt5-small-top_v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# byt5-small-top_v2

This model is a fine-tuned version of [google/byt5-small](https://huggingface.co/google/byt5-small) on the top_v2 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0164
- Exact Match: 0.8596

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 32
- total_train_batch_size: 512
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 3000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Exact Match |
|:-------------:|:-----:|:----:|:---------------:|:-----------:|
| 0.3962        | 0.82  | 200  | 0.0976          | 0.0061      |
| 0.0548        | 1.65  | 400  | 0.0281          | 0.0367      |
| 0.0277        | 2.47  | 600  | 0.0210          | 0.0396      |
| 0.0205        | 3.29  | 800  | 0.0192          | 0.0406      |
| 0.0172        | 4.12  | 1000 | 0.0185          | 0.0412      |
| 0.0145        | 4.94  | 1200 | 0.0168          | 0.0414      |
| 0.0127        | 5.76  | 1400 | 0.0165          | 0.0414      |
| 0.0113        | 6.58  | 1600 | 0.0164          | 0.0416      |
| 0.0101        | 7.41  | 1800 | 0.0167          | 0.0413      |
| 0.009         | 8.23  | 2000 | 0.0169          | 0.0417      |
| 0.0082        | 9.05  | 2200 | 0.0164          | 0.0416      |
| 0.0073        | 9.88  | 2400 | 0.0169          | 0.0416      |
| 0.0066        | 10.7  | 2600 | 0.0171          | 0.0417      |
| 0.0061        | 11.52 | 2800 | 0.0171          | 0.0417      |
| 0.0058        | 12.35 | 3000 | 0.0170          | 0.0416      |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.0
- Tokenizers 0.13.2
