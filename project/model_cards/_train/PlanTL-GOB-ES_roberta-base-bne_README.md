---

language:

- es

license: apache-2.0

tags:

- "national library of spain"

- "spanish"

- "bne"

- "roberta-base-bne"

datasets:

- "bne"

metrics:

- "ppl"

widget:
- text: "Por la ventanilla del coche vi la Giralda y pensé que bonita que es la ciudad de <mask>." 
- text: "Más vale <mask> que lamentar."
- text: "Caminante no hay camino, se hace camino al <mask>."
- text: "Tengo una pelota roja y otra amarilla. Si le doy la roja a Jose, sólo me queda la <mask>."
- text: "Tengo una pelota roja y otra amarilla. Si le doy la amarilla a Jose, sólo me queda la <mask>."
- text: "El <mask> es el pico más alto de España."

---

# RoBERTa base trained with data from the National Library of Spain (BNE)

## Table of Contents
<details>
<summary>Click to expand</summary>

- [Overview](#overview)
- [Model description](#model-description)
- [Intended uses and limitations](#intended-uses-and-limitations)
- [How to use](#how-to-use)
- [Limitations and bias](#limitations-and-bias)
- [Training](#training)
  - [Training data](#training-data)
  - [Training procedure](#training-procedure)
- [Evaluation](#evaluation)
- [Additional information](#additional-information)
  - [Author](#author)
  - [Contact information](#contact-information)
  - [Copyright](#copyright)
  - [Licensing information](#licensing-information)
  - [Funding](#funding)
  - [Citation Information](#citation-information)
  - [Disclaimer](#disclaimer)

</details>

## Overview
- **Architecture:** roberta-base
- **Language:** Spanish
- **Task:** fill-mask
- **Data:** BNE

## Model description
The **roberta-base-bne** is a transformer-based masked language model for the Spanish language. It is based on the [RoBERTa](https://arxiv.org/abs/1907.11692) base model and has been pre-trained using the largest Spanish corpus known to date, with a total of 570GB of clean and deduplicated text processed for this work, compiled from the web crawlings performed by the [National Library of Spain (Biblioteca Nacional de España)](http://www.bne.es/en/Inicio/index.html) from 2009 to 2019.

## Intended uses and limitations
The **roberta-base-bne** model is ready-to-use only for masked language modeling to perform the Fill Mask task (try the inference API or read the next section).
However, it is intended to be fine-tuned on non-generative downstream tasks such as Question Answering, Text Classification, or Named Entity Recognition.
You can use the raw model for fill mask or fine-tune it to a downstream task.

## How to use
Here is how to use this model:

```python
>>> from transformers import pipeline
>>> from pprint import pprint
>>> unmasker = pipeline('fill-mask', model='PlanTL-GOB-ES/roberta-base-bne')
>>> pprint(unmasker("Gracias a los datos de la BNE se ha podido <mask> este modelo del lenguaje."))
[{'score': 0.08422081917524338, 
'token': 3832, 
'token_str': ' desarrollar', 
'sequence': 'Gracias a los datos de la BNE se ha podido desarrollar este modelo del lenguaje.'}, 
{'score': 0.06348305940628052, 
'token': 3078, 
'token_str': ' crear', 
'sequence': 'Gracias a los datos de la BNE se ha podido crear este modelo del lenguaje.'}, 
{'score': 0.06148449331521988, 
'token': 2171, 
'token_str': ' realizar', 
'sequence': 'Gracias a los datos de la BNE se ha podido realizar este modelo del lenguaje.'}, 
{'score': 0.056218471378088, 
'token': 10880, 
'token_str': ' elaborar', 
'sequence': 'Gracias a los datos de la BNE se ha podido elaborar este modelo del lenguaje.'}, 
{'score': 0.05133328214287758, 
'token': 31915, 
'token_str': ' validar', 
'sequence': 'Gracias a los datos de la BNE se ha podido validar este modelo del lenguaje.'}]
```

Here is how to use this model to get the features of a given text in PyTorch:

```python
>>> from transformers import RobertaTokenizer, RobertaModel
>>> tokenizer = RobertaTokenizer.from_pretrained('PlanTL-GOB-ES/roberta-base-bne')
>>> model = RobertaModel.from_pretrained('PlanTL-GOB-ES/roberta-base-bne')
>>> text = "Gracias a los datos de la BNE se ha podido desarrollar este modelo del lenguaje."
>>> encoded_input = tokenizer(text, return_tensors='pt')
>>> output = model(**encoded_input)
>>> print(output.last_hidden_state.shape)
torch.Size([1, 19, 768])
```


## Limitations and bias

At the time of submission, no measures have been taken to estimate the bias and toxicity embedded in the model. However, we are well aware that our models may be biased since the corpora have been collected using crawling techniques on multiple web sources. We intend to conduct research in these areas in the future, and if completed, this model card will be updated. Nevertheless, here's an example of how the model can have biased predictions:

```python
>>> from transformers import pipeline, set_seed
>>> from pprint import pprint
>>> unmasker = pipeline('fill-mask', model='PlanTL-GOB-ES/roberta-base-bne')
>>> set_seed(42)
>>> pprint(unmasker("Antonio está pensando en <mask>."))
[{'score': 0.07950365543365479,
  'sequence': 'Antonio está pensando en ti.',
  'token': 486,
  'token_str': ' ti'},
 {'score': 0.03375273942947388,
  'sequence': 'Antonio está pensando en irse.',
  'token': 13134,
  'token_str': ' irse'},
 {'score': 0.031026942655444145,
  'sequence': 'Antonio está pensando en casarse.',
  'token': 24852,
  'token_str': ' casarse'},
 {'score': 0.030703715980052948,
  'sequence': 'Antonio está pensando en todo.',
  'token': 665,
  'token_str': ' todo'},
 {'score': 0.02838558703660965,
  'sequence': 'Antonio está pensando en ello.',
  'token': 1577,
  'token_str': ' ello'}]

>>> set_seed(42)
>>> pprint(unmasker("Mohammed está pensando en <mask>."))
[{'score': 0.05433618649840355,
  'sequence': 'Mohammed está pensando en morir.',
  'token': 9459,
  'token_str': ' morir'},
 {'score': 0.0400255024433136,
  'sequence': 'Mohammed está pensando en irse.',
  'token': 13134,
  'token_str': ' irse'},
 {'score': 0.03705748915672302,
  'sequence': 'Mohammed está pensando en todo.',
  'token': 665,
  'token_str': ' todo'},
 {'score': 0.03658654913306236,
  'sequence': 'Mohammed está pensando en quedarse.',
  'token': 9331,
  'token_str': ' quedarse'},
 {'score': 0.03329474478960037,
  'sequence': 'Mohammed está pensando en ello.',
  'token': 1577,
  'token_str': ' ello'}]
```


## Training

### Training data 

The [National Library of Spain (Biblioteca Nacional de España)](http://www.bne.es/en/Inicio/index.html) crawls all .es domains once a year. The training corpus consists of 59TB of WARC files from these crawls, carried out from 2009 to 2019.

To obtain a high-quality training corpus, the corpus has been preprocessed with a pipeline of operations, including among others, sentence splitting, language detection, filtering of bad-formed sentences, and deduplication of repetitive contents. During the process, document boundaries are kept. This resulted in 2TB of Spanish clean corpus. Further global deduplication among the corpus is applied, resulting in 570GB of text.

Some of the statistics of the corpus:

| Corpora | Number of documents | Number of tokens | Size (GB) |
|---------|---------------------|------------------|-----------|
| BNE     |         201,080,084 |  135,733,450,668 |     570GB |


### Training procedure
The training corpus has been tokenized using a byte version of Byte-Pair Encoding (BPE) used in the original [RoBERTA](https://arxiv.org/abs/1907.11692) model with a vocabulary size of 50,262 tokens.

The **roberta-base-bne** pre-training consists of a masked language model training, that follows the approach employed for the RoBERTa base. The training lasted a total of 48 hours with 16 computing nodes, each one with 4 NVIDIA V100 GPUs of 16GB VRAM.

## Evaluation

When fine-tuned on downstream tasks, this model achieves the following results:

| Dataset      | Metric   | [**RoBERTa-base**](https://huggingface.co/PlanTL-GOB-ES/roberta-base-bne)   |
|--------------|----------|------------|
| MLDoc        | F1       |     0.9664 |
| CoNLL-NERC   | F1       |     0.8851 |
| CAPITEL-NERC | F1       |     0.8960 |
| PAWS-X       | F1       |     0.9020 |
| UD-POS       | F1       |     0.9907 |
| CAPITEL-POS  | F1       |     0.9846 |
| SQAC         | F1       |     0.7923 |
| STS          | Combined |     0.8533 |
| XNLI         | Accuracy |     0.8016 |

For more evaluation details visit our [GitHub repository](https://github.com/PlanTL-GOB-ES/lm-spanish) or [paper](http://journal.sepln.org/sepln/ojs/ojs/index.php/pln/article/view/6405). 

## Additional information

### Author
Text Mining Unit (TeMU) from Barcelona Supercomputing Center (<bsc-temu@bsc.es>).

### Contact information
For further information, send an email to <plantl-gob-es@bsc.es>.

### Copyright
Copyright by the [Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA)](https://portal.mineco.gob.es/en-us/digitalizacionIA/Pages/sedia.aspx).

### Licensing information
This work is licensed under a [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

### Funding
This work was funded by the [Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA)](https://portal.mineco.gob.es/en-us/digitalizacionIA/Pages/sedia.aspx) within the framework of the Plan-TL.

### Citation information
If you use this model, please cite our [paper](http://journal.sepln.org/sepln/ojs/ojs/index.php/pln/article/view/6405):
```
@article{,
   title = {MarIA: Spanish Language Models},
   author = {Asier Gutiérrez Fandiño and Jordi Armengol Estapé and Marc Pàmies and Joan Llop Palao and Joaquin Silveira Ocampo and Casimiro Pio Carrino and Carme Armentano Oller and Carlos Rodriguez Penagos and Aitor Gonzalez Agirre and Marta Villegas},
   doi = {10.26342/2022-68-3},
   issn = {1135-5948},
   journal = {Procesamiento del Lenguaje Natural},
   publisher = {Sociedad Española para el Procesamiento del Lenguaje Natural},
   url = {https://upcommons.upc.edu/handle/2117/367156#.YyMTB4X9A-0.mendeley},
   volume = {68},
   year = {2022},
}
```

### Disclaimer
<details>
<summary>Click to expand</summary>

The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and/or any other undesirable distortions.

When third parties deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of Artificial Intelligence.

In no event shall the owner of the models (SEDIA) nor the creator (BSC) be liable for any results arising from the use made by third parties of these models.


Los modelos publicados en este repositorio tienen una finalidad generalista y están a disposición de terceros. Estos modelos pueden tener sesgos y/u otro tipo de distorsiones indeseables.

Cuando terceros desplieguen o proporcionen sistemas y/o servicios a otras partes usando alguno de estos modelos (o utilizando sistemas basados en estos modelos) o se conviertan en usuarios de los modelos, deben tener en cuenta que es su responsabilidad mitigar los riesgos derivados de su uso y, en todo caso, cumplir con la normativa aplicable, incluyendo la normativa en materia de uso de Inteligencia Artificial.

En ningún caso el propietario de los modelos (SEDIA) ni el creador (BSC) serán responsables de los resultados derivados del uso que hagan terceros de estos models.
</details>