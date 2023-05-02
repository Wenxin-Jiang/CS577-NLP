---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-large-xls-r-300m-tr
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-tr

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2891
- Wer: 0.4741

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 5.4933        | 0.39  | 400   | 1.0543          | 0.9316 |
| 0.7039        | 0.78  | 800   | 0.6927          | 0.7702 |
| 0.4768        | 1.17  | 1200  | 0.4779          | 0.6774 |
| 0.4004        | 1.57  | 1600  | 0.4462          | 0.6450 |
| 0.3739        | 1.96  | 2000  | 0.4287          | 0.6296 |
| 0.317         | 2.35  | 2400  | 0.4395          | 0.6248 |
| 0.3027        | 2.74  | 2800  | 0.4052          | 0.6027 |
| 0.2633        | 3.13  | 3200  | 0.4026          | 0.5938 |
| 0.245         | 3.52  | 3600  | 0.3814          | 0.5902 |
| 0.2415        | 3.91  | 4000  | 0.3691          | 0.5708 |
| 0.2193        | 4.31  | 4400  | 0.3626          | 0.5623 |
| 0.2057        | 4.7   | 4800  | 0.3591          | 0.5551 |
| 0.1874        | 5.09  | 5200  | 0.3670          | 0.5512 |
| 0.1782        | 5.48  | 5600  | 0.3483          | 0.5406 |
| 0.1706        | 5.87  | 6000  | 0.3392          | 0.5338 |
| 0.153         | 6.26  | 6400  | 0.3189          | 0.5207 |
| 0.1493        | 6.65  | 6800  | 0.3185          | 0.5164 |
| 0.1381        | 7.05  | 7200  | 0.3199          | 0.5185 |
| 0.1244        | 7.44  | 7600  | 0.3082          | 0.4993 |
| 0.1182        | 7.83  | 8000  | 0.3122          | 0.4998 |
| 0.1136        | 8.22  | 8400  | 0.3003          | 0.4936 |
| 0.1047        | 8.61  | 8800  | 0.2945          | 0.4858 |
| 0.0986        | 9.0   | 9200  | 0.2827          | 0.4809 |
| 0.0925        | 9.39  | 9600  | 0.2894          | 0.4786 |
| 0.0885        | 9.78  | 10000 | 0.2891          | 0.4741 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.12.1+cu116
- Datasets 2.1.0
- Tokenizers 0.12.1
