---
language: en
license: apache-2.0
tags:
- summarization
datasets: arxiv-summarization
---

## Introduction

A led-large-16384 model to summarize ArXiv papers. Inputs are the abstracts of papers and full documents, and outputs are the summaries of the papers.

[Allenai's Longformer Encoder-Decoder (LED)](https://github.com/allenai/longformer#longformer).

As described in [Longformer: The Long-Document Transformer](https://arxiv.org/pdf/2004.05150.pdf) by Iz Beltagy, Matthew E. Peters, Arman Cohan, 
*led-base-16384* was initialized from [*bart-base*](https://huggingface.co/facebook/bart-base) since both models share the exact same architecture. To 
be able to process 16K tokens, *bart-base*'s position embedding matrix was simply copied 16 times.
