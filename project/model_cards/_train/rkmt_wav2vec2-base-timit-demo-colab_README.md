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

This model is a fine-tuned version of [facebook/hubert-large-ls960-ft](https://huggingface.co/facebook/hubert-large-ls960-ft) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0280
- Wer: 0.0082

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
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 0.1152        | 1.42  | 500   | 0.0416          | 0.0159 |
| 0.0803        | 2.83  | 1000  | 0.0372          | 0.0144 |
| 0.0672        | 4.25  | 1500  | 0.0345          | 0.0119 |
| 0.0564        | 5.67  | 2000  | 0.0338          | 0.0106 |
| 0.0513        | 7.08  | 2500  | 0.0307          | 0.0100 |
| 0.0448        | 8.5   | 3000  | 0.0343          | 0.0098 |
| 0.0374        | 9.92  | 3500  | 0.0300          | 0.0084 |
| 0.0368        | 11.33 | 4000  | 0.0314          | 0.0086 |
| 0.0388        | 12.75 | 4500  | 0.0283          | 0.0089 |
| 0.0277        | 14.16 | 5000  | 0.0302          | 0.0089 |
| 0.0298        | 15.58 | 5500  | 0.0298          | 0.0089 |
| 0.0271        | 17.0  | 6000  | 0.0320          | 0.0098 |
| 0.024         | 18.41 | 6500  | 0.0286          | 0.0088 |
| 0.0236        | 19.83 | 7000  | 0.0284          | 0.0084 |
| 0.0238        | 21.25 | 7500  | 0.0290          | 0.0086 |
| 0.0227        | 22.66 | 8000  | 0.0284          | 0.0093 |
| 0.0198        | 24.08 | 8500  | 0.0280          | 0.0088 |
| 0.0225        | 25.5  | 9000  | 0.0281          | 0.0086 |
| 0.018         | 26.91 | 9500  | 0.0280          | 0.0082 |
| 0.0178        | 28.33 | 10000 | 0.0280          | 0.0082 |
| 0.0209        | 29.75 | 10500 | 0.0280          | 0.0082 |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.9.0+cu111
- Datasets 1.17.0
- Tokenizers 0.10.3
