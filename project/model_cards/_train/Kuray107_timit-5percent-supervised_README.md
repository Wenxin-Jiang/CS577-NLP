---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: timit-5percent-supervised
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# timit-5percent-supervised

This model is a fine-tuned version of [facebook/wav2vec2-large-lv60](https://huggingface.co/facebook/wav2vec2-large-lv60) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6615
- Wer: 0.2788

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 200
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 5.3773        | 33.33  | 500  | 2.9693          | 1.0    |
| 1.4746        | 66.67  | 1000 | 0.5050          | 0.3359 |
| 0.1067        | 100.0  | 1500 | 0.5981          | 0.3054 |
| 0.0388        | 133.33 | 2000 | 0.6192          | 0.2712 |
| 0.0244        | 166.67 | 2500 | 0.6392          | 0.2776 |
| 0.018         | 200.0  | 3000 | 0.6615          | 0.2788 |


### Framework versions

- Transformers 4.14.1
- Pytorch 1.10.2
- Datasets 1.18.2
- Tokenizers 0.10.3
