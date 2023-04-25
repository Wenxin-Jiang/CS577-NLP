---
language: en
tags:
- summarization
license: apache-2.0
datasets:
- cnn_dailymail
- xsum
thumbnail: https://huggingface.co/front/thumbnails/distilbart_medium.png
---

# This is an Tensorflow fork of [sshleifer/distilbart-cnn-12-6](https://huggingface.co/sshleifer/distilbart-cnn-12-6)

### Usage

This checkpoint should be loaded into `BartForConditionalGeneration.from_pretrained`. See the [BART docs](https://huggingface.co/transformers/model_doc/bart.html?#transformers.BartForConditionalGeneration) for more information.

### Metrics for DistilBART models

| Model Name                 |   MM Params |   Inference Time (MS) |   Speedup |   Rouge 2 |   Rouge-L |
|:---------------------------|------------:|----------------------:|----------:|----------:|----------:|
| distilbart-xsum-12-1       |         222 |                    90 |      2.54 |     18.31 |     33.37 |
| distilbart-xsum-6-6        |         230 |                   132 |      1.73 |     20.92 |     35.73 |
| distilbart-xsum-12-3       |         255 |                   106 |      2.16 |     21.37 |     36.39 |
| distilbart-xsum-9-6        |         268 |                   136 |      1.68 |     21.72 |     36.61 |
| bart-large-xsum (baseline) |         406 |                   229 |      1    |     21.85 |     36.50 |
| distilbart-xsum-12-6       |         306 |                   137 |      1.68 |     22.12 |     36.99 |
| bart-large-cnn (baseline)  |         406 |                   381 |      1    |     21.06 |     30.63 |
| distilbart-12-3-cnn        |         255 |                   214 |      1.78 |     20.57 |     30.00 |
| distilbart-12-6-cnn        |         306 |                   307 |      1.24 |     21.26 |     30.59 |
| distilbart-6-6-cnn         |         230 |                   182 |      2.09 |     20.17 |     29.70 |