---
tags:
- generated_from_trainer
datasets:
- dcc_v1.1.0
metrics:
- accuracy
model-index:
- name: dfm-debertav2-large-v1
  results:
  - task:
      name: Masked Language Modeling
      type: fill-mask
    dataset:
      name: dcc_v1.1.0
      type: dcc_v1.1.0
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.6311476982710648
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dfm-debertav2-large-v1

This model is a fine-tuned version of [/home/kenneth/github/danish-foundation-models/default-models-configs/large-deberta-v2-32000-config.json](https://huggingface.co//home/kenneth/github/danish-foundation-models/default-models-configs/large-deberta-v2-32000-config.json) on the dcc_v1.1.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8881
- Accuracy: 0.6311

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
- train_batch_size: 256
- eval_batch_size: 256
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 1024
- optimizer: Adam with betas=(0.9,0.98) and epsilon=1e-06
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 10000
- training_steps: 100000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step   | Accuracy | Validation Loss |
|:-------------:|:-----:|:------:|:--------:|:---------------:|
| 5.2842        | 0.02  | 2000   | 0.2451   | 5.5486          |
| 3.5009        | 0.04  | 4000   | 0.3869   | 3.9854          |
| 2.8           | 0.06  | 6000   | 3.3670   | 0.4498          |
| 2.4834        | 0.08  | 8000   | 3.1489   | 0.4743          |
| 2.3383        | 0.1   | 10000  | 3.0157   | 0.4890          |
| 2.2111        | 0.12  | 12000  | 2.8378   | 0.5042          |
| 2.1184        | 0.14  | 14000  | 2.7617   | 0.5192          |
| 2.0401        | 0.16  | 16000  | 2.7342   | 0.5211          |
| 1.9915        | 0.18  | 18000  | 2.6763   | 0.5314          |
| 1.9448        | 0.2   | 20000  | 2.5955   | 0.5341          |
| 1.8949        | 0.22  | 22000  | 2.5706   | 0.5408          |
| 1.8642        | 0.24  | 24000  | 2.5000   | 0.5484          |
| 1.8172        | 0.26  | 26000  | 2.4841   | 0.5513          |
| 1.8324        | 0.28  | 28000  | 2.4866   | 0.5525          |
| 1.7903        | 0.3   | 30000  | 2.4493   | 0.5546          |
| 1.7352        | 0.32  | 32000  | 2.3910   | 0.5592          |
| 1.7004        | 0.34  | 34000  | 2.3819   | 0.5646          |
| 1.7032        | 0.36  | 36000  | 2.3526   | 0.5686          |
| 1.6953        | 0.38  | 38000  | 2.2946   | 0.5776          |
| 1.6469        | 0.4   | 40000  | 2.2981   | 0.5751          |
| 1.6281        | 0.42  | 42000  | 2.2742   | 0.5770          |
| 1.6181        | 0.44  | 44000  | 2.2670   | 0.5808          |
| 1.5769        | 0.46  | 46000  | 2.2626   | 0.5844          |
| 1.6279        | 0.48  | 48000  | 2.2693   | 0.5777          |
| 1.5754        | 0.5   | 50000  | 2.2665   | 0.5825          |
| 1.5369        | 0.52  | 52000  | 2.2728   | 0.5812          |
| 1.5335        | 0.54  | 54000  | 2.2725   | 0.5805          |
| 1.5324        | 0.56  | 56000  | 2.1889   | 0.5912          |
| 1.53          | 0.58  | 58000  | 2.1571   | 0.5947          |
| 1.4736        | 0.6   | 60000  | 2.1756   | 0.5938          |
| 1.4824        | 0.62  | 62000  | 2.1570   | 0.5957          |
| 1.4566        | 0.64  | 64000  | 2.0989   | 0.6008          |
| 1.4576        | 0.66  | 66000  | 2.0975   | 0.6019          |
| 1.4473        | 0.68  | 68000  | 2.0646   | 0.6032          |
| 1.4177        | 0.7   | 70000  | 2.0544   | 0.6068          |
| 1.4314        | 0.72  | 72000  | 2.0642   | 0.6056          |
| 1.3949        | 0.74  | 74000  | 2.0406   | 0.6086          |
| 1.4035        | 0.76  | 76000  | 1.9857   | 0.6186          |
| 1.3797        | 0.78  | 78000  | 1.9847   | 0.6190          |
| 1.3584        | 0.8   | 80000  | 1.9804   | 0.6196          |
| 1.3256        | 0.82  | 82000  | 1.9586   | 0.6193          |
| 1.303         | 0.84  | 84000  | 1.9547   | 0.6230          |
| 1.3575        | 0.86  | 86000  | 1.9251   | 0.6248          |
| 1.3429        | 0.88  | 88000  | 1.9556   | 0.6207          |
| 1.3239        | 0.9   | 90000  | 1.9374   | 0.6229          |
| 1.306         | 0.92  | 92000  | 1.9121   | 0.6289          |
| 1.2934        | 0.94  | 94000  | 1.9145   | 0.6291          |
| 1.3001        | 0.96  | 96000  | 1.9247   | 0.6280          |
| 1.2969        | 0.98  | 98000  | 1.9224   | 0.6264          |
| 1.2922        | 1.0   | 100000 | 1.9248   | 0.6266          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu102
- Datasets 2.5.3.dev0
- Tokenizers 0.12.1
