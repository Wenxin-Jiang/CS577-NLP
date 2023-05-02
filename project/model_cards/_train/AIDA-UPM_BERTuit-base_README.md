---
pipeline_tag: fill-mask
tags:
- online social networks
- twitter
- spanish
language: es
license: apache-2.0
widget:
- text: "Las <mask> causan hipoxia."
  example_title: "Mask filling"
---

Model BERTuit as presented in the [BERTuit: Understanding Spanish language in Twitter through a native transformer](https://arxiv.org/abs/2204.03465) article.

Before tokenization replace user tags and urls with "\<usr\>" and "\<url\>" respectively.

Tokenize text with base class RoBERTaTokenizer.