---
language: es
tags:
- generated_from_trainer
- fake
- news
- competition

datasets:
- fakedes

widget:
- text: 'La palabra "haiga", aceptada por la RAE [SEP] La palabra "haiga", aceptada por la RAE La Real Academia de la Lengua (RAE), ha aceptado el uso de "HAIGA", para su utilización en las tres personas del singular del presente del subjuntivo del verbo hacer, aunque asegura que la forma más recomendable en la lengua culta para este tiempo, sigue siendo "haya".
Así lo han confirmado fuentes de la RAE, que explican que este cambio ha sido propuesto y aprobado por el pleno de la Academia de la Lengua, tras la extendida utilización por todo el territorio nacional, sobre todo, empleado por personas carentes de estudios o con estudios básicos de graduado escolar. Ya no será objeto de burla ese compañero que a diario repite aquello de "Mientras que haiga faena, no podemos quejarnos" o esa abuela que repite aquello de "El que haiga sacao los juguetes, que los recoja".
Entre otras palabras novedosas que ha aceptado la RAE, contamos también con "Descambiar", significa deshacer un cambio, por ejemplo "devolver la compra". Visto lo visto, nadie apostaría que la palabra "follamigos" sea la siguiente de la lista.'

metrics:
- f1
- accuracy
model-index:
- name: roberta-large-fake-news-detection-spanish
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# RoBERTa-large-fake-news-detection-spanish

This model is a fine-tuned version of [PlanTL-GOB-ES/roberta-large-bne](https://huggingface.co/PlanTL-GOB-ES/roberta-large-bne) on an [Spanish Fake News Dataset](https://sites.google.com/view/iberlef2020/#h.p_w0c31bn0r-SW).

It achieves the following results on the evaluation set:
- Loss: 1.7474
- F1: **0.7717**
- Accuracy: 0.7797

> So, based on the [leaderboard](https://sites.google.com/view/fakedes/results?authuser=0) our model **outperforms** the best model (scores F1 = 0.7666).

## Model description

RoBERTa-large-bne is a transformer-based masked language model for the Spanish language. It is based on the RoBERTa large model and has been pre-trained using the largest Spanish corpus known to date, with a total of 570GB of clean and deduplicated text processed for this work, compiled from the web crawlings performed by the National Library of Spain (Biblioteca Nacional de España) from 2009 to 2019.

## Intended uses & limitations

The objective of this task is to decide if a news item is fake or real by analyzing its textual representation.

## Training and evaluation data
**FakeDeS**: [Fake News Detection in Spanish Shared Task](https://sites.google.com/view/fakedes/home)

Fake news provides information that aims to manipulate people for different purposes: terrorism, political elections, advertisement, satire, among others. In social networks, misinformation extends in seconds among thousands of people, so it is necessary to develop tools that help control the amount of false information on the web. Similar tasks are detection of popularity in social networks and detection of subjectivity of messages in this media. A fake news detection system aims to help users detect and filter out potentially deceptive news. The prediction of intentionally misleading news is based on the analysis of truthful and fraudulent previously reviewed news, i.e., annotated corpora. 

The Spanish Fake News Corpus is a collection of news compiled from several web sources: established newspapers websites,media companies websites, special websites dedicated to validating fake news, websites designated by different journalists as sites that regularly publish fake news. The news were collected from January to July of 2018 and all of them were written in Mexican Spanish.

The corpus has 971 news collected from January to July, 2018, from different sources:

- Established newspapers websites,
- Media companies websites,
- Special websites dedicated to validating fake news,
- Websites designated by different journalists as sites that regularly publish fake news.

The corpus was tagged considering only two classes (true or fake), following a manual labeling process:

- A news is true if there is evidence that it has been published in reliable sites.
- A news is fake if there is news from reliable sites or specialized website in detection of deceptive content that contradicts it or no other evidence was found about the news besides the source.
- We collected the true-fake news pair of an event so there is a correlation of news in the corpus.
In order to avoid topic bias, the corpus covers news from 9 different topics: Science, Sport, Economy, Education, Entertainment, Politics, Health, Security, and Society. As it can be seen in the table below, the number of fake and true news is quite balanced. Approximately 70% will be used as training corpus (676 news), and the 30% as testing corpus (295 news).

The training corpus contains the following information:

- Category: Fake/ True

- Topic: Science/ Sport/ Economy/ Education/ Entertainment/ Politics, Health/ Security/ Society

- Headline: The title of the news.

- Text: The complete text of the news.

- Link: The URL where the news was published.

More information needed

## Training procedure

TBA

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:------:|:--------:|
| No log        | 1.0   | 243  | 0.6282          | 0.7513 | 0.75     |
| No log        | 2.0   | 486  | 0.9600          | 0.7346 | 0.7587   |
| 0.5099        | 3.0   | 729  | 1.2128          | 0.7656 | 0.7570   |
| 0.5099        | 4.0   | 972  | 1.4001          | 0.7606 | 0.7622   |
| 0.1949        | 5.0   | 1215 | 1.9748          | 0.6475 | 0.7220   |
| 0.1949        | 6.0   | 1458 | 1.7386          | 0.7706 | 0.7710   |
| 0.0263        | 7.0   | 1701 | 1.7474          | 0.7717 | 0.7797   |
| 0.0263        | 8.0   | 1944 | 1.8114          | 0.7695 | 0.7780   |
| 0.0046        | 9.0   | 2187 | 1.8444          | 0.7709 | 0.7797   |
| 0.0046        | 10.0  | 2430 | 1.8552          | 0.7709 | 0.7797   |


### Fast usage with HF `pipelines`

```python
from transformers import pipeline
ckpt = "Narrativaai/fake-news-detection-spanish"

classifier = pipeline("text-classification", model=ckpt)

headline = "Your headline"
text = "Your article text here..."
    
classifier(headline + " [SEP] " + text)
```

### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.0+cu111
- Datasets 1.14.0
- Tokenizers 0.10.3

Created by: [Narrativa](https://www.narrativa.com/)

About Narrativa: Natural Language Generation (NLG) | Gabriele, our machine learning-based platform, builds and deploys natural language solutions. #NLG #AI