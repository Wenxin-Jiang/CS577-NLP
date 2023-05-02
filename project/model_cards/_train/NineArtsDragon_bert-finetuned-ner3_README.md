---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-finetuned-ner3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner3

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0002
- Precision: 0.9795
- Recall: 0.9922
- F1: 0.9858
- Accuracy: 0.9999
- Name Precision: 0.9892
- Name Recall: 0.9946
- Name F1: 0.9919
- Dob Precision: 0.9707
- Dob Recall: 0.9900
- Dob F1: 0.9803

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy | Name Precision | Name Recall | Name F1 | Dob Precision | Dob Recall | Dob F1 |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|:--------------:|:-----------:|:-------:|:-------------:|:----------:|:------:|
| No log        | 1.0   | 108  | 0.0024          | 0.7581    | 0.9766 | 0.8536 | 0.9989   | 0.9579         | 0.9891      | 0.9733  | 0.6340        | 0.9652     | 0.7653 |
| No log        | 2.0   | 216  | 0.0016          | 0.8519    | 0.9558 | 0.9009 | 0.9995   | 0.9624         | 0.9728      | 0.9676  | 0.7683        | 0.9403     | 0.8456 |
| No log        | 3.0   | 324  | 0.0007          | 0.9193    | 0.9766 | 0.9471 | 0.9998   | 0.9784         | 0.9837      | 0.9810  | 0.8705        | 0.9701     | 0.9176 |
| No log        | 4.0   | 432  | 0.0006          | 0.9305    | 0.9740 | 0.9518 | 0.9998   | 0.9838         | 0.9891      | 0.9864  | 0.8853        | 0.9602     | 0.9212 |
| 0.0023        | 5.0   | 540  | 0.0007          | 0.8929    | 0.9532 | 0.9221 | 0.9997   | 0.9733         | 0.9891      | 0.9811  | 0.8259        | 0.9204     | 0.8706 |
| 0.0023        | 6.0   | 648  | 0.0003          | 0.9646    | 0.9922 | 0.9782 | 0.9999   | 0.9892         | 0.9946      | 0.9919  | 0.9431        | 0.9900     | 0.9660 |
| 0.0023        | 7.0   | 756  | 0.0006          | 0.9259    | 0.9740 | 0.9494 | 0.9998   | 0.9581         | 0.9946      | 0.976   | 0.8972        | 0.9552     | 0.9253 |
| 0.0023        | 8.0   | 864  | 0.0007          | 0.9322    | 0.9636 | 0.9476 | 0.9998   | 0.9945         | 0.9891      | 0.9918  | 0.8791        | 0.9403     | 0.9087 |
| 0.0023        | 9.0   | 972  | 0.0002          | 0.9821    | 0.9948 | 0.9884 | 0.9999   | 0.9946         | 0.9946      | 0.9946  | 0.9709        | 0.9950     | 0.9828 |
| 0.0008        | 10.0  | 1080 | 0.0003          | 0.9646    | 0.9922 | 0.9782 | 0.9999   | 0.9946         | 0.9946      | 0.9946  | 0.9387        | 0.9900     | 0.9637 |
| 0.0008        | 11.0  | 1188 | 0.0002          | 0.9846    | 0.9974 | 0.9910 | 0.9999   | 0.9946         | 0.9946      | 0.9946  | 0.9757        | 1.0        | 0.9877 |
| 0.0008        | 12.0  | 1296 | 0.0002          | 0.9720    | 0.9922 | 0.9820 | 0.9999   | 0.9786         | 0.9946      | 0.9865  | 0.9660        | 0.9900     | 0.9779 |
| 0.0008        | 13.0  | 1404 | 0.0002          | 0.9745    | 0.9922 | 0.9833 | 0.9999   | 0.9839         | 0.9946      | 0.9892  | 0.9660        | 0.9900     | 0.9779 |
| 0.0004        | 14.0  | 1512 | 0.0002          | 0.9846    | 0.9974 | 0.9910 | 0.9999   | 0.9839         | 0.9946      | 0.9892  | 0.9853        | 1.0        | 0.9926 |
| 0.0004        | 15.0  | 1620 | 0.0003          | 0.9744    | 0.9896 | 0.9820 | 0.9999   | 0.9786         | 0.9946      | 0.9865  | 0.9706        | 0.9851     | 0.9778 |
| 0.0004        | 16.0  | 1728 | 0.0002          | 0.9769    | 0.9896 | 0.9832 | 0.9999   | 0.9838         | 0.9891      | 0.9864  | 0.9707        | 0.9900     | 0.9803 |
| 0.0004        | 17.0  | 1836 | 0.0003          | 0.9693    | 0.9844 | 0.9768 | 0.9999   | 0.9892         | 0.9946      | 0.9919  | 0.9515        | 0.9751     | 0.9631 |
| 0.0004        | 18.0  | 1944 | 0.0002          | 0.9846    | 0.9948 | 0.9897 | 1.0000   | 0.9892         | 0.9946      | 0.9919  | 0.9804        | 0.9950     | 0.9877 |
| 0.0002        | 19.0  | 2052 | 0.0002          | 0.9795    | 0.9922 | 0.9858 | 0.9999   | 0.9892         | 0.9946      | 0.9919  | 0.9707        | 0.9900     | 0.9803 |
| 0.0002        | 20.0  | 2160 | 0.0002          | 0.9795    | 0.9922 | 0.9858 | 0.9999   | 0.9892         | 0.9946      | 0.9919  | 0.9707        | 0.9900     | 0.9803 |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.2
