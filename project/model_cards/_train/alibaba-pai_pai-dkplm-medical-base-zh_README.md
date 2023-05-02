---
language: zh
pipeline_tag: fill-mask
widget:
- text: "感冒需要吃[MASK]"
- text: "人类的[MASK]温是37度"
tags:
- bert
license: apache-2.0
---
## Chinese DKPLM (Decomposable Knowledge-enhanced Pre-trained Language Model) for the medical domain
For Chinese natural language processing in specific domains, we provide **Chinese DKPLM (Decomposable Knowledge-enhanced Pre-trained Language Model)** for the medical domain named **pai-dkplm-bert-zh**, from our AAAI 2021 paper named **DKPLM: Decomposable Knowledge-enhanced Pre-trained Language Model for Natural Language Understanding**.

This repository is developed based on the EasyNLP framework: [https://github.com/alibaba/EasyNLP](https://github.com/alibaba/EasyNLP ) developed by the Alibaba PAI team. Please find the DKPLM tutorial here: [DKPLM Tutorial](https://github.com/alibaba/EasyNLP/tree/master/examples/dkplm_pretraining).

## Citation
If you find the resource is useful, please cite the following papers in your work.

- For the EasyNLP framework:
```
@article{easynlp, 
title = {EasyNLP: A Comprehensive and Easy-to-use Toolkit for Natural Language Processing},   		
	publisher = {arXiv}, 
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
  publisher = {AAAI}, 
  year = {2021} 
} 
```