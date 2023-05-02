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
- name: wav2vec2-base-ks-linear_lrX10
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-ks-linear_lrX10

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the superb dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0471
- Accuracy: 0.6686

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
| 1.6226        | 1.0   | 50   | 1.7588          | 0.6209   |
| 1.382         | 2.0   | 100  | 1.5696          | 0.6209   |
| 1.2373        | 3.0   | 150  | 1.3818          | 0.6212   |
| 1.1019        | 4.0   | 200  | 1.2577          | 0.6228   |
| 0.9831        | 5.0   | 250  | 1.1826          | 0.6331   |
| 0.9241        | 6.0   | 300  | 1.1200          | 0.6481   |
| 0.8695        | 7.0   | 350  | 1.0821          | 0.6581   |
| 0.8529        | 8.0   | 400  | 1.0632          | 0.6652   |
| 0.8385        | 9.0   | 450  | 1.0494          | 0.6677   |
| 0.8162        | 10.0  | 500  | 1.0471          | 0.6686   |


### Framework versions

- Transformers 4.22.0.dev0
- Pytorch 1.11.0+cu115
- Datasets 2.4.0
- Tokenizers 0.12.1
