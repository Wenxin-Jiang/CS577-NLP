---
tags:
- generated_from_trainer
model-index:
- name: torgo-TestedSpeakerM01-finetuned-On-torgoSentenceModel
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# torgo-TestedSpeakerM01-finetuned-On-torgoSentenceModel

This model is a fine-tuned version of [alexziweiwang/torgo-sentences-TestedSpeakerM01](https://huggingface.co/alexziweiwang/torgo-sentences-TestedSpeakerM01) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3376
- Wer: 0.7172

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
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 15.6854       | 0.84  | 500   | 0.4620          | 1.0596 |
| 0.3374        | 1.69  | 1000  | 0.2646          | 1.0921 |
| 0.3121        | 2.53  | 1500  | 0.2602          | 1.0704 |
| 0.2683        | 3.37  | 2000  | 0.2417          | 1.0997 |
| 0.2478        | 4.22  | 2500  | 0.2438          | 1.0217 |
| 0.2368        | 5.06  | 3000  | 0.2600          | 0.9729 |
| 0.2236        | 5.9   | 3500  | 0.2400          | 0.9112 |
| 0.2183        | 6.75  | 4000  | 0.3123          | 0.9805 |
| 0.1989        | 7.59  | 4500  | 0.2716          | 0.9231 |
| 0.1852        | 8.43  | 5000  | 0.2539          | 0.8732 |
| 0.1778        | 9.27  | 5500  | 0.2673          | 0.8516 |
| 0.1769        | 10.12 | 6000  | 0.2951          | 0.8819 |
| 0.1798        | 10.96 | 6500  | 0.3194          | 0.9122 |
| 0.1525        | 11.8  | 7000  | 0.2320          | 0.8830 |
| 0.1497        | 12.65 | 7500  | 0.2814          | 0.8007 |
| 0.1401        | 13.49 | 8000  | 0.2693          | 0.8039 |
| 0.1227        | 14.33 | 8500  | 0.2681          | 0.7887 |
| 0.1259        | 15.18 | 9000  | 0.2592          | 0.7584 |
| 0.1278        | 16.02 | 9500  | 0.2795          | 0.7920 |
| 0.1124        | 16.86 | 10000 | 0.3190          | 0.7714 |
| 0.1116        | 17.71 | 10500 | 0.3306          | 0.7909 |
| 0.1024        | 18.55 | 11000 | 0.2935          | 0.7519 |
| 0.1417        | 19.39 | 11500 | 0.3441          | 0.7638 |
| 0.0924        | 20.24 | 12000 | 0.3136          | 0.7454 |
| 0.0916        | 21.08 | 12500 | 0.3144          | 0.7107 |
| 0.0875        | 21.92 | 13000 | 0.3350          | 0.7421 |
| 0.087         | 22.77 | 13500 | 0.3129          | 0.7530 |
| 0.0741        | 23.61 | 14000 | 0.3384          | 0.7454 |
| 0.0708        | 24.45 | 14500 | 0.3688          | 0.7486 |
| 0.0812        | 25.3  | 15000 | 0.3383          | 0.7216 |
| 0.0669        | 26.14 | 15500 | 0.3201          | 0.7205 |
| 0.0612        | 26.98 | 16000 | 0.3116          | 0.7140 |
| 0.0637        | 27.82 | 16500 | 0.3303          | 0.7064 |
| 0.0629        | 28.67 | 17000 | 0.3382          | 0.7129 |
| 0.0667        | 29.51 | 17500 | 0.3350          | 0.7161 |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 1.18.3
- Tokenizers 0.13.2
