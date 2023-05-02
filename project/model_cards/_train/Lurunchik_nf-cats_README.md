---
language: 
  - en
license: mit

tags:
  - text-classification

inference: false

widget:
- text: "Why do we need an NFQA taxonomy?"
---

# Non Factoid Question Category classification in English
## NFQA model

Repository: [https://github.com/Lurunchik/NF-CATS](https://github.com/Lurunchik/NF-CATS)

Model trained with NFQA dataset. Base model is [roberta-base-squad2](https://huggingface.co/deepset/roberta-base-squad2), a RoBERTa-based model for the task of Question Answering, fine-tuned using the SQuAD2.0 dataset.

Uses `NOT-A-QUESTION`, `FACTOID`, `DEBATE`, `EVIDENCE-BASED`, `INSTRUCTION`, `REASON`, `EXPERIENCE`, `COMPARISON` labels.

## How to use NFQA cat with HuggingFace

##### Load NFQA cat and its tokenizer:
```python
from transformers import AutoTokenizer

from nfqa_model import RobertaNFQAClassification 

nfqa_model = RobertaNFQAClassification.from_pretrained("Lurunchik/nf-cats")
nfqa_tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")
```

##### Make prediction using helper function:
```python
def get_nfqa_category_prediction(text):
    output = nfqa_model(**nfqa_tokenizer(text, return_tensors="pt"))
    index = output.logits.argmax()
    return nfqa_model.config.id2label[int(index)]

get_nfqa_category_prediction('how to assign category?')
# result
#'INSTRUCTION'
```

## Demo 
You can test the model via [hugginface space](https://huggingface.co/spaces/Lurunchik/nf-cats).

[![demo.png](demo.png)](https://huggingface.co/spaces/Lurunchik/nf-cats)


## Citation

If you use `NFQA-cats` in your work, please cite [this paper](https://dl.acm.org/doi/10.1145/3477495.3531926)

```
@misc{bolotova2022nfcats,
        author = {Bolotova, Valeriia and Blinov, Vladislav and Scholer, Falk and Croft, W. Bruce and Sanderson, Mark},
        title = {A Non-Factoid Question-Answering Taxonomy},
        year = {2022},
        isbn = {9781450387323},
        publisher = {Association for Computing Machinery},
        address = {New York, NY, USA},
        url = {https://doi.org/10.1145/3477495.3531926},
        doi = {10.1145/3477495.3531926},
        booktitle = {Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval},
        pages = {1196–1207},
        numpages = {12},
        keywords = {question taxonomy, non-factoid question-answering, editorial study, dataset analysis},
        location = {Madrid, Spain},
        series = {SIGIR '22}
}
```
Enjoy! 🤗