---
language: en
license: apache-2.0
---

## Introduction

[Allenai's Longformer Encoder-Decoder (LED)](https://github.com/allenai/longformer#longformer).

As described in [Longformer: The Long-Document Transformer](https://arxiv.org/pdf/2004.05150.pdf) by Iz Beltagy, Matthew E. Peters, Arman Cohan, *led-large-16384* was initialized from [*bart-large*](https://huggingface.co/facebook/bart-large) since both models share the exact same architecture. To be able to process 16K tokens, *bart-large*'s position embedding matrix was simply copied 16 times.

This model is especially interesting for long-range summarization and question answering.

## Fine-tuning for down-stream task

[This notebook](https://colab.research.google.com/drive/12LjJazBl7Gam0XBPy_y0CTOJZeZ34c2v?usp=sharing) shows how *led-large-16384* can effectively be fine-tuned on a downstream task.

