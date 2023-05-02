---
language: 
- ar
license: apache-2.0
widget:
 - text: "أنا بخير"
---
# CAMeLBERT-DA SA Model
## Model description
**CAMeLBERT-DA SA Model** is a Sentiment Analysis (SA) model that was built by fine-tuning the [CAMeLBERT Dialectal Arabic (DA)](https://huggingface.co/CAMeL-Lab/bert-base-arabic-camelbert-da/) model.
For the fine-tuning, we used the [ASTD](https://aclanthology.org/D15-1299.pdf), [ArSAS](http://lrec-conf.org/workshops/lrec2018/W30/pdf/22_W30.pdf), and [SemEval](https://aclanthology.org/S17-2088.pdf) datasets.
Our fine-tuning procedure and the hyperparameters we used can be found in our paper *"[The Interplay of Variant, Size, and Task Type in Arabic Pre-trained Language Models](https://arxiv.org/abs/2103.06678)."
* Our fine-tuning code can be found [here](https://github.com/CAMeL-Lab/CAMeLBERT).

## Intended uses
You can use the CAMeLBERT-DA SA model directly as part of our [CAMeL Tools](https://github.com/CAMeL-Lab/camel_tools) SA component (*recommended*) or as part of the transformers pipeline.
#### How to use
To use the model with the [CAMeL Tools](https://github.com/CAMeL-Lab/camel_tools) SA component:
```python
>>> from camel_tools.sentiment import SentimentAnalyzer
>>> sa = SentimentAnalyzer("CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment")
>>> sentences = ['أنا بخير', 'أنا لست بخير']
>>> sa.predict(sentences)
>>> ['positive', 'negative']
```
You can also use the SA model directly with a transformers pipeline:
```python
>>> from transformers import pipeline
>>> sa = pipeline('text-classification', model='CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment')
>>> sentences = ['أنا بخير', 'أنا لست بخير']
>>> sa(sentences)
[{'label': 'positive', 'score': 0.9616648554801941},
 {'label': 'negative', 'score': 0.9779177904129028}]
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