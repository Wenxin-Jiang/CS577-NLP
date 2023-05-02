---
language: ur
license: afl-3.0

---

# XLM-RoBERTa-Urdu-Classification

This [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) text classification model trained on Urdu sentiment [data-set](https://huggingface.co/datasets/hassan4830/urdu-binary-classification-data) performs binary sentiment classification on any given Urdu sentence. The model has been fine-tuned for better results in manageable time frames.

## Model description

XLM-RoBERTa is a scaled cross-lingual sentence encoder. It is trained on 2.5T of data across 100 languages data filtered from Common Crawl. XLM-R achieves state-of-the-arts results on multiple cross-lingual benchmarks.

The XLM-RoBERTa model was proposed in Unsupervised Cross-lingual Representation Learning at Scale by Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco GuzmÃ¡n, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov.

It is based on Facebook’s RoBERTa model released in 2019. It is a large multi-lingual language model, trained on 2.5TB of filtered CommonCrawl data.

### How to use

You can import this model directly from the transformers library:

```python
>>> from transformers import AutoTokenizer, AutoModelForSequenceClassification
>>> tokenizer = AutoTokenizer.from_pretrained("Aimlab/xlm-roberta-base-finetuned-urdu")
>>> model = AutoModelForSequenceClassification.from_pretrained("Aimlab/xlm-roberta-base-finetuned-urdu", id2label = {0: 'negative', 1: 'positive'})

```

Here is how to use this model to get the label of a given text:

```python
>>> from transformers import TextClassificationPipeline
>>> text = "وہ ایک برا شخص ہے"
>>> pipe = TextClassificationPipeline(model = model, tokenizer = tokenizer, top_k = 2, device = 0)
>>> pipe(text)

[{'label': 'negative', 'score': 0.9987003803253174},
 {'label': 'positive', 'score': 0.001299630501307547}]

```