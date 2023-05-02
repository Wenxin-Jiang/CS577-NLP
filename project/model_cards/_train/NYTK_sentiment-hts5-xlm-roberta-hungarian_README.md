---
language:
- hu
tags:
- text-classification
license: mit
metrics:
- accuracy
widget:
- text: Jó reggelt! majd küldöm az élményhozókat :).
---

# Hungarian Sentence-level Sentiment Analysis Model with XLM-RoBERTa

For further models, scripts and details, see [our repository](https://github.com/nytud/sentiment-analysis) or [our demo site](https://juniper.nytud.hu/demo/nlp).

  - Pretrained model used: XLM-RoBERTa base
  - Finetuned on Hungarian Twitter Sentiment (HTS) Corpus
  - Labels: 0 (very negative), 1 (negative), 2 (neutral), 3 (positive), 4 (very positive)
  	
## Limitations

- max_seq_length = 128

## Results

| Model | HTS2 | HTS5 |
| ------------- | ------------- | ------------- |
| huBERT | 85.56 | **68.99**  |
| XLM-RoBERTa| 85.56 | 66.50 |

## Citation
If you use this model, please cite the following paper:

```
@inproceedings {laki-yang-sentiment,
    title = {Improving Performance of Sentence-level Sentiment Analysis with Data Augmentation Methods},
	booktitle = {Proceedings of 12th IEEE International Conference on Cognitive Infocommunications (CogInfoCom 2021)},
	year = {2021},
	publisher = {IEEE},
	address = {Online},
	author = {Laki, László and Yang, Zijian Győző}
	pages = {417--422}
}

```