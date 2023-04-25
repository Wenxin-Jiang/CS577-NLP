---
tags:
- spacy
- token-classification
language:
- it
model-index:
- name: it_nerIta_trf
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9196
    - name: NER Recall
      type: recall
      value: 0.9086
    - name: NER F Score
      type: f_score
      value: 0.9147
widget:
- text: "E' stato pubblicato il decreto legge recante “disposizioni urgenti per il superamento delle misure di contrasto alla diffusione dell'epidemia da COVID-19, in conseguenza della cessazione dello stato di emergenza” prevista al 31 marzo 2022 (D.L. 24 marzo 2022, n. 24)."
- text: "Il Regolamento (UE) n. 1245/2020 modifica gli allegati I, II, IV e V del Regolamento cardine relativo ai MOCA in materiale plastico (Materiali e Oggetti destinati a venire in Contatto con prodotti Alimentari), ovvero il Regolamento (UE) n. 10/2011."	  
- text: "Aspetterò Marco per un altro quarto d'ora. Con questo ritardo rischio di prendere una multa di 40 euro. Oggi ho fatto 3 km di corsa in compagnia della musica con il mio I-Phone. Oggi ho ascoltato anche 'L'anno che verrà' di Lucio Dalla."
- text: "Con la pubblicazione in Gazzetta Ufficiale della legge di conversione del c.d. decreto Sostegni ter sono previste disposizioni per l'ingresso in Italia per lavoro dei nomadi digitali e lavoratori da remoto (Legge 28 marzo 2022, n. 25).\r\nL’Agenzia delle Entrate analizza le novità in materia di imposta di registro, IVA e IRAP contenute nel decreto Milleproroghe 2022. In particolare, si ricorda il rinvio del termine per regolarizzare gli omessi versamenti IRAP per errata applicazione dell’esonero previsto dal decreto Rilancio (Agenzia Entrate, circolare n. 8/E/2022; art. 20-bis, D.L. n. 228/2021 conv. l. 15/2022; art. 1-bis D.L. n. 146/2021)."
- text: "In particolare, con riferimento all’articolo 14 del d.l. n. 63 del 2013, concernente detrazioni per interventi di efficienza energetica (ecobonus), la lettera a), n. 1), del comma 37 art. 1 della Legge di Bilancio 2022 proroga dal 31 dicembre 2021 al 31 dicembre 2024 il termine previsto per avvalersi di tali detrazioni: nella misura del 65 per cento per le spese sostenute per taluni interventi; -nelle misure del 70 o del 75 per cento per le spese sostenute per gli interventi di cui al comma 2-quater7 del citato articolo 14, effettuati sulle parti comuni degli edifici."
---
## Model description (NerIta)
**it_nerIta_trf** is a fine-tuned spacy model ready to be used for **Named Entity Recognition** on **Italian language** texts based on a pipeline composed by the **hseBert-it-cased** transformer.
It has been trained to recognize 18 types of entities: PER, NORP, ORG, GPE, LOC, DATE, MONEY, FAC, PRODUCT, EVENT, WORK_OF_ART, LAW, LANGUAGE, TIME, PERCENT, QUANTITY, ORDINAL, CARDINAL. See table below for details.

| Feature | Description |
| --- | --- |
| **Name** | `nerIta_trf` |
| **Version** | `0.0.1` |
| **spaCy** | `>=3.2.1,<3.3.0` |
| **Default Pipeline** | `transformer`, `ner` |
| **Components** | `transformer`, `ner` |
| **Based on transformer** | `bullmount/hseBert-it-cased` |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (18 labels)</summary>

Predicts 18 tags:

| **tag**                        | **meaning** |
|---------------------------------|-----------|
| PER         | People, including fictional. | 
| NORP         | Nationalities or religious or political groups. | 
| ORG         | Companies, agencies, institutions, etc. | 
| GPE         | Countries, cities, states. | 
| LOC         | Non-GPE locations, mountain ranges, bodies of water. | 
| DATE         | Absolute or relative dates or periods. | 
| MONEY         | Monetary values, including unit. | 
| FAC         | Buildings, airports, highways, bridges, etc. | 
| PRODUCT         | Objects, vehicles, foods, etc. (Not services.) | 
| EVENT         | Named hurricanes, battles, wars, sports events, etc. |
| WORK_OF_ART | Titles of books, songs, etc. |
| LAW | Named documents made into laws. |
| LANGUAGE | Any named language. |
| TIME | Times smaller than a day. |
| PERCENT | Percentage, including "%". |
| QUANTITY | Measurements, as of weight or distance.|
| ORDINAL | "first", "second", etc.|
| CARDINAL | Numerals that do not fall under another type. |
| MISC         | other name |

</details>

### Accuracy
| Type | Score |
| --- | --- |
| `ENTS_F` | 91.96 |
| `ENTS_P` | 91.47 |
| `ENTS_R` | 90.86 |