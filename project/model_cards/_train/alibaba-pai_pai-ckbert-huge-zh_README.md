---
language: zh
pipeline_tag: fill-mask
widget:
- text: "巴黎是[MASK]国的首都。"
- text: "生活的真谛是[MASK]。"
tags:
- bert
license: apache-2.0
---
## Chinese Kowledge-enhanced BERT (CKBERT) 

Knowledge-enhanced pre-trained language models (KEPLMs) improve context-aware representations via learning from structured relations in knowledge graphs, and/or linguistic knowledge from syntactic or dependency analysis. Unlike English, there is a lack of high-performing open-source Chinese KEPLMs in the natural language processing (NLP) community to support various language understanding applications.

For Chinese natural language processing, we provide three **Chinese Kowledge-enhanced BERT (CKBERT)** models named **pai-ckbert-bert-zh**, **pai-ckbert-large-zh** and **pai-ckbert-huge-zh**, from our **EMNLP 2022** paper named **Revisiting and Advancing Chinese Natural Language Understanding with Accelerated Heterogeneous Knowledge Pre-training**.

This repository is developed based on the EasyNLP framework: [https://github.com/alibaba/EasyNLP](https://github.com/alibaba/EasyNLP ) 

## Citation
If you find the resource is useful, please cite the following papers in your work.

- For the EasyNLP framework:
```
@article{easynlp, 
title = {EasyNLP: A Comprehensive and Easy-to-use Toolkit for Natural Language Processing},   		
  author = {Wang, Chengyu and Qiu, Minghui and Zhang, Taolin and Liu, Tingting and Li, Lei and Wang, Jianing and Wang, Ming and Huang, Jun and Lin, Wei}, 
  publisher = {arXiv}, 
  url = {https://arxiv.org/abs/2205.00258}, 
  year = {2022} 
} 
```
- For CKBERT:
```
@article{ckbert, 
  title = {Revisiting and Advancing Chinese Natural Language Understanding with Accelerated Heterogeneous Knowledge Pre-training}, 
  author = {Zhang, Taolin and Dong, Junwei and Wang, Jianing and Wang, Chengyu and Wang, An and Liu, Yinghui and Huang, Jun and Li, Yong and He, Xiaofeng}, 	
  publisher = {EMNLP}, 
  url = {https://arxiv.org/abs/2210.05287}, 
  year = {2022} 
} 
```