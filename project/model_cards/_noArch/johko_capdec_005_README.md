---
license: apache-2.0
language:
- en
pipeline_tag: image-to-text
datasets:
- MS-COCO
- Flickr30k
tags:
- Image Captioning
---

# CapDec - NoiseLevel: 0.005

## Model Description

These are model weights originally provided by the authors of the paper [Text-Only Training for Image Captioning using Noise-Injected CLIP](https://arxiv.org/pdf/2211.00575.pdf).

Their method aims to train CLIP with only text samples. Therefore they are injecting zero-mean Gaussian Noise into the text embeddings before decoding.

In their words:
*Specifically, we assume that the visual embedding corresponding to a text embedding 
lies somewhere within a ball of small radius around the text embedding (see Fig. 1). 
We would like all text embeddings in this ball to decode to the same caption,which should 
also correspond to the visual content mapped to this ball. We implement this intuition by 
adding zero-mean Gaussian noise of STD to the text embedding before decoding it.*

The "Noise Level" of 0.005 is equivalent to the Noise Variance which is the square of the STD.

The reported metrics are results of a model with a Noise Variance of 0.016, which the authors unfortunately do not provide in their repository. 

## Datasets
The authors trained the model on MS-COCO and Flickr30k datasets.

## Performance
The authors don't explicitly report the performance for this NoiseLevel but it can be estimated from the following figure from the original paper:
![](capdec_performance.png)