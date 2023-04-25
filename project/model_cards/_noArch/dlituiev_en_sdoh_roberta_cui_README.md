---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_sdoh_roberta_cui
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.8016997167
    - name: NER Recall
      type: recall
      value: 0.7526595745
    - name: NER F Score
      type: f_score
      value: 0.7764060357
widget:
- text: "She lives in Oakland with her bf and commutes to work by bus."
  example_title: "SDOH NER example 1"
  
- text: "There are some logistical barriers, as she lives in Oakland and works at the VA, commuting by bus"
  example_title: "SDOH NER example 2"
  
- text: "I have also been very moody/tearful and generally depressed on a daily basis"
  example_title: "SDOH NER example 3"
  
- text: "Patient is a 85 yo widow, who lives in section 8 housing. She is occasionally visited by her daughter and grandchildren."
  example_title: "SDOH NER example 4"
  
---
RoBERTA based Social determinants of health NER with a standard ontology extension interface (SNOMED_CT and CUI)


| Feature | Description |
| --- | --- |
| **Name** | `en_sdoh_roberta_cui` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.2.1,<3.3.0` |
| **Default Pipeline** | `transformer`, `ner`, `sdoh_cui` |
| **Components** | `transformer`, `ner`, `sdoh_cui` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [Dima Lituiev](mailto:d.lituiev@gmail.com) |
| **Reference** | [Automatic Extraction of Social Determinants of Health from Medical Notes of Chronic Lower Back Pain Patients](https://www.medrxiv.org/content/10.1101/2022.03.04.22271541v1) |

### Label Scheme

<details>

<summary>View label scheme (52 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `Anxiety: GAD`, `Anxiety: Generalized Anxiety Disorder`, `Anxiety: Level of anxiety`, `Anxiety: NA`, `Anxiety: Signs and symptoms of anxiety`, `Anxiety: family hx: Anxiety state`, `Anxiety: hx of anxiety state`, `Depression: Family hx: Depression`, `Depression: Major depressive disorder`, `Depression: NA`, `Depression: PHQ`, `Depression: Symptoms of depression`, `Depression: hx of Depression`, `Financial_strain: Financial problem`, `Financial_strain: Financially secure`, `Financial_strain: NA`, `Financial_strain: Unable to afford medication`, `Food: Able to obtain food`, `Food: Fruit and vegetable intake`, `Food: NA`, `Housing: Homeless`, `Housing: Housing unsuited to needs`, `Housing: Marginally housed`, `Housing: NA`, `Housing: Stably housed`, `Housing: Subsidized housing`, `Housing: lives in facility`, `Insurance_status: Inadequate healthcare resources`, `Insurance_status: NA`, `Marital_or_partnership_status: Divorced`, `Marital_or_partnership_status: Engaged to be married`, `Marital_or_partnership_status: Married`, `Marital_or_partnership_status: NA`, `Marital_or_partnership_status: Partner`, `Marital_or_partnership_status: Partner relationship problem`, `Marital_or_partnership_status: Separated`, `Marital_or_partnership_status: Single person`, `Marital_or_partnership_status: Widowed`, `Social_isolation: At risk for loneliness`, `Social_isolation: Has social support`, `Social_isolation: Lives alone`, `Social_isolation: Lives with`, `Social_isolation: NA`, `Social_isolation: Personal relationship breakdown`, `Social_isolation: Social Isolation`, `Transportation: Has access to a car`, `Transportation: Has access to public transport vehicle`, `Transportation: NA`, `Transportation: Transportation problems`, `pain_and_disability: NA`, `pain_and_disability: Pain intensity rating scale, current`, `pain_and_disability: Pain intensity rating scale, worst` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 77.64 |
| `ENTS_P` | 80.17 |
| `ENTS_R` | 75.27 |
| `TRANSFORMER_LOSS` | 37708138.10 |
| `NER_LOSS` | 1444086.80 |
