---
language:
- en
- nl
tags:
- bert
- legal
- multilingual
license: apache-2.0
metrics:
- F1
---

# Legal BERT model applicable for Dutch and English
A BERT model further trained from [mBERT](https://huggingface.co/bert-base-multilingual-uncased) on legal documents. The thesis can be downloaded [here](https://www.ru.nl/publish/pages/769526/gerwin_de_kruijf.pdf).

## Data
The model is further trained the same way as [EurlexBERT](https://huggingface.co/nlpaueb/bert-base-uncased-eurlex): regulations, decisions, directives, and parliamentary questions were acquired in both Dutch and English. A total of 184k documents, around 295M words, was used to further train the model. This is less than 9% the size of the original BERT model.
Further training was done for 60k steps, since it showed better results compared to a 100k checkpoint (which was suggested in the original BERT paper). Using more than 100k steps was not beneficial.

## How to use
```python
from transformers import AutoTokenizer, AutoModel, TFAutoModel
tokenizer = AutoTokenizer.from_pretrained("Gerwin/legal-bert-dutch-english")
model = AutoModel.from_pretrained("Gerwin/legal-bert-dutch-english")  # PyTorch
model = TFAutoModel.from_pretrained("Gerwin/legal-bert-dutch-english")  # TensorFlow
```

## Benchmarks
Here are a couple of comparisons between popular BERT models and this model. The fine-tuning procedures for these benchmarks are identical for each pre-trained model, and are more explained in the thesis. You may be able to achieve higher scores for individual models by optimizing fine-tuning procedures. The table shows the weighted F1 scores.

### Legal topic classification
| Model                                                                         | [Multi-EURLEX (NL)](https://huggingface.co/datasets/multi_eurlex) |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **legal-bert-dutch-english**                                                  | **0.786**                                                                                 |
| [mBERT](https://huggingface.co/bert-base-multilingual-uncased)                | 0.779                                                                                     |
| [BERTje](https://huggingface.co/GroNLP/bert-base-dutch-cased)                 | 0.775                                                                                     |

| Model                                                                         | [Multi-EURLEX (EN)](https://huggingface.co/datasets/multi_eurlex) |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **legal-bert-dutch-english**                                                  | 0.786                                                                                     |
| [mBERT](https://huggingface.co/bert-base-multilingual-uncased)                | 0.772                                                                                     |
| [BERT](https://huggingface.co/bert-base-uncased)                              | 0.791                                                                                     |  
| [LegalBERT](https://huggingface.co/nlpaueb/legal-bert-base-uncased)           | 0.791                                                                                     |
| [EurlexBERT](https://huggingface.co/nlpaueb/bert-base-uncased-eurlex)         | **0.795**                                                                                 |  


### Multi-class classification (Rabobank)
This dataset is not open-source, but it is still an interesting case since the dataset contains both Dutch and English legal documents that have to be classified. The dataset consists of 8000 long legal documents (2000 Dutch & 6000 English) with a total of 30 classes. Using a combined architecture of a Dutch and English BERT model was not beneficial, since documents from both languages could belong to the same class.

| Model                              | Rabobank                           |
| ---------------------------------- | ---------------------------------- |
| **legal-bert-dutch-english**       | **0.732**                                                                                 |
| [mBERT](https://huggingface.co/bert-base-multilingual-uncased) | 0.713                                                                                     |
