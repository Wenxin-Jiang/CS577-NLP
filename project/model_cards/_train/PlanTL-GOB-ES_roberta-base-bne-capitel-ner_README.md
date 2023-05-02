---
language:

- es

license: apache-2.0

tags:

- "national library of spain"

- "spanish"

- "bne"

- "capitel"

- "ner"

datasets:

- "bne"

- "capitel"  


metrics:

- "f1"

inference:
  parameters:
    aggregation_strategy: "first"

model-index:
- name: roberta-base-bne-capiter-ner
  results:
  - task: 
      type: token-classification
    dataset:
      type:  ner
      name: CAPITEL-NERC
    metrics:
      - name: F1
        type: f1
        value: 0.8960
        

widget:

- "Me llamo Francisco Javier y vivo en Madrid."

- "Mi hermano Ramón y su mejor amigo Luis trabajan en el BSC."

---

# Spanish RoBERTa-base trained on BNE finetuned for CAPITEL Named Entity Recognition (NER) dataset.

## Table of contents
<details>
<summary>Click to expand</summary>

- [Model description](#model-description)
- [Intended uses and limitations](#intended-use)
- [How to use](#how-to-use)
- [Limitations and bias](#limitations-and-bias)
- [Training](#training)
- [Training](#training)
  - [Training data](#training-data)
  - [Training procedure](#training-procedure)
- [Evaluation](#evaluation)
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
The **roberta-base-bne-capitel-ner** is a Named Entity Recognition (NER) model for the Spanish language fine-tuned from the [roberta-base-bne](https://huggingface.co/PlanTL-GOB-ES/roberta-base-bne) model, a [RoBERTa](https://arxiv.org/abs/1907.11692) base model pre-trained using the largest Spanish corpus known to date, with a total of 570GB of clean and deduplicated text, processed for this work, compiled from the web crawlings performed by the [National Library of Spain (Biblioteca Nacional de España)](http://www.bne.es/en/Inicio/index.html) from 2009 to 2019.

## Intended uses and limitations

**roberta-base-bne-capitel-ner** model can be used to recognize Named Entities (NE). The model is limited by its training dataset and may not generalize well for all use cases.

## How to use

```python
from transformers import pipeline
from pprint import pprint

nlp = pipeline("ner", model="PlanTL-GOB-ES/roberta-base-bne-capitel-ner")
example = "Me llamo Francisco Javier y vivo en Madrid."

ner_results = nlp(example)
pprint(ner_results)
```

## Limitations and bias
At the time of submission, no measures have been taken to estimate the bias embedded in the model. However, we are well aware that our models may be biased since the corpora have been collected using crawling techniques on multiple web sources. We intend to conduct research in these areas in the future, and if completed, this model card will be updated.

## Training

The dataset used for training and evaluation is the one from the [CAPITEL competition at IberLEF 2020](https://sites.google.com/view/capitel2020) (sub-task 1).

### Training procedure
The model was trained with a batch size of 16 and a learning rate of 5e-5 for 5 epochs. We then selected the best checkpoint using the downstream task metric in the corresponding development set and then evaluated it on the test set.

## Evaluation 


### Variable and metrics
This model was finetuned maximizing F1 score.

## Evaluation results
We evaluated the **roberta-base-bne-capitel-ner** on the CAPITEL-NERC test set against standard multilingual and monolingual baselines:


| Model        | CAPITEL-NERC (F1) | 
| ------------|:----|
| roberta-large-bne-capitel-ner | **90.51** |
| roberta-base-bne-capitel-ner | 89.60|
| BETO       | 87.72 |
| mBERT       | 88.10 |
| BERTIN | 88.56 |
| ELECTRA | 80.35 |

For more details, check the fine-tuning and evaluation scripts in the official [GitHub repository](https://github.com/PlanTL-GOB-ES/lm-spanish).


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

### Citing information
If you use this model, please cite our [paper](http://journal.sepln.org/sepln/ojs/ojs/index.php/pln/article/view/6405):
```
@article{,
   abstract = {We want to thank the National Library of Spain for such a large effort on the data gathering and the Future of Computing Center, a
Barcelona Supercomputing Center and IBM initiative (2020). This work was funded by the Spanish State Secretariat for Digitalization and Artificial
Intelligence (SEDIA) within the framework of the Plan-TL.},
   author = {Asier Gutiérrez Fandiño and Jordi Armengol Estapé and Marc Pàmies and Joan Llop Palao and Joaquin Silveira Ocampo and Casimiro Pio Carrino and Carme Armentano Oller and Carlos Rodriguez Penagos and Aitor Gonzalez Agirre and Marta Villegas},
   doi = {10.26342/2022-68-3},
   issn = {1135-5948},
   journal = {Procesamiento del Lenguaje Natural},
   keywords = {Artificial intelligence,Benchmarking,Data processing.,MarIA,Natural language processing,Spanish language modelling,Spanish language resources,Tractament del llenguatge natural (Informàtica),Àrees temàtiques de la UPC::Informàtica::Intel·ligència artificial::Llenguatge natural},
   publisher = {Sociedad Española para el Procesamiento del Lenguaje Natural},
   title = {MarIA: Spanish Language Models},
   volume = {68},
   url = {https://upcommons.upc.edu/handle/2117/367156#.YyMTB4X9A-0.mendeley},
   year = {2022},
}

```

### Disclaimer

The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and/or any other undesirable distortions.

When third  parties, deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of artificial intelligence.

In no event shall the owner of the models (SEDIA – State Secretariat for digitalization and artificial intelligence) nor the creator (BSC – Barcelona Supercomputing Center) be liable for any results arising from the use made by third parties of these models.


Los modelos publicados en este repositorio tienen una finalidad generalista y están a disposición de terceros. Estos modelos pueden tener sesgos y/u otro tipo de distorsiones indeseables.

Cuando terceros desplieguen o proporcionen sistemas y/o servicios a otras partes usando alguno de estos modelos (o utilizando sistemas basados en estos modelos) o se conviertan en usuarios de los modelos, deben tener en cuenta que es su responsabilidad mitigar los riesgos derivados de su uso y, en todo caso, cumplir con la normativa aplicable, incluyendo la normativa en materia de uso de inteligencia artificial.

En ningún caso el propietario de los modelos (SEDIA – Secretaría de Estado de Digitalización e Inteligencia Artificial) ni el creador (BSC – Barcelona Supercomputing Center) serán responsables de los resultados derivados del uso que hagan terceros de estos modelos.