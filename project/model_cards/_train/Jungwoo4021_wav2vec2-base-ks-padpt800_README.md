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
- name: wav2vec2-base-ks-padpt800
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-ks-padpt800

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the superb dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5281
- Accuracy: 0.6142

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
| 1.328         | 1.0   | 50   | 1.5281          | 0.6142   |
| 0.9328        | 2.0   | 100  | 1.3054          | 0.5853   |
| 0.8277        | 3.0   | 150  | 1.3858          | 0.4966   |
| 0.7689        | 4.0   | 200  | 1.4112          | 0.4975   |
| 0.7154        | 5.0   | 250  | 1.4042          | 0.5035   |
| 0.706         | 6.0   | 300  | 1.3635          | 0.5171   |
| 0.6878        | 7.0   | 350  | 1.4373          | 0.4873   |
| 0.6868        | 8.0   | 400  | 1.2890          | 0.5505   |
| 0.6705        | 9.0   | 450  | 1.3019          | 0.5405   |
| 0.6579        | 10.0  | 500  | 1.3337          | 0.5272   |


### Framework versions

- Transformers 4.22.0.dev0
- Pytorch 1.11.0+cu115
- Datasets 2.4.0
- Tokenizers 0.12.1
