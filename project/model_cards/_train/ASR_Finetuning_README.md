---
tags:
- generated_from_trainer
model-index:
- name: CV11_finetuning1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CV11_finetuning1

This model is a fine-tuned version of [Roshana/Wav2Vec1_CV](https://huggingface.co/Roshana/Wav2Vec1_CV) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7162
- Wer: 0.3625

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.5067        | 0.86  | 400  | 0.6193          | 0.4492 |
| 0.4448        | 1.72  | 800  | 0.6325          | 0.4384 |
| 0.3781        | 2.59  | 1200 | 0.6248          | 0.4197 |
| 0.3172        | 3.45  | 1600 | 0.6408          | 0.4343 |
| 0.2556        | 4.31  | 2000 | 0.6593          | 0.4230 |
| 0.2148        | 5.17  | 2400 | 0.6742          | 0.3987 |
| 0.1779        | 6.03  | 2800 | 0.6658          | 0.3929 |
| 0.1446        | 6.9   | 3200 | 0.6768          | 0.3846 |
| 0.1248        | 7.76  | 3600 | 0.6809          | 0.3804 |
| 0.108         | 8.62  | 4000 | 0.7214          | 0.3683 |
| 0.0938        | 9.48  | 4400 | 0.7162          | 0.3625 |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1
