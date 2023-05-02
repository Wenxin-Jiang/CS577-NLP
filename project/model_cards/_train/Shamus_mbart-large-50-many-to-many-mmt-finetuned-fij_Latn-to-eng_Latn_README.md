---
license: cc-by-nc-4.0
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: mbart-large-50-many-to-many-mmt-finetuned-fij_Latn-to-eng_Latn
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mbart-large-50-many-to-many-mmt-finetuned-fij_Latn-to-eng_Latn

This model is a fine-tuned version of [facebook/nllb-200-distilled-600M](https://huggingface.co/facebook/nllb-200-distilled-600M) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9598
- Bleu: 45.0972
- Gen Len: 42.752

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
- training_steps: 8000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|
| 2.4054        | 0.49  | 500  | 1.7028          | 24.9597 | 43.04   |
| 1.6855        | 0.98  | 1000 | 1.3701          | 33.3128 | 42.2    |
| 1.4042        | 1.47  | 1500 | 1.2224          | 37.6016 | 43.536  |
| 1.2991        | 1.96  | 2000 | 1.1467          | 40.3541 | 42.428  |
| 1.1819        | 2.45  | 2500 | 1.0950          | 42.2106 | 42.58   |
| 1.1323        | 2.94  | 3000 | 1.0523          | 42.9418 | 42.76   |
| 1.0676        | 3.43  | 3500 | 1.0238          | 43.4974 | 42.684  |
| 1.0404        | 3.93  | 4000 | 1.0082          | 43.6092 | 42.616  |
| 0.9882        | 4.42  | 4500 | 0.9942          | 44.7199 | 42.912  |
| 0.982         | 4.91  | 5000 | 0.9814          | 44.8061 | 42.516  |
| 0.9372        | 5.4   | 5500 | 0.9781          | 44.3808 | 42.476  |
| 0.9382        | 5.89  | 6000 | 0.9675          | 45.0267 | 42.76   |
| 0.915         | 6.38  | 6500 | 0.9659          | 45.0073 | 42.676  |
| 0.9126        | 6.87  | 7000 | 0.9617          | 44.9582 | 42.548  |
| 0.8903        | 7.36  | 7500 | 0.9609          | 44.8713 | 42.724  |
| 0.8873        | 7.85  | 8000 | 0.9598          | 45.0972 | 42.752  |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
