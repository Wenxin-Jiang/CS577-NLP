---
license: cc-by-nc-sa-4.0
tags:
- generated_from_trainer
datasets:
- wildreceipt
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: layoutlmv3-finetuned-wildreceipt
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: wildreceipt
      type: wildreceipt
      config: WildReceipt
      split: train
      args: WildReceipt
    metrics:
    - name: Precision
      type: precision
      value: 0.877962408063198
    - name: Recall
      type: recall
      value: 0.8870235310306867
    - name: F1
      type: f1
      value: 0.8824697104524608
    - name: Accuracy
      type: accuracy
      value: 0.9265109136777449
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# layoutlmv3-finetuned-wildreceipt

This model is a fine-tuned version of [microsoft/layoutlmv3-base](https://huggingface.co/microsoft/layoutlmv3-base) on the wildreceipt dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3129
- Precision: 0.8780
- Recall: 0.8870
- F1: 0.8825
- Accuracy: 0.9265

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 4000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 0.32  | 100  | 1.2240          | 0.6077    | 0.3766 | 0.4650 | 0.7011   |
| No log        | 0.63  | 200  | 0.8417          | 0.6440    | 0.5089 | 0.5685 | 0.7743   |
| No log        | 0.95  | 300  | 0.6466          | 0.7243    | 0.6583 | 0.6897 | 0.8311   |
| No log        | 1.26  | 400  | 0.5516          | 0.7533    | 0.7158 | 0.7341 | 0.8537   |
| 0.9961        | 1.58  | 500  | 0.4845          | 0.7835    | 0.7557 | 0.7693 | 0.8699   |
| 0.9961        | 1.89  | 600  | 0.4506          | 0.7809    | 0.7930 | 0.7869 | 0.8770   |
| 0.9961        | 2.21  | 700  | 0.4230          | 0.8101    | 0.8107 | 0.8104 | 0.8886   |
| 0.9961        | 2.52  | 800  | 0.3797          | 0.8211    | 0.8296 | 0.8253 | 0.8983   |
| 0.9961        | 2.84  | 900  | 0.3576          | 0.8289    | 0.8411 | 0.8349 | 0.9016   |
| 0.4076        | 3.15  | 1000 | 0.3430          | 0.8394    | 0.8371 | 0.8382 | 0.9055   |
| 0.4076        | 3.47  | 1100 | 0.3354          | 0.8531    | 0.8405 | 0.8467 | 0.9071   |
| 0.4076        | 3.79  | 1200 | 0.3331          | 0.8371    | 0.8504 | 0.8437 | 0.9076   |
| 0.4076        | 4.1   | 1300 | 0.3184          | 0.8445    | 0.8609 | 0.8526 | 0.9118   |
| 0.4076        | 4.42  | 1400 | 0.3087          | 0.8617    | 0.8580 | 0.8598 | 0.9150   |
| 0.2673        | 4.73  | 1500 | 0.3013          | 0.8613    | 0.8657 | 0.8635 | 0.9177   |
| 0.2673        | 5.05  | 1600 | 0.2971          | 0.8630    | 0.8689 | 0.8659 | 0.9181   |
| 0.2673        | 5.36  | 1700 | 0.3075          | 0.8675    | 0.8639 | 0.8657 | 0.9177   |
| 0.2673        | 5.68  | 1800 | 0.2989          | 0.8551    | 0.8764 | 0.8656 | 0.9193   |
| 0.2673        | 5.99  | 1900 | 0.3011          | 0.8572    | 0.8762 | 0.8666 | 0.9194   |
| 0.2026        | 6.31  | 2000 | 0.3107          | 0.8595    | 0.8722 | 0.8658 | 0.9181   |
| 0.2026        | 6.62  | 2100 | 0.3050          | 0.8678    | 0.8800 | 0.8739 | 0.9220   |
| 0.2026        | 6.94  | 2200 | 0.2971          | 0.8722    | 0.8789 | 0.8755 | 0.9237   |
| 0.2026        | 7.26  | 2300 | 0.3057          | 0.8666    | 0.8785 | 0.8725 | 0.9209   |
| 0.2026        | 7.57  | 2400 | 0.3172          | 0.8593    | 0.8773 | 0.8682 | 0.9184   |
| 0.1647        | 7.89  | 2500 | 0.3018          | 0.8695    | 0.8823 | 0.8759 | 0.9228   |
| 0.1647        | 8.2   | 2600 | 0.3001          | 0.8760    | 0.8795 | 0.8777 | 0.9256   |
| 0.1647        | 8.52  | 2700 | 0.3068          | 0.8758    | 0.8745 | 0.8752 | 0.9235   |
| 0.1647        | 8.83  | 2800 | 0.3007          | 0.8779    | 0.8779 | 0.8779 | 0.9248   |
| 0.1647        | 9.15  | 2900 | 0.3063          | 0.8740    | 0.8763 | 0.8751 | 0.9228   |
| 0.1342        | 9.46  | 3000 | 0.3096          | 0.8675    | 0.8834 | 0.8754 | 0.9235   |
| 0.1342        | 9.78  | 3100 | 0.3052          | 0.8736    | 0.8848 | 0.8792 | 0.9249   |
| 0.1342        | 10.09 | 3200 | 0.3120          | 0.8727    | 0.8885 | 0.8805 | 0.9252   |
| 0.1342        | 10.41 | 3300 | 0.3146          | 0.8718    | 0.8843 | 0.8780 | 0.9243   |
| 0.1342        | 10.73 | 3400 | 0.3124          | 0.8720    | 0.8880 | 0.8799 | 0.9253   |
| 0.117         | 11.04 | 3500 | 0.3088          | 0.8761    | 0.8817 | 0.8789 | 0.9252   |
| 0.117         | 11.36 | 3600 | 0.3082          | 0.8782    | 0.8834 | 0.8808 | 0.9257   |
| 0.117         | 11.67 | 3700 | 0.3129          | 0.8767    | 0.8847 | 0.8807 | 0.9256   |
| 0.117         | 11.99 | 3800 | 0.3116          | 0.8792    | 0.8847 | 0.8820 | 0.9265   |
| 0.117         | 12.3  | 3900 | 0.3142          | 0.8768    | 0.8874 | 0.8821 | 0.9261   |
| 0.1022        | 12.62 | 4000 | 0.3129          | 0.8780    | 0.8870 | 0.8825 | 0.9265   |


### Framework versions

- Transformers 4.22.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
