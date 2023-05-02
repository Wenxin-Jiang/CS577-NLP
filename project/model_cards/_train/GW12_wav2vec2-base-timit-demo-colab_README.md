---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-base-timit-demo-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-timit-demo-colab

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4234
- Wer: 0.2752

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
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 3.5378        | 1.73  | 500  | 1.3767          | 0.8694 |
| 0.6656        | 3.46  | 1000 | 0.4546          | 0.3897 |
| 0.3113        | 5.19  | 1500 | 0.3904          | 0.3470 |
| 0.1922        | 6.92  | 2000 | 0.3746          | 0.3178 |
| 0.1433        | 8.65  | 2500 | 0.3837          | 0.3120 |
| 0.1146        | 10.38 | 3000 | 0.3520          | 0.3016 |
| 0.0946        | 12.11 | 3500 | 0.3713          | 0.3096 |
| 0.0793        | 13.84 | 4000 | 0.4005          | 0.3021 |
| 0.0667        | 15.57 | 4500 | 0.4141          | 0.2941 |
| 0.0565        | 17.3  | 5000 | 0.4006          | 0.2888 |
| 0.0514        | 19.03 | 5500 | 0.4050          | 0.2908 |
| 0.0466        | 20.76 | 6000 | 0.3882          | 0.2844 |
| 0.0387        | 22.49 | 6500 | 0.4054          | 0.2806 |
| 0.0337        | 24.22 | 7000 | 0.4094          | 0.2800 |
| 0.0312        | 25.95 | 7500 | 0.4291          | 0.2815 |
| 0.0278        | 27.68 | 8000 | 0.3999          | 0.2761 |
| 0.0251        | 29.41 | 8500 | 0.4234          | 0.2752 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0
- Datasets 1.13.3
- Tokenizers 0.10.3
