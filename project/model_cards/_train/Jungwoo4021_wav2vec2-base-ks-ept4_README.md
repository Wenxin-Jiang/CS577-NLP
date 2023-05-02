---
license: apache-2.0
tags:
- audio-classification
- generated_from_trainer
datasets:
- superb
metrics:
- accuracy
model-index:
- name: wav2vec2-base-ks-ept4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-ks-ept4

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the superb dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5663
- Accuracy: 0.6209

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
- train_batch_size: 256
- eval_batch_size: 256
- seed: 0
- gradient_accumulation_steps: 4
- total_train_batch_size: 1024
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.5133        | 1.0   | 50   | 1.5663          | 0.6209   |
| 1.4819        | 2.0   | 100  | 1.5675          | 0.6169   |
| 1.4082        | 3.0   | 150  | 1.5372          | 0.5802   |
| 1.3536        | 4.0   | 200  | 1.6716          | 0.5338   |
| 1.296         | 5.0   | 250  | 1.7601          | 0.5399   |
| 1.3053        | 6.0   | 300  | 1.6778          | 0.5630   |
| 1.2734        | 7.0   | 350  | 1.6554          | 0.5734   |
| 1.2837        | 8.0   | 400  | 1.7338          | 0.5741   |
| 1.2682        | 9.0   | 450  | 1.7313          | 0.5774   |
| 1.2776        | 10.0  | 500  | 1.7083          | 0.5791   |


### Framework versions

- Transformers 4.22.0.dev0
- Pytorch 1.11.0+cu115
- Datasets 2.4.0
- Tokenizers 0.12.1
