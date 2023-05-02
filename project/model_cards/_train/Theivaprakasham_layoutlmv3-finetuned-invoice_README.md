---
tags:
- generated_from_trainer
datasets:
- invoice
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: layoutlmv3-finetuned-invoice
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: Invoice
      type: invoice
      args: invoice
    metrics:
    - name: Precision
      type: precision
      value: 1.0
    - name: Recall
      type: recall
      value: 1.0
    - name: F1
      type: f1
      value: 1.0
    - name: Accuracy
      type: accuracy
      value: 1.0
---

# LayoutLM-v3 model fine-tuned on invoice dataset

This model is a fine-tuned version of [microsoft/layoutlmv3-base](https://huggingface.co/microsoft/layoutlmv3-base) on the invoice dataset.

We use Microsoft’s LayoutLMv3 trained on Invoice Dataset to predict the Biller Name, Biller Address, Biller post_code, Due_date, GST, Invoice_date, Invoice_number, Subtotal and Total. To use it, simply upload an image or use the example image below. Results will show up in a few seconds.

It achieves the following results on the evaluation set:
- Loss: 0.0012
- Precision: 1.0
- Recall: 1.0
- F1: 1.0
- Accuracy: 1.0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data
All the training codes are available from the below GitHub link.

https://github.com/Theivaprakasham/layoutlmv3


The model can be evaluated at the HuggingFace Spaces link:

https://huggingface.co/spaces/Theivaprakasham/layoutlmv3_invoice

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 2000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 2.0   | 100  | 0.0878          | 0.968     | 0.9817 | 0.9748 | 0.9966   |
| No log        | 4.0   | 200  | 0.0241          | 0.972     | 0.9858 | 0.9789 | 0.9971   |
| No log        | 6.0   | 300  | 0.0186          | 0.972     | 0.9858 | 0.9789 | 0.9971   |
| No log        | 8.0   | 400  | 0.0184          | 0.9854    | 0.9574 | 0.9712 | 0.9956   |
| 0.1308        | 10.0  | 500  | 0.0121          | 0.972     | 0.9858 | 0.9789 | 0.9971   |
| 0.1308        | 12.0  | 600  | 0.0076          | 0.9939    | 0.9878 | 0.9908 | 0.9987   |
| 0.1308        | 14.0  | 700  | 0.0047          | 1.0       | 0.9959 | 0.9980 | 0.9996   |
| 0.1308        | 16.0  | 800  | 0.0036          | 0.9960    | 0.9980 | 0.9970 | 0.9996   |
| 0.1308        | 18.0  | 900  | 0.0045          | 0.9960    | 0.9980 | 0.9970 | 0.9996   |
| 0.0069        | 20.0  | 1000 | 0.0043          | 0.9960    | 0.9980 | 0.9970 | 0.9996   |
| 0.0069        | 22.0  | 1100 | 0.0016          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0069        | 24.0  | 1200 | 0.0015          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0069        | 26.0  | 1300 | 0.0014          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0069        | 28.0  | 1400 | 0.0013          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0026        | 30.0  | 1500 | 0.0012          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0026        | 32.0  | 1600 | 0.0012          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0026        | 34.0  | 1700 | 0.0011          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0026        | 36.0  | 1800 | 0.0011          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.0026        | 38.0  | 1900 | 0.0011          | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.002         | 40.0  | 2000 | 0.0011          | 1.0       | 1.0    | 1.0    | 1.0      |


### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
