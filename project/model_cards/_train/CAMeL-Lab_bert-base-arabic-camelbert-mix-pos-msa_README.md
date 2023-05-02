---
language: 
- ar
license: apache-2.0
widget:
 - text: 'إمارة أبوظبي هي إحدى إمارات دولة الإمارات العربية المتحدة السبع'
---
# CAMeLBERT-Mix POS-MSA Model
## Model description
**CAMeLBERT-Mix POS-MSA Model** is a Modern Standard Arabic (MSA) POS tagging model that was built by fine-tuning the [CAMeLBERT-Mix](https://huggingface.co/CAMeL-Lab/bert-base-arabic-camelbert-mix/) model.
For the fine-tuning, we used the [PATB](https://dl.acm.org/doi/pdf/10.5555/1621804.1621808) dataset.
Our fine-tuning procedure and the hyperparameters we used can be found in our paper *"[The Interplay of Variant, Size, and Task Type in Arabic Pre-trained Language Models](https://arxiv.org/abs/2103.06678)."* Our fine-tuning code can be found [here](https://github.com/CAMeL-Lab/CAMeLBERT).

## Intended uses
You can use the CAMeLBERT-Mix POS-MSA model as part of the transformers pipeline.
This model will also be available in [CAMeL Tools](https://github.com/CAMeL-Lab/camel_tools) soon.

#### How to use
To use the model with a transformers pipeline:
```python
>>> from transformers import pipeline
>>> pos = pipeline('token-classification', model='CAMeL-Lab/bert-base-arabic-camelbert-mix-pos-msa')
>>> text = 'إمارة أبوظبي هي إحدى إمارات دولة الإمارات العربية المتحدة السبع'
>>> pos(text)
[{'entity': 'noun', 'score': 0.9999592, 'index': 1, 'word': 'إمارة', 'start': 0, 'end': 5}, {'entity': 'noun_prop', 'score': 0.9997877, 'index': 2, 'word': 'أبوظبي', 'start': 6, 'end': 12}, {'entity': 'pron', 'score': 0.9998405, 'index': 3, 'word': 'هي', 'start': 13, 'end': 15}, {'entity': 'noun', 'score': 0.9697179, 'index': 4, 'word': 'إحدى', 'start': 16, 'end': 20}, {'entity': 'noun', 'score': 0.99967164, 'index': 5, 'word': 'إما', 'start': 21, 'end': 24}, {'entity': 'noun', 'score': 0.99980617, 'index': 6, 'word': '##رات', 'start': 24, 'end': 27}, {'entity': 'noun', 'score': 0.99997973, 'index': 7, 'word': 'دولة', 'start': 28, 'end': 32}, {'entity': 'noun', 'score': 0.99995637, 'index': 8, 'word': 'الإمارات', 'start': 33, 'end': 41}, {'entity': 'adj', 'score': 0.9983974, 'index': 9, 'word': 'العربية', 'start': 42, 'end': 49}, {'entity': 'adj', 'score': 0.9999469, 'index': 10, 'word': 'المتحدة', 'start': 50, 'end': 57}, {'entity': 'noun_num', 'score': 0.9993273, 'index': 11, 'word': 'السبع', 'start': 58, 'end': 63}]
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