---
tags:
- spacy
- floret
- fasttext
- feature-extraction
- token-classification
language:
- hu
license: cc-by-sa-4.0
model-index:
- name: hu_vectors_web_md
  results:
  - task:
      name: Analogical questions
      type: token-classification
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.1010
    - name: MRR
      type: mrr
      value: 0.1772
 
---
Hungarian word vectors for HuSpaCy. 

The model is trained on the Hungarian Webcorpus 2.0 using floret with the following hyperparameters: `floret cbow -dim 100 -mode floret -bucket 200000 -minn 4 -maxn 6 -minCount 100 -neg 10 -hashCount 2 -lr 0.1 -thread 30 -epoch 5`

Vectors are published in fasttext and floret format.

| Feature | Description |
| --- | --- |
| **Name** | `hu_vectors_web_lg` |
| **Version** | `1.0` |
| **Vectors** | 200000 keys (300 dimensions) |
| **Sources** | [Hungarian Webcorpus 2.0](https://hlt.bme.hu/en/resources/webcorpus2) (Dávid Márk Nemeskey (SZTAKI-HLT)) |
| **License** | `cc-by-sa-4.0` |
| **Author** | [SzegedAI, MILAB](https://github.com/huspacy/huspacy) |


### Accuracy

| Type | Score |
| --- | --- |
| `ACC` | 10.10 |
| `MRR` | 0.1772 |
