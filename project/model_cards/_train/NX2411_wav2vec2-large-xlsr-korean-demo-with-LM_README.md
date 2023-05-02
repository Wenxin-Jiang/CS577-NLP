---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-large-xlsr-korean-demo-with-LM
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xlsr-korean-demo-with-LM

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3015
- Wer: 0.2113

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
| 4.7496        | 1.08  | 400   | 3.1801          | 1.0    |
| 1.4505        | 2.16  | 800   | 0.5090          | 0.5659 |
| 0.566         | 3.23  | 1200  | 0.3600          | 0.4039 |
| 0.4265        | 4.31  | 1600  | 0.3224          | 0.3639 |
| 0.3611        | 5.39  | 2000  | 0.3152          | 0.3575 |
| 0.3035        | 6.47  | 2400  | 0.2814          | 0.3054 |
| 0.2863        | 7.55  | 2800  | 0.2749          | 0.2923 |
| 0.247         | 8.63  | 3200  | 0.2787          | 0.2884 |
| 0.232         | 9.7   | 3600  | 0.2924          | 0.2788 |
| 0.2069        | 10.78 | 4000  | 0.2668          | 0.2694 |
| 0.1922        | 11.86 | 4400  | 0.2873          | 0.2667 |
| 0.1747        | 12.94 | 4800  | 0.2870          | 0.2589 |
| 0.1755        | 14.02 | 5200  | 0.2778          | 0.2543 |
| 0.1546        | 15.09 | 5600  | 0.3062          | 0.2621 |
| 0.1456        | 16.17 | 6000  | 0.3043          | 0.2479 |
| 0.1404        | 17.25 | 6400  | 0.2885          | 0.2443 |
| 0.1308        | 18.33 | 6800  | 0.3274          | 0.2417 |
| 0.125         | 19.41 | 7200  | 0.2922          | 0.2401 |
| 0.1148        | 20.49 | 7600  | 0.2899          | 0.2300 |
| 0.1129        | 21.56 | 8000  | 0.2963          | 0.2276 |
| 0.1086        | 22.64 | 8400  | 0.2903          | 0.2209 |
| 0.097         | 23.72 | 8800  | 0.3041          | 0.2220 |
| 0.099         | 24.8  | 9200  | 0.2870          | 0.2168 |
| 0.0905        | 25.88 | 9600  | 0.2992          | 0.2176 |
| 0.0929        | 26.95 | 10000 | 0.2934          | 0.2115 |
| 0.0827        | 28.03 | 10400 | 0.2945          | 0.2141 |
| 0.0818        | 29.11 | 10800 | 0.3015          | 0.2113 |


### Usage




### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
