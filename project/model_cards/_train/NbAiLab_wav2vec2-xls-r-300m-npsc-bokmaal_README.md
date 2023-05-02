---
license: apache-2.0
tags:
- generated_from_trainer
- automatic-speech-recognition
- NbAiLab/NPSC
- robust-speech-event
- false
- nb-NO
- hf-asr-leaderboard
datasets:
- NbAiLab/NPSC
language:
- nb-NO
model-index:
- name: wav2vec2-xls-r-300m-npsc-bokmaal
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: NPSC
      type: NbAiLab/NPSC
      args: 16K_mp3_bokmaal
    metrics:
    - name: "Test (Bokm\xE5l) WER"
      type: wer
      value: 0.07556265455560153
    - name: "Test (Bokm\xE5l) CER"
      type: cer
      value: 0.028191288775481386
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xls-r-300m-npsc-bokmaal

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1663
- Wer: 0.0932

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 15.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 0.0969        | 0.32  | 500   | 0.1773          | 0.1054 |
| 0.0929        | 0.64  | 1000  | 0.1672          | 0.1061 |
| 0.1018        | 0.97  | 1500  | 0.1770          | 0.1067 |
| 0.0871        | 1.29  | 2000  | 0.1832          | 0.1087 |
| 0.0908        | 1.61  | 2500  | 0.1830          | 0.1101 |
| 0.0975        | 1.93  | 3000  | 0.1848          | 0.1100 |
| 0.0936        | 2.26  | 3500  | 0.1853          | 0.1113 |
| 0.1025        | 2.58  | 4000  | 0.1958          | 0.1149 |
| 0.0989        | 2.9   | 4500  | 0.1776          | 0.1123 |
| 0.0946        | 3.22  | 5000  | 0.1825          | 0.1097 |
| 0.0859        | 3.55  | 5500  | 0.1864          | 0.1072 |
| 0.0867        | 3.87  | 6000  | 0.1886          | 0.1081 |
| 0.0783        | 4.19  | 6500  | 0.1883          | 0.1063 |
| 0.0804        | 4.51  | 7000  | 0.1831          | 0.1063 |
| 0.0797        | 4.84  | 7500  | 0.1884          | 0.1058 |
| 0.0705        | 5.16  | 8000  | 0.1802          | 0.1057 |
| 0.0795        | 5.48  | 8500  | 0.1854          | 0.1038 |
| 0.0711        | 5.8   | 9000  | 0.1766          | 0.1032 |
| 0.0973        | 6.13  | 9500  | 0.1663          | 0.1014 |
| 0.087         | 6.45  | 10000 | 0.1664          | 0.1014 |
| 0.0962        | 6.77  | 10500 | 0.1631          | 0.1009 |
| 0.0857        | 7.09  | 11000 | 0.1659          | 0.1002 |
| 0.0882        | 7.41  | 11500 | 0.1668          | 0.1007 |
| 0.0784        | 7.74  | 12000 | 0.1688          | 0.0996 |
| 0.0838        | 8.06  | 12500 | 0.1675          | 0.0984 |
| 0.0863        | 8.38  | 13000 | 0.1639          | 0.0979 |
| 0.0763        | 8.7   | 13500 | 0.1638          | 0.0980 |
| 0.0822        | 9.03  | 14000 | 0.1709          | 0.0972 |
| 0.0769        | 9.35  | 14500 | 0.1700          | 0.0965 |
| 0.0838        | 9.67  | 15000 | 0.1703          | 0.0974 |
| 0.0799        | 9.99  | 15500 | 0.1667          | 0.0957 |
| 0.0712        | 10.32 | 16000 | 0.1754          | 0.0960 |
| 0.0737        | 10.64 | 16500 | 0.1725          | 0.0968 |
| 0.0851        | 10.96 | 17000 | 0.1733          | 0.0958 |
| 0.076         | 11.28 | 17500 | 0.1682          | 0.0954 |
| 0.0712        | 11.61 | 18000 | 0.1713          | 0.0943 |
| 0.0745        | 11.93 | 18500 | 0.1662          | 0.0951 |
| 0.0864        | 12.25 | 19000 | 0.1692          | 0.0947 |
| 0.0937        | 12.57 | 19500 | 0.1624          | 0.0943 |
| 0.0915        | 12.89 | 20000 | 0.1678          | 0.0942 |
| 0.0926        | 13.22 | 20500 | 0.1641          | 0.0945 |
| 0.0912        | 13.54 | 21000 | 0.1665          | 0.0937 |
| 0.0917        | 13.86 | 21500 | 0.1648          | 0.0936 |
| 0.094         | 14.18 | 22000 | 0.1635          | 0.0935 |
| 0.0864        | 14.51 | 22500 | 0.1678          | 0.0934 |
| 0.0899        | 14.83 | 23000 | 0.1663          | 0.0932 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu113
- Datasets 1.18.4.dev0
- Tokenizers 0.11.0
