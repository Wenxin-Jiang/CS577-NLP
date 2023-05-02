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
- name: wav2vec2-base-ks-finetuning
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-ks-finetuning

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the superb dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2261
- Accuracy: 0.9813

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
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
| 1.6773        | 1.0   | 50   | 1.6218          | 0.6209   |
| 1.4707        | 2.0   | 100  | 1.4400          | 0.6209   |
| 1.1387        | 3.0   | 150  | 1.0470          | 0.6599   |
| 0.7909        | 4.0   | 200  | 0.6997          | 0.8903   |
| 0.5488        | 5.0   | 250  | 0.4567          | 0.9640   |
| 0.4195        | 6.0   | 300  | 0.3288          | 0.9754   |
| 0.3445        | 7.0   | 350  | 0.2598          | 0.9809   |
| 0.3107        | 8.0   | 400  | 0.2261          | 0.9813   |
| 0.2781        | 9.0   | 450  | 0.2104          | 0.9810   |
| 0.2729        | 10.0  | 500  | 0.2050          | 0.9813   |


### Framework versions

- Transformers 4.22.0.dev0
- Pytorch 1.11.0+cu115
- Datasets 2.4.0
- Tokenizers 0.12.1
