---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-finetuned-ner_swedish_small_set_health_and_standart
  results: []
---
# Named Entity Recognition model for swedish
This model is a fine-tuned version of [KBLab/bert-base-swedish-cased-ner](https://huggingface.co/KBLab/bert-base-swedish-cased-ner)for only Swedish. It has been fine-tuned on the concatenation of a smaller version of SUC 3.0 and some medical text from the Swedish website 1177.

The model will predict the following entities:

| Tag | Name | Exampel |
|:-------------:|:-----:|:----:|
| PER	        |Person   | (e.g.,  Johan  and  Sofia)   |
| LOC        | Location  | (e.g., Göteborg and Spanien)   | 
| ORG        | Organisation   | (e.g., Volvo and Skatteverket) \  | 
| PHARMA_DRUGS        | Medication  |  (e.g., Paracetamol and Omeprazol)|
| HEALTH        | Illness/Diseases  | (e.g., Cancer, sjuk and diabetes)  | 
| Relation        | Family members  |  (e.g., Mamma and Farmor)  | 



<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner_swedish_small_set_health_and_standart

It achieves the following results on the evaluation set:
- Loss: 0.0963
- Precision: 0.7548
- Recall: 0.7811
- F1: 0.7677
- Accuracy: 0.9756

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 219  | 0.1123          | 0.7674    | 0.6567 | 0.7078 | 0.9681   |
| No log        | 2.0   | 438  | 0.0934          | 0.7643    | 0.7662 | 0.7652 | 0.9738   |
| 0.1382        | 3.0   | 657  | 0.0963          | 0.7548    | 0.7811 | 0.7677 | 0.9756   |


### Framework versions

- Transformers 4.19.3
- Pytorch 1.7.1
- Datasets 2.2.2
- Tokenizers 0.12.1
