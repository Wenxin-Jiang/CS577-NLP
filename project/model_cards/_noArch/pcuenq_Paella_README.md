---
title: Paella
emoji: 🥘
language:
- en
tags:
- text-to-image
- endpoints-template
license: mit
---

Paella is a novel text-to-image model that uses a compressed quantized latent space, based on a f8 VQGAN, and a masked training objective to achieve fast generation in ~10 inference steps.

* [Paper](https://arxiv.org/abs/2211.07292)
* [Official implementation](https://github.com/dome272/Paella)

Biases and content acknowledgment

Despite how impressive being able to turn text into image is, beware to the fact that this model may output content that reinforces or exacerbates societal biases, as well as realistic faces, pornography and violence. The model was trained on 600 million images from the improved <a href="https://laion.ai/blog/laion-5b/" style="text-decoration: underline;" target="_blank">LAION-5B aesthetic</a> dataset, which scraped non-curated image-text-pairs from the internet (the exception being the removal of illegal content) and is meant for research purposes.

