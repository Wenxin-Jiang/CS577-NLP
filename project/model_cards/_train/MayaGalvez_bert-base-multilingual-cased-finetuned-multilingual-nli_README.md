---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: bert-base-multilingual-cased-finetuned-multilingual-nli_newdata_oneepoch
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-multilingual-cased-finetuned-multilingual-nli_newdata_oneepoch

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7647
- Accuracy: 0.6853
- Precision: 0.6932
- Recall: 0.6853
- F1: 0.6847

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.9394        | 0.04  | 500   | 0.9044          | 0.592    | 0.5985    | 0.592  | 0.5917 |
| 0.8603        | 0.08  | 1000  | 0.9159          | 0.579    | 0.6210    | 0.579  | 0.5739 |
| 0.8293        | 0.11  | 1500  | 0.8520          | 0.6214   | 0.6278    | 0.6214 | 0.6215 |
| 0.8042        | 0.15  | 2000  | 0.8085          | 0.6418   | 0.6439    | 0.6418 | 0.6414 |
| 0.7945        | 0.19  | 2500  | 0.8251          | 0.6319   | 0.6575    | 0.6319 | 0.6262 |
| 0.7768        | 0.23  | 3000  | 0.8298          | 0.6383   | 0.6556    | 0.6383 | 0.6365 |
| 0.753         | 0.27  | 3500  | 0.8225          | 0.6464   | 0.6684    | 0.6464 | 0.6436 |
| 0.754         | 0.3   | 4000  | 0.7979          | 0.6529   | 0.6750    | 0.6529 | 0.6523 |
| 0.7466        | 0.34  | 4500  | 0.7644          | 0.6718   | 0.6727    | 0.6718 | 0.6713 |
| 0.7331        | 0.38  | 5000  | 0.7861          | 0.6591   | 0.6757    | 0.6591 | 0.6581 |
| 0.72          | 0.42  | 5500  | 0.7972          | 0.6595   | 0.6815    | 0.6595 | 0.6582 |
| 0.7103        | 0.46  | 6000  | 0.7652          | 0.6702   | 0.6728    | 0.6702 | 0.6688 |
| 0.7103        | 0.49  | 6500  | 0.7732          | 0.6684   | 0.6796    | 0.6684 | 0.6670 |
| 0.7023        | 0.53  | 7000  | 0.7921          | 0.6657   | 0.6834    | 0.6657 | 0.6663 |
| 0.6827        | 0.57  | 7500  | 0.7672          | 0.6733   | 0.6824    | 0.6733 | 0.6726 |
| 0.6826        | 0.61  | 8000  | 0.7665          | 0.6755   | 0.6789    | 0.6755 | 0.6747 |
| 0.6705        | 0.65  | 8500  | 0.7659          | 0.6755   | 0.6815    | 0.6755 | 0.6748 |
| 0.662         | 0.68  | 9000  | 0.7738          | 0.6767   | 0.6833    | 0.6767 | 0.6757 |
| 0.6556        | 0.72  | 9500  | 0.7623          | 0.6805   | 0.6906    | 0.6805 | 0.6799 |
| 0.6462        | 0.76  | 10000 | 0.7863          | 0.6719   | 0.6849    | 0.6719 | 0.6701 |
| 0.6405        | 0.8   | 10500 | 0.7523          | 0.681    | 0.6845    | 0.681  | 0.6805 |
| 0.6407        | 0.84  | 11000 | 0.7661          | 0.6807   | 0.6856    | 0.6807 | 0.6801 |
| 0.6341        | 0.87  | 11500 | 0.7672          | 0.6787   | 0.6904    | 0.6787 | 0.6770 |
| 0.6292        | 0.91  | 12000 | 0.7742          | 0.682    | 0.6922    | 0.682  | 0.6803 |
| 0.6238        | 0.95  | 12500 | 0.7584          | 0.6855   | 0.6926    | 0.6855 | 0.6850 |
| 0.6201        | 0.99  | 13000 | 0.7647          | 0.6853   | 0.6932    | 0.6853 | 0.6847 |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu102
- Datasets 2.4.0
- Tokenizers 0.12.1
