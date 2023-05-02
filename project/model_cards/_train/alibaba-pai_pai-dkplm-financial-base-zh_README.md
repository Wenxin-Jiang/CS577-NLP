---
language: zh
pipeline_tag: fill-mask
widget:
- text: "根据新闻报道，三大[MASK]数午后集体涨超1％。"
- text: "用各种途径支持中小[MASK]企业融资。"
tags:
- bert
license: apache-2.0
---
## Chinese DKPLM (Decomposable Knowledge-enhanced Pre-trained Language Model) for the financial domain
For Chinese natural language processing in specific domains, we provide **Chinese DKPLM (Decomposable Knowledge-enhanced Pre-trained Language Model)** for the financial domain named **pai-dkplm-financial-base-zh**, from our AAAI 2021 paper named **DKPLM: Decomposable Knowledge-enhanced Pre-trained Language Model for Natural Language Understanding**.

This repository is developed based on the EasyNLP framework: [https://github.com/alibaba/EasyNLP](https://github.com/alibaba/EasyNLP ) developed by the Alibaba PAI team.

## Citation
If you find the resource is useful, please cite the following papers in your work.

- For the EasyNLP framework:
```
@article{easynlp, 
title = {EasyNLP: A Comprehensive and Easy-to-use Toolkit for Natural Language Processing},   			publisher = {arXiv}, 
  author = {Wang, Chengyu and Qiu, Minghui and Zhang, Taolin and Liu, Tingting and Li, Lei and Wang, Jianing and Wang, Ming and Huang, Jun and Lin, Wei}, 
  url = {https://arxiv.org/abs/2205.00258}, 
  year = {2022} 
} 
```
- For DKPLM:
```
@article{dkplm, 
  title = {DKPLM: Decomposable Knowledge-enhanced Pre-trained Language Model for Natural Language Understanding}, 
  author = {Zhang, Taolin and Wang, Chengyu and Hu, Nan and Qiu, Minghui and Tang, Chengguang and He, Xiaofeng and Huang, Jun}, 
  url = {https://arxiv.org/abs/2112.01047},   			
  publisher = {arXiv}, 
  year = {2021} 
} 
```