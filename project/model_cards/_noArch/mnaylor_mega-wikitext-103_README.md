---
license: mit
datasets:
- wikitext
language:
- en
pipeline_tag: fill-mask
---

**NOTE: THIS MODEL IS NOT INTEGRATED WITH HUGGING FACE**. Please use the version of this model converted to the newly implemented `Mega` 
architecture in `transformers` ([link](https://huggingface.co/mnaylor/mega-base-wikitext))

# Moving Average Gated Attention (Mega): Pretrained LM

This repo contains pretrained weights for a language model with the Mega architecture (see [paper](https://arxiv.org/abs/2209.10655)). 
I used the Mega source code (namely the `MegaEncoderLayer` class) and created wrappers for token embeddings and MLM prediction. This model
was pretrained for 5 epochs (11.3k gradient steps) on wikitext-103, which took roughly 5 hours on a single T4 (in Colab's free tier).

See [the Colab notebook](https://colab.research.google.com/drive/1qfUO6o5HRdxBblWlw058HVyvaEPhPpH8?usp=sharing) 
for further training details. In order to load the pretrained weights for this model, you'll need to use the 
[Mega repo](https://github.com/facebookresearch/mega) along with the example code at the end of the Colab notebook.