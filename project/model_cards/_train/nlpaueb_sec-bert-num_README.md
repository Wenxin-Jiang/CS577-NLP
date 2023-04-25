---
language: en
pipeline_tag: fill-mask
license: cc-by-sa-4.0
thumbnail: https://i.ibb.co/0yz81K9/sec-bert-logo.png
tags:
- finance
- financial
widget:
- text: "Total net sales decreased [MASK]% or $[NUM] billion during [NUM] compared to [NUM]."
- text: "Total net sales decreased [NUM]% or $[MASK] billion during [NUM] compared to [NUM]."
- text: "Total net sales decreased [NUM]% or $[NUM] billion during [MASK] compared to [NUM]."
- text: "During [MASK], the Company repurchased $[NUM] billion of its common stock and paid dividend equivalents of $[NUM] billion."
- text: "During 2019, the Company repurchased $[MASK] billion of its common stock and paid dividend equivalents of $[NUM] billion."
---

# SEC-BERT

<img align="center" src="https://i.ibb.co/0yz81K9/sec-bert-logo.png" alt="sec-bert-logo" width="400"/>

<div style="text-align: justify">

SEC-BERT is a family of BERT models for the financial domain, intended to assist financial NLP research and FinTech applications.
SEC-BERT consists of the following models:
* [**SEC-BERT-BASE**](https://huggingface.co/nlpaueb/sec-bert-base): Same architecture as BERT-BASE trained on financial documents.
* **SEC-BERT-NUM** (this model): Same as SEC-BERT-BASE but we replace every number token with a [NUM] pseudo-token handling all numeric expressions in a uniform manner, disallowing their fragmentation).
* [**SEC-BERT-SHAPE**](https://huggingface.co/nlpaueb/sec-bert-shape): Same as SEC-BERT-BASE but we replace numbers with pseudo-tokens that represent the number’s shape, so numeric expressions (of known shapes) are no longer fragmented, e.g., '53.2' becomes '[XX.X]' and '40,200.5' becomes '[XX,XXX.X]'.
</div>

## Pre-training corpus

The model was pre-trained on 260,773 10-K filings from 1993-2019, publicly available at <a href="https://www.sec.gov/">U.S. Securities and Exchange Commission (SEC)</a>

## Pre-training details

<div style="text-align: justify">

* We created a new vocabulary of 30k subwords by training a [BertWordPieceTokenizer](https://github.com/huggingface/tokenizers) from scratch on the pre-training corpus.
* We trained BERT using the official code provided in [Google BERT's GitHub repository](https://github.com/google-research/bert)</a>.
* We then used [Hugging Face](https://huggingface.co)'s [Transformers](https://github.com/huggingface/transformers) conversion script to convert the TF checkpoint in the desired format in order to be able to load the model in two lines of code for both PyTorch and TF2 users.
* We release a model similar to the English BERT-BASE model (12-layer, 768-hidden, 12-heads, 110M parameters).
* We chose to follow the same training set-up: 1 million training steps with batches of 256 sequences of length 512 with an initial learning rate 1e-4.
* We were able to use a single Google Cloud TPU v3-8 provided for free from [TensorFlow Research Cloud (TRC)](https://sites.research.google/trc), while also utilizing [GCP research credits](https://edu.google.com/programs/credits/research). Huge thanks to both Google programs for supporting us!
</div>

## Load Pretrained Model

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("nlpaueb/sec-bert-num")
model = AutoModel.from_pretrained("nlpaueb/sec-bert-num")
```

## Pre-process Text

<div style="text-align: justify">

To use SEC-BERT-NUM, you have to pre-process texts replacing every numerical token with [NUM] pseudo-token.
Below there is an example of how you can pre-process a simple sentence. This approach is quite simple; feel free to modify it as you see fit.
</div>

```python
import re
import spacy
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("nlpaueb/sec-bert-num")
spacy_tokenizer = spacy.load("en_core_web_sm")

sentence = "Total net sales decreased 2% or $5.4 billion during 2019 compared to 2018."

def sec_bert_num_preprocess(text):
    tokens = [t.text for t in spacy_tokenizer(text)]

    processed_text = []
    for token in tokens:
        if re.fullmatch(r"(\d+[\d,.]*)|([,.]\d+)", token):
            processed_text.append('[NUM]')
        else:
            processed_text.append(token)
            
    return ' '.join(processed_text)
        
tokenized_sentence = tokenizer.tokenize(sec_bert_num_preprocess(sentence))
print(tokenized_sentence)
"""
['total', 'net', 'sales', 'decreased', '[NUM]', '%', 'or', '$', '[NUM]', 'billion', 'during', '[NUM]', 'compared', 'to', '[NUM]', '.']
"""
```

## Using SEC-BERT variants as Language Models

| Sample                                              | Masked Token |
| --------------------------------------------------- | ------------ |
| Total net sales [MASK] 2% or $5.4 billion during 2019 compared to 2018. | decreased

| Model                                               | Predictions (Probability)  |
| --------------------------------------------------- | ------------ |
| **BERT-BASE-UNCASED** | increased (0.221), were (0.131), are (0.103), rose (0.075), of (0.058)
| **SEC-BERT-BASE** | increased (0.678), decreased (0.282), declined (0.017), grew (0.016), rose (0.004)
| **SEC-BERT-NUM** | increased (0.753), decreased (0.211), grew (0.019), declined (0.010), rose (0.006)
| **SEC-BERT-SHAPE** | increased (0.747), decreased (0.214), grew (0.021), declined (0.013), rose (0.002)


| Sample                                              | Masked Token |
| --------------------------------------------------- | ------------ |
| Total net sales decreased 2% or $5.4 [MASK] during 2019 compared to 2018. | billion

| Model                                               | Predictions (Probability)  |
| --------------------------------------------------- | ------------ |
| **BERT-BASE-UNCASED** | billion (0.841), million (0.097), trillion (0.028), ##m (0.015), ##bn (0.006)
| **SEC-BERT-BASE** | million (0.972), billion (0.028), millions (0.000), ##million (0.000), m (0.000)
| **SEC-BERT-NUM** | million (0.974), billion (0.012), , (0.010), thousand (0.003), m (0.000)
| **SEC-BERT-SHAPE** | million (0.978), billion (0.021), % (0.000), , (0.000), millions (0.000)


| Sample                                              | Masked Token |
| --------------------------------------------------- | ------------ |
| Total net sales decreased [MASK]% or $5.4 billion during 2019 compared to 2018. | 2

| Model                                               | Predictions (Probability)  |
| --------------------------------------------------- | ------------ |
| **BERT-BASE-UNCASED** | 20 (0.031), 10 (0.030), 6 (0.029), 4 (0.027), 30 (0.027)
| **SEC-BERT-BASE** | 13 (0.045), 12 (0.040), 11 (0.040), 14 (0.035), 10 (0.035)
| **SEC-BERT-NUM** | [NUM] (1.000), one (0.000), five (0.000), three (0.000), seven (0.000)
| **SEC-BERT-SHAPE** | [XX] (0.316), [XX.X] (0.253), [X.X] (0.237), [X] (0.188), [X.XX] (0.002)


| Sample                                              | Masked Token |
| --------------------------------------------------- | ------------ |
| Total net sales decreased 2[MASK] or $5.4 billion during 2019 compared to 2018. | %

| Model                                               | Predictions (Probability)  |
| --------------------------------------------------- | ------------ |
| **BERT-BASE-UNCASED** | % (0.795), percent (0.174), ##fold (0.009), billion (0.004), times (0.004)
| **SEC-BERT-BASE** | % (0.924), percent (0.076), points (0.000), , (0.000), times (0.000)
| **SEC-BERT-NUM** | % (0.882), percent (0.118), million (0.000), units (0.000), bps (0.000)
| **SEC-BERT-SHAPE** | % (0.961), percent (0.039), bps (0.000), , (0.000), bcf (0.000)


| Sample                                              | Masked Token |
| --------------------------------------------------- | ------------ |
| Total net sales decreased 2% or $[MASK] billion during 2019 compared to 2018. | 5.4

| Model                                               | Predictions (Probability)  |
| --------------------------------------------------- | ------------ |
| **BERT-BASE-UNCASED** | 1 (0.074), 4 (0.045), 3 (0.044), 2 (0.037), 5 (0.034)
| **SEC-BERT-BASE** | 1 (0.218), 2 (0.136), 3 (0.078), 4 (0.066), 5 (0.048)
| **SEC-BERT-NUM** | [NUM] (1.000), l (0.000), 1 (0.000), - (0.000), 30 (0.000)
| **SEC-BERT-SHAPE** | [X.X] (0.787), [X.XX] (0.095), [XX.X] (0.049), [X.XXX] (0.046), [X] (0.013)


| Sample                                              | Masked Token |
| --------------------------------------------------- | ------------ |
| Total net sales decreased 2% or $5.4 billion during [MASK] compared to 2018. | 2019

| Model                                               | Predictions (Probability)  |
| --------------------------------------------------- | ------------ |
| **BERT-BASE-UNCASED** | 2017 (0.485), 2018 (0.169), 2016 (0.164), 2015 (0.070), 2014 (0.022)
| **SEC-BERT-BASE** | 2019 (0.990), 2017 (0.007), 2018 (0.003), 2020 (0.000), 2015 (0.000)
| **SEC-BERT-NUM** | [NUM] (1.000), as (0.000), fiscal (0.000), year (0.000), when (0.000)
| **SEC-BERT-SHAPE** | [XXXX] (1.000), as (0.000), year (0.000), periods (0.000), , (0.000)


| Sample                                              | Masked Token |
| --------------------------------------------------- | ------------ |
| Total net sales decreased 2% or $5.4 billion during 2019 compared to [MASK]. | 2018

| Model                                               | Predictions (Probability)  |
| --------------------------------------------------- | ------------ |
| **BERT-BASE-UNCASED** | 2017 (0.100), 2016 (0.097), above (0.054), inflation (0.050), previously (0.037)
| **SEC-BERT-BASE** | 2018 (0.999), 2019 (0.000), 2017 (0.000), 2016 (0.000), 2014 (0.000)
| **SEC-BERT-NUM** | [NUM] (1.000), year (0.000), last (0.000), sales (0.000), fiscal (0.000)
| **SEC-BERT-SHAPE** | [XXXX] (1.000), year (0.000), sales (0.000), prior (0.000), years (0.000)


| Sample                                              | Masked Token |
| --------------------------------------------------- | ------------ |
| During 2019, the Company [MASK] $67.1 billion of its common stock and paid dividend equivalents of $14.1 billion. | repurchased

| Model                                               | Predictions (Probability)  |
| --------------------------------------------------- | ------------ |
| **BERT-BASE-UNCASED** | held (0.229), sold (0.192), acquired (0.172), owned (0.052), traded (0.033)
| **SEC-BERT-BASE** | repurchased (0.913), issued (0.036), purchased (0.029), redeemed (0.010), sold (0.003)
| **SEC-BERT-NUM** | repurchased (0.917), purchased (0.054), reacquired (0.013), issued (0.005), acquired (0.003)
| **SEC-BERT-SHAPE** | repurchased (0.902), purchased (0.068), issued (0.010), reacquired (0.008), redeemed (0.006)


| Sample                                              | Masked Token |
| --------------------------------------------------- | ------------ |
| During 2019, the Company repurchased $67.1 billion of its common [MASK] and paid dividend equivalents of $14.1 billion. | stock

| Model                                               | Predictions (Probability)  |
| --------------------------------------------------- | ------------ |
| **BERT-BASE-UNCASED** | stock (0.835), assets (0.039), equity (0.025), debt (0.021), bonds (0.017)
| **SEC-BERT-BASE** | stock (0.857), shares (0.135), equity (0.004), units (0.002), securities (0.000)
| **SEC-BERT-NUM** | stock (0.842), shares (0.157), equity (0.000), securities (0.000), units (0.000)
| **SEC-BERT-SHAPE** | stock (0.888), shares (0.109), equity (0.001), securities (0.001), stocks (0.000)


| Sample                                              | Masked Token |
| --------------------------------------------------- | ------------ |
| During 2019, the Company repurchased $67.1 billion of its common stock and paid [MASK] equivalents of $14.1 billion. | dividend

| Model                                               | Predictions (Probability)  |
| --------------------------------------------------- | ------------ |
| **BERT-BASE-UNCASED** | cash (0.276), net (0.128), annual (0.083), the (0.040), debt (0.027)
| **SEC-BERT-BASE** | dividend (0.890), cash (0.018), dividends (0.016), share (0.013), tax (0.010)
| **SEC-BERT-NUM** | dividend (0.735), cash (0.115), share (0.087), tax (0.025), stock (0.013)
| **SEC-BERT-SHAPE** | dividend (0.655), cash (0.248), dividends (0.042), share (0.019), out (0.003)


| Sample                                              | Masked Token |
| --------------------------------------------------- | ------------ |
| During 2019, the Company repurchased $67.1 billion of its common stock and paid dividend [MASK] of $14.1 billion. | equivalents

| Model                                               | Predictions (Probability)  |
| --------------------------------------------------- | ------------ |
| **BERT-BASE-UNCASED** | revenue (0.085), earnings (0.078), rates (0.065), amounts (0.064), proceeds (0.062)
| **SEC-BERT-BASE** | payments (0.790), distributions (0.087), equivalents (0.068), cash (0.013), amounts (0.004)
| **SEC-BERT-NUM** | payments (0.845), equivalents (0.097), distributions (0.024), increases (0.005), dividends (0.004)
| **SEC-BERT-SHAPE** | payments (0.784), equivalents (0.093), distributions (0.043), dividends (0.015), requirements (0.009)

## Publication

<div style="text-align: justify">

If you use this model cite the following article:<br> 
[**FiNER: Financial Numeric Entity Recognition for XBRL Tagging**](https://arxiv.org/abs/2203.06482)<br>
Lefteris Loukas, Manos Fergadiotis, Ilias Chalkidis, Eirini Spyropoulou, Prodromos Malakasiotis, Ion Androutsopoulos and George Paliouras<br>
In the Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL 2022) (Long Papers), Dublin, Republic of Ireland, May 22 - 27, 2022
</div>

```
@inproceedings{loukas-etal-2022-finer,
    title = {FiNER: Financial Numeric Entity Recognition for XBRL Tagging},
    author = {Loukas, Lefteris and
      Fergadiotis, Manos and
      Chalkidis, Ilias and
      Spyropoulou, Eirini and
      Malakasiotis, Prodromos and
      Androutsopoulos, Ion and
      Paliouras George},
    booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL 2022)},
    publisher = {Association for Computational Linguistics},
    location = {Dublin, Republic of Ireland},
    year = {2022},
    url = {https://arxiv.org/abs/2203.06482}
}
```

## About Us

<div style="text-align: justify">

[AUEB's Natural Language Processing Group](http://nlp.cs.aueb.gr) develops algorithms, models, and systems that allow computers to process and generate natural language texts.

The group's current research interests include:
* question answering systems for databases, ontologies, document collections, and the Web, especially biomedical question answering,
* natural language generation from databases and ontologies, especially Semantic Web ontologies,
text classification, including filtering spam and abusive content,
* information extraction and opinion mining, including legal text analytics and sentiment analysis,
* natural language processing tools for Greek, for example parsers and named-entity recognizers,
machine learning in natural language processing, especially deep learning.

The group is part of the Information Processing Laboratory of the Department of Informatics of the Athens University of Economics and Business.
</div>

[Manos Fergadiotis](https://manosfer.github.io) on behalf of [AUEB's Natural Language Processing Group](http://nlp.cs.aueb.gr)