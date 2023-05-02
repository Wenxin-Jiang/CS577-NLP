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
- name: wav2vec2-base-ks-linear_lrX100
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-ks-linear_lrX100

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the superb dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6970
- Accuracy: 0.8001

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
| 1.1789        | 1.0   | 50   | 1.3621          | 0.6225   |
| 0.636         | 2.0   | 100  | 0.9176          | 0.6912   |
| 0.5575        | 3.0   | 150  | 0.8543          | 0.7376   |
| 0.5289        | 4.0   | 200  | 0.6970          | 0.8001   |
| 0.4926        | 5.0   | 250  | 0.8232          | 0.7548   |
| 0.4831        | 6.0   | 300  | 0.7442          | 0.7755   |
| 0.4539        | 7.0   | 350  | 0.7484          | 0.7785   |
| 0.4816        | 8.0   | 400  | 0.7038          | 0.7982   |
| 0.4666        | 9.0   | 450  | 0.7277          | 0.7764   |
| 0.4417        | 10.0  | 500  | 0.7289          | 0.7870   |


### Framework versions

- Transformers 4.22.0.dev0
- Pytorch 1.11.0+cu115
- Datasets 2.4.0
- Tokenizers 0.12.1
