---
language: "ca"
tags:
- masked-lm
- BERTa
- catalan
widget:
- text: "El Català és una llengua molt <mask>."
- text: "Salvador Dalí va viure a <mask>."
- text: "La Costa Brava té les millors <mask> d'Espanya."
- text: "El cacaolat és un batut de <mask>."
- text: "<mask> és la capital de la Garrotxa."
- text: "Vaig al <mask> a buscar bolets."
- text: "Antoni Gaudí vas ser un <mask> molt important per la ciutat."
- text: "Catalunya és una referència en <mask> a nivell europeu."
license: apache-2.0
---

# BERTa: RoBERTa-based Catalan language model

## Table of contents
<details>
<summary>Click to expand</summary>

- [Model description](#model-description)
- [Intended uses and limitations](#intended-use)
- [How to use](#how-to-use)
- [Limitations and bias](#limitations-and-bias)
- [Training](#training)
- [Evaluation](#evaluation)
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
BERTa is a transformer-based masked language model for the Catalan language. 
It is based on the [RoBERTA](https://github.com/pytorch/fairseq/tree/master/examples/roberta) base model 
and has been trained on a medium-size corpus collected from publicly available corpora and crawlers.

This model was originally published as [bsc/roberta-base-ca-cased](https://huggingface.co/bsc/roberta-base-ca-cased).

## Intended uses and limitations
The model is ready-to-use only for masked language modelling to perform the Fill Mask task (try the inference API or read the next section). 
However, it is intended to be fine-tuned on non-generative downstream tasks such as Question Answering, Text Classification or Named Entity Recognition.


## How to use

### Load model and tokenizer

``` python
from transformers import AutoTokenizer, AutoModelForMaskedLM
tokenizer = AutoTokenizer.from_pretrained("PlanTL-GOB-ES/roberta-base-ca-cased")
model = AutoModelForMaskedLM.from_pretrained("PlanTL-GOB-ES/roberta-base-ca-cased")
```

### Fill Mask task

Below, an example of how to use the masked language modelling task with a pipeline.

```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='PlanTL-GOB-ES/roberta-base-ca-cased')
>>> unmasker("Situada a la costa de la mar Mediterrània, <mask> s'assenta en una plana formada "
             "entre els deltes de les desembocadures dels rius Llobregat, al sud-oest, "
             "i Besòs, al nord-est, i limitada pel sud-est per la línia de costa,"
             "i pel nord-oest per la serralada de Collserola "
             "(amb el cim del Tibidabo, 516,2 m, com a punt més alt) que segueix paral·lela "
             "la línia de costa encaixant la ciutat en un perímetre molt definit.")

[
  {
    "sequence": " Situada a la costa de la mar Mediterrània, <mask> s'assenta en una plana formada "
                "entre els deltes de les desembocadures dels rius Llobregat, al sud-oest, "
                "i Besòs, al nord-est, i limitada pel sud-est per la línia de costa,"
                "i pel nord-oest per la serralada de Collserola "
                "(amb el cim del Tibidabo, 516,2 m, com a punt més alt) que segueix paral·lela "
                "la línia de costa encaixant la ciutat en un perímetre molt definit.",
    "score": 0.4177263379096985,
    "token": 734,
    "token_str": " Barcelona"
  },
  {
    "sequence": " Situada a la costa de la mar Mediterrània, <mask> s'assenta en una plana formada "
                "entre els deltes de les desembocadures dels rius Llobregat, al sud-oest, "
                "i Besòs, al nord-est, i limitada pel sud-est per la línia de costa,"
                "i pel nord-oest per la serralada de Collserola "
                "(amb el cim del Tibidabo, 516,2 m, com a punt més alt) que segueix paral·lela "
                "la línia de costa encaixant la ciutat en un perímetre molt definit.",
    "score": 0.10696165263652802,
    "token": 3849,
    "token_str": " Badalona"
  },
  {
    "sequence": " Situada a la costa de la mar Mediterrània, <mask> s'assenta en una plana formada "
                "entre els deltes de les desembocadures dels rius Llobregat, al sud-oest, "
                "i Besòs, al nord-est, i limitada pel sud-est per la línia de costa,"
                "i pel nord-oest per la serralada de Collserola "
                "(amb el cim del Tibidabo, 516,2 m, com a punt més alt) que segueix paral·lela "
                "la línia de costa encaixant la ciutat en un perímetre molt definit.",
    "score": 0.08135009557008743,
    "token": 19349,
    "token_str": " Collserola"
  },
  {
   "sequence": " Situada a la costa de la mar Mediterrània, <mask> s'assenta en una plana formada "
                "entre els deltes de les desembocadures dels rius Llobregat, al sud-oest, "
                "i Besòs, al nord-est, i limitada pel sud-est per la línia de costa,"
                "i pel nord-oest per la serralada de Collserola "
                "(amb el cim del Tibidabo, 516,2 m, com a punt més alt) que segueix paral·lela "
                "la línia de costa encaixant la ciutat en un perímetre molt definit.",
    "score": 0.07330769300460815,
    "token": 4974,
    "token_str": " Terrassa"
  },
  {
    "sequence": " Situada a la costa de la mar Mediterrània, <mask> s'assenta en una plana formada "
                "entre els deltes de les desembocadures dels rius Llobregat, al sud-oest, "
                "i Besòs, al nord-est, i limitada pel sud-est per la línia de costa,"
                "i pel nord-oest per la serralada de Collserola "
                "(amb el cim del Tibidabo, 516,2 m, com a punt més alt) que segueix paral·lela "
                "la línia de costa encaixant la ciutat en un perímetre molt definit.",
    "score": 0.03317456692457199,
    "token": 14333,
    "token_str": " Gavà"
  }
]
```


## Limitations and bias

## Training
### Training corpora and preprocessing

The training corpus consists of several corpora gathered from web crawling and public corpora.

The publicly available corpora are:

 1. the Catalan part of the [DOGC](http://opus.nlpl.eu/DOGC-v2.php) corpus, a set of documents from the Official Gazette of the Catalan Government
    
 2. the [Catalan Open Subtitles](http://opus.nlpl.eu/download.php?f=OpenSubtitles/v2018/mono/OpenSubtitles.raw.ca.gz), a collection of translated movie subtitles
    
 3. the non-shuffled version of the Catalan part of the [OSCAR](https://traces1.inria.fr/oscar/) corpus \\\\cite{suarez2019asynchronous}, 
    a collection of monolingual corpora, filtered from [Common Crawl](https://commoncrawl.org/about/)
    
 4. The [CaWac](http://nlp.ffzg.hr/resources/corpora/cawac/) corpus, a web corpus of Catalan built from the .cat top-level-domain in late 2013
    the non-deduplicated version

 5. the [Catalan Wikipedia articles](https://ftp.acc.umu.se/mirror/wikimedia.org/dumps/cawiki/20200801/) downloaded on 18-08-2020.

The crawled corpora are:

 6. The Catalan General Crawling, obtained by crawling the 500 most popular .cat and .ad domains
 7. the Catalan Government Crawling, obtained by crawling the .gencat domain and subdomains, belonging to the Catalan Government
    
 8. the ACN corpus with 220k news items from March 2015 until October 2020, crawled from the [Catalan News Agency](https://www.acn.cat/)

To obtain a high-quality training corpus, each corpus have preprocessed with a pipeline of operations, including among the others,
sentence splitting, language detection, filtering of bad-formed sentences and deduplication of repetitive contents.
During the process, we keep document boundaries are kept. 
Finally, the corpora are concatenated and further global deduplication among the corpora is applied.
The final training corpus consists of about 1,8B tokens.


### Tokenization and pretraining 

The training corpus has been tokenized using a byte version of [Byte-Pair Encoding (BPE)](https://github.com/openai/gpt-2)
used in the original [RoBERTA](https://github.com/pytorch/fairseq/tree/master/examples/roberta) model with a vocabulary size of 52,000 tokens. 

The BERTa pretraining consists of a masked language model training that follows the approach employed for the RoBERTa base model
with the same hyperparameters as in the original work.

The training lasted a total of 48 hours with 16 NVIDIA V100 GPUs of 16GB DDRAM.

## Evaluation

### CLUB benchmark

The BERTa model has been fine-tuned on the downstream tasks of the Catalan Language Understanding Evaluation benchmark (CLUB),
that has been created along with the model.

It contains the following tasks and their related datasets:

 1. Part-of-Speech Tagging (POS)
    
    Catalan-Ancora: from the [Universal Dependencies treebank](https://github.com/UniversalDependencies/UD_Catalan-AnCora) of the well-known Ancora corpus

 2. Named Entity Recognition (NER)
    
    **[AnCora Catalan 2.0.0](https://zenodo.org/record/4762031#.YKaFjqGxWUk)**: extracted named entities from the original [Ancora](https://doi.org/10.5281/zenodo.4762030) version,
    filtering out some unconventional ones, like book titles, and transcribed them into a standard CONLL-IOB format

 3. Text Classification (TC)
     
    **[TeCla](https://doi.org/10.5281/zenodo.4627197)**: consisting of 137k news pieces from the Catalan News Agency ([ACN](https://www.acn.cat/)) corpus

 4. Semantic Textual Similarity (STS)
    
    **[Catalan semantic textual similarity](https://doi.org/10.5281/zenodo.4529183)**: consisting of more than 3000 sentence pairs, annotated with the semantic similarity between them, 
    scraped from the [Catalan Textual Corpus](https://doi.org/10.5281/zenodo.4519349)

 5. Question Answering (QA):
    
    **[ViquiQuAD](https://doi.org/10.5281/zenodo.4562344)**: consisting of more than 15,000 questions outsourced from Catalan Wikipedia randomly chosen from a set of 596 articles that were originally written in Catalan.
    
    **[XQuAD](https://doi.org/10.5281/zenodo.4526223)**: the Catalan translation of XQuAD, a multilingual collection of manual translations of 1,190 question-answer pairs from English Wikipedia used only as a _test set_
    
Here are the train/dev/test splits of the datasets:

| Task (Dataset) | Total | Train | Dev  | Test |
|:--|:--|:--|:--|:--|
| NER (Ancora)  |13,581 | 10,628 | 1,427 | 1,526 |
| POS (Ancora)| 16,678 | 13,123 | 1,709 | 1,846 |
| STS         | 3,073 | 2,073 | 500 | 500 |
| TC (TeCla) |  137,775 | 110,203 | 13,786 |  13,786|
| QA (ViquiQuAD) | 14,239  | 11,255  | 1,492  | 1,429 | 
 

_The fine-tuning on downstream tasks have been performed with the HuggingFace [**Transformers**](https://github.com/huggingface/transformers) library_

### Results

Below the evaluation results on the CLUB tasks compared with the multilingual mBERT, XLM-RoBERTa models and 
the Catalan WikiBERT-ca model


| Task        | NER (F1)      | POS (F1)   | STS (Pearson)   | TC (accuracy) | QA (ViquiQuAD) (F1/EM)  | QA (XQuAD) (F1/EM) | 
| ------------|:-------------:| -----:|:------|:-------|:------|:----|
| BERTa       | **88.13** | **98.97** | **79.73** | **74.16** | **86.97/72.29** | **68.89/48.87** |
| mBERT       | 86.38 | 98.82 | 76.34 | 70.56 | 86.97/72.22 | 67.15/46.51 |
| XLM-RoBERTa | 87.66 | 98.89 | 75.40 | 71.68 | 85.50/70.47 | 67.10/46.42 |
| WikiBERT-ca | 77.66 | 97.60 | 77.18 | 73.22 | 85.45/70.75 | 65.21/36.60 |


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

If you use this model, please cite our latest paper:

```bibtex
@inproceedings{armengol-estape-etal-2021-multilingual,
    title = "Are Multilingual Models the Best Choice for Moderately Under-resourced Languages? {A} Comprehensive Assessment for {C}atalan",
    author = "Armengol-Estap{\'e}, Jordi  and
      Carrino, Casimiro Pio  and
      Rodriguez-Penagos, Carlos  and
      de Gibert Bonet, Ona  and
      Armentano-Oller, Carme  and
      Gonzalez-Agirre, Aitor  and
      Melero, Maite  and
      Villegas, Marta",
    booktitle = "Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-acl.437",
    doi = "10.18653/v1/2021.findings-acl.437",
    pages = "4933--4946",
}
```

### Disclaimer
The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and/or any other undesirable distortions.

When third  parties, deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of artificial intelligence.

In no event shall the owner of the models (SEDIA – State Secretariat for digitalization and artificial intelligence) nor the creator (BSC – Barcelona Supercomputing Center) be liable for any results arising from the use made by third parties of these models.


Los modelos publicados en este repositorio tienen una finalidad generalista y están a disposición de terceros. Estos modelos pueden tener sesgos y/u otro tipo de distorsiones indeseables.

Cuando terceros desplieguen o proporcionen sistemas y/o servicios a otras partes usando alguno de estos modelos (o utilizando sistemas basados en estos modelos) o se conviertan en usuarios de los modelos, deben tener en cuenta que es su responsabilidad mitigar los riesgos derivados de su uso y, en todo caso, cumplir con la normativa aplicable, incluyendo la normativa en materia de uso de inteligencia artificial.

En ningún caso el propietario de los modelos (SEDIA – Secretaría de Estado de Digitalización e Inteligencia Artificial) ni el creador (BSC – Barcelona Supercomputing Center) serán responsables de los resultados derivados del uso que hagan terceros de estos modelos.