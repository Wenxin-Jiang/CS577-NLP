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
- name: NER_EHR_Spanish_model_Mulitlingual_BERT
  results: []
  
widget:

- text: 'Presentamos el caso de una mujer de 30 años, fumadora de 20 cigarrillos/día y sin otros antecedentes personales de interés. La paciente refiere infecciones urinarias de repetición. Se indica realización de ecografía abdominal, observándose una lesión nodular intravesical, por lo que es derivada a consulta de urología.
En cistoscopia se visualiza tumoración exofítica de 3x3 cms. en cara lateral derecha con mucosa vesical íntegra, no encontrándose alteraciones en el resto de la vejiga. Se realiza exploración bajo anestesia (EBA) y resección transuretral de dicha lesión (RTU).
En el informe de anatomía patológica macroscópicamente se describen fragmentos de pared vesical con urotelio conservado sin displasia, destacando en la capa muscular propia y en continuidad con el tejido muscular de la misma, una tumoración fusocelular con células que muestran unos núcleos de gran tamaño, pleomórficos, de aspecto vesiculoso y unos citoplasmas amplios eosinófilos. Esta celularidad se dispone en formas de fascículos mal definidos y entre la misma se reconoce abundante celularidad constituida fundamentalmente por numerosas células plasmáticas y leucocitos polimorfonucleares eosinófilos. No se observa un índice mitótico elevado, aunque el índice de proliferación medido como positividad nuclear con anticuerpos frente a MIB-1 se encuentra entre el 10 y el 25% de la celularidad tumoral. No se han objetivado áreas de necrosis. En estudio inmunohistoquímico se observa marcada positividad frente a citoqueratinas (AE1/AE3) y CAM5.2 a nivel citoplasmático, así como una marcada positividad citoplasmática con anticuerpos frente a p80 (proteína ALK). La celularidad descrita ha resultado negativa con anticuerpos frente a músculo liso (actina de músculo liso, MyO D1 y Calretinina), así como para CEA y citoqueratinas de alto peso molecular, observándose tan sólo positividad focal y aislada frente a EMA. Tras realización de FISH sobre material parafinado no se evidencia traslocación en el gen de la ALK.
El diagnóstico anatomopatológico definitivo es tumor miofibroblástico inflamatorio vesical.'
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# NER_EHR_Spanish_model_Mulitlingual_BERT

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on the DisTEMIST shared task 2022 dataset. It is available at: https://temu.bsc.es/distemist/category/data/


It achieves the following results on the evaluation set:
- Loss: 0.2603
- Precision: 0.5637
- Recall: 0.5801
- F1: 0.5718
- Accuracy: 0.9534

## Model description

For a complete description of our system, please go to: https://ceur-ws.org/Vol-3180/paper-26.pdf

## Training and evaluation data

Dataset provided by DisTEMIST shared task, it is available at: https://temu.bsc.es/distemist/category/data/

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

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 71   | 0.2060          | 0.5017    | 0.5540 | 0.5266 | 0.9496   |
| No log        | 2.0   | 142  | 0.2163          | 0.5363    | 0.5433 | 0.5398 | 0.9495   |
| No log        | 3.0   | 213  | 0.2245          | 0.5521    | 0.5356 | 0.5438 | 0.9514   |
| No log        | 4.0   | 284  | 0.2453          | 0.5668    | 0.5985 | 0.5822 | 0.9522   |
| No log        | 5.0   | 355  | 0.2433          | 0.5657    | 0.5579 | 0.5617 | 0.9530   |
| No log        | 6.0   | 426  | 0.2553          | 0.5762    | 0.5762 | 0.5762 | 0.9536   |
| No log        | 7.0   | 497  | 0.2603          | 0.5637    | 0.5801 | 0.5718 | 0.9534   |


### How to cite this work:

Tamayo, A., Burgos, D. A., & Gelbukh, A. (2022). mbert and simple post-processing: A baseline for disease mention detection in spanish. In Working Notes of Conference and Labs of the Evaluation (CLEF) Forum. CEUR Workshop Proceedings.

@inproceedings{tamayo2022mbert,
  title={mbert and simple post-processing: A baseline for disease mention detection in spanish},
  author={Tamayo, Antonio and Burgos, Diego A and Gelbukh, Alexander},
  booktitle={Working Notes of Conference and Labs of the Evaluation (CLEF) Forum. CEUR Workshop Proceedings},
  year={2022}
}

### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu113
- Datasets 2.2.0
- Tokenizers 0.12.1
