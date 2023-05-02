---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: wav2vec2-xlsr-53-espeak-cv-ft-intent-classification-ori
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xlsr-53-espeak-cv-ft-intent-classification-ori

This model is a fine-tuned version of [facebook/wav2vec2-xlsr-53-espeak-cv-ft](https://huggingface.co/facebook/wav2vec2-xlsr-53-espeak-cv-ft) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9124
- Accuracy: 0.625

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 45

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.1894        | 1.0   | 14   | 2.1812          | 0.3333   |
| 2.1795        | 2.0   | 28   | 2.1553          | 0.3333   |
| 2.144         | 3.0   | 42   | 2.1066          | 0.3333   |
| 2.1175        | 4.0   | 56   | 2.0283          | 0.3542   |
| 2.0542        | 5.0   | 70   | 1.9253          | 0.3958   |
| 2.0007        | 6.0   | 84   | 1.8468          | 0.4167   |
| 1.8891        | 7.0   | 98   | 1.7655          | 0.4583   |
| 1.8484        | 8.0   | 112  | 1.6695          | 0.4792   |
| 1.8256        | 9.0   | 126  | 1.5920          | 0.5      |
| 1.6832        | 10.0  | 140  | 1.5331          | 0.5      |
| 1.6149        | 11.0  | 154  | 1.4763          | 0.5      |
| 1.5853        | 12.0  | 168  | 1.4453          | 0.5      |
| 1.4357        | 13.0  | 182  | 1.3588          | 0.5      |
| 1.4789        | 14.0  | 196  | 1.3238          | 0.4792   |
| 1.3886        | 15.0  | 210  | 1.2822          | 0.4792   |
| 1.313         | 16.0  | 224  | 1.2609          | 0.5      |
| 1.3559        | 17.0  | 238  | 1.2191          | 0.5208   |
| 1.1937        | 18.0  | 252  | 1.1936          | 0.5      |
| 1.1847        | 19.0  | 266  | 1.1547          | 0.5417   |
| 1.197         | 20.0  | 280  | 1.1390          | 0.5417   |
| 1.1057        | 21.0  | 294  | 1.1310          | 0.5208   |
| 1.0291        | 22.0  | 308  | 1.1086          | 0.5417   |
| 1.0768        | 23.0  | 322  | 1.1075          | 0.5417   |
| 1.0249        | 24.0  | 336  | 1.0654          | 0.5625   |
| 1.0433        | 25.0  | 350  | 1.0390          | 0.5625   |
| 0.9974        | 26.0  | 364  | 1.0086          | 0.6458   |
| 0.9578        | 27.0  | 378  | 0.9939          | 0.625    |
| 0.916         | 28.0  | 392  | 0.9938          | 0.625    |
| 0.9187        | 29.0  | 406  | 0.9843          | 0.625    |
| 0.8759        | 30.0  | 420  | 0.9755          | 0.625    |
| 0.9199        | 31.0  | 434  | 0.9822          | 0.6042   |
| 0.8791        | 32.0  | 448  | 0.9522          | 0.6458   |
| 0.8436        | 33.0  | 462  | 0.9414          | 0.6458   |
| 0.8692        | 34.0  | 476  | 0.9510          | 0.625    |
| 0.8201        | 35.0  | 490  | 0.9208          | 0.6667   |
| 0.8284        | 36.0  | 504  | 0.9398          | 0.6458   |
| 0.8761        | 37.0  | 518  | 0.9438          | 0.6458   |
| 0.7948        | 38.0  | 532  | 0.9253          | 0.6667   |
| 0.8339        | 39.0  | 546  | 0.9250          | 0.6458   |
| 0.8002        | 40.0  | 560  | 0.9145          | 0.6458   |
| 0.7791        | 41.0  | 574  | 0.9062          | 0.6667   |
| 0.7944        | 42.0  | 588  | 0.9077          | 0.6667   |
| 0.7777        | 43.0  | 602  | 0.9069          | 0.6458   |
| 0.7943        | 44.0  | 616  | 0.9118          | 0.625    |
| 0.7573        | 45.0  | 630  | 0.9124          | 0.625    |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
