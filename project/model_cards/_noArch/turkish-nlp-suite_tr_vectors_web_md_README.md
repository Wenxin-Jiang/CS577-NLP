---
tags:
- spacy
- floret
- fasttext
- feature-extraction
- token-classification
language:
- tr
license: cc-by-sa-4.0
model-index:
- name: tr_vectors_web_md
  results:
  - task:
      name: NMT
      type: token-classification
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.1112

---
Medium sized Turkish Floret word vectors for spaCy.

The vectors are trained on MC4 corpus using Floret with the follwing hyperparameters:

```
floret cbow -dim 300 --mode floret --bucket 50000 -minn 4 -maxn5 -minCount 100 
-neg 10 -hashCount 2 -thread 12 -epoch 5
```

Vector are published in Floret format.

| Feature | Description |
| --- | --- |
| **Name** | `tr_vectors_web_md` |
| **Version** | `1.0` |
| **Vectors** | 50000 keys (300 dimensions) |
| **Sources** | [MC4](https://arxiv.org/abs/1910.10683) |
| **License** | `cc-by-sa-4.0` |
| **Author** | [Duygu Altinok](https://www.onlyduygu.com/) |

