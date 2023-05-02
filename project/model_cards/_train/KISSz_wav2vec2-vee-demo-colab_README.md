---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
model_index:
  name: wav2vec2-vee-demo-colab
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-vee-demo-colab

This model is a fine-tuned version of [airesearch/wav2vec2-large-xlsr-53-th](https://huggingface.co/airesearch/wav2vec2-large-xlsr-53-th) on an unkown dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 8
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 1

### Training results



### Framework versions

- Transformers 4.9.1
- Pytorch 1.9.0+cpu
- Datasets 1.11.0
- Tokenizers 0.10.3
