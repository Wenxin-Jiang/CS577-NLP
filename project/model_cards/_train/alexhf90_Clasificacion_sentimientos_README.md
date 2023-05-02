---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: Clasificacion_sentimientos
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Clasificacion_sentimientos

This model is a fine-tuned version of [BSC-TeMU/roberta-base-bne](https://huggingface.co/BSC-TeMU/roberta-base-bne) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3399
- Accuracy: 0.9428

## Model description

Se entrena un modelo que es capaz de clasificar si es un comentario postivo o negativo.

## Intended uses & limitations

More information needed

## Training and evaluation data

Se entrenó el modelo usando comentarios de peliculas de la página $https://www.filmaffinity.com/es/main.html$
   - Estos comentarios estan en la base de datos alojada en Kaggle, 
     url : https://www.kaggle.com/ricardomoya/criticas-peliculas-filmaffinity-en-espaniol/code

## Training procedure

La variable review_rate se usó para clasificar los comentarios positivos y negativos así:
Positivos: los rating con 8,9,10.
Negativos: Los rating con 3,2,1.

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.2566        | 1.0   | 901  | 0.5299          | 0.8935   |
| 0.0963        | 2.0   | 1802 | 0.2885          | 0.9383   |
| 0.0133        | 3.0   | 2703 | 0.3546          | 0.9406   |
| 0.0002        | 4.0   | 3604 | 0.3399          | 0.9428   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
