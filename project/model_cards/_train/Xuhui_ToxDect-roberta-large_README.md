---
language: 
- 
-
thumbnail: 
tags:
- 
-
- 
license: 
datasets:
- 
-
metrics:
- 
-
---

# Toxic language detection

## Model description

A toxic language detection model trained on tweets. The base model is Roberta-large. For more information, 
including the **training data**, **limitations and bias**, please refer to the [paper](https://arxiv.org/pdf/2102.00086.pdf) and
Github [repo](https://github.com/XuhuiZhou/Toxic_Debias) for more details.

#### How to use
Note that LABEL_1 means toxic and LABEL_0 means non-toxic in the output.

```python
from transformers import pipeline
classifier = pipeline("text-classification",model='Xuhui/ToxDect-roberta-large', return_all_scores=True)
prediction = classifier("You are f**king stupid!", )
print(prediction)

"""
Output:
[[{'label': 'LABEL_0', 'score': 0.002632011892274022}, {'label': 'LABEL_1', 'score': 0.9973680377006531}]]
"""
```

## Training procedure
The random seed for this model is 22. For other details, please refer to the Github [repo](https://github.com/XuhuiZhou/Toxic_Debias) for more details.

### BibTeX entry and citation info

```bibtex
@inproceedings{zhou-etal-2020-debiasing,
  title = {Challenges in Automated Debiasing for Toxic Language Detection},
  author = {Zhou, Xuhui and Sap, Maarten and Swayamdipta, Swabha and Choi, Yejin and Smith, Noah A.},
  booktitle = {EACL},
  abbr = {EACL},
  html = {https://www.aclweb.org/anthology/2021.eacl-main.274.pdf},
  code = {https://github.com/XuhuiZhou/Toxic_Debias},
  year = {2021},
  bibtex_show = {true},
  selected = {true}
}
```