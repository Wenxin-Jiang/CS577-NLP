---
language: ca

tags:
- summarization

widget:
- text: "La Universitat Politècnica de València (UPV), a través del projecte Atenea “plataforma de dones, art i tecnologia” i en col·laboració amb les companyies tecnològiques Metric Salad i Zetalab, ha digitalitzat i modelat en 3D per a la 35a edició del Festival Dansa València, que se celebra del 2 al 10 d'abril, la primera peça de dansa en un metaverso específic. La peça No és amor, dirigida per Lara Misó, forma part de la programació d'aquesta edició del Festival Dansa València i explora la figura geomètrica del cercle des de totes les seues perspectives: espacial, corporal i compositiva. No és amor està inspirada en el treball de l'artista japonesa Yayoi Kusama i mira de prop les diferents facetes d'una obsessió. Així dona cabuda a la insistència, la repetició, el trastorn, la hipnosi i l'alliberament. El procés de digitalització, materialitzat per Metric Salad i ZetaLab, ha sigut complex respecte a uns altres ja realitzats a causa de l'enorme desafiament que comporta el modelatge en 3D de cossos en moviment al ritme de la composició de l'obra. L'objectiu era generar una experiència el més realista possible i fidedigna de l'original perquè el resultat final fora un procés absolutament immersiu.Així, el metaverso està compost per figures modelades en 3D al costat de quatre projeccions digitalitzades en pantalles flotants amb les quals l'usuari podrà interactuar segons es vaja acostant, bé mitjançant els comandaments de l'ordinador, bé a través d'ulleres de realitat virtual. L'objectiu és que quan l'usuari s'acoste a cadascuna de les projeccions tinga la sensació d'una immersió quasi completa en fondre's amb el contingut audiovisual que li genere una experiència intimista i molt real."
---
# mT5 (base model), fine-tuned on the *Dataset for Automatic summarization of Catalan and Spanish newspaper Articles (DACSA)* dataset for Catalan

The mT5 model was presented in [mT5: A massively multilingual pre-trained text-to-text transformer](https://arxiv.org/abs/2010.11934) by Linting Xue, Noah Constant, Adam Roberts, Mihir Kale, Rami Al-Rfou, Aditya Siddhant, Aditya Barua, Colin Raffel. The base version of the mT5 model is pre-trained in 101 languages, including English, Spanish, Italian, Catalan and other ones.

# Model description

The mT5-base model has been fine-tuned for abstractive text summarization for Catalan.

# Training data

The mT5-base model has been fine-tuned on *the Dataset for Automatic summarization of Catalan and Spanish newspaper Articles (DACSA)* dataset, specifically with the Catalan articles. The Catalan subset contains 636.596 document-summary pairs of Catalan news articles.

The DACSA dataset can be requested at the following address: https://xarrador.dsic.upv.es/resources/dacsa

# Intended uses & limitations

The model can be used for text summarization, especially in news articles.

# How to use
You can use the summarization model with the [pipeline API](https://huggingface.co/transformers/main_classes/pipelines.html):

```python
from transformers import pipeline

summarizer = pipeline("summarization", model="ELiRF/mt5-base-dacsa-ca")

ARTICLE = """La Universitat Politècnica de València (UPV), a través del
projecte Atenea “plataforma de dones, art i tecnologia” i en col·laboració amb
les companyies tecnològiques Metric Salad i Zetalab, ha digitalitzat i modelat
en 3D per a la 35a edició del Festival Dansa València, que se celebra del 2 al
10 d'abril, la primera peça de dansa en un metaverso específic. La peça No és
amor, dirigida per Lara Misó, forma part de la programació d'aquesta edició del
Festival Dansa València i explora la figura geomètrica del cercle des de totes
les seues perspectives: espacial, corporal i compositiva. No és amor està
inspirada en el treball de l'artista japonesa Yayoi Kusama i mira de prop les
diferents facetes d'una obsessió. Així dona cabuda a la insistència, la
repetició, el trastorn, la hipnosi i l'alliberament. El procés de
digitalització, materialitzat per Metric Salad i ZetaLab, ha sigut complex
respecte a uns altres ja realitzats a causa de l'enorme desafiament que
comporta el modelatge en 3D de cossos en moviment al ritme de la composició de
l'obra. L'objectiu era generar una experiència el més realista possible i
fidedigna de l'original perquè el resultat final fora un procés absolutament
immersiu.Així, el metaverso està compost per figures modelades en 3D al costat
de quatre projeccions digitalitzades en pantalles flotants amb les quals
l'usuari podrà interactuar segons es vaja acostant, bé mitjançant els
comandaments de l'ordinador, bé a través d'ulleres de realitat virtual.
L'objectiu és que quan l'usuari s'acoste a cadascuna de les projeccions tinga
la sensació d'una immersió quasi completa en fondre's amb el contingut
audiovisual que li genere una experiència intimista i molt real.
"""
print(summarizer(ARTICLE, truncation=True))
>>>[{'summary_text': "La Universitat Politècnica de València ha digitalitzat i modelat en 3D la primera peça de dansa en un metaverso específic."}]
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