---
license: mit
tags:
- generated_from_trainer
model-index:
- name: Romance-cleaned-3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Romance-cleaned-3

This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.9593

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 1000
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 16   | 10.0173         |
| No log        | 2.0   | 32   | 9.1598          |
| No log        | 3.0   | 48   | 8.6820          |
| No log        | 4.0   | 64   | 8.3963          |
| No log        | 5.0   | 80   | 8.1259          |
| No log        | 6.0   | 96   | 7.9259          |
| No log        | 7.0   | 112  | 7.6943          |
| No log        | 8.0   | 128  | 7.4803          |
| No log        | 9.0   | 144  | 7.2883          |
| No log        | 10.0  | 160  | 7.1145          |
| No log        | 11.0  | 176  | 6.9568          |
| No log        | 12.0  | 192  | 6.8000          |
| No log        | 13.0  | 208  | 6.6515          |
| No log        | 14.0  | 224  | 6.5033          |
| No log        | 15.0  | 240  | 6.3471          |
| No log        | 16.0  | 256  | 6.2029          |
| No log        | 17.0  | 272  | 6.0583          |
| No log        | 18.0  | 288  | 5.9173          |
| No log        | 19.0  | 304  | 5.7819          |
| No log        | 20.0  | 320  | 5.6710          |
| No log        | 21.0  | 336  | 5.5588          |
| No log        | 22.0  | 352  | 5.4729          |
| No log        | 23.0  | 368  | 5.3980          |
| No log        | 24.0  | 384  | 5.3261          |
| No log        | 25.0  | 400  | 5.2801          |
| No log        | 26.0  | 416  | 5.2317          |
| No log        | 27.0  | 432  | 5.1942          |
| No log        | 28.0  | 448  | 5.1523          |
| No log        | 29.0  | 464  | 5.1235          |
| No log        | 30.0  | 480  | 5.1008          |
| No log        | 31.0  | 496  | 5.0667          |
| No log        | 32.0  | 512  | 5.0472          |
| No log        | 33.0  | 528  | 5.0252          |
| No log        | 34.0  | 544  | 5.0143          |
| No log        | 35.0  | 560  | 5.0049          |
| No log        | 36.0  | 576  | 4.9938          |
| No log        | 37.0  | 592  | 4.9827          |
| No log        | 38.0  | 608  | 4.9719          |
| No log        | 39.0  | 624  | 4.9666          |
| No log        | 40.0  | 640  | 4.9540          |
| No log        | 41.0  | 656  | 4.9549          |
| No log        | 42.0  | 672  | 4.9485          |
| No log        | 43.0  | 688  | 4.9602          |
| No log        | 44.0  | 704  | 4.9464          |
| No log        | 45.0  | 720  | 4.9592          |
| No log        | 46.0  | 736  | 4.9611          |
| No log        | 47.0  | 752  | 4.9558          |
| No log        | 48.0  | 768  | 4.9659          |
| No log        | 49.0  | 784  | 4.9739          |
| No log        | 50.0  | 800  | 4.9593          |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
