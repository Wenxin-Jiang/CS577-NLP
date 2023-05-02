---
language: 
- ar
license: apache-2.0
tags:
- Arabic
- Dialect
- Egyptian
- Gulf
- Levantine
- Classical Arabic
- MSA
- Modern Standard Arabic
 
widget:
 - text: "الهدف من الحياة هو [MASK] ."
---

# CAMeLBERT: A collection of pre-trained models for Arabic NLP tasks

## Model description

**CAMeLBERT** is a collection of BERT models pre-trained on Arabic texts with different sizes and variants.
We release pre-trained language models for Modern Standard Arabic (MSA), dialectal Arabic (DA), and classical Arabic (CA), in addition to a model pre-trained on a mix of the three.
We also provide additional models that are pre-trained on a scaled-down set of the MSA variant (half, quarter, eighth, and sixteenth).
The details are described in the paper *"[The Interplay of Variant, Size, and Task Type in Arabic Pre-trained Language Models](https://arxiv.org/abs/2103.06678)."*

This model card describes **CAMeLBERT-Mix** (`bert-base-arabic-camelbert-mix`), a model pre-trained on a mixture of these variants: MSA, DA, and CA.

||Model|Variant|Size|#Word|
|-|-|:-:|-:|-:|
|✔|`bert-base-arabic-camelbert-mix`|CA,DA,MSA|167GB|17.3B|
||`bert-base-arabic-camelbert-ca`|CA|6GB|847M|
||`bert-base-arabic-camelbert-da`|DA|54GB|5.8B|
||`bert-base-arabic-camelbert-msa`|MSA|107GB|12.6B|
||`bert-base-arabic-camelbert-msa-half`|MSA|53GB|6.3B|
||`bert-base-arabic-camelbert-msa-quarter`|MSA|27GB|3.1B|
||`bert-base-arabic-camelbert-msa-eighth`|MSA|14GB|1.6B|
||`bert-base-arabic-camelbert-msa-sixteenth`|MSA|6GB|746M|

## Intended uses
You can use the released model for either masked language modeling or next sentence prediction.
However, it is mostly intended to be fine-tuned on an NLP task, such as NER, POS tagging, sentiment analysis, dialect identification, and poetry classification.
We release our fine-tuninig code [here](https://github.com/CAMeL-Lab/CAMeLBERT).

#### How to use
You can use this model directly with a pipeline for masked language modeling:
```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='CAMeL-Lab/bert-base-arabic-camelbert-mix')
>>> unmasker("الهدف من الحياة هو [MASK] .")
[{'sequence': '[CLS] الهدف من الحياة هو النجاح. [SEP]',
  'score': 0.10861027985811234,
  'token': 6232,
  'token_str': 'النجاح'},
 {'sequence': '[CLS] الهدف من الحياة هو.. [SEP]',
  'score': 0.07626965641975403,
  'token': 18,
  'token_str': '.'},
 {'sequence': '[CLS] الهدف من الحياة هو الحياة. [SEP]',
  'score': 0.05131986364722252,
  'token': 3696,
  'token_str': 'الحياة'},
 {'sequence': '[CLS] الهدف من الحياة هو الموت. [SEP]',
  'score': 0.03734956309199333,
  'token': 4295,
  'token_str': 'الموت'},
 {'sequence': '[CLS] الهدف من الحياة هو العمل. [SEP]',
  'score': 0.027189988642930984,
  'token': 2854,
  'token_str': 'العمل'}]
```

*Note*: to download our models, you would need `transformers>=3.5.0`. Otherwise, you could download the models manually.

Here is how to use this model to get the features of a given text in PyTorch:
```python
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained('CAMeL-Lab/bert-base-arabic-camelbert-mix')
model = AutoModel.from_pretrained('CAMeL-Lab/bert-base-arabic-camelbert-mix')
text = "مرحبا يا عالم."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
```

and in TensorFlow:
```python
from transformers import AutoTokenizer, TFAutoModel
tokenizer = AutoTokenizer.from_pretrained('CAMeL-Lab/bert-base-arabic-camelbert-mix')
model = TFAutoModel.from_pretrained('CAMeL-Lab/bert-base-arabic-camelbert-mix')
text = "مرحبا يا عالم."
encoded_input = tokenizer(text, return_tensors='tf')
output = model(encoded_input)
```

## Training data
- MSA (Modern Standard Arabic)
  - [The Arabic Gigaword Fifth Edition](https://catalog.ldc.upenn.edu/LDC2011T11)
  - [Abu El-Khair Corpus](http://www.abuelkhair.net/index.php/en/arabic/abu-el-khair-corpus)
  - [OSIAN corpus](https://vlo.clarin.eu/search;jsessionid=31066390B2C9E8C6304845BA79869AC1?1&q=osian)
  - [Arabic Wikipedia](https://archive.org/details/arwiki-20190201)
  - The unshuffled version of the Arabic [OSCAR corpus](https://oscar-corpus.com/)
- DA (dialectal Arabic)
  - A collection of dialectal Arabic data described in [our paper](https://arxiv.org/abs/2103.06678).
- CA (classical Arabic)
  - [OpenITI (Version 2020.1.2)](https://zenodo.org/record/3891466#.YEX4-F0zbzc)

## Training procedure
We use [the original implementation](https://github.com/google-research/bert) released by Google for pre-training.
We follow the original English BERT model's hyperparameters for pre-training, unless otherwise specified.

### Preprocessing
- After extracting the raw text from each corpus, we apply the following pre-processing.
- We first remove invalid characters and normalize white spaces using the utilities provided by [the original BERT implementation](https://github.com/google-research/bert/blob/eedf5716ce1268e56f0a50264a88cafad334ac61/tokenization.py#L286-L297).
- We also remove lines without any Arabic characters.
- We then remove diacritics and kashida using [CAMeL Tools](https://github.com/CAMeL-Lab/camel_tools).
- Finally, we split each line into sentences with a heuristics-based sentence segmenter.
- We train a WordPiece tokenizer on the entire dataset (167 GB text) with a vocabulary size of 30,000 using [HuggingFace's tokenizers](https://github.com/huggingface/tokenizers).
- We do not lowercase letters nor strip accents.

### Pre-training
- The model was trained on a single cloud TPU (`v3-8`) for one million steps in total.
- The first 90,000 steps were trained with a batch size of 1,024 and the rest was trained with a batch size of 256.
- The sequence length was limited to 128 tokens for 90% of the steps and 512 for the remaining 10%.
- We use whole word masking and a duplicate factor of 10.
- We set max predictions per sequence to 20 for the dataset with max sequence length of 128 tokens and 80 for the dataset with max sequence length of 512 tokens.
- We use a random seed of 12345, masked language model probability of 0.15, and short sequence probability of 0.1.
- The optimizer used is Adam with a learning rate of 1e-4, \\(\beta_{1} = 0.9\\) and \\(\beta_{2} = 0.999\\), a weight decay of 0.01, learning rate warmup for 10,000 steps and linear decay of the learning rate after.

## Evaluation results
- We evaluate our pre-trained language models on five NLP tasks: NER, POS tagging, sentiment analysis, dialect identification, and poetry classification.
- We fine-tune and evaluate the models using 12 dataset.
- We used Hugging Face's transformers to fine-tune our CAMeLBERT models.
- We used transformers `v3.1.0` along with PyTorch `v1.5.1`.
- The fine-tuning was done by adding a fully connected linear layer to the last hidden state.
- We use \\(F_{1}\\) score as a metric for all tasks.
- Code used for fine-tuning is available [here](https://github.com/CAMeL-Lab/CAMeLBERT).

### Results

| Task                 | Dataset         | Variant | Mix   | CA    | DA    | MSA   | MSA-1/2 | MSA-1/4 | MSA-1/8 | MSA-1/16 |
| -------------------- | --------------- | ------- | ----- | ----- | ----- | ----- | ------- | ------- | ------- | -------- |
| NER                  | ANERcorp        | MSA     | 80.8% | 67.9% | 74.1% | 82.4% | 82.0%   | 82.1%   | 82.6%   | 80.8%    |
| POS                  | PATB (MSA)      | MSA     | 98.1% | 97.8% | 97.7% | 98.3% | 98.2%   | 98.3%   | 98.2%   | 98.2%    |
|                      | ARZTB (EGY)     | DA      | 93.6% | 92.3% | 92.7% | 93.6% | 93.6%   | 93.7%   | 93.6%   | 93.6%    |
|                      | Gumar (GLF)     | DA      | 97.3% | 97.7% | 97.9% | 97.9% | 97.9%   | 97.9%   | 97.9%   | 97.9%    |
| SA                   | ASTD            | MSA     | 76.3% | 69.4% | 74.6% | 76.9% | 76.0%   | 76.8%   | 76.7%   | 75.3%    |
|                      | ArSAS           | MSA     | 92.7% | 89.4% | 91.8% | 93.0% | 92.6%   | 92.5%   | 92.5%   | 92.3%    |
|                      | SemEval         | MSA     | 69.0% | 58.5% | 68.4% | 72.1% | 70.7%   | 72.8%   | 71.6%   | 71.2%    |
| DID                  | MADAR-26        | DA      | 62.9% | 61.9% | 61.8% | 62.6% | 62.0%   | 62.8%   | 62.0%   | 62.2%    |
|                      | MADAR-6         | DA      | 92.5% | 91.5% | 92.2% | 91.9% | 91.8%   | 92.2%   | 92.1%   | 92.0%    |
|                      | MADAR-Twitter-5 | MSA     | 75.7% | 71.4% | 74.2% | 77.6% | 78.5%   | 77.3%   | 77.7%   | 76.2%    |
|                      | NADI            | DA      | 24.7% | 17.3% | 20.1% | 24.9% | 24.6%   | 24.6%   | 24.9%   | 23.8%    |
| Poetry               | APCD            | CA      | 79.8% | 80.9% | 79.6% | 79.7% | 79.9%   | 80.0%   | 79.7%   | 79.8%    |

### Results (Average)
|                      | Variant | Mix   | CA    | DA    | MSA   | MSA-1/2 | MSA-1/4 | MSA-1/8 | MSA-1/16 |
| -------------------- | ------- | ----- | ----- | ----- | ----- | ------- | ------- | ------- | -------- |
| Variant-wise-average<sup>[[1]](#footnote-1)</sup> | MSA     | 82.1% | 75.7% | 80.1% | 83.4% | 83.0%   | 83.3%   | 83.2%   | 82.3%    |
|                      | DA      | 74.4% | 72.1% | 72.9% | 74.2% | 74.0%   | 74.3%   | 74.1%   | 73.9%    |
|                      | CA      | 79.8% | 80.9% | 79.6% | 79.7% | 79.9%   | 80.0%   | 79.7%   | 79.8%    |
| Macro-Average        | ALL     | 78.7% | 74.7% | 77.1% | 79.2% | 79.0%   | 79.2%   | 79.1%   | 78.6%    |

<a name="footnote-1">[1]</a>: Variant-wise-average refers to average over a group of tasks in the same language variant.

## Acknowledgements
This research was supported with Cloud TPUs from Google’s TensorFlow Research Cloud (TFRC).

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
