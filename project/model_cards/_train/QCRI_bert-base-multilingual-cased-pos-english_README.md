---
language:
  - en
tags:
  - part-of-speech
  - finetuned
license: cc-by-nc-3.0
---

# BERT-base-multilingual-cased finetuned for Part-of-Speech tagging

This is a multilingual BERT model fine tuned for part-of-speech tagging for English. It is trained using the Penn TreeBank (Marcus et al., 1993) and achieves an F1-score of 96.69.

## Usage
A *transformers* pipeline can be used to run the model:

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification, TokenClassificationPipeline

model_name = "QCRI/bert-base-multilingual-cased-pos-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

pipeline = TokenClassificationPipeline(model=model, tokenizer=tokenizer)
outputs = pipeline("A test example")
print(outputs)
```


## Citation
This model was used for all the part-of-speech tagging based results in *Analyzing Encoded Concepts in Transformer Language Models*, published at NAACL'22. If you find this model useful for your own work, please use the following citation:

```bib
@inproceedings{sajjad-NAACL,
  title={Analyzing Encoded Concepts in Transformer Language Models},
  author={Hassan Sajjad, Nadir Durrani, Fahim Dalvi, Firoj Alam, Abdul Rafae Khan and Jia Xu},
  booktitle={North American Chapter of the Association of Computational Linguistics: Human Language Technologies (NAACL)},
  series={NAACL~'22},
  year={2022},
  address={Seattle}
}
```