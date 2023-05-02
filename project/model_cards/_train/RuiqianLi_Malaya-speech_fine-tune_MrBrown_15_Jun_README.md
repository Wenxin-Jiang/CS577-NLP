---
tags:
- generated_from_trainer
datasets:
- uob_singlish
model-index:
- name: Malaya-speech_fine-tune_MrBrown_15_Jun
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Malaya-speech_fine-tune_MrBrown_15_Jun

This model is a fine-tuned version of [malay-huggingface/wav2vec2-xls-r-300m-mixed](https://huggingface.co/malay-huggingface/wav2vec2-xls-r-300m-mixed) on the uob_singlish dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4822
- Wer: 0.2449

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
- train_batch_size: 2
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 100
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 1.1607        | 5.26  | 200  | 0.3983          | 0.2381 |
| 0.5184        | 10.52 | 400  | 0.3256          | 0.2245 |
| 0.2993        | 15.78 | 600  | 0.3437          | 0.2426 |
| 0.2485        | 21.05 | 800  | 0.4547          | 0.2585 |
| 0.1917        | 26.31 | 1000 | 0.4598          | 0.2517 |
| 0.1586        | 31.57 | 1200 | 0.4050          | 0.2290 |
| 0.1486        | 36.83 | 1400 | 0.4186          | 0.2653 |
| 0.1307        | 42.1  | 1600 | 0.4284          | 0.2857 |
| 0.0895        | 47.36 | 1800 | 0.5158          | 0.2562 |
| 0.0526        | 52.62 | 2000 | 0.4525          | 0.2449 |
| 0.0553        | 57.88 | 2200 | 0.4364          | 0.2336 |
| 0.037         | 63.16 | 2400 | 0.3873          | 0.2449 |
| 0.0439        | 68.42 | 2600 | 0.3914          | 0.2404 |
| 0.0411        | 73.68 | 2800 | 0.4673          | 0.2494 |
| 0.0242        | 78.94 | 3000 | 0.4801          | 0.2426 |
| 0.0833        | 84.21 | 3200 | 0.4641          | 0.2630 |
| 0.034         | 89.47 | 3400 | 0.4607          | 0.2449 |
| 0.02          | 94.73 | 3600 | 0.4825          | 0.2449 |
| 0.0211        | 99.99 | 3800 | 0.4822          | 0.2449 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3
