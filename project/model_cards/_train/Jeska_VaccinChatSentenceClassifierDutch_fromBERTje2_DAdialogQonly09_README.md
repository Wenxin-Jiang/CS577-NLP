---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: VaccinChatSentenceClassifierDutch_fromBERTje2_DAdialogQonly09
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# VaccinChatSentenceClassifierDutch_fromBERTje2_DAdialogQonly09

This model is a fine-tuned version of [outputDAQonly09/](https://huggingface.co/outputDAQonly09/) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4978
- Accuracy: 0.9031

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 30.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 330  | 3.9692          | 0.2249   |
| 4.3672        | 2.0   | 660  | 3.1312          | 0.4031   |
| 4.3672        | 3.0   | 990  | 2.5068          | 0.5658   |
| 3.1495        | 4.0   | 1320 | 2.0300          | 0.6600   |
| 2.2491        | 5.0   | 1650 | 1.6517          | 0.7450   |
| 2.2491        | 6.0   | 1980 | 1.3604          | 0.7943   |
| 1.622         | 7.0   | 2310 | 1.1328          | 0.8327   |
| 1.1252        | 8.0   | 2640 | 0.9484          | 0.8611   |
| 1.1252        | 9.0   | 2970 | 0.8212          | 0.8757   |
| 0.7969        | 10.0  | 3300 | 0.7243          | 0.8830   |
| 0.5348        | 11.0  | 3630 | 0.6597          | 0.8867   |
| 0.5348        | 12.0  | 3960 | 0.5983          | 0.8857   |
| 0.3744        | 13.0  | 4290 | 0.5635          | 0.8976   |
| 0.2564        | 14.0  | 4620 | 0.5437          | 0.8985   |
| 0.2564        | 15.0  | 4950 | 0.5124          | 0.9013   |
| 0.1862        | 16.0  | 5280 | 0.5074          | 0.9022   |
| 0.1349        | 17.0  | 5610 | 0.5028          | 0.9049   |
| 0.1349        | 18.0  | 5940 | 0.4876          | 0.9077   |
| 0.0979        | 19.0  | 6270 | 0.4971          | 0.9049   |
| 0.0763        | 20.0  | 6600 | 0.4941          | 0.9022   |
| 0.0763        | 21.0  | 6930 | 0.4957          | 0.9049   |
| 0.0602        | 22.0  | 7260 | 0.4989          | 0.9049   |
| 0.0504        | 23.0  | 7590 | 0.4959          | 0.9040   |
| 0.0504        | 24.0  | 7920 | 0.4944          | 0.9031   |
| 0.0422        | 25.0  | 8250 | 0.4985          | 0.9040   |
| 0.0379        | 26.0  | 8580 | 0.4970          | 0.9049   |
| 0.0379        | 27.0  | 8910 | 0.4949          | 0.9040   |
| 0.0351        | 28.0  | 9240 | 0.4971          | 0.9040   |
| 0.0321        | 29.0  | 9570 | 0.4967          | 0.9031   |
| 0.0321        | 30.0  | 9900 | 0.4978          | 0.9031   |


### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.10.0
- Datasets 1.16.1
- Tokenizers 0.10.3
