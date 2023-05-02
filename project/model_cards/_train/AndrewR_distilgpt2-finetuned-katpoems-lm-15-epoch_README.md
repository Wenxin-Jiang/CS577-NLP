---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: distilgpt2-finetuned-katpoems-lm-15-epoch
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilgpt2-finetuned-katpoems-lm-15-epoch

This model is a fine-tuned version of [distilgpt2](https://huggingface.co/distilgpt2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.8145

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15.0

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 59   | 4.6495          |
| No log        | 2.0   | 118  | 4.6555          |
| No log        | 3.0   | 177  | 4.6696          |
| No log        | 4.0   | 236  | 4.6930          |
| No log        | 5.0   | 295  | 4.7132          |
| No log        | 6.0   | 354  | 4.7185          |
| No log        | 7.0   | 413  | 4.7444          |
| No log        | 8.0   | 472  | 4.7611          |
| 4.2244        | 9.0   | 531  | 4.7794          |
| 4.2244        | 10.0  | 590  | 4.7841          |
| 4.2244        | 11.0  | 649  | 4.7929          |
| 4.2244        | 12.0  | 708  | 4.8048          |
| 4.2244        | 13.0  | 767  | 4.8058          |
| 4.2244        | 14.0  | 826  | 4.8124          |
| 4.2244        | 15.0  | 885  | 4.8145          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
