---
language: 
- ar
license: apache-2.0
widget:
 - text: 'شلونك ؟ شخبارك ؟'
---
# CAMeLBERT-CA POS-GLF Model
## Model description
**CAMeLBERT-CA POS-GLF Model** is a Gulf Arabic POS tagging model that was built by fine-tuning the [CAMeLBERT-CA](https://huggingface.co/CAMeL-Lab/bert-base-arabic-camelbert-ca/) model.
For the fine-tuning, we used the [Gumar](https://camel.abudhabi.nyu.edu/annotated-gumar-corpus/) dataset.
Our fine-tuning procedure and the hyperparameters we used can be found in our paper *"[The Interplay of Variant, Size, and Task Type in Arabic Pre-trained Language Models](https://arxiv.org/abs/2103.06678)."*
Our fine-tuning code can be found [here](https://github.com/CAMeL-Lab/CAMeLBERT).

## Intended uses
You can use the CAMeLBERT-CA POS-GLF model as part of the transformers pipeline.
This model will also be available in [CAMeL Tools](https://github.com/CAMeL-Lab/camel_tools) soon.

#### How to use
To use the model with a transformers pipeline:
```python
>>> from transformers import pipeline
>>> pos = pipeline('token-classification', model='CAMeL-Lab/bert-base-arabic-camelbert-ca-pos-glf')
>>> text = 'شلونك ؟ شخبارك ؟'
>>> pos(text)
[{'entity': 'noun', 'score': 0.99572617, 'index': 1, 'word': 'شلون', 'start': 0, 'end': 4}, {'entity': 'noun', 'score': 0.9411187, 'index': 2, 'word': '##ك', 'start': 4, 'end': 5}, {'entity': 'punc', 'score': 0.9999661, 'index': 3, 'word': '؟', 'start': 6, 'end': 7}, {'entity': 'noun', 'score': 0.99286526, 'index': 4, 'word': 'ش', 'start': 8, 'end': 9}, {'entity': 'noun', 'score': 0.9983397, 'index': 5, 'word': '##خبار', 'start': 9, 'end': 13}, {'entity': 'noun', 'score': 0.9609381, 'index': 6, 'word': '##ك', 'start': 13, 'end': 14}, {'entity': 'punc', 'score': 0.9999668, 'index': 7, 'word': '؟', 'start': 15, 'end': 16}]
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