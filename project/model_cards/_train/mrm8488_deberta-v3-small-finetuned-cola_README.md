---
language:
- en
license: mit
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- matthews_correlation
widget:
- text: They represented seriously to the dean Mary as a genuine linguist.
model-index:
- name: deberta-v3-small
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: GLUE COLA
      type: glue
      args: cola
    metrics:
    - type: matthews_correlation
      value: 0.6333205721749096
      name: Matthews Correlation
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: glue
      type: glue
      config: cola
      split: validation
    metrics:
    - type: accuracy
      value: 0.8494726749760306
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMjJjOTM0MTEzMzBlZWJlMWYwNzgzZmI3M2NiZWVjMDQ5ZDA1MWY0NGY3NjU1NTlmZWE3N2JjZWEzODE0ZTNkNSIsInZlcnNpb24iOjF9.Kt-3jnDTp3-Te5zMHVgG_5hpB5UMCkAMP7fmjx46QDWJfFHpyRgBlf-qz_fw5saFPAQ5G6QNq3bjEJ6mY2lhAw
    - type: precision
      value: 0.8455882352941176
      name: Precision
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiODAxMzNkZGEwNGNmYjk4NWRhZDk4OWE4MzA5Y2NiNjQyNTdkOWRmYjU0ZjY0YzQzYmE4ZmI3MjQ4OTk4OWIwNCIsInZlcnNpb24iOjF9.YBFnePtD5-HX15aST39xpPLroFYBgqEn5iLyVaClh62j0M7HQbB8aaGEbgaTIUIr-qz12gVfIQ7UZZIHxby_BQ
    - type: recall
      value: 0.957004160887656
      name: Recall
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMjRjMTVhN2E4YjNlOWY2MWRhODZiM2FhZDVjNzYwMjIyNWUyYTMxMWFlZjkwNzVhYjNmMjQxYjk2MTFmMzYyYiIsInZlcnNpb24iOjF9.40GYlU9Do74Y_gLmbIKR2WM8okz5fm-QUwJAsoIyM1UtQ71lKd-FV5Yr9CdAh3fyQYa3SMYe6tm9OByNMMw_AA
    - type: auc
      value: 0.9167413271767129
      name: AUC
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYzVjYmMyZDkyMzM0ZTQ1MTk0ZmY4MWUwZmIxMGRlOWMyMjJmNDRiZGNkMGZlZDZmY2I5OWI2NDYzMGQ2YzhiNSIsInZlcnNpb24iOjF9.setZF_g9x-aknFXM1k0NxrOWMJcmpNi6z7QlyfL0i6fTPJOj6SbKJ1WQb3J1zTuabgx9cOc5xgHtBH3IA7fkDQ
    - type: f1
      value: 0.8978529603122967
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNmQ1NmNiMDhmNTU2Y2UxMzU0ODRmYmZmZTFkYjI4MzczMWUwYWQ4OTk2NGJlY2MzNmViYTA4MTRkODJhMTU1MyIsInZlcnNpb24iOjF9.GUIRxsYKgjYK63JS2rd9vCLHHmCiB4H68Xo5GxMaITfyzcUcdNc6l62njmQGrOoUidlTt1F7DzGP2Cu_Gz8HDg
    - type: loss
      value: 0.4050811529159546
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNjBjNjg0OTFjOTc5Mzc2MWQ1ZDIyYmM5MmIzZDVlY2JjYzBlZjMyN2IwOWU4YzNlMDcwZmM0NTMxYjExY2I0MiIsInZlcnNpb24iOjF9.xayLZc97iUW0zNqG65TiW9BXoqzV-tqF8g9qGCYQ1ZGuSDSjLlK7Y4og7-wqPEiME8JtNyVxl6-ZcWnF1t8cDg
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# DeBERTa-v3-small fine-tuned on CoLA

This model is a fine-tuned version of [microsoft/deberta-v3-small](https://huggingface.co/microsoft/deberta-v3-small) on the GLUE COLA dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4051
- Matthews Correlation: 0.6333

## Model description

[DeBERTa](https://arxiv.org/abs/2006.03654) improves the BERT and RoBERTa models using disentangled attention and enhanced mask decoder. With those two improvements, DeBERTa out perform RoBERTa on a majority of NLU tasks with 80GB training data. 

Please check the [official repository](https://github.com/microsoft/DeBERTa) for more details and updates.

In [DeBERTa V3](https://arxiv.org/abs/2111.09543), we replaced the MLM objective with the RTD(Replaced Token Detection) objective introduced by ELECTRA for pre-training, as well as some innovations to be introduced in our upcoming paper. Compared to DeBERTa-V2,  our V3 version significantly improves the model performance in downstream tasks.  You can find a simple introduction about the model from the appendix A11 in our original [paper](https://arxiv.org/abs/2006.03654),  but we will provide more details in a separate write-up.

The DeBERTa V3 small model comes with 6 layers and a hidden size of 768. Its total parameter number is 143M since we use a vocabulary containing 128K tokens which introduce 98M parameters in the Embedding layer.  This model was trained using the 160GB data as DeBERTa V2.

## Intended uses & limitations

More information needed

## Training and evaluation data


The Corpus of Linguistic Acceptability (CoLA) in its full form consists of 10657 sentences from 23 linguistics publications, expertly annotated for acceptability (grammaticality) by their original authors. The public version provided here contains 9594 sentences belonging to training and development sets, and excludes 1063 sentences belonging to a held out test set.


## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Matthews Correlation |
|:-------------:|:-----:|:----:|:---------------:|:--------------------:|
| No log        | 1.0   | 535  | 0.4051          | 0.6333               |
| 0.3371        | 2.0   | 1070 | 0.4455          | 0.6531               |
| 0.3371        | 3.0   | 1605 | 0.5755          | 0.6499               |
| 0.1305        | 4.0   | 2140 | 0.7188          | 0.6553               |
| 0.1305        | 5.0   | 2675 | 0.8047          | 0.6700               |


### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.10.0+cu111
- Datasets 1.16.1
- Tokenizers 0.10.3
