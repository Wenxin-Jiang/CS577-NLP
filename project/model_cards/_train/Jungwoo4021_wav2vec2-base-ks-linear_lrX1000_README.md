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
- name: wav2vec2-base-ks-linear_lrX1000
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-ks-linear_lrX1000

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the superb dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5661
- Accuracy: 0.8325

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.03
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
| 0.7558        | 1.0   | 50   | 1.0584          | 0.6462   |
| 0.5971        | 2.0   | 100  | 0.7816          | 0.7510   |
| 0.5382        | 3.0   | 150  | 0.7870          | 0.7520   |
| 0.5045        | 4.0   | 200  | 0.6647          | 0.7880   |
| 0.4717        | 5.0   | 250  | 1.1572          | 0.6053   |
| 0.4651        | 6.0   | 300  | 0.6387          | 0.7945   |
| 0.4205        | 7.0   | 350  | 0.5661          | 0.8325   |
| 0.4423        | 8.0   | 400  | 0.7100          | 0.7846   |
| 0.426         | 9.0   | 450  | 0.7054          | 0.7829   |
| 0.4067        | 10.0  | 500  | 0.6288          | 0.8114   |


### Framework versions

- Transformers 4.22.0.dev0
- Pytorch 1.11.0+cu115
- Datasets 2.4.0
- Tokenizers 0.12.1
