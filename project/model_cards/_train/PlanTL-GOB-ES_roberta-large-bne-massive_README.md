---

language:
- es

license: apache-2.0

tags:
- "spanish"
- "text-classification"
- "multi-class-classification"
- "natural-language-understanding"
- "intent-classificaiton"
- "roberta-large"


datasets:
- "AmazonScience/massive"

metrics:
- f1
    
model-index:
- name: roberta-large-bne-massive
  results:
  - task: 
      name: text-classification
      type: text-classification  
    dataset:
      name: MASSIVE
      type: AmazonScience/massive
      config: es-ES
      split: test
    metrics:
      - name: F1
        type: f1
        value: 0.8727
        
widget:

- text: "pon una playlist de nirvana"
- text: "olly apaga las luces"
- text: "aspira el pasillo"
- text: "cuál es el pronóstico del tiempo de hoy en madrid"
---

# Spanish BERTa (roberta-large-bne-massive) finetuned for Intent Classification

## Table of Contents
<details>
<summary>Click to expand</summary>

- [Model description](#model-description)
- [Intended uses and limitations](#intended-use)
- [How to use](#how-to-use)
- [Limitations and bias](#limitations-and-bias)
- [Training](#training)
  - [Training data](#training-data)
  - [Training procedure](#training-procedure)
- [Evaluation](#evaluation)
   - [Variable and metrics](#variable-and-metrics)
   - [Evaluation results](#evaluation-results)
- [Additional information](#additional-information)
  - [Author](#author)
  - [Contact information](#contact-information)
  - [Copyright](#copyright)
  - [Licensing information](#licensing-information)
  - [Funding](#funding)
  - [Citing information](#citing-information)
  - [Disclaimer](#disclaimer)
</details>

## Model description

The **roberta-large-bne-massive** is a Intent Classification model for the Spanish language fine-tuned from the roberta-large-bne-massive model, a [RoBERTa](https://arxiv.org/abs/1907.11692) based model pre-trained on a medium-size corpus collected from publicly available corpora and crawlers.

The model uses [MASSIVE 1.1](https://huggingface.co/datasets/AmazonScience/massive), a parallel dataset of > 1M utterances across 52 languages with annotations for the Natural Language Understanding tasks of intent prediction and slot annotation. Utterances span 60 intents and include 55 slot types.


## Intended uses and limitations

The **roberta-large-bne-massive** model can be used for intent prediction in plain text sentences in Spanish. It can be used in combination with an Automatic Speech Recognition model in order to implement a Voice Assistant. The model is limited by its training dataset and may not generalize well for all use cases.

## How to use

Here is how to use this model:

```python
from transformers import pipeline
from pprint import pprint

nlp = pipeline("text-classification", model="PlanTL-GOB-ES/roberta-large-bne-massive")
example = "m'agraden les cançons del serrat"

intent = nlp(example)
pprint(intent)
```

## Limitations and bias
At the time of submission, no measures have been taken to estimate the bias embedded in the model. However, we are well aware that our models may be biased since the corpora have been collected using crawling techniques on multiple web sources. We intend to conduct research in these areas in the future, and if completed, this model card will be updated.

## Training

### Training data
We used the Spanish split of the [MASSIVE](https://huggingface.co/datasets/AmazonScience/massive)  dataset for training and evaluation.

### Training procedure
The model was trained with a batch size of 16 and a learning rate of 1e-5 for 20 epochs. We then selected the best checkpoint using the downstream task metric in the corresponding development set and then evaluated it on the test set.

## Evaluation

### Variable and metrics

This model was finetuned maximizing the weighted F1 score.

### Evaluation results
We evaluated the _roberta-large-bne-massive_ on the MASSIVE test set obtaining a weighted F1 score of 87.27.

## Additional information

### Author
Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es)

### Contact information
For further information, send an email to <plantl-gob-es@bsc.es>

### Copyright
Copyright by the Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA) (2022)

### Licensing information
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

### Funding
This work was funded by the Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA) within the framework of the Plan-TL.

### Disclaimer

<details>
<summary>Click to expand</summary>

The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and/or any other undesirable distortions.

When third parties, deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of Artificial Intelligence.

In no event shall the owner of the models (SEDIA – State Secretariat for Digitalization and Artificial Intelligence) nor the creator (BSC – Barcelona Supercomputing Center) be liable for any results arising from the use made by third parties of these models.


Los modelos publicados en este repositorio tienen una finalidad generalista y están a disposición de terceros. Estos modelos pueden tener sesgos y/u otro tipo de distorsiones indeseables.

Cuando terceros desplieguen o proporcionen sistemas y/o servicios a otras partes usando alguno de estos modelos (o utilizando sistemas basados en estos modelos) o se conviertan en usuarios de los modelos, deben tener en cuenta que es su responsabilidad mitigar los riesgos derivados de su uso y, en todo caso, cumplir con la normativa aplicable, incluyendo la normativa en materia de uso de inteligencia artificial.

En ningún caso el propietario de los modelos (SEDIA – Secretaría de Estado de Digitalización e Inteligencia Artificial) ni el creador (BSC – Barcelona Supercomputing Center) serán responsables de los resultados derivados del uso que hagan terceros de estos modelos.
</details>