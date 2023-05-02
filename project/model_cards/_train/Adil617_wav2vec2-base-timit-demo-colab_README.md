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
- Loss: 2.9314
- Wer: 1.0

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
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer |
|:-------------:|:-----:|:----:|:---------------:|:---:|
| 8.686         | 0.16  | 20   | 13.6565         | 1.0 |
| 8.0711        | 0.32  | 40   | 12.5379         | 1.0 |
| 6.9967        | 0.48  | 60   | 9.7215          | 1.0 |
| 5.2368        | 0.64  | 80   | 5.8459          | 1.0 |
| 3.4499        | 0.8   | 100  | 3.3413          | 1.0 |
| 3.1261        | 0.96  | 120  | 3.2858          | 1.0 |
| 3.0654        | 1.12  | 140  | 3.1945          | 1.0 |
| 3.0421        | 1.28  | 160  | 3.1296          | 1.0 |
| 3.0035        | 1.44  | 180  | 3.1172          | 1.0 |
| 3.0067        | 1.6   | 200  | 3.1217          | 1.0 |
| 2.9867        | 1.76  | 220  | 3.0715          | 1.0 |
| 2.9653        | 1.92  | 240  | 3.0747          | 1.0 |
| 2.9629        | 2.08  | 260  | 2.9984          | 1.0 |
| 2.9462        | 2.24  | 280  | 2.9991          | 1.0 |
| 2.9391        | 2.4   | 300  | 3.0391          | 1.0 |
| 2.934         | 2.56  | 320  | 2.9682          | 1.0 |
| 2.9193        | 2.72  | 340  | 2.9701          | 1.0 |
| 2.8985        | 2.88  | 360  | 2.9314          | 1.0 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu111
- Datasets 1.13.3
- Tokenizers 0.10.3
