---
tags:
- spacy
- token-classification
language:
- en
widget:
- text: "Blood glucose control is the primary strategy to prevent complications in diabetes. At the onset of kidney disease, therapies that inhibit components of the renin angiotensin system (RAS) are also indicated, but these approaches are not wholly effective. Here, we show that once daily administration of the novel glucose lowering agent, empagliflozin, an SGLT2 inhibitor which targets the kidney to block glucose reabsorption, has the potential to improve kidney disease in type 2 diabetes. In male db/db mice, a 10-week treatment with empagliflozin attenuated the diabetes-induced upregulation of profibrotic gene markers, fibronectin and transforming-growth-factor-beta. Other molecular (collagen IV and connective tissue growth factor) and histological (tubulointerstitial total collagen and glomerular collagen IV accumulation) benefits were seen upon dual therapy with metformin. Albuminuria, urinary markers of tubule damage (kidney injury molecule-1, KIM-1 and neutrophil gelatinase-associated lipocalin, NGAL), kidney growth, and glomerulosclerosis, however, were not improved with empagliflozin or metformin, and plasma and intra-renal renin activity was enhanced with empagliflozin. In this model, blood glucose lowering with empagliflozin attenuated some molecular and histological markers of fibrosis but, as per treatment with metformin, did not provide complete renoprotection. Further research to refine the treatment regimen in type 2 diabetes and nephropathy is warranted."
- text: "Chronic kidney disease (CKD) is a global public health problem, and its prevalence is gradually increasing, mainly due to an increase in the number of patients with type 2 diabetes mellitus (T2DM) [1,2,3,4].  Human multidrug and toxin extrusion member 2 (MATE2-K, SLC47A2) plays an important role in the renal elimination of various clinical drugs including the antidiabetic drug metformin. The goal of this study was to characterize genetic variants of MATE2-K and determine their association with the pharmacokinetics of metformin."
model-index:
- name: en_BiomedNER_EuropePMC
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.871384947
    - name: NER Recall
      type: recall
      value: 0.9057132188
    - name: NER F Score
      type: f_score
      value: 0.8882175227
---
Bio literature Named Entity Recognition using microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext transformer model. The model recognises the following entities:
**CD**: Chemical/Drugs, **DS**: Diseases, **GP**: Gene/Protein and **OG**: Organism

| Feature | Description |
| --- | --- |
| **Name** | `en_BiomedNER_EuropePMC` |
| **Version** | `1.0.0` |
| **spaCy** | `>=3.2.4,<3.3.0` |
| **Default Pipeline** | `transformer`, `ner` |
| **Components** | `transformer`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [Santosh Tirunagari](https://europepmc.org/) |

### Label Scheme

<details>

<summary>View label scheme (4 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `CD`, `DS`, `GP`, `OG` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 88.82 |
| `ENTS_P` | 87.14 |
| `ENTS_R` | 90.57 |
| `TRANSFORMER_LOSS` | 92291.81 |
| `NER_LOSS` | 109755.03 |