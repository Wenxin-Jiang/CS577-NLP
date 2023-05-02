---
language: ca

tags:
- summarization

widget:
- text: "La Universitat Politècnica de València (UPV), a través del projecte Atenea “plataforma de dones, art i tecnologia” i en col·laboració amb les companyies tecnològiques Metric Salad i Zetalab, ha digitalitzat i modelat en 3D per a la 35a edició del Festival Dansa València, que se celebra del 2 al 10 d'abril, la primera peça de dansa en un metaverso específic. La peça No és amor, dirigida per Lara Misó, forma part de la programació d'aquesta edició del Festival Dansa València i explora la figura geomètrica del cercle des de totes les seues perspectives: espacial, corporal i compositiva. No és amor està inspirada en el treball de l'artista japonesa Yayoi Kusama i mira de prop les diferents facetes d'una obsessió. Així dona cabuda a la insistència, la repetició, el trastorn, la hipnosi i l'alliberament. El procés de digitalització, materialitzat per Metric Salad i ZetaLab, ha sigut complex respecte a uns altres ja realitzats a causa de l'enorme desafiament que comporta el modelatge en 3D de cossos en moviment al ritme de la composició de l'obra. L'objectiu era generar una experiència el més realista possible i fidedigna de l'original perquè el resultat final fora un procés absolutament immersiu.Així, el metaverso està compost per figures modelades en 3D al costat de quatre projeccions digitalitzades en pantalles flotants amb les quals l'usuari podrà interactuar segons es vaja acostant, bé mitjançant els comandaments de l'ordinador, bé a través d'ulleres de realitat virtual. L'objectiu és que quan l'usuari s'acoste a cadascuna de les projeccions tinga la sensació d'una immersió quasi completa en fondre's amb el contingut audiovisual que li genere una experiència intimista i molt real."
---

**IMPORTANT:** On the 5th of April 2022, we detected a mistake in the configuration file; thus, the model was not generating the summaries correctly, and it was underperforming in all scenarios. For this reason, if you had used the model until that day, we would be glad if you would re-evaluate the model if you are publishing some results with it. We apologize for the inconvenience and thank you for your understanding.

# NASca and NASes: Two Monolingual Pre-Trained Models for Abstractive Summarization in Catalan and Spanish

Most of the models proposed in the literature for abstractive summarization are generally suitable for the English language but not for other languages. Multilingual models were introduced to address that language constraint, but despite their applicability being broader than that of the monolingual models, their performance is typically lower, especially for minority languages like Catalan. In this paper, we present a monolingual model for abstractive summarization of textual content in the Catalan language. The model is a Transformer encoder-decoder which is pretrained and fine-tuned specifically for the Catalan language using a corpus of newspaper articles. In the pretraining phase, we introduced several self-supervised tasks to specialize the model on the summarization task and to increase the abstractivity of the generated summaries. To study the performance of our proposal in languages with higher resources than Catalan, we replicate the model and the experimentation for the Spanish language. The usual evaluation metrics, not only the most used ROUGE measure but also other more semantic ones such as BertScore, do not allow to correctly evaluate the abstractivity of the generated summaries. In this work, we also present a new metric, called content reordering, to evaluate one of the most common characteristics of abstractive summaries, the rearrangement of the original content. We carried out an exhaustive experimentation to compare the performance of the monolingual models proposed in this work with two of the most widely used multilingual models in text summarization, mBART and mT5. The experimentation results support the quality of our monolingual models, especially considering that the multilingual models were pretrained with many more resources than those used in our models. Likewise, it is shown that the pretraining tasks helped to increase the degree of abstractivity of the generated summaries. To our knowledge, this is the first work that explores a monolingual approach for abstractive summarization both in Catalan and Spanish. 

# The NASca model
News Abstractive Summarization for Catalan (NASca) is a Transformer encoder-decoder model, with the same hyper-parameters than BART, to perform summarization of Catalan news articles. It is pre-trained on a combination of several self-supervised tasks that help to increase the abstractivity of the generated summaries. Four pre-training tasks have been combined: sentence permutation, text infilling, Gap Sentence Generation, and Next Segment Generation. Catalan newspapers, the Catalan subset of the OSCAR corpus and Wikipedia articles in Catalan were used for pre-training the model (9.3GB of raw text -2.5 millions of documents-).

NASca is finetuned for the summarization task on 636.596 (document, summary) pairs from the Dataset for Automatic summarization of Catalan and Spanish newspaper Articles (DACSA).

### BibTeX entry
```bibtex
@Article{app11219872,
AUTHOR = {Ahuir, Vicent and Hurtado, Lluís-F. and González, José Ángel and Segarra, Encarna},
TITLE = {NASca and NASes: Two Monolingual Pre-Trained Models for Abstractive Summarization in Catalan and Spanish},
JOURNAL = {Applied Sciences},
VOLUME = {11},
YEAR = {2021},
NUMBER = {21},
ARTICLE-NUMBER = {9872},
URL = {https://www.mdpi.com/2076-3417/11/21/9872},
ISSN = {2076-3417},
DOI = {10.3390/app11219872}
}
```