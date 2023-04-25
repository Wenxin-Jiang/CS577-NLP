---
tags:
- spacy
- token-classification
widget:
- text: "Section 319 Cr.P.C. contemplates a situation where the evidence adduced by the prosecution for Respondent No.3-G. Sambiah on 20th June 1984"
- text: "In The High Court Of Kerala At Ernakulam\n\nCrl Mc No. 1622 of 2006()\n\n\n1. T.R.Ajayan, S/O. O.Raman,\n                      ...  Petitioner\n\n                        Vs\n\n\n\n1. M.Ravindran,\n                       ...       Respondent\n\n2. Mrs. Nirmala Dinesh, W/O. Dinesh,\n\n                For Petitioner  :Sri.A.Kumar\n\n                For Respondent  :Smt.M.K.Pushpalatha\n\nThe Hon'ble Mr. Justice P.R.Raman\nThe Hon'ble Mr. Justice V.K.Mohanan\n\n Dated :07/01/2008\n\n O R D E R\n"
language:
- en
license: mit
model-index:
- name: en_legal_ner_sm
  results:
  - task:
      type: token-classification             
      name: Named Entity Recognition              
    dataset:
      type: Named Entity Recognition 
      name: InLegalNER
      split: Test       
    metrics:
      - type: F1-Score         
        value: 74.87
        name: Test F1-Score              
---
## This model is for efficiency purposes for better accuracy refer to [en_legal_ner_trf](https://huggingface.co/opennyaiorg/en_legal_ner_trf)
---
# To Update

[AUTHORS] "[PAPER NAME]". [PAPER DETAILS] [PAPER LINK]

---
Indian Legal Named Entity Recognition(NER): Identifying relevant named entities in an Indian legal judgement using legal NER trained on [spacy](https://github.com/explosion/spaCy).


### Scores
| Type | Score |
| --- | --- |
| **F1-Score** | **74.87** |
| `Precision` | 72.98 |
| `Recall` | 76.85 |


| Feature | Description |
| --- | --- |
| **Name** | `en_legal_ner_sm` |
| **Version** | `3.2.0` |
| **spaCy** | `>=3.2.2,<3.3.0` |
| **Default Pipeline** | `token2vec`, `ner` |
| **Components** | `token2vec`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | [InLegalNER Train Data](https://storage.googleapis.com/indianlegalbert/OPEN_SOURCED_FILES/NER/NER_TRAIN.zip) [GitHub](https://github.com/Legal-NLP-EkStep/legal_NER)|
| **License** | `MIT` |
| **Author** | [Aman Tiwari](https://www.linkedin.com/in/amant555/) |

## Load Pretrained Model

Install the model using pip

```sh
pip install https://huggingface.co/opennyaiorg/en_legal_ner_sm/resolve/main/en_legal_ner_sm-any-py3-none-any.whl
```

Using pretrained NER model

```python
# Using spacy.load().
import spacy
nlp = spacy.load("en_legal_ner_sm")
text = "Section 319 Cr.P.C. contemplates a situation where the evidence adduced by the prosecution for Respondent No.3-G. Sambiah on 20th June 1984"
doc = nlp(text)

# Print indentified entites
for ent in doc.ents:
     print(ent,ent.label_)

##OUTPUT     
#Section 319 PROVISION
#Cr.P.C. STATUTE
#G. Sambiah RESPONDENT
#20th June 1984 DATE
```


### Label Scheme

<details>

<summary>View label scheme (14 labels for 1 components)</summary>

| ENTITY | BELONGS TO |
| --- | --- |
| `LAWYER` | PREAMBLE |
| `COURT` | PREAMBLE, JUDGEMENT |
| `JUDGE` | PREAMBLE, JUDGEMENT |
| `PETITIONER` | PREAMBLE, JUDGEMENT |
| `RESPONDENT` | PREAMBLE, JUDGEMENT |
| `CASE_NUMBER` | JUDGEMENT | 
| `GPE` | JUDGEMENT |
| `DATE` | JUDGEMENT |
| `ORG` | JUDGEMENT |
| `STATUTE` | JUDGEMENT |
| `WITNESS` | JUDGEMENT |
| `PRECEDENT` | JUDGEMENT |
| `PROVISION` | JUDGEMENT |
| `OTHER_PERSON` | JUDGEMENT |

</details>


## Author - Publication

```
[CITATION DETAILS]
```