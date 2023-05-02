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

This model is a fine-tuned version of [microsoft/layoutlmv3-base](https://huggingface.co/microsoft/layoutlmv3-base) on the Eurocorporation dataset.

We use Microsoft’s LayoutLMv3 trained on Eurocorporation Dataset to predict the produttore_key, produttore_value, unitloc_key, unitloc_value, cliente_key, cliente_value, operatore_key, operatore_value, referente_key, referente_value, telefono_key, telefono_value, cfproduttore_key, cfproduttore_value, emailcliente_key, emailcliente_value, datarichiesta_key, datarichiesta_value, orariorichiesta_key, orariorichiesta_value,emailproduttore_key,emailproduttore_value,mattina_key,mattina_value,pomeriggio_key,pomeriggio_value,cer_key,cer_value,descrizione_key,descrizione_value,sf_key,sf_value,classpericolo_key,destino_key,destino_value,confezionamento_key,confezionamento_value,destinazione_key and destinazione_value.. To use it, simply upload an image. Results will show up in a few seconds.

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

https://github.com/jyotiyadav94/data/blob/main/Layoutlmv3_training_inference_1_(1).ipynb


The model can be evaluated at the HuggingFace Spaces link:

https://huggingface.co/DataIntelligenceTeam/layoutlmv3-finetuned-eurocorporation

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 5
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 2000

### Training results

| Step | Training Loss | Validation Loss| Precision | Recall | F1     | Accuracy |
|:---:|:------------:|:--------------:|:---------:|:------:|:------:|:---------:|
|100 |	No log       | 0.57765	|0.568773	| 0.600000	|0.583969|  	0.895848|
|200 |	No log       | 0.181364 |	0.933594|	0.937255|	0.935421|	0.988037|
|300 |	No log       |	0.091626|	0.945312|	0.949020|	0.947162|	0.991555|
|400 |	No log       |	0.060504|	0.964981|	0.972549|	0.968750|	0.995074|
|500 |	0.360900     |	0.046041|	0.988327|	0.996078|	0.992188|	0.999296|
|600 |	0.360900     |	0.036889|	0.988327|	0.996078|	0.992188|	0.999296|
|700 |	0.360900     |	0.032077|	0.988327|	0.996078|	0.992188|	0.999296|
|800 |	0.360900     |	0.028109|	0.988327|	0.996078|	0.992188|	0.999296|
|900 |	0.360900     |	0.027945|	0.988327|	0.996078|	0.992188|	0.999296|
|1000|	0.037800     |	0.027469|	0.988327|	0.996078|	0.992188|	0.999296

### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
