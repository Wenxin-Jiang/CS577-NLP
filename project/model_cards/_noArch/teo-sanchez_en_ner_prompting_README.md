---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_ner_prompting
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.7437641723
    - name: NER Recall
      type: recall
      value: 0.7248618785
    - name: NER F Score
      type: f_score
      value: 0.7341913822
widget:
  - text: Golden statue of a victorious warrior raising his sword to the sky, heroic, glorious, in the style of artgerm, gerald brom, atey ghailan and mike mignola, vibrant colors and hard shadows and strong rim light, plain background, comic cover art, trending on artstation
  - text: Italian renaissance dragon statue castle gallery highly detailed artstation concept art sharp focus illustration briclot rutkowski mucha
  - text: Quetzalcoatl in an epic battle with garuda, fantasy, stained glass, d & d, intricate, elegant, highly detailed, digital painting, artstation, concept art, matte, sharp focus, illustration, art by john collier and albert aublet and krenz cushart and artem demura and alphonse mucha
lisence: CC BY 3.0
---
| Feature | Description |
| --- | --- |
| **Name** | `en_ner_prompting` |
| **Version** | `0.0.3` |
| **spaCy** | `>=3.4.3,<3.5.0` |
| **Default Pipeline** | `tok2vec`, `ner` |
| **Components** | `tok2vec`, `ner` |
| **Vectors** | 514157 keys, 514157 unique vectors (300 dimensions) |
| **Sources** | n/a |
| **License** | CC BY 3.0 |
| **Author** | [Selas.ai](www.selas.ai) |

![](https://www.selas.ai/assets/logo-selas.86b7b0b6.svg)

### Description

Name entity recognition model to analyzing text-to-image prompts (Stable Diffusion).

  The entities comprise 7 main categories and 11 subcategories for a total of 16 categories, extracted from a topic analysis made with [BERTopic](https://maartengr.github.io/BERTopic/index.html).
  The topic analysis can be explored [the following visualization](https://teo-sanchez.github.io/projects/prompting_map.html).

```
  ├── medium/
  │   ├── photography
  │   ├── painting
  │   ├── rendering
  │   └── illustration
  ├── influence/
  │   ├── artist
  │   ├── genre
  │   ├── artwork
  │   └── repository
  ├── light
  ├── color
  ├── composition
  ├── detail
  └── context/
      ├── era
      ├── weather
      └── emotion
```
      
  Prompt data are from the [diffusionDB](https://poloclub.github.io/diffusiondb/) database and were annotated by hand using [Prodigy](https://prodi.gy/).

### Label Scheme

<details>

<summary>View label scheme (16 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `color`, `composition`, `context/emotion`, `context/era`, `context/weather`, `detail`, `influence/artist`, `influence/artwork`, `influence/genre`, `influence/repository`, `light`, `medium/illustration`, `medium/painting`, `medium/photography`, `medium/rendering`, `subject` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 73.42 |
| `ENTS_P` | 74.38 |
| `ENTS_R` | 72.49 |
| `TOK2VEC_LOSS` | 19323.84 |
| `NER_LOSS` | 144524.82 |