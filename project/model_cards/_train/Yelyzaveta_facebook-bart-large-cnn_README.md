---
language:
- en
tags:
- summarization
license: mit
thumbnail: https://huggingface.co/front/thumbnails/facebook.png
model-index:
- name: facebook/bart-large-cnn
  results:
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: cnn_dailymail
      type: cnn_dailymail
      config: 3.0.0
      split: train
    metrics:
    - name: ROUGE-1
      type: rouge
      value: 42.9486
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 20.8149
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 30.6186
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 40.0376
      verified: true
    - name: loss
      type: loss
      value: 2.529000997543335
      verified: true
    - name: gen_len
      type: gen_len
      value: 78.5866
      verified: true
---
# BART (large-sized model), fine-tuned on CNN Daily Mail 

BART model pre-trained on English language, and fine-tuned on [CNN Daily Mail](https://huggingface.co/datasets/cnn_dailymail). It was introduced in the paper [BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](https://arxiv.org/abs/1910.13461) by Lewis et al. and first released in [this repository (https://github.com/pytorch/fairseq/tree/master/examples/bart). 

Disclaimer: The team releasing BART did not write a model card for this model so this model card has been written by the Hugging Face team.

## Model description

BART is a transformer encoder-encoder (seq2seq) model with a bidirectional (BERT-like) encoder and an autoregressive (GPT-like) decoder. BART is pre-trained by (1) corrupting text with an arbitrary noising function, and (2) learning a model to reconstruct the original text.

BART is particularly effective when fine-tuned for text generation (e.g. summarization, translation) but also works well for comprehension tasks (e.g. text classification, question answering). This particular checkpoint has been fine-tuned on CNN Daily Mail, a large collection of text-summary pairs.

## Intended uses & limitations

You can use this model for text summarization. 

### How to use

Here is how to use this model with the [pipeline API](https://huggingface.co/transformers/main_classes/pipelines.html):

```python
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

ARTICLE = """ New York (CNN)When Liana Barrientos was 23 years old, she got married in Westchester County, New York.
A year later, she got married again in Westchester County, but to a different man and without divorcing her first husband.
Only 18 days after that marriage, she got hitched yet again. Then, Barrientos declared "I do" five more times, sometimes only within two weeks of each other.
In 2010, she married once more, this time in the Bronx. In an application for a marriage license, she stated it was her "first and only" marriage.
Barrientos, now 39, is facing two criminal counts of "offering a false instrument for filing in the first degree," referring to her false statements on the
2010 marriage license application, according to court documents.
Prosecutors said the marriages were part of an immigration scam.
On Friday, she pleaded not guilty at State Supreme Court in the Bronx, according to her attorney, Christopher Wright, who declined to comment further.
After leaving court, Barrientos was arrested and charged with theft of service and criminal trespass for allegedly sneaking into the New York subway through an emergency exit, said Detective
Annette Markowski, a police spokeswoman. In total, Barrientos has been married 10 times, with nine of her marriages occurring between 1999 and 2002.
All occurred either in Westchester County, Long Island, New Jersey or the Bronx. She is believed to still be married to four men, and at one time, she was married to eight men at once, prosecutors say.
Prosecutors said the immigration scam involved some of her husbands, who filed for permanent residence status shortly after the marriages.
Any divorces happened only after such filings were approved. It was unclear whether any of the men will be prosecuted.
The case was referred to the Bronx District Attorney\'s Office by Immigration and Customs Enforcement and the Department of Homeland Security\'s
Investigation Division. Seven of the men are from so-called "red-flagged" countries, including Egypt, Turkey, Georgia, Pakistan and Mali.
Her eighth husband, Rashid Rajput, was deported in 2006 to his native Pakistan after an investigation by the Joint Terrorism Task Force.
If convicted, Barrientos faces up to four years in prison.  Her next court appearance is scheduled for May 18.
"""
print(summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False))
>>> [{'summary_text': 'Liana Barrientos, 39, is charged with two counts of "offering a false instrument for filing in the first degree" In total, she has been married 10 times, with nine of her marriages occurring between 1999 and 2002. She is believed to still be married to four men.'}]
```

### BibTeX entry and citation info

```bibtex
@article{DBLP:journals/corr/abs-1910-13461,
  author    = {Mike Lewis and
               Yinhan Liu and
               Naman Goyal and
               Marjan Ghazvininejad and
               Abdelrahman Mohamed and
               Omer Levy and
               Veselin Stoyanov and
               Luke Zettlemoyer},
  title     = {{BART:} Denoising Sequence-to-Sequence Pre-training for Natural Language
               Generation, Translation, and Comprehension},
  journal   = {CoRR},
  volume    = {abs/1910.13461},
  year      = {2019},
  url       = {http://arxiv.org/abs/1910.13461},
  eprinttype = {arXiv},
  eprint    = {1910.13461},
  timestamp = {Thu, 31 Oct 2019 14:02:26 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1910-13461.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}