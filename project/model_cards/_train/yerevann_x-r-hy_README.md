---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-large-xls-r-2b-armenian-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-2b-armenian-colab

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-2b](https://huggingface.co/facebook/wav2vec2-xls-r-2b) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5166
- Wer: 0.7397

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
- train_batch_size: 1
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 120
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step  | Validation Loss | Wer    |
|:-------------:|:------:|:-----:|:---------------:|:------:|
| 3.7057        | 2.38   | 200   | 0.7731          | 0.8091 |
| 0.5797        | 4.76   | 400   | 0.8279          | 0.7804 |
| 0.4341        | 7.14   | 600   | 1.0343          | 0.8285 |
| 0.3135        | 9.52   | 800   | 1.0551          | 0.8066 |
| 0.2409        | 11.9   | 1000  | 1.0686          | 0.7897 |
| 0.1998        | 14.29  | 1200  | 1.1329          | 0.7766 |
| 0.1729        | 16.67  | 1400  | 1.3234          | 0.8567 |
| 0.1533        | 19.05  | 1600  | 1.2432          | 0.8160 |
| 0.1354        | 21.43  | 1800  | 1.2780          | 0.7954 |
| 0.12          | 23.81  | 2000  | 1.2228          | 0.8054 |
| 0.1175        | 26.19  | 2200  | 1.3484          | 0.8129 |
| 0.1141        | 28.57  | 2400  | 1.2881          | 0.9130 |
| 0.1053        | 30.95  | 2600  | 1.1972          | 0.7910 |
| 0.0954        | 33.33  | 2800  | 1.3702          | 0.8048 |
| 0.0842        | 35.71  | 3000  | 1.3963          | 0.7960 |
| 0.0793        | 38.1   | 3200  | 1.4690          | 0.7991 |
| 0.0707        | 40.48  | 3400  | 1.5045          | 0.8085 |
| 0.0745        | 42.86  | 3600  | 1.4749          | 0.8004 |
| 0.0693        | 45.24  | 3800  | 1.5047          | 0.7960 |
| 0.0646        | 47.62  | 4000  | 1.4216          | 0.7997 |
| 0.0555        | 50.0   | 4200  | 1.4676          | 0.8029 |
| 0.056         | 52.38  | 4400  | 1.4273          | 0.8104 |
| 0.0465        | 54.76  | 4600  | 1.3999          | 0.7841 |
| 0.046         | 57.14  | 4800  | 1.6130          | 0.8473 |
| 0.0404        | 59.52  | 5000  | 1.5586          | 0.7841 |
| 0.0403        | 61.9   | 5200  | 1.3959          | 0.7653 |
| 0.0404        | 64.29  | 5400  | 1.5318          | 0.8041 |
| 0.0365        | 66.67  | 5600  | 1.5300          | 0.7854 |
| 0.0338        | 69.05  | 5800  | 1.5051          | 0.7885 |
| 0.0307        | 71.43  | 6000  | 1.5647          | 0.7935 |
| 0.0235        | 73.81  | 6200  | 1.4919          | 0.8154 |
| 0.0268        | 76.19  | 6400  | 1.5259          | 0.8060 |
| 0.0275        | 78.57  | 6600  | 1.3985          | 0.7897 |
| 0.022         | 80.95  | 6800  | 1.5515          | 0.8154 |
| 0.017         | 83.33  | 7000  | 1.5737          | 0.7647 |
| 0.0205        | 85.71  | 7200  | 1.4876          | 0.7572 |
| 0.0174        | 88.1   | 7400  | 1.6331          | 0.7829 |
| 0.0188        | 90.48  | 7600  | 1.5108          | 0.7685 |
| 0.0134        | 92.86  | 7800  | 1.7125          | 0.7866 |
| 0.0125        | 95.24  | 8000  | 1.6042          | 0.7635 |
| 0.0133        | 97.62  | 8200  | 1.4608          | 0.7478 |
| 0.0272        | 100.0  | 8400  | 1.4784          | 0.7309 |
| 0.0133        | 102.38 | 8600  | 1.4471          | 0.7459 |
| 0.0094        | 104.76 | 8800  | 1.4852          | 0.7272 |
| 0.0103        | 107.14 | 9000  | 1.5679          | 0.7409 |
| 0.0088        | 109.52 | 9200  | 1.5090          | 0.7309 |
| 0.0077        | 111.9  | 9400  | 1.4994          | 0.7290 |
| 0.0068        | 114.29 | 9600  | 1.5008          | 0.7340 |
| 0.0054        | 116.67 | 9800  | 1.5166          | 0.7390 |
| 0.0052        | 119.05 | 10000 | 1.5166          | 0.7397 |


### Framework versions

- Transformers 4.14.1
- Pytorch 1.10.0
- Datasets 1.16.1
- Tokenizers 0.10.3
