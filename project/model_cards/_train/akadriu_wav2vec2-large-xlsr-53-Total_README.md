---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-large-xlsr-53-Total
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xlsr-53-Total

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2814
- Wer: 0.2260

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 2.9157        | 0.2   | 400   | 2.8204          | 0.9707 |
| 0.9554        | 0.4   | 800   | 0.5295          | 0.5046 |
| 0.7585        | 0.6   | 1200  | 0.4007          | 0.3850 |
| 0.7288        | 0.8   | 1600  | 0.3632          | 0.3447 |
| 0.6792        | 1.0   | 2000  | 0.3433          | 0.3216 |
| 0.6085        | 1.2   | 2400  | 0.3254          | 0.2928 |
| 0.6225        | 1.4   | 2800  | 0.3161          | 0.2832 |
| 0.6183        | 1.6   | 3200  | 0.3111          | 0.2721 |
| 0.5947        | 1.8   | 3600  | 0.2969          | 0.2615 |
| 0.5953        | 2.0   | 4000  | 0.2912          | 0.2515 |
| 0.5358        | 2.2   | 4400  | 0.2920          | 0.2501 |
| 0.5535        | 2.4   | 4800  | 0.2939          | 0.2538 |
| 0.5408        | 2.6   | 5200  | 0.2854          | 0.2452 |
| 0.5272        | 2.8   | 5600  | 0.2816          | 0.2434 |
| 0.5248        | 3.0   | 6000  | 0.2755          | 0.2354 |
| 0.4923        | 3.2   | 6400  | 0.2795          | 0.2353 |
| 0.489         | 3.4   | 6800  | 0.2767          | 0.2330 |
| 0.4932        | 3.6   | 7200  | 0.2821          | 0.2335 |
| 0.4841        | 3.8   | 7600  | 0.2756          | 0.2349 |
| 0.4794        | 4.0   | 8000  | 0.2751          | 0.2265 |
| 0.444         | 4.2   | 8400  | 0.2809          | 0.2283 |
| 0.4533        | 4.4   | 8800  | 0.2804          | 0.2312 |
| 0.4563        | 4.6   | 9200  | 0.2830          | 0.2256 |
| 0.4498        | 4.8   | 9600  | 0.2819          | 0.2251 |
| 0.4532        | 5.0   | 10000 | 0.2814          | 0.2260 |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.10.3
