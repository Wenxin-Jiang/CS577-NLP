---
language: es

tags:
- summarization

widget:
- text: "La Agencia Valenciana de la Innovación (AVI) financia el desarrollo de un software que integra diferentes modelos y tecnologías para la monitorización y análisis multilingüe de las redes sociales. A través de técnicas de 'deep learning' y procesamiento del lenguaje natural es capaz de interpretar la ironía y las emociones en los textos, incluso en aquellos escritos en idiomas menos extendidos, a menudo no contemplados por las herramientas comerciales. La iniciativa, bautizada como 'Guaita', está liderada por el Instituto Valenciano de Investigación en Inteligencia Artificial (VRAIN), adscrito a la Universidad Politécnica de Valencia (UPV), que cuenta a su vez para su desarrollo con la colaboración del Instituto Valenciano de Informática (ITI) y la Corporación Valenciana de Mitjans de Comunicación (CVMC).De este modo, y a solicitud del usuario o usuaria, monitorizará las redes sociales para obtener la información asociada a los temas objeto de interés y ofrecerá los resultados de forma gráfica, bien a través de una interfaz web, bien mediante la generación de informes. El programa será, además, capaz de determinar la reputación de una empresa o institución a partir de dichos análisis gracias a la combinación de distintas tecnologías de procesamiento e interpretación, destaca la agencia en un comunicado."
---
**IMPORTANT:** On the 5th of April 2022, we detected a mistake in the configuration file; thus, the model was not generating the summaries correctly, and it was underperforming in all scenarios. For this reason, if you had used the model until that day, we would be glad if you would re-evaluate the model if you are publishing some results with it. We apologize for the inconvenience and thank you for your understanding.

# NASca and NASes: Two Monolingual Pre-Trained Models for Abstractive Summarization in Catalan and Spanish

Most of the models proposed in the literature for abstractive summarization are generally suitable for the English language but not for other languages. Multilingual models were introduced to address that language constraint, but despite their applicability being broader than that of the monolingual models, their performance is typically lower, especially for minority languages like Catalan. In this paper, we present a monolingual model for abstractive summarization of textual content in the Catalan language. The model is a Transformer encoder-decoder which is pretrained and fine-tuned specifically for the Catalan language using a corpus of newspaper articles. In the pretraining phase, we introduced several self-supervised tasks to specialize the model on the summarization task and to increase the abstractivity of the generated summaries. To study the performance of our proposal in languages with higher resources than Catalan, we replicate the model and the experimentation for the Spanish language. The usual evaluation metrics, not only the most used ROUGE measure but also other more semantic ones such as BertScore, do not allow to correctly evaluate the abstractivity of the generated summaries. In this work, we also present a new metric, called content reordering, to evaluate one of the most common characteristics of abstractive summaries, the rearrangement of the original content. We carried out an exhaustive experimentation to compare the performance of the monolingual models proposed in this work with two of the most widely used multilingual models in text summarization, mBART and mT5. The experimentation results support the quality of our monolingual models, especially considering that the multilingual models were pretrained with many more resources than those used in our models. Likewise, it is shown that the pretraining tasks helped to increase the degree of abstractivity of the generated summaries. To our knowledge, this is the first work that explores a monolingual approach for abstractive summarization both in Catalan and Spanish. 

# The NASes model

News Abstractive Summarization for Spanish (NASes) is a Transformer encoder-decoder model, with the same hyper-parameters than BART, to perform summarization of Spanish news articles. It is pre-trained on a combination of several self-supervised tasks that help to increase the abstractivity of the generated summaries. Four pre-training tasks have been combined: sentence permutation, text infilling, Gap Sentence Generation, and Next Segment Generation. Spanish newspapers, and Wikipedia articles in Spanish were used for pre-training the model (21GB of raw text -8.5 millions of documents-).

NASes is finetuned for the summarization task on 1.802.919 (document, summary) pairs from the Dataset for Automatic summarization of Catalan and Spanish newspaper Articles (DACSA).

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