---
language: fr
datasets:
- etalab-ia/piaf
- fquad
- lincoln/newsquadfr
- pragnakalp/squad_v2_french_translated
widget:
- text: Combien de personnes utilisent le français tous les jours ?
  context: >-
    Le français est une langue indo-européenne de la famille des langues romanes
    dont les locuteurs sont appelés francophones. Elle est parfois surnommée la
    langue de Molière.  Le français est parlé, en 2023, sur tous les continents
    par environ 321 millions de personnes : 235 millions l'emploient
    quotidiennement et 90 millions en sont des locuteurs natifs. En 2018, 80
    millions d'élèves et étudiants s'instruisent en français dans le monde.
    Selon l'Organisation internationale de la francophonie (OIF), il pourrait y
    avoir 700 millions de francophones sur Terre en 2050.
license: cc-by-4.0
metrics:
- f1
- exact_match
library_name: transformers
pipeline_tag: question-answering
---

# QAmembert

## Model Description

We present **QAmemBERT**, which is a [CamemBERT base](https://huggingface.co/camembert-base) fine-tuned for the Question-Answering task for the French language on five French Q&A datasets composed of contexts and questions with their answers inside the context (= SQuAD v1 format) but also contexts and questions with their answers not inside the context (= SQuAD v2 format).
This represents a total of over **138 061 questions/answers pairs used to finetune this model and 3,188 to test it**.


## Datasets

| Dataset     | Format      | Train split | Dev split   | Test split  |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| [PIAFv1.2](https://www.data.gouv.fr/en/datasets/piaf-le-dataset-francophone-de-questions-reponses/)| SQuAD v1    | 9 225 Q & A  | X  | X  |         
| [FQuADv1.0](https://fquad.illuin.tech/)| SQuAD v1    | 20 731 Q & A | 3 188 Q & A  (not used in training because it serves as a test dataset) | 2 189 Q & A (not used in our work because not freely available)|         
| [lincoln/newsquadfr](https://huggingface.co/datasets/lincoln/newsquadfr) | SQuAD v1    | 1 650 Q & A  | 455 Q & A (not used in our work) | 415 Q & A (not used in our work) |         
| [pragnakalp/squad_v2_french_translated](https://huggingface.co/datasets/pragnakalp/squad_v2_french_translated)| SQuAD v2    | 79 069 Q & A  | X  | X  |         
| [Mfa]()♪   | SQuAD v2    | 27 386 Q & A  | X  | X  |         

♪ this fifth data set will be added soon.

## Evaluation results
### FQuAD v1.0 Evaluation
```shell
{"f1": 80.75789384679857, "exact_match": 57.214554579673774}
```


### Benchmark 

| Model       | Exact_match | F1-score    |
| ----------- | ----------- | ----------- |
| [etalab-ia/camembert-base-squadFR-fquad-piaf](https://huggingface.co/etalab-ia/camembert-base-squadFR-fquad-piaf) | 55.14       | 79.81       |
| QAmembert   | **57.21**       | **80.76**       |


## Usage
### Example with answer in the context

```python
from transformers import pipeline

qa = pipeline('question-answering', model='CATIE-AQ/QAmembert', tokenizer='CATIE-AQ/QAmembert')

result = qa({
    'question': "Combien de personnes utilisent le français tous les jours ?",
    'context': "Le français est une langue indo-européenne de la famille des langues romanes dont les locuteurs sont appelés francophones. Elle est parfois surnommée la langue de Molière.  Le français est parlé, en 2023, sur tous les continents par environ 321 millions de personnes : 235 millions l'emploient quotidiennement et 90 millions en sont des locuteurs natifs. En 2018, 80 millions d'élèves et étudiants s'instruisent en français dans le monde. Selon l'Organisation internationale de la francophonie (OIF), il pourrait y avoir 700 millions de francophones sur Terre en 2050."
})

if result['score'] < 0.1:
    print("La réponse n'est pas dans le contexte fourni.")
else :
    print(result['answer'])
```
```python
235 millions
```
```python
# details
result
{
  "score": 0.9703257083892822,
  "start": 269,
  "end": 281,
  "answer": "235 millions"
}
```


### Example with answer not in the context
```python
from transformers import pipeline

qa = pipeline('question-answering', model='CATIE-AQ/QAmembert', tokenizer='CATIE-AQ/QAmembert')

result = qa({
    'question': "Quel est le meilleur vin du monde ?",
    'context': "La tour Eiffel est une tour de fer puddlé de 330 m de hauteur (avec antennes) située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. Son adresse officielle est 5, avenue Anatole-France.  
Construite en deux ans par Gustave Eiffel et ses collaborateurs pour l'Exposition universelle de Paris de 1889, célébrant le centenaire de la Révolution française, et initialement nommée « tour de 300 mètres », elle est devenue le symbole de la capitale française et un site touristique de premier plan : il s’agit du quatrième site culturel français payant le plus visité en 2016, avec 5,9 millions de visiteurs. Depuis son ouverture au public, elle a accueilli plus de 300 millions de visiteurs."
})

if result['score'] < 0.1:
    print("La réponse n'est pas dans le contexte fourni.")
else :
    print(result['answer'])
```
```python
La réponse n'est pas dans le contexte fourni.
```
```python
# details
result
{
  "score": 0.00011322159843984991,
  "start": 0,
  "end": 14,
  "answer": "La tour Eiffel"
}
```

## Citations

### PIAF
```
@inproceedings{KeraronLBAMSSS20,
  author    = {Rachel Keraron and
               Guillaume Lancrenon and
               Mathilde Bras and
               Fr{\'{e}}d{\'{e}}ric Allary and
               Gilles Moyse and
               Thomas Scialom and
               Edmundo{-}Pavel Soriano{-}Morales and
               Jacopo Staiano},
  title     = {Project {PIAF:} Building a Native French Question-Answering Dataset},
  booktitle = {{LREC}},
  pages     = {5481--5490},
  publisher = {European Language Resources Association},
  year      = {2020}
}

```

### FQuAD
```
@article{dHoffschmidt2020FQuADFQ,
  title={FQuAD: French Question Answering Dataset},
  author={Martin d'Hoffschmidt and Maxime Vidal and Wacim Belblidia and Tom Brendl'e and Quentin Heinrich},
  journal={ArXiv},
  year={2020},
  volume={abs/2002.06071}
}
```

### lincoln/newsquadfr
```
Hugging Face repository : https://huggingface.co/datasets/lincoln/newsquadfr
```

### pragnakalp/squad_v2_french_translated
```
Hugging Face repository : https://huggingface.co/datasets/pragnakalp/squad_v2_french_translated
```

### CamemBERT
```
@inproceedings{martin2020camembert,
  title={CamemBERT: a Tasty French Language Model},
  author={Martin, Louis and Muller, Benjamin and Su{\'a}rez, Pedro Javier Ortiz and Dupont, Yoann and Romary, Laurent and de la Clergerie, {\'E}ric Villemonte and Seddah, Djam{\'e} and Sagot, Beno{\^\i}t},
  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},
  year={2020}
}
```

## License
 [cc-by-4.0](https://creativecommons.org/licenses/by/4.0/deed.en)