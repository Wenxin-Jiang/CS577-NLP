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
- name: wav2vec2-base-ft-keyword-spotting
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-ft-keyword-spotting

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the superb dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0795
- Accuracy: 0.9829

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 0
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 5.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.5546        | 1.0   | 399  | 0.4250          | 0.9618   |
| 0.2128        | 2.0   | 798  | 0.1331          | 0.9781   |
| 0.1763        | 3.0   | 1197 | 0.0935          | 0.9807   |
| 0.1485        | 4.0   | 1596 | 0.0852          | 0.9828   |
| 0.1335        | 5.0   | 1995 | 0.0795          | 0.9829   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.10.0+cu111
- Datasets 2.7.1
- Tokenizers 0.13.2
