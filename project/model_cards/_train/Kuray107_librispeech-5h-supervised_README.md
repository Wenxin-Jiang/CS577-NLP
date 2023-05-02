---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: librispeech-5h-supervised
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# librispeech-5h-supervised

This model is a fine-tuned version of [facebook/wav2vec2-large-lv60](https://huggingface.co/facebook/wav2vec2-large-lv60) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2041
- Wer: 0.0624

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
- num_epochs: 100
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 3.7758        | 11.11 | 1000 | 0.3120          | 0.2337 |
| 0.1238        | 22.22 | 2000 | 0.1651          | 0.0826 |
| 0.0383        | 33.33 | 3000 | 0.1667          | 0.0712 |
| 0.023         | 44.44 | 4000 | 0.1893          | 0.0685 |
| 0.0166        | 55.56 | 5000 | 0.2008          | 0.0666 |
| 0.0131        | 66.67 | 6000 | 0.1942          | 0.0639 |
| 0.0106        | 77.78 | 7000 | 0.1979          | 0.0628 |
| 0.0091        | 88.89 | 8000 | 0.2027          | 0.0628 |
| 0.008         | 100.0 | 9000 | 0.2041          | 0.0624 |


### Framework versions

- Transformers 4.14.1
- Pytorch 1.10.2
- Datasets 1.18.2
- Tokenizers 0.10.3
