---
language: 
- ar
license: apache-2.0
widget:
 - text: "إمارة أبوظبي هي إحدى إمارات دولة الإمارات العربية المتحدة السبع"
---
# CAMeLBERT-Mix NER Model
## Model description
**CAMeLBERT-Mix NER Model** is a Named Entity Recognition (NER) model that was built by fine-tuning the [CAMeLBERT Mix](https://huggingface.co/CAMeL-Lab/bert-base-arabic-camelbert-mix/) model.
For the fine-tuning, we used the [ANERcorp](https://camel.abudhabi.nyu.edu/anercorp/) dataset.
Our fine-tuning procedure and the hyperparameters we used can be found in our paper *"[The Interplay of Variant, Size, and Task Type in Arabic Pre-trained Language Models](https://arxiv.org/abs/2103.06678).
"* Our fine-tuning code can be found [here](https://github.com/CAMeL-Lab/CAMeLBERT).

## Intended uses
You can use the CAMeLBERT-Mix NER model directly as part of our [CAMeL Tools](https://github.com/CAMeL-Lab/camel_tools) NER component (*recommended*) or as part of the transformers pipeline.

#### How to use
To use the model with the [CAMeL Tools](https://github.com/CAMeL-Lab/camel_tools) NER component:
```python
>>> from camel_tools.ner import NERecognizer
>>> from camel_tools.tokenizers.word import simple_word_tokenize
>>> ner = NERecognizer('CAMeL-Lab/bert-base-arabic-camelbert-mix-ner')
>>> sentence = simple_word_tokenize('إمارة أبوظبي هي إحدى إمارات دولة الإمارات العربية المتحدة السبع')
>>> ner.predict_sentence(sentence)
>>> ['O', 'B-LOC', 'O', 'O', 'O', 'O', 'B-LOC', 'I-LOC', 'I-LOC', 'O']
```
You can also use the NER model directly with a transformers pipeline:
```python
>>> from transformers import pipeline
>>> ner = pipeline('ner', model='CAMeL-Lab/bert-base-arabic-camelbert-mix-ner')
>>> ner("إمارة أبوظبي هي إحدى إمارات دولة الإمارات العربية المتحدة السبع")
[{'word': 'أبوظبي',
  'score': 0.9895730018615723,
  'entity': 'B-LOC',
  'index': 2,
  'start': 6,
  'end': 12},
 {'word': 'الإمارات',
  'score': 0.8156259655952454,
  'entity': 'B-LOC',
  'index': 8,
  'start': 33,
  'end': 41},
 {'word': 'العربية',
  'score': 0.890906810760498,
  'entity': 'I-LOC',
  'index': 9,
  'start': 42,
  'end': 49},
 {'word': 'المتحدة',
  'score': 0.8169114589691162,
  'entity': 'I-LOC',
  'index': 10,
  'start': 50,
  'end': 57}]
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