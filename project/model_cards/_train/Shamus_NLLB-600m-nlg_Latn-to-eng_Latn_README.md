---
license: cc-by-nc-4.0
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: NLLB-600m-nlg_Latn-to-eng_Latn
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# NLLB-600m-nlg_Latn-to-eng_Latn

This model is a fine-tuned version of [facebook/nllb-200-distilled-600M](https://huggingface.co/facebook/nllb-200-distilled-600M) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9402
- Bleu: 45.9717
- Gen Len: 42.476

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 6
- total_train_batch_size: 12
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 10000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|
| 2.5032        | 0.49  | 500   | 1.7451          | 24.369  | 42.66   |
| 1.732         | 0.98  | 1000  | 1.3896          | 31.9939 | 42.304  |
| 1.4344        | 1.47  | 1500  | 1.2333          | 36.4344 | 42.384  |
| 1.3141        | 1.96  | 2000  | 1.1442          | 38.5023 | 41.96   |
| 1.1877        | 2.45  | 2500  | 1.0936          | 41.3292 | 42.668  |
| 1.1355        | 2.94  | 3000  | 1.0460          | 43.1357 | 43.22   |
| 1.0623        | 3.43  | 3500  | 1.0197          | 43.2339 | 42.692  |
| 1.0353        | 3.93  | 4000  | 1.0010          | 43.8863 | 43.012  |
| 0.9786        | 4.42  | 4500  | 0.9899          | 44.2478 | 43.012  |
| 0.9682        | 4.91  | 5000  | 0.9731          | 44.9191 | 42.816  |
| 0.9184        | 5.4   | 5500  | 0.9690          | 44.908  | 42.496  |
| 0.9208        | 5.89  | 6000  | 0.9558          | 45.5488 | 42.772  |
| 0.8854        | 6.38  | 6500  | 0.9561          | 45.7261 | 42.844  |
| 0.8815        | 6.87  | 7000  | 0.9495          | 45.1231 | 42.38   |
| 0.8543        | 7.36  | 7500  | 0.9475          | 45.6717 | 42.56   |
| 0.8462        | 7.85  | 8000  | 0.9442          | 45.9782 | 42.652  |
| 0.8422        | 8.34  | 8500  | 0.9436          | 45.9353 | 42.628  |
| 0.8323        | 8.83  | 9000  | 0.9407          | 45.7945 | 42.492  |
| 0.8218        | 9.32  | 9500  | 0.9405          | 46.0215 | 42.472  |
| 0.8226        | 9.81  | 10000 | 0.9402          | 45.9717 | 42.476  |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
