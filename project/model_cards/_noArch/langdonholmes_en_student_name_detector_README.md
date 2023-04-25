---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_student_name_detector
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.8311688312
    - name: NER Recall
      type: recall
      value: 0.8421052632
    - name: NER F Score
      type: f_score
      value: 0.8366013072
---
| Feature | Description |
| --- | --- |
| **Name** | `en_student_name_detector` |
| **Version** | `0.0.1` |
| **spaCy** | `>=3.4.1,<3.5.0` |
| **Default Pipeline** | `transformer`, `ner` |
| **Components** | `transformer`, `ner` |
| **Sources** | [longformer](https://huggingface.co/allenai/longformer-base-4096) |
| **License** | [Apache 2.0](https://huggingface.co/langdonholmes/en_student_name_detector/blob/main/LICENSE) |
| **Author** | [Langdon Holmes](https://huggingface.co/langdonholmes) |

### Label Scheme

<details>

<summary>View label scheme (1 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `STUDENT` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 83.66 |
| `ENTS_P` | 83.12 |
| `ENTS_R` | 84.21 |
| `TRANSFORMER_LOSS` | 56255026.35 |
| `NER_LOSS` | 31154.89 |


### Training Data

6,293 student writing assignments were submitted as PDF files. All documents were reflection assignments in response to the same prompt in the same online course. Student names were labeled by human raters (one rater per document). A preliminary model was trained and all disagreements between this model and the human annotations were adjudicated by two additional reviewers. The training dataset includes all 6,293 documents, 845 of which include student names. There are 1,155 student name annotations in total.

### To Use

This model has been packaged using spaCy. It is available as a huggingface model or a pip package. Performance of the model should be evaluated on in-domain data before deployment in production, particularly when confidential information is involved.