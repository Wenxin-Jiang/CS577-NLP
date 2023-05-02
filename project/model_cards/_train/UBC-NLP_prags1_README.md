---
license: cc-by-nc-3.0
---

PragS1: Pragmatic Masked Language Modeling with Hashtag_end dataset followed by Emoji-Based Surrogate Fine-Tuning

You can load this model and use for downstream fine-tuning. For example:
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained('UBC-NLP/prags1', use_fast = True)
model = AutoModelForSequenceClassification.from_pretrained('UBC-NLP/prags1',num_labels=lable_size)
```


More details are in our paper:
```
@inproceedings{zhang-abdul-mageed-2022-improving,
    title = "Improving Social Meaning Detection with Pragmatic Masking and Surrogate Fine-Tuning",
    author = "Zhang, Chiyu  and
      Abdul-Mageed, Muhammad",
    booktitle = "Proceedings of the 12th Workshop on Computational Approaches to Subjectivity, Sentiment {\&} Social Media Analysis",
    month = may,
    year = "2022",
    address = "Dublin, Ireland",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.wassa-1.14",
    pages = "141--156",
}
```