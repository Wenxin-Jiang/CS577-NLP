---

language: 
  - hu
tags:
- token-classification
license: gpl
metrics:
- F1
widget:
- text: "A jótékonysági szervezet által idézett Forbes-adatok szerint a világ tíz leggazdagabb embere: Elon Musk (Tesla, SpaceX), Jeff Bezos (Amazon, Blue Origin), Bernard Arnault és családja (LVMH, azaz Louis Vuitton és Moët Hennessy), Bill Gates (Microsoft), Larry Ellison (Oracle), Larry Page (Google), Sergey Brin (Google), Mark Zuckerberg (Facebook), Steve Ballmer (Microsoft) és Warren Buffett (befektető).
Miközben vagyonuk együttesen 700 milliárdról másfél ezer milliárd dollárra nőtt 2020 márciusa és 2021 novembere között, jelentős eltérések vannak közöttük: Musk vagyona több mint 1000 százalékos, míg Gatesé szerényebb, 30 százalékos növekedést mutatott."
inference:
  parameters:
    aggregation_strategy: "first"

---

# Hungarian named entity recognition model with OntoNotes5 + more entity types

  - Pretrained model used: SZTAKI-HLT/hubert-base-cc 
  - Finetuned on NerKor+CARS-ONPP Corpus
  	
## Limitations

- max_seq_length = 448

## Training data

The underlying corpus, [NerKor+CARS-OntoNotes++](https://github.com/ppke-nlpg/NYTK-NerKor-Cars-OntoNotesPP), was derived from [NYTK-NerKor](https://github.com/nytud/NYTK-NerKor), a Hungarian gold standard named entity annotated corpus containing about 1 million tokens. 
It includes a small addition of 12k tokens of text (individual sentences) concerning motor vehicles (cars, buses, motorcycles) from the news archive of [hvg.hu](hvg.hu).
While the annotation in NYTK-NerKor followed the CoNLL2002 labelling standard with just four NE categories (`PER`, `LOC`, `MISC`, `ORG`), this version of the corpus features over 30 entity types, including all entity types used in the [OntoNotes 5.0] English NER annotation.
The new annotation elaborates on subtypes of the `LOC` and `MISC` entity types, and includes annotation for non-names like times and dates, quantities, languages and nationalities or religious or political groups. The annotation was elaborated with further entity subtypes not present in the Ontonotes 5 annotation (see below).

## Tags derived from the OntoNotes 5.0 annotation

Names are annotated according to the following set of types:

| | | 
|---|---------|
|`PER` | = PERSON People, including fictional |
|`FAC` | = FACILITY Buildings, airports, highways, bridges, etc. |
|`ORG` | = ORGANIZATION Companies, agencies, institutions, etc. |
|`GPE` | Geopolitical entites: countries, cities, states |
|`LOC` | = LOCATION Non-GPE locations, mountain ranges, bodies of water |
|`PROD` | = PRODUCT Vehicles, weapons, foods, etc. (Not services) |
|`EVENT` | Named hurricanes, battles, wars, sports events, etc. |
|`WORK_OF_ART` | Titles of books, songs, etc. |
|`LAW` | Named documents made into laws  |

The following are also annotated in a style similar to names:

| | | 
|---|---------|
| `NORP` | Nationalities or religious or political groups |
| `LANGUAGE` | Any named language |
| `DATE` | Absolute or relative dates or periods |
| `TIME` | Times smaller than a day |
| `PERCENT` | Percentage (including "%") |
| `MONEY` | Monetary values, including unit |
| `QUANTITY` | Measurements, as of weight or distance |
| `ORDINAL` | "first", "second" |
| `CARDINAL` | Numerals that do not fall under another type |

## Additional tags (not in OntoNotes 5)
Further subtypes of names of type `MISC`:

| | |
|-|-|
|`AWARD`| Awards and prizes |
| `CAR` | Cars and other motor vehicles |
|`MEDIA`| Media outlets, TV channels, news portals|
|`SMEDIA`| Social media platforms|
|`PROJ`| Projects and initiatives |
|`MISC`| Unresolved subtypes of MISC entities |
|`MISC-ORG`| Organization-like unresolved subtypes of MISC entities |

Further non-name entities:

| | |
|-|-|
|`DUR` |Time duration
|`AGE` |Age
|`ID`| Identifier

### If you use this model, please cite:

```bibtex
@inproceedings{novak-novak-2022-nerkor,
    title = "{N}er{K}or+{C}ars-{O}nto{N}otes++",
    author = "Nov{\'a}k, Attila  and
      Nov{\'a}k, Borb{\'a}la",
    booktitle = "Proceedings of the Thirteenth Language Resources and Evaluation Conference",
    month = jun,
    year = "2022",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://aclanthology.org/2022.lrec-1.203",
    pages = "1907--1916",
    abstract = "In this paper, we present an upgraded version of the Hungarian NYTK-NerKor named entity corpus, which contains about twice as many annotated spans and 7 times as many distinct entity types as the original version. We used an extended version of the OntoNotes 5 annotation scheme including time and numerical expressions. NerKor is the newest and biggest NER corpus for Hungarian containing diverse domains. We applied cross-lingual transfer of NER models trained for other languages based on multilingual contextual language models to preannotate the corpus. We corrected the annotation semi-automatically and manually. Zero-shot preannotation was very effective with about 0.82 F1 score for the best model. We also added a 12000-token subcorpus on cars and other motor vehicles. We trained and release a transformer-based NER tagger for Hungarian using the annotation in the new corpus version, which provides similar performance to an identical model trained on the original version of the corpus.",
}
```