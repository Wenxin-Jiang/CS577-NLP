---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: output
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2822
- Wer: 0.2423
- Cer: 0.0842

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

I have used dataset other than mozila common voice, thats why for fair evaluation, i do 80:20 split. 


## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 48
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 192
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Cer    | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:------:|:---------------:|:------:|
| No log        | 1.0   | 174  | 0.9860 | 3.1257          | 1.0    |
| No log        | 2.0   | 348  | 0.9404 | 2.4914          | 0.9997 |
| No log        | 3.0   | 522  | 0.1889 | 0.5970          | 0.5376 |
| No log        | 4.0   | 696  | 0.1428 | 0.4462          | 0.4121 |
| No log        | 5.0   | 870  | 0.1211 | 0.3775          | 0.3525 |
| 1.7           | 6.0   | 1044 | 0.1113 | 0.3594          | 0.3264 |
| 1.7           | 7.0   | 1218 | 0.1032 | 0.3354          | 0.3013 |
| 1.7           | 8.0   | 1392 | 0.1005 | 0.3171          | 0.2843 |
| 1.7           | 9.0   | 1566 | 0.0953 | 0.3115          | 0.2717 |
| 1.7           | 10.0  | 1740 | 0.0934 | 0.3058          | 0.2671 |
| 1.7           | 11.0  | 1914 | 0.0926 | 0.3060          | 0.2656 |
| 0.3585        | 12.0  | 2088 | 0.0899 | 0.3070          | 0.2566 |
| 0.3585        | 13.0  | 2262 | 0.0888 | 0.2979          | 0.2509 |
| 0.3585        | 14.0  | 2436 | 0.0868 | 0.3005          | 0.2473 |
| 0.3585        | 15.0  | 2610 | 0.2822 | 0.2423          | 0.0842 |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0
- Datasets 2.4.0
- Tokenizers 0.12.1
