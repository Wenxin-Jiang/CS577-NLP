---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- nubes
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Negation_Scope_Detection_NubEs_Spanish_mBERT_fine_tuned
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: nubes
      type: nubes
      config: Nubes
      split: train
      args: Nubes
    metrics:
    - name: Precision
      type: precision
      value: 0.9012345679012346
    - name: Recall
      type: recall
      value: 0.9184315370098554
    - name: F1
      type: f1
      value: 0.909751791463288
    - name: Accuracy
      type: accuracy
      value: 0.9743603468579382

widget:

- text: "Paciente con diagnóstico de ELA en abril de 2015 que presenta desde hace más de dos meses disfagia progresiva, para líquidos preferentemente, con dos neumonías por aspiración, por lo que se programa ingreso para colocación de sonda de gastrostomía, realizándose el día 31 de diciembre, sin complicaciones y tolerando posteriormente la dieta por gastrostomía."
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Negation_Scope_Detection_NubEs_Spanish_mBERT_fine_tuned

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on the nubes dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1624
- Precision: 0.9012
- Recall: 0.9184
- F1: 0.9098
- Accuracy: 0.9744

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 7

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1802        | 1.0   | 1726  | 0.1849          | 0.7843    | 0.8526 | 0.8170 | 0.9509   |
| 0.1216        | 2.0   | 3452  | 0.1512          | 0.8706    | 0.8352 | 0.8525 | 0.9579   |
| 0.0817        | 3.0   | 5178  | 0.1083          | 0.8845    | 0.9038 | 0.8940 | 0.9710   |
| 0.0517        | 4.0   | 6904  | 0.1314          | 0.8858    | 0.8960 | 0.8909 | 0.9693   |
| 0.0265        | 5.0   | 8630  | 0.1514          | 0.8963    | 0.9079 | 0.9021 | 0.9721   |
| 0.0136        | 6.0   | 10356 | 0.1524          | 0.9045    | 0.9092 | 0.9068 | 0.9729   |
| 0.0045        | 7.0   | 12082 | 0.1624          | 0.9012    | 0.9184 | 0.9098 | 0.9744   |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
