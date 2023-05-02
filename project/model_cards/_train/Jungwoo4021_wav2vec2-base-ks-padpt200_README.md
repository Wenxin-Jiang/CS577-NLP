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
- name: wav2vec2-base-ks-padpt200
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-ks-padpt200

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the superb dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6540
- Accuracy: 0.6037

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
| 1.2728        | 1.0   | 50   | 1.6540          | 0.6037   |
| 0.8498        | 2.0   | 100  | 1.2559          | 0.6015   |
| 0.7563        | 3.0   | 150  | 1.4192          | 0.5035   |
| 0.701         | 4.0   | 200  | 1.3318          | 0.5641   |
| 0.6592        | 5.0   | 250  | 1.3236          | 0.5666   |
| 0.6404        | 6.0   | 300  | 1.3653          | 0.5469   |
| 0.6315        | 7.0   | 350  | 1.4052          | 0.5082   |
| 0.6306        | 8.0   | 400  | 1.2818          | 0.5590   |
| 0.6297        | 9.0   | 450  | 1.3096          | 0.5659   |
| 0.6056        | 10.0  | 500  | 1.3595          | 0.5368   |


### Framework versions

- Transformers 4.22.0.dev0
- Pytorch 1.11.0+cu115
- Datasets 2.4.0
- Tokenizers 0.12.1
