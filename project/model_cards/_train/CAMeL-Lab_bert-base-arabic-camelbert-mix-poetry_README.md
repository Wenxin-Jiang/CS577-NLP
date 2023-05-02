---
language: 
- ar
license: apache-2.0
widget:
 - text: 'الخيل والليل والبيداء تعرفني [SEP] والسيف والرمح والقرطاس والقلم'
---
# CAMeLBERT-Mix Poetry Classification Model
## Model description
**CAMeLBERT-Mix Poetry Classification Model** is a poetry classification model that was built by fine-tuning the [CAMeLBERT Mix](https://huggingface.co/CAMeL-Lab/bert-base-arabic-camelbert-mix/) model.
For the fine-tuning, we used the [APCD](https://arxiv.org/pdf/1905.05700.pdf) dataset.
Our fine-tuning procedure and the hyperparameters we used can be found in our paper *"[The Interplay of Variant, Size, and Task Type in Arabic Pre-trained Language Models](https://arxiv.org/abs/2103.06678)."* Our fine-tuning code can be found [here](https://github.com/CAMeL-Lab/CAMeLBERT).
## Intended uses
You can use the CAMeLBERT-Mix Poetry Classification model as part of the transformers pipeline.
This model will also be available in [CAMeL Tools](https://github.com/CAMeL-Lab/camel_tools) soon.
#### How to use
To use the model with a transformers pipeline:
```python
>>> from transformers import pipeline
>>> poetry = pipeline('text-classification', model='CAMeL-Lab/bert-base-arabic-camelbert-mix-poetry')
>>> # A list of verses where each verse consists of two parts.
>>> verses = [
        ['الخيل والليل والبيداء تعرفني' ,'والسيف والرمح والقرطاس والقلم'],
        ['قم للمعلم وفه التبجيلا' ,'كاد المعلم ان يكون رسولا']
    ]
>>> # A function that concatenates the halves of each verse by using the [SEP] token.
>>> join_verse = lambda half: ' [SEP] '.join(half)
>>> # Apply this to all the verses in the list.
>>> verses = [join_verse(verse) for verse in verses]
>>> poetry(sentences)
[{'label': 'البسيط', 'score': 0.9937475919723511},
 {'label': 'الكامل', 'score': 0.971284031867981}]
```
*Note*: to download our models, you would need `transformers>=3.5.0`.
Otherwise, you could download the models manually.
 
## Citation
```bibtex
@inproceedings{inoue-etal-2021-interplay,
    title = "The Interplay of Variant, Size, and Task Type in {A}rabic Pre-trained Language Models",
    author = "Inoue, Go  and
      Alhafni, Bashar  and
      Baimukan, Nurpeiis  and
      Bouamor, Houda  and
      Habash, Nizar",
    booktitle = "Proceedings of the Sixth Arabic Natural Language Processing Workshop",
    month = apr,
    year = "2021",
    address = "Kyiv, Ukraine (Online)",
    publisher = "Association for Computational Linguistics",
    abstract = "In this paper, we explore the effects of language variants, data sizes, and fine-tuning task types in Arabic pre-trained language models. To do so, we build three pre-trained language models across three variants of Arabic: Modern Standard Arabic (MSA), dialectal Arabic, and classical Arabic, in addition to a fourth language model which is pre-trained on a mix of the three. We also examine the importance of pre-training data size by building additional models that are pre-trained on a scaled-down set of the MSA variant. We compare our different models to each other, as well as to eight publicly available models by fine-tuning them on five NLP tasks spanning 12 datasets. Our results suggest that the variant proximity of pre-training data to fine-tuning data is more important than the pre-training data size. We exploit this insight in defining an optimized system selection model for the studied tasks.",
}
```