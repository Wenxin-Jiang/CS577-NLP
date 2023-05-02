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
- name: layoutlmv3-fine-tuning-invoice 
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
## LayoutLMv3-Fine-Tuning-Invoice Model

#### Model description
**LayoutLMv3-Fine-Tuning-Invoice Model** is a fine-tuned version of [microsoft/layoutlmv3-base](https://huggingface.co/microsoft/layoutlmv3-base) on the invoice dataset. For the fine-tuning, We used [Invoice Dataset](https://huggingface.co/datasets/darentang/generated) that includes 12 labels ('Other', 'ABN', 'BILLER', 'BILLER_ADDRESS', 'BILLER_POST_CODE', 'DUE_DATE', 'GST', 'INVOICE_DATE', 'INVOICE_NUMBER', 'SUBTOTAL', 'TOTAL', 'BILLER_ADDRESS').

It achieves the following results on the evaluation set:
- Loss: 0.005334
- Precision: 1.0
- Recall: 1.0
- F1: 1.0
- Accuracy: 1.0



## Training procedure
### Training hyperparameters
The following hyperparameters were used during training:
- learning_rate: 1.5e-05
- train_batch_size: 2
- eval_batch_size: 2
- optimizer: epsilon=1e-08
- lr_scheduler_type: cosine
- training_steps: 1000

### Training results

| Training Loss |  Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 100 | 0.070030         | 0.972000  | 0.985801 | 0.978852 | 0.997051  |
| No log        | 200 | 0.017637         | 0.972000  | 0.985801 | 0.978852 | 0.997051   |
| No log        | 300 | 0.015573         | 0.972000  | 0.985801 | 0.978852 | 0.997051   |
| No log        | 400 | 0.011000         | 0.973737  | 0.977688 | 0.978852 | 0.996419   |
| 0.110800      | 500 | 0.005334         | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.110800      | 600 | 0.002994         | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.110800      | 700 | 0.002330         | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.110800      | 800 | 0.002188         | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.110800      | 900 | 0.002105         | 1.0       | 1.0    | 1.0    | 1.0      |
| 0.004900      | 1000 | 0.002111        | 1.0       | 1.0    | 1.0    | 1.0      |



### Framework versions

- Transformers 4.20.1