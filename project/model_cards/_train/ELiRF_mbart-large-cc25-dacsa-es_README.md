---
language: es

tags:
- summarization

widget:
- text: "La Universitat Politècnica de València (UPV), a través del proyecto Atenea “plataforma de mujeres, arte y tecnología” y en colaboración con las compañías tecnológicas Metric Salad y Zetalab, ha digitalizado y modelado en 3D para la 35ª edición del Festival Dansa València, que se celebra del 2 al 10 de abril, la primera pieza de danza en un metaverso específico.La pieza No es amor, dirigida por Lara Misó, forma parte de la programación de esta edición del Festival Dansa València y explora la figura geométrica del círculo desde todas sus perspectivas: espacial, corporal y compositiva. No es amor está inspirada en el trabajo de la artista japonesa Yayoi Kusama y mira de cerca las diferentes facetas de una obsesión. Así da cabida a la insistencia, la repetición, el trastorno, la hipnosis y la liberación. El proceso de digitalización, materializado por Metric Salad y ZetaLab, ha sido complejo respecto a otros ya realizados debido al enorme desafío que conlleva el modelado en 3D de cuerpos en movimiento al ritmo de la composición de la obra. El objetivo era generar una experiencia lo más realista posible y fidedigna de la original para que el resultado final fuera un proceso absolutamente inmersivo. Así, el metaverso está compuesto por figuras modeladas en 3D junto a cuatro proyecciones digitalizadas en pantallas flotantes con las que el usuario podrá interactuar según se vaya acercando, bien mediante los comandos del ordenador, bien a través de gafas de realidad virtual. El objetivo es que cuando el usuario se acerque a cada una de las proyecciones tenga la sensación de una inmersión casi completa al fundirse con el contenido audiovisual que le genere una experiencia intimista y muy real."
---
# mBART (large-cc25 model), fine-tuned on the *Dataset for Automatic summarization of Catalan and Spanish newspaper Articles (DACSA)* dataset for Spanish

The mBART model was presented in [Multilingual Denoising Pre-training for Neural Machine Translation](https://arxiv.org/abs/2001.08210) by Yinhan Liu, Jiatao Gu, Naman Goyal, Xian Li, Sergey Edunov Marjan Ghazvininejad, Mike Lewis, Luke Zettlemoyer. The large-cc25 version of the mBART model is pre-trained in 25 languages, including English, Spanish, Italian, and other ones.

# Model description

The mBART-large-cc25 model has been fine-tuned for abstractive text summarization for Spanish.

# Training data

The mBART-larges-cc25 model has been fine-tuned on *the Dataset for Automatic summarization of Catalan and Spanish newspaper Articles (DACSA)* dataset, specifically with the Spanish articles. The Spanish subset contains 1.802.919 document-summary pairs of Spanish news articles.

The DACSA dataset can be requested at the following address: https://xarrador.dsic.upv.es/resources/dacsa

# Intended uses & limitations

The model can be used for text summarization, especially in news articles.

# How to use

You can use the summarization model with the [pipeline API](https://huggingface.co/transformers/main_classes/pipelines.html):

```python
from transformers import pipeline

summarizer = pipeline("summarization", model="ELiRF/mbart-large-cc25-dacsa-es")

ARTICLE = """La Universitat Politècnica de València (UPV), a través del
proyecto Atenea “plataforma de mujeres, arte y tecnología” y en colaboración
con las compañías tecnológicas Metric Salad y Zetalab, ha digitalizado y
modelado en 3D para la 35ª edición del Festival Dansa València, que se celebra
del 2 al 10 de abril, la primera pieza de danza en un metaverso específico.La
pieza No es amor, dirigida por Lara Misó, forma parte de la programación de
esta edición del Festival Dansa València y explora la figura geométrica del
círculo desde todas sus perspectivas: espacial, corporal y compositiva. No es
amor está inspirada en el trabajo de la artista japonesa Yayoi Kusama y mira de
cerca las diferentes facetas de una obsesión. Así da cabida a la insistencia,
la repetición, el trastorno, la hipnosis y la liberación. El proceso de
digitalización, materializado por Metric Salad y ZetaLab, ha sido complejo
respecto a otros ya realizados debido al enorme desafío que conlleva el
modelado en 3D de cuerpos en movimiento al ritmo de la composición de la obra.
El objetivo era generar una experiencia lo más realista posible y fidedigna de
la original para que el resultado final fuera un proceso absolutamente
inmersivo. Así, el metaverso está compuesto por figuras modeladas en 3D junto a
cuatro proyecciones digitalizadas en pantallas flotantes con las que el usuario
podrá interactuar según se vaya acercando, bien mediante los comandos del
ordenador, bien a través de gafas de realidad virtual. El objetivo es que
cuando el usuario se acerque a cada una de las proyecciones tenga la sensación
de una inmersión casi completa al fundirse con el contenido audiovisual que le
genere una experiencia intimista y muy real.
"""

print(summarizer(ARTICLE, truncation=True))
>>>[{'summary_text': "La pieza No es amor, dirigida por Lara Misó, forma parte de la programación de esta edición del Festival Dansa València."}]
```

### BibTeX entry
```bibtex
@inproceedings{segarra-soriano-etal-2022-dacsa,
    title = "{DACSA}: A large-scale Dataset for Automatic summarization of {C}atalan and {S}panish newspaper Articles",
    author = "Segarra Soriano, Encarnaci{\'o}n  and
      Ahuir, Vicent  and
      Hurtado, Llu{\'\i}s-F.  and
      Gonz{\'a}lez, Jos{\'e}",
    booktitle = "Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jul,
    year = "2022",
    address = "Seattle, United States",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.naacl-main.434",
    pages = "5931--5943",
    abstract = "The application of supervised methods to automatic summarization requires the availability of adequate corpora consisting of a set of document-summary pairs. As in most Natural Language Processing tasks, the great majority of available datasets for summarization are in English, making it difficult to develop automatic summarization models for other languages. Although Spanish is gradually forming part of some recent summarization corpora, it is not the same for minority languages such as Catalan.In this work, we describe the construction of a corpus of Catalan and Spanish newspapers, the Dataset for Automatic summarization of Catalan and Spanish newspaper Articles (DACSA) corpus. It is a high-quality large-scale corpus that can be used to train summarization models for Catalan and Spanish.We have carried out an analysis of the corpus, both in terms of the style of the summaries and the difficulty of the summarization task. In particular, we have used a set of well-known metrics in the summarization field in order to characterize the corpus. Additionally, for benchmarking purposes, we have evaluated the performances of some extractive and abstractive summarization systems on the DACSA corpus.",
}

```