---
language: en
tags:
- newspapers
- library
- historic
- glam
- mdma
license: mit
metrics:
- pseudo-perplexity
widget:
- text: "[1820] [SEP] We received a letter from [MASK] Majesty."
- text: "[1850] [SEP] We received a letter from [MASK] Majesty."
- text: "[MASK] [SEP] The Franco-Prussian war is a matter of great concern."
- text: "[MASK] [SEP] The Schleswig war is a matter of great concern."

---
**MODEL CARD UNDER CONSTRUCTION, ETA END OF NOVEMBER**

<img src="https://upload.wikimedia.org/wikipedia/commons/5/5b/NCI_peas_in_pod.jpg" alt="erwt" width="200" >

# ERWT-year-st

🌺ERWT\* a language model that (🤭 maybe 🤫) knows more about history than you...🌺

ERWT is a fine-tuned [`distilbert-base-uncased`](https://huggingface.co/distilbert-base-uncased) model trained on historical newspapers from the [Heritage Made Digital collection](https://huggingface.co/datasets/davanstrien/hmd-erwt-training).

 We trained a model based on a combination of text and **temporal metadata** (i.e. year information).

ERWT performs [**time-sensitive masked language modelling**](#historical-language-change-herhis-majesty-%F0%9F%91%91) or [**date prediction**]((#date-prediction-pub-quiz-with-lms-%F0%9F%8D%BB)).

This model is served by [Kaspar von Beelen](https://huggingface.co/Kaspar) and [Daniel van Strien](https://huggingface.co/davanstrien), *"Improving AI, one pea at a time"*.

If these models happen to be useful, please cite our working paper.

```
@misc{https://doi.org/10.48550/arxiv.2211.10086,
  doi = {10.48550/ARXIV.2211.10086},
  url = {https://arxiv.org/abs/2211.10086},
  author = {Beelen, Kaspar and van Strien, Daniel},
  keywords = {Computation and Language (cs.CL), Digital Libraries (cs.DL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Metadata Might Make Language Models Better},
  publisher = {arXiv},
  year = {2022},
  copyright = {Creative Commons Attribution 4.0 International}}
```

\*ERWT is dutch for PEA.

# Overview

- [Introduction: Repent Now 😇](#introductory-note-repent-now-%F0%9F%98%87)
- [Background: MDMA to the rescue 🙂](#background-mdma-to-the-rescue-%F0%9F%99%82)
- [Intended Use: LMs as History Machines 🚂](#intended-use-lms-as-history-machines)
   - [Historical Language Change: Her/His Majesty? 👑](#historical-language-change-herhis-majesty-%F0%9F%91%91)
   - [Date Prediction: Pub Quiz with LMs 🍻](#date-prediction-pub-quiz-with-lms-%F0%9F%8D%BB)
- [Limitations: Not all is well 😮](#limitations-not-all-is-well-%F0%9F%98%AE)
    - [Training Data](#training-data)
    - [Training Routine](#training-routine)
- [Data Description](#data-description)
- [Evaluation: 🤓 In case you care to count 🤓](#evaluation-%F0%9F%A4%93-in-case-you-care-to-count-%F0%9F%A4%93)
 
   

## Introductory Note: Repent Now. 😇

The ERWT models are trained for **experimental purposes**. 

Please consult the [**limitations**](#limitations-not-all-is-well-%F0%9F%98%AE) section (seriously before using the models. Seriously, read this section, **we don't repent in public just for fun**). 

If you can't get enough of these neural peas and crave some more. In that case, you can consult our working paper ["Metadata Might Make Language Models Better"](https://arxiv.org/abs/2211.10086) for more background information and nerdy evaluation stuff (work in progress, handle with care and kindness).

## Background: MDMA to the rescue. 🙂

ERWT was created using a **M**eta**D**ata **M**asking **A**pproach (or **MDMA** 💊), a scenario in which we train a Masked Language Model (MLM) on text and metadata simultaneously. Our intuition was that incorporating metadata (information that *describes* a text but and is not part of the content) may make language models "better", or at least make them more **sensitive** to historical, political and geographical aspects of language use. We mainly use temporal, political and geographical metadata.

ERWT is a [`distilbert-base-uncased`](https://huggingface.co/distilbert-base-uncased) model, fine-tuned on a random subsample taken from the [Heritage Made Digital newspaper collection]((https://huggingface.co/datasets/davanstrien/hmd-erwt-training)). The training data comprises around half a billion words. 

To unleash the power of MDMA, we adapted to the training routine mainly by fidgeting with the input data. 

When preprocessing the text, we prepended each segment of hundred words with a time stamp (year of publication) and a special `[DATE]` token. 


The snippet below, taken from the [Londonderry Sentinel]:(https://www.britishnewspaperarchive.co.uk/viewer/bl/0001480/18700722/014/0002)...
```
Every scrap of intelligence relative to the war between France and Prussia is now read with interest.
```
 
... would be formatted as:
      
```python
"1870 [DATE] Every scrap of intelligence relative to the war between France and Prussia is now read with interest."
```

These text chunks are then forwarded to the data collator and eventually the language model.

Exposed to the tokens and (temporal) metadata, the model learns a relation between text and time. When a text token is hidden, the prepended `year` field influences the prediction of the masked words. Vice versa, when the prepended metadata is hidden, the model predicts the year of publication based on the content.

## Intended Use: LMs as History Machines.

Exposing the model to temporal metadata allows us to investigate **historical language change** and perform **date prediction**.

### Historical Language Change: Her/His Majesty? 👑

Let's show how ERWT works with a very concrete example. 

The ERWT models are trained on a handful of British newspapers published between 1800 and 1870. It can be used to monitor historical change in this specific context.

Imagine you are confronted with the following snippet: "We received a letter from [MASK] Majesty" and want to predict the correct pronoun for the masked token (again assuming a British context). 

👩‍🏫 **History Intermezzo** Please remember, for most of the nineteenth century, Queen Victoria ruled Britain, from 1837 to 1901 to be precise. Her nineteenth-century predecessors (George III, George IV and William IV) were all male.

While a standard language model will provide you with one a general prediction—based on what it has observed during training–ERWT allows you to manipulate to prediction, by anchoring the text in a specific year.

Doing this requires just a few lines of code:

```python
from transformers import pipeline

mask_filler = pipeline("fill-mask",
                       model='Livingwithmachines/erwt-year-st')

mask_filler(f"1820 [DATE] We received a letter from [MASK] Majesty.")
```

This returns "his" as the most likely filler:

```python
{'score': 0.8527863025665283,
  'token': 2010,
  'token_str': 'his',
  'sequence': '1820 we received a letter from his majesty.'}
```

However, if we change the date at the start of the sentence to 1850:

```python
mask_filler(f"1850 [DATE] We received a letter from [MASK] Majesty.")
```

ERWT puts most of the probability mass on the token "her" and only a little bit on "his".

```python
{'score': 0.8168327212333679,
  'token': 2014,
  'token_str': 'her',
  'sequence': '1850 we received a letter from her majesty.'}
```

You can repeat this experiment for yourself using the example sentences in the **Hosted inference API** at the top right.

Okay, but why is this **interesting**? 

Firstly, eyeballing some toy examples (but also using more rigorous metrics such as [perplexity](#evaluation-%F0%9F%A4%93-in-case-you-care-to-count-%F0%9F%A4%93)) shows that MLMs yield more accurate predictions when they have access to temporal metadata. 

In other words, **ERWT models are better at capturing historical context.**

Secondly, MDMA may **reduce biases** that arise from imbalanced training data (or at least give us more of a handle on this problem). Admittedly, we have to prove this more formally, but some experiments at least hint in this direction.

### Date Prediction: Pub Quiz with LMs 🍻

Another feature of ERWT is **date prediction**. Remember that during training the temporal metadata token is regularly masked. In this case, the model effectively learns to situate documents in time based on the tokens in a text.

By masking the year token at the beginning of the text string, ERWT guesses the document's year of publication.

👩‍🏫 **History Intermezzo** To unite the German states (there used to be [plenty](https://www.britannica.com/topic/German-Confederation)!), Prussia fought a number of wars with its neighbours in the second half of the nineteenth century. It invaded Denmark in 1864 (the second of the Schleswig Wars) and France in 1870 (the Franco-Prussian war). 

Reusing to code above, we can time-stamp documents by masking the year. For example, the line of python code below:

```python
mask_filler("[MASK] [DATE] The Schleswig war is a matter of great concern.")

```

Outputs as most likely filler:

```python
{'score': 0.48822104930877686,
  'token': 6717,
  'token_str': '1864',
  'sequence': '1864 the schleswig war is a matter of great concern.'}

```


The prediction "1864" makes sense; this was indeed the year of Prussian troops (with some help of their Austrian friends) crossed the border into Schleswig, then part of the Kingdom of Denmark.

A few years later, in 1870, Prussia aimed its artillery and bayonets southwards and invaded France. 

```python
mask_filler("[MASK] [DATE] The Franco-Prussian war is a matter of great concern.")
```

ERWT clearly learned a lot about the history of German unification by ploughing through a plethora of nineteenth-century newspaper articles: it correctly returns "1870" as the predicted year for the Franco-Prussian war!

Again, we have to ask: Who cares? Wikipedia can tell us pretty much the same. More importantly, don't we already have timestamps for newspaper data?

In both cases, our answer sounds "yes, but...". ERWT's time-stamping powers have little instrumental use and won't make us rich (but donations are welcome of course 🤑). Nonetheless, we believe date prediction has value for research purposes. We can use ERWT for "fictitious" prediction, i.e. as a diagnostic tool. 

Firstly, we used date prediction for evaluation purposes, to measure which training routine produces models that best capture the year of publication from a set of tokens.

Secondly, we could use date prediction as an analytical or research tool, and study, for example, temporal variation **within** text documents; or scrutinise which features drive the time prediction (it goes without saying that the same applies to other metadata fields, like political orientation).

## Limitations: Not all is well 😮.

The ERWT series were trained for evaluation purposes and therefore carry some critical limitations. 

### Training Data

Many of the limitations are a direct result of the training data. ERWT models are trained on a rather small subsample of nineteenth-century **British newspapers**, and its predictions have to be understood in this context (remember, "Her Majesty?"). The corpus has a strong **Metropolitan and liberal bias** (see the section on Data Description for more information). 

The training data spans from **1800 to 1870**. If your research interest is outside of this period, it's unlikely that ERWT will be of much use. Don't ask the poor model to predict when the Second World War happened. ERWT can be smart (at times) but it doesn't have the power of fortune-telling. At least not yet...

Furthermore, historical models tend to reflect past (and present?) stereotypes and prejudices. We strongly advise against using these models outside of a research context. The predictions are likely to exhibit harmful biases, they should be investigated critically and understood within the context of nineteenth-century British cultural history.

One way of evaluating a model's bias is to gauge the impact of changing a prompt on the predicted [MASK] token. Often a comparison is made between the predictions given for 'The **man** worked as a [MASK]' to 'The **woman** worked as a [MASK]'. 

An example of the output for this model:

```
1810 [DATE] The man worked as a [MASK].
```

Produces the following three top predicted mask tokens

```python
[
  {
    "score": 0.17358914017677307,
    "token": 10533,
    "token_str": "carpenter",
  },
  {
    "score": 0.08387620747089386,
    "token": 22701,
    "token_str": "tailor",
  },
  {
    "score": 0.068501777946949,
    "token": 6243,
    "token_str": "baker",
  }
]
```

```
1810 [DATE] The woman worked as a [MASK].
```

Produces the following three top predicted mask tokens

```python
[
  {
    "score": 0.148710235953331,
    "token": 7947,
    "token_str": "servant",
  },
  {
    "score": 0.07184035331010818,
    "token": 6243,
    "token_str": "baker",
  },
  {
    "score": 0.0675836056470871,
    "token": 6821,
    "token_str": "nurse",
  },
]
```

Mostly, prompt evaluation is done to assess the bias in *contemporary* language models. In the case of historic language models, the bias exhibited by a model *may* be a valuable research tool in assessing (at scale) language use over time, and the stereotypes and prejudices encoded in text corpora. 

For this particular prompt, the 'bias' exhibited by the language model (and the underlying data) may be a relatively accurate reflection of employment patterns during the 19th century. A possible area of exploration is to see how these predictions change when the model is prompted with different dates. With a dataset covering a more extended time period, we may expect to see a decline in the [MASK] `servant` toward the end of the 19th Century and particularly following the start of the First World War when the number of domestic servants employed in the United Kingdom fell rapidly. 

### Training Routine

We created various ERWT models as part of a wider experiment that aimed to establish best practices and guidelines for training models with metadata. An overview of all the models is available on our [GitHub](https://github.com/Living-with-machines/ERWT/) page.

To reduce training time, we based our experiments on a random subsample of the HMD corpus, consisting of half a billion tokens. 
Furthermore, we only trained the models for one epoch, which implies they are most likely **undertrained** at the moment. 

We were mainly interested in the **relative** performance of the different ERWT models. We did, however, compared ERWT with [`distilbert-base-uncased`](https://huggingface.co/distilbert-base-uncased) in our evaluation experiments. And, of course, our tiny LM peas 
did much better. 🎉🥳 

Want to know the details—Oh, critical reader!—then consult and cite [our working paper](https://arxiv.org/abs/2211.10086)!

## Data Description

The ERWT models are trained on an openly accessible newspaper corpus created by the [Heritage Made Digital (HMD) newspaper digitisation project](footnote{https://blogs.bl.uk/thenewsroom/2019/01/heritage-made-digital-the-newspapers.html).
The HMD newspapers comprise around 2 billion words in total, but the bulk of the articles originate from the (then) liberal paper *The Sun*. 
Geographically, most papers are metropolitan (i.e. based in London). The inclusion of *The Northern Daily Times* and *Liverpool Standard*, adds some geographical diversity to this corpus. The political classification is based on historical newspaper press directories, please read [our paper](https://academic.oup.com/dsh/advance-article/doi/10.1093/llc/fqac037/6644524?searchresult=1) on bias in newspaper collections for more information. 

The table below contains a more detailed overview of the corpus.

|      |                          |              |           |               |
|------|--------------------------|--------------|-----------|---------------|
| NLP  | Title                    | Politics     | Location  | Tokens        |
| 2083 | The Northern Daily Times | NEUTRAL      | LIVERPOOL | 14.094.212    |
| 2084 | The Northern Daily Times | NEUTRAL      | LIVERPOOL | 34.450.366    |
| 2085 | The Northern Daily Times | NEUTRAL      | LIVERPOOL | 16.166.627    |
| 2088 | The Liverpool Standard   | CONSERVATIVE | LIVERPOOL | 149.204.800   |
| 2090 | The Liverpool Standard   | CONSERVATIVE | LIVERPOOL | 6.417.320     |
| 2194 | The Sun                  | LIBERAL      | LONDON    | 1.155.791.480 |
| 2244 | Colored News             | NONE         | LONDON    | 53.634        |
| 2642 | The Express              | LIBERAL      | LONDON    | 236.240.555   |
| 2644 | National Register        | CONSERVATIVE | LONDON    | 23.409.733    |
| 2645 | The Press                | CONSERVATIVE | LONDON    | 15.702.276    |
| 2646 | The Star                 | NONE         | LONDON    | 163.072.742   |
| 2647 | The Statesman            | RADICAL      | LONDON    | 61.225.215    |


Temporally, most of the articles date from the second half of the nineteenth century. The figure below gives an overview of the number of articles by year.

![number of article by year](https://github.com/Living-with-machines/ERWT/raw/main/articles_by_year.png)

## Evaluation: 🤓 In case you care to count 🤓

Our article ["Metadata Might Make Language Models Better"](https://arxiv.org/abs/2211.10086) comprises an extensive evaluation of all the MDMA-infused language models. 

The table below shows the [pseudo-perplexity](https://arxiv.org/abs/1910.14659) scores for different models based on text documents of 64 and 128 tokens.

In general, [ERWT-year-masked-25](https://huggingface.co/Livingwithmachines/erwt-year-masked-25) turned out to yield the most competitive scores across different tasks and we generally recommend you use this model. 


| text length         | 64             |        | 128            |        |
|------------------|----------------|--------|----------------|--------|
| model         | mean           | sd     | mean           | sd     |
| DistilBERT       | 354.40         | 376.32 | 229.19         | 294.70 |
| HMDistilBERT     | 32.94          | 64.78  | 25.72          | 45.99  |
| ERWT-year             | 31.49          | 61.85  | 24.97          | 44.58  |
| ERWT-st         | 31.69          | 62.42  | 25.03          | 44.74  |
| ERWT-year-masked-25 | **30.97** | 61.50  | **24.59** | 44.36  |
| ERWT-year-masked-75 | 31.02          | 61.41  | 24.63          | 44.40  |
| PEA              | 31.63          | 62.09  | 25.58          | 44.99  |
| PEA-st          | 31.65          | 62.19  | 25.59          | 44.99  |


## Questions?

Questions? Feedback? Please leave a message!


