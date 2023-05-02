---
language:

- es

license: apache-2.0

tags:

- "national library of spain"
- "spanish"
- "bne"
- "xnli"
- "textual entailment"

datasets:

- "xnli"

metrics:
- "accuracy"

model-index:
- name: roberta-large-bne-te
  results:
  - task: 
      type: text-classification
    dataset:
      type:  xnli
      name: XNLI
    metrics:
      - name: Accuracy
        type: accuracy
        value: 0.8263
        

widget:

- "Me gustas. Te quiero."

- "Mi cumpleaños es el 27 de mayo. Cumpliré años a finales de mayo."

---

# Spanish RoBERTa-large trained on BNE finetuned for the Spanish Cross-lingual Natural Language Inference (XNLI) dataset.

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
The **roberta-large-bne-te** is a Textual Entailment (TE) model for the Spanish language fine-tuned from the [roberta-large-bne](https://huggingface.co/PlanTL-GOB-ES/roberta-large-bne) model, a [RoBERTa](https://arxiv.org/abs/1907.11692) large model pre-trained using the largest Spanish corpus known to date, with a total of 570GB of clean and deduplicated text, processed for this work, compiled from the web crawlings performed by the [National Library of Spain (Biblioteca Nacional de España)](http://www.bne.es/en/Inicio/index.html) from 2009 to 2019.



## Intended uses and limitations

**roberta-large-bne-te** model can be used to recognize Textual Entailment (TE). The model is limited by its training dataset and may not generalize well for all use cases.


## How to use

Here is how to use this model:

```python
from transformers import pipeline
from pprint import pprint

nlp = pipeline("text-classification", model="PlanTL-GOB-ES/roberta-large-bne-te")
example = "Mi cumpleaños es el 27 de mayo. Cumpliré años a finales de mayo."

te_results = nlp(example)
pprint(te_results)
```

## Limitations and bias
At the time of submission, no measures have been taken to estimate the bias embedded in the model. However, we are well aware that our models may be biased since the corpora have been collected using crawling techniques on multiple web sources. We intend to conduct research in these areas in the future, and if completed, this model card will be updated.

## Training

We used the TE dataset in Spanish called [XNLI dataset](https://huggingface.co/datasets/xnli) for training and evaluation.

### Training procedure
The model was trained with a batch size of 16 and a learning rate of 1e-5 for 5 epochs. We then selected the best checkpoint using the downstream task metric in the corresponding development set and then evaluated it on the test set.


## Evaluation 

### Variable and metrics

This model was finetuned maximizing accuracy.

## Evaluation results
We evaluated the *roberta-large-bne-te* on the XNLI test set against standard multilingual and monolingual baselines:


| Model        | XNLI (Accuracy) | 
| ------------|:----|
| roberta-large-bne | **82.63** |
| roberta-base-bne | 80.16 |
| BETO       | 81.30 |
| mBERT       | 78.76 |
| BERTIN | 78.90 |
| ELECTRA | 78.78 |

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

## Citing information

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

## Disclaimer

<details>
<summary>Click to expand</summary>

The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and/or any other undesirable distortions.

When third  parties, deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of artificial intelligence.

In no event shall the owner of the models (SEDIA – State Secretariat for digitalization and artificial intelligence) nor the creator (BSC – Barcelona Supercomputing Center) be liable for any results arising from the use made by third parties of these models.


Los modelos publicados en este repositorio tienen una finalidad generalista y están a disposición de terceros. Estos modelos pueden tener sesgos y/u otro tipo de distorsiones indeseables.

Cuando terceros desplieguen o proporcionen sistemas y/o servicios a otras partes usando alguno de estos modelos (o utilizando sistemas basados en estos modelos) o se conviertan en usuarios de los modelos, deben tener en cuenta que es su responsabilidad mitigar los riesgos derivados de su uso y, en todo caso, cumplir con la normativa aplicable, incluyendo la normativa en materia de uso de inteligencia artificial.

En ningún caso el propietario de los modelos (SEDIA – Secretaría de Estado de Digitalización e Inteligencia Artificial) ni el creador (BSC – Barcelona Supercomputing Center) serán responsables de los resultados derivados del uso que hagan terceros de estos modelos.
