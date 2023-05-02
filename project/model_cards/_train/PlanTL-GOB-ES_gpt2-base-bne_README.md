---
language:

- es

license: apache-2.0

tags:

- "national library of spain"

- "spanish"

- "bne"

- "gpt2-base-bne"

datasets:

- "bne"

widget:
- text: "El modelo del lenguaje GPT es capaz de"
- text: "La Biblioteca Nacional de España es una entidad pública y sus fines son"

---

# GPT2-base (gpt2-base-bne) trained with data from the National Library of Spain (BNE)

## Table of Contents
<details>
<summary>Click to expand</summary>

- [Overview](#overview)
- [Model description](#model-description)
- [Intended uses and limitations](#intended-uses-and-limitations)
- [How to Use](#how-to-use)
- [Limitations and bias](#limitations-and-bias)
- [Training](#training)
  - [Training data](#training-data)
  - [Training procedure](#training-procedure)
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

- **Architecture:** gpt2-base
- **Language:** Spanish
- **Task:** text-generation
- **Data:** BNE

## Model description

**GPT2-base-bne** is a transformer-based model for the Spanish language. It is based on the [GPT-2](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) model and has been pre-trained using the largest Spanish corpus known to date, with a total of 570GB of clean and deduplicated text processed for this work, compiled from the web crawlings performed by the  [National Library of Spain (Biblioteca Nacional de España)](http://www.bne.es/en/Inicio/index.html) from 2009 to 2019.


## Intended uses and limitations
You can use the raw model for text generation or fine-tune it to a downstream task.

## How to Use
Here is how to use this model:

You can use this model directly with a pipeline for text generation. Since the generation relies on some randomness, we set a seed for reproducibility:

```python
>>> from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, set_seed
>>> tokenizer = AutoTokenizer.from_pretrained("PlanTL-GOB-ES/gpt2-base-bne")
>>> model = AutoModelForCausalLM.from_pretrained("PlanTL-GOB-ES/gpt2-base-bne")
>>> generator = pipeline('text-generation', tokenizer=tokenizer, model=model)
>>> set_seed(42)
>>> generator("La Biblioteca Nacional de España es una entidad pública y sus fines son", num_return_sequences=5)

[{'generated_text': 'La Biblioteca Nacional de España es una entidad pública y sus fines son difundir la cultura y el arte hispánico, así como potenciar las publicaciones de la Biblioteca y colecciones de la Biblioteca Nacional de España para su difusión e inquisición. '}, 
{'generated_text': 'La Biblioteca Nacional de España es una entidad pública y sus fines son diversos. '}, 
{'generated_text': 'La Biblioteca Nacional de España es una entidad pública y sus fines son la publicación, difusión y producción de obras de arte español, y su patrimonio intelectual es el que tiene la distinción de Patrimonio de la Humanidad. '}, 
{'generated_text': 'La Biblioteca Nacional de España es una entidad pública y sus fines son los de colaborar en el mantenimiento de los servicios bibliotecarios y mejorar la calidad de la información de titularidad institucional y en su difusión, acceso y salvaguarda para la sociedad. '}, 
{'generated_text': 'La Biblioteca Nacional de España es una entidad pública y sus fines son la conservación, enseñanza y difusión del patrimonio bibliográfico en su lengua específica y/o escrita. '}]
```

Here is how to use this model to get the features of a given text in PyTorch:

```python
>>> from transformers import AutoTokenizer, GPT2Model
>>> tokenizer = AutoTokenizer.from_pretrained("PlanTL-GOB-ES/gpt2-base-bne")
>>> model = GPT2Model.from_pretrained("PlanTL-GOB-ES/gpt2-base-bne")
>>> text = "La Biblioteca Nacional de España es una entidad pública y sus fines son"
>>> encoded_input = tokenizer(text, return_tensors='pt')
>>> output = model(**encoded_input)
>>> print(output.last_hidden_state.shape)
torch.Size([1, 14, 768])
```

## Limitations and bias

At the time of submission, no measures have been taken to estimate the bias and toxicity embedded in the model. However, we are well aware that our models may be biased since the corpora have been collected using crawling techniques on multiple web sources. We intend to conduct research in these areas in the future, and if completed, this model card will be updated. Nevertheless, here's an example of how the model can have biased predictions:

```python
>>> from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, set_seed
>>> tokenizer = AutoTokenizer.from_pretrained("PlanTL-GOB-ES/gpt2-base-bne")
>>> model = AutoModelForCausalLM.from_pretrained("PlanTL-GOB-ES/gpt2-base-bne")
>>> generator = pipeline('text-generation', tokenizer=tokenizer, model=model)
>>> set_seed(42)
>>> generator("El hombre se dedica a", num_return_sequences=5)
[{'generated_text': 'El hombre se dedica a comprar armas a sus amigos, pero les cuenta la historia de las ventajas de ser "buenos y regulares en la vida" e ir "bien" por los pueblos. '}, 
{'generated_text': 'El hombre se dedica a la venta de todo tipo de juguetes durante todo el año y los vende a través de Internet con la intención de alcanzar una mayor rentabilidad. '}, 
{'generated_text': 'El hombre se dedica a la venta ambulante en plena Plaza Mayor. '}, 
{'generated_text': 'El hombre se dedica a los toros y él se dedica a los servicios religiosos. '}, 
{'generated_text': 'El hombre se dedica a la caza y a la tala de pinos. '}]

>>> set_seed(42)
>>> generator("La mujer se dedica a", num_return_sequences=5)
[{'generated_text': 'La mujer se dedica a comprar vestidos de sus padres, como su madre, y siempre le enseña el último que ha hecho en poco menos de un año para ver si le da tiempo. '}, 
{'generated_text': 'La mujer se dedica a la venta ambulante y su pareja vende su cuerpo desde que tenía uso del automóvil. '}, 
{'generated_text': 'La mujer se dedica a la venta ambulante en plena ola de frío. '}, 
{'generated_text': 'La mujer se dedica a limpiar los suelos y paredes en pueblos con mucha humedad. '}, 
{'generated_text': 'La mujer se dedica a la prostitución en varios locales de alterne clandestinos en Barcelona. '}]

```

## Training

### Training Data

The [National Library of Spain (Biblioteca Nacional de España)](http://www.bne.es/en/Inicio/index.html) crawls all .es domains once a year. The training corpus consists of 59TB of WARC files from these crawls, carried out from 2009 to 2019.

To obtain a high-quality training corpus, the corpus has been preprocessed with a pipeline of operations, including among others, sentence splitting, language detection, filtering of bad-formed sentences, and deduplication of repetitive contents. During the process, document boundaries are kept. This resulted in 2TB of Spanish clean corpus. Further global deduplication among the corpus is applied, resulting in 570GB of text.

Some of the statistics of the corpus:

| Corpora | Number of documents | Number of tokens | Size (GB) |
|---------|---------------------|------------------|-----------|
| BNE     |         201,080,084 |  135,733,450,668 |     570GB |

### Training Procedure
The pretraining objective used for this architecture is next token prediction.
The configuration of the **GPT2-base-bne** model is as follows:
 - gpt2-base: 12-layer, 768-hidden, 12-heads, 117M parameters.
 
The training corpus has been tokenized using a byte version of Byte-Pair Encoding (BPE) used in the original [GPT-2](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) model with a vocabulary size of 50,262 tokens. 

The GPT2-base-bne pre-training consists of an autoregressive language model training that follows the approach of the GPT-2. 

The training lasted a total of 3 days with 16 computing nodes each one with 4 NVIDIA V100 GPUs of 16GB VRAM.

## Additional information

### Author
Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es)

### Contact information

For further information, send an email to <plantl-gob-es@bsc.es>

### Copyright

Copyright by the Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA) (2022)

### Licensing information

This work is licensed under a [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

### Funding

This work was funded by the Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA) within the framework of the Plan-TL.

### Citation information
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

<details>
<summary>Click to expand</summary>

The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and/or any other undesirable distortions.

When third parties, deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of Artificial Intelligence.

In no event shall the owner of the models (SEDIA – State Secretariat for Digitalization and Artificial Intelligence) nor the creator (BSC – Barcelona Supercomputing Center) be liable for any results arising from the use made by third parties of these models.


Los modelos publicados en este repositorio tienen una finalidad generalista y están a disposición de terceros. Estos modelos pueden tener sesgos y/u otro tipo de distorsiones indeseables.

Cuando terceros desplieguen o proporcionen sistemas y/o servicios a otras partes usando alguno de estos modelos (o utilizando sistemas basados en estos modelos) o se conviertan en usuarios de los modelos, deben tener en cuenta que es su responsabilidad mitigar los riesgos derivados de su uso y, en todo caso, cumplir con la normativa aplicable, incluyendo la normativa en materia de uso de inteligencia artificial.

En ningún caso el propietario de los modelos (SEDIA – Secretaría de Estado de Digitalización e Inteligencia Artificial) ni el creador (BSC – Barcelona Supercomputing Center) serán responsables de los resultados derivados del uso que hagan terceros de estos modelos.
</details>