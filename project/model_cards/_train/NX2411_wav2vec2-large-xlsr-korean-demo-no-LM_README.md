---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-large-xlsr-korean-demo-no-LM
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xlsr-korean-demo-no-LM

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3215
- Wer: 0.2209

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
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 4.7322        | 1.08  | 400   | 3.1660          | 1.0    |
| 1.6742        | 2.16  | 800   | 0.5714          | 0.5945 |
| 0.6009        | 3.23  | 1200  | 0.3934          | 0.4298 |
| 0.4335        | 4.31  | 1600  | 0.3855          | 0.4100 |
| 0.3615        | 5.39  | 2000  | 0.3226          | 0.3525 |
| 0.2975        | 6.47  | 2400  | 0.3079          | 0.3176 |
| 0.2822        | 7.55  | 2800  | 0.3226          | 0.3091 |
| 0.2468        | 8.63  | 3200  | 0.2935          | 0.2907 |
| 0.2307        | 9.7   | 3600  | 0.2826          | 0.2728 |
| 0.2035        | 10.78 | 4000  | 0.2876          | 0.2728 |
| 0.1959        | 11.86 | 4400  | 0.2988          | 0.2667 |
| 0.1714        | 12.94 | 4800  | 0.3176          | 0.2751 |
| 0.1728        | 14.02 | 5200  | 0.2889          | 0.2649 |
| 0.1552        | 15.09 | 5600  | 0.2893          | 0.2490 |
| 0.144         | 16.17 | 6000  | 0.2909          | 0.2548 |
| 0.1402        | 17.25 | 6400  | 0.2999          | 0.2494 |
| 0.1297        | 18.33 | 6800  | 0.3704          | 0.2584 |
| 0.1268        | 19.41 | 7200  | 0.3464          | 0.2497 |
| 0.1162        | 20.49 | 7600  | 0.3620          | 0.2461 |
| 0.1117        | 21.56 | 8000  | 0.2935          | 0.2387 |
| 0.1081        | 22.64 | 8400  | 0.3588          | 0.2427 |
| 0.0984        | 23.72 | 8800  | 0.4317          | 0.2507 |
| 0.0996        | 24.8  | 9200  | 0.3023          | 0.2277 |
| 0.0925        | 25.88 | 9600  | 0.3224          | 0.2292 |
| 0.0923        | 26.95 | 10000 | 0.3009          | 0.2243 |
| 0.0839        | 28.03 | 10400 | 0.3118          | 0.2219 |
| 0.0814        | 29.11 | 10800 | 0.3215          | 0.2209 |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
