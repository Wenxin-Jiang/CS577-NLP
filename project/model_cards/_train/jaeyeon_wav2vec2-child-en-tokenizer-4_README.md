---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-child-en-tokenizer-4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-child-en-tokenizer-4

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4709
- Wer: 0.3769

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
- train_batch_size: 24
- eval_batch_size: 24
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 48
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.0334        | 1.72  | 100  | 1.4709          | 0.3769 |
| 0.0332        | 3.45  | 200  | 1.4709          | 0.3769 |
| 0.0343        | 5.17  | 300  | 1.4709          | 0.3769 |
| 0.032         | 6.9   | 400  | 1.4709          | 0.3769 |
| 0.0332        | 8.62  | 500  | 1.4709          | 0.3769 |
| 0.0327        | 10.34 | 600  | 1.4709          | 0.3769 |
| 0.0331        | 12.07 | 700  | 1.4709          | 0.3769 |
| 0.0334        | 13.79 | 800  | 1.4709          | 0.3769 |
| 0.0319        | 15.52 | 900  | 1.4709          | 0.3769 |
| 0.0338        | 17.24 | 1000 | 1.4709          | 0.3769 |
| 0.0321        | 18.97 | 1100 | 1.4709          | 0.3769 |
| 0.0367        | 20.69 | 1200 | 1.4709          | 0.3769 |
| 0.0331        | 22.41 | 1300 | 1.4709          | 0.3769 |
| 0.0332        | 24.14 | 1400 | 1.4709          | 0.3769 |
| 0.0347        | 25.86 | 1500 | 1.4709          | 0.3769 |
| 0.0319        | 27.59 | 1600 | 1.4709          | 0.3769 |
| 0.0302        | 29.31 | 1700 | 1.4709          | 0.3769 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3
