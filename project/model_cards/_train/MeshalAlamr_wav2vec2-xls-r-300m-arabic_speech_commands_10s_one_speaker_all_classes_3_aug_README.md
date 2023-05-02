---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: wav2vec2-xls-r-300m-arabic_speech_commands_10s_one_speaker_all_classes_3_aug
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xls-r-300m-arabic_speech_commands_10s_one_speaker_all_classes_3_aug

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1190
- Accuracy: 0.7137

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 60

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 3.6888        | 0.96  | 12   | 3.6887          | 0.025    |
| 3.8686        | 1.96  | 24   | 3.6837          | 0.0488   |
| 3.844         | 2.96  | 36   | 3.5466          | 0.1062   |
| 3.7114        | 3.96  | 48   | 3.2589          | 0.1133   |
| 2.8339        | 4.96  | 60   | 2.9553          | 0.1883   |
| 2.5667        | 5.96  | 72   | 2.8784          | 0.1963   |
| 2.1911        | 6.96  | 84   | 2.6379          | 0.2771   |
| 1.8461        | 7.96  | 96   | 2.8874          | 0.2929   |
| 1.6044        | 8.96  | 108  | 2.4989          | 0.34     |
| 1.0916        | 9.96  | 120  | 2.3111          | 0.425    |
| 0.9371        | 10.96 | 132  | 2.0899          | 0.4829   |
| 0.8177        | 11.96 | 144  | 2.0116          | 0.4971   |
| 0.6366        | 12.96 | 156  | 2.0598          | 0.5558   |
| 0.549         | 13.96 | 168  | 2.0084          | 0.5575   |
| 0.2917        | 14.96 | 180  | 1.8231          | 0.6038   |
| 0.2283        | 15.96 | 192  | 1.9943          | 0.6079   |
| 0.2382        | 16.96 | 204  | 2.2098          | 0.6083   |
| 0.2475        | 17.96 | 216  | 2.3519          | 0.5992   |
| 0.1612        | 18.96 | 228  | 2.2483          | 0.5929   |
| 0.133         | 19.96 | 240  | 2.2263          | 0.6079   |
| 0.1301        | 20.96 | 252  | 2.6094          | 0.5683   |
| 0.0993        | 21.96 | 264  | 2.0289          | 0.6417   |
| 0.0779        | 22.96 | 276  | 1.9693          | 0.6479   |
| 0.0824        | 23.96 | 288  | 2.2471          | 0.6258   |
| 0.0872        | 24.96 | 300  | 2.3715          | 0.6538   |
| 0.0694        | 25.96 | 312  | 2.5367          | 0.6325   |
| 0.0704        | 26.96 | 324  | 2.4467          | 0.6388   |
| 0.061         | 27.96 | 336  | 2.1581          | 0.6621   |
| 0.0835        | 28.96 | 348  | 2.1672          | 0.6792   |
| 0.0402        | 29.96 | 360  | 2.2166          | 0.6596   |
| 0.0329        | 30.96 | 372  | 2.6316          | 0.6217   |
| 0.0516        | 31.96 | 384  | 2.0840          | 0.6908   |
| 0.0455        | 32.96 | 396  | 2.2299          | 0.67     |
| 0.0449        | 33.96 | 408  | 2.4341          | 0.6733   |
| 0.0332        | 34.96 | 420  | 2.2830          | 0.6725   |
| 0.0334        | 35.96 | 432  | 2.2060          | 0.6829   |
| 0.025         | 36.96 | 444  | 2.2836          | 0.6554   |
| 0.0351        | 37.96 | 456  | 2.5417          | 0.6517   |
| 0.0372        | 38.96 | 468  | 2.2738          | 0.6779   |
| 0.0136        | 39.96 | 480  | 2.4606          | 0.6525   |
| 0.0178        | 40.96 | 492  | 2.1996          | 0.675    |
| 0.0116        | 41.96 | 504  | 2.2557          | 0.6763   |
| 0.0113        | 42.96 | 516  | 2.2061          | 0.6863   |
| 0.014         | 43.96 | 528  | 2.1279          | 0.6925   |
| 0.015         | 44.96 | 540  | 2.2151          | 0.6871   |
| 0.0197        | 45.96 | 552  | 2.1506          | 0.6929   |
| 0.0102        | 46.96 | 564  | 2.1609          | 0.685    |
| 0.0115        | 47.96 | 576  | 2.1685          | 0.6854   |
| 0.0097        | 48.96 | 588  | 2.2892          | 0.6821   |
| 0.0148        | 49.96 | 600  | 2.4085          | 0.6921   |
| 0.0114        | 50.96 | 612  | 2.2171          | 0.7104   |
| 0.0141        | 51.96 | 624  | 2.1458          | 0.7075   |
| 0.0066        | 52.96 | 636  | 2.2046          | 0.7013   |
| 0.0128        | 53.96 | 648  | 2.1424          | 0.705    |
| 0.0063        | 54.96 | 660  | 2.1425          | 0.7075   |
| 0.0094        | 55.96 | 672  | 2.1554          | 0.7087   |
| 0.0161        | 56.96 | 684  | 2.1892          | 0.7063   |
| 0.0067        | 57.96 | 696  | 2.1819          | 0.7067   |
| 0.0099        | 58.96 | 708  | 2.1341          | 0.7125   |
| 0.0067        | 59.96 | 720  | 2.1190          | 0.7137   |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
