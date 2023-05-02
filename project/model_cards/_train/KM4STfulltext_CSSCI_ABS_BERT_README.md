---
license: apache-2.0
---
# Pre-trained Language Model for the Humanities and Social Sciences in Chinese 

## Introduction

The research for social science texts in Chinese needs the support natural language processing tools. 

The pre-trained language model has greatly improved the accuracy of text mining in general texts. At present, there is an urgent need for a pre-trained language model specifically for the automatic processing of scientific texts in Chinese social science. 

We used the abstract of social science research as the training set. Based on the deep language model framework of BERT, we constructed CSSCI_ABS_BERT, CSSCI_ABS_roberta and CSSCI_ABS_roberta-wwm  pre-training language models by [transformers/run_mlm.py](https://github.com/huggingface/transformers/blob/main/examples/pytorch/language-modeling/run_mlm.py) and [transformers/mlm_wwm](https://github.com/huggingface/transformers/tree/main/examples/research_projects/mlm_wwm). 

We designed four downstream tasks of  Text Classification on different Chinese social scientific article corpus to verify the performance of the model.

- CSSCI_ABS_BERT , CSSCI_ABS_roberta and CSSCI_ABS_roberta-wwm are trained on the abstract of  articles published in CSSCI journals. The training set involved in the experiment included a total of `510,956,094 words`. 
- Based on the idea of Domain-Adaptive Pretraining, `CSSCI_ABS_BERT` and `CSSCI_ABS_roberta` combine a large amount of abstracts of scientific articles in Chinese  based on the BERT structure, and continue to train the BERT and Chinese-RoBERTa models respectively to obtain pre-training models for the automatic processing of Chinese Social science research texts. 



## News 

- 2022-06-15 : CSSCI_ABS_BERT, CSSCI_ABS_roberta and CSSCI_ABS_roberta-wwm has been put forward for the first time.



##  How to use

### Huggingface Transformers 

The `from_pretrained` method based on [Huggingface Transformers](https://github.com/huggingface/transformers) can directly obtain CSSCI_ABS_BERT, CSSCI_ABS_roberta and CSSCI_ABS_roberta-wwm models online. 



- CSSCI_ABS_BERT

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("KM4STfulltext/CSSCI_ABS_BERT")

model = AutoModel.from_pretrained("KM4STfulltext/CSSCI_ABS_BERT")
```

- CSSCI_ABS_roberta

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("KM4STfulltext/CSSCI_ABS_roberta")

model = AutoModel.from_pretrained("KM4STfulltext/CSSCI_ABS_roberta")
```

- CSSCI_ABS_roberta-wwm

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("KM4STfulltext/CSSCI_ABS_roberta_wwm")

model = AutoModel.from_pretrained("KM4STfulltext/CSSCI_ABS_roberta_wwm")
```

### Download Models

- The version of the model we provide is `PyTorch`. 

### From Huggingface 

- Download directly through Huggingface's official website. 
- [KM4STfulltext/CSSCI_ABS_BERT](https://huggingface.co/KM4STfulltext/CSSCI_ABS_BERT)
- [KM4STfulltext/CSSCI_ABS_roberta](https://huggingface.co/KM4STfulltext/CSSCI_ABS_roberta)
- [KM4STfulltext/CSSCI_ABS_roberta_wwm](https://huggingface.co/KM4STfulltext/CSSCI_ABS_roberta_wwm)

##  Evaluation & Results

- We useCSSCI_ABS_BERT, CSSCI_ABS_roberta and CSSCI_ABS_roberta-wwm to perform Text Classificationon different social science research corpus. The experimental results are as follows. 

#### Discipline classification experiments of articles published in CSSCI journals

https://github.com/S-T-Full-Text-Knowledge-Mining/CSSCI-BERT


#### Movement recognition experiments for data analysis and knowledge discovery abstract

| Tag          | bert-base-Chinese | chinese-roberta-wwm,ext | CSSCI_ABS_BERT | CSSCI_ABS_roberta | CSSCI_ABS_roberta_wwm | support |
| ------------ | ----------------- | ----------------------- | -------------- | ----------------- | --------------------- | ------- |
| Abstract     | 55.23             | 62.44                   | 56.8           | 57.96             | 58.26                 | 223     |
| Location     | 61.61             | 54.38                   | 61.83          | 61.4              | 61.94                 | 2866    |
| Metric       | 45.08             | 41                      | 45.27          | 46.74             | 47.13                 | 622     |
| Organization | 46.85             | 35.29                   | 45.72          | 45.44             | 44.65                 | 327     |
| Person       | 88.66             | 82.79                   | 88.21          | 88.29             | 88.51                 | 4850    |
| Thing        | 71.68             | 65.34                   | 71.88          | 71.68             | 71.81                 | 5993    |
| Time         | 65.35             | 60.38                   | 64.15          | 65.26             | 66.03                 | 1272    |
| avg          | 72.69             | 66.62                   | 72.59          | 72.61             | 72.89                 | 16153   |

#### Chinese literary entity recognition

| Tag          | bert-base-Chinese | chinese-roberta-wwm,ext | CSSCI_ABS_BERT | CSSCI_ABS_roberta | CSSCI_ABS_roberta_wwm | support |
| ------------ | ----------------- | ----------------------- | -------------- | ----------------- | --------------------- | ------- |
| Abstract     | 55.23             | 62.44                   | 56.8           | 57.96             | 58.26                 | 223     |
| Location     | 61.61             | 54.38                   | 61.83          | 61.4              | 61.94                 | 2866    |
| Metric       | 45.08             | 41                      | 45.27          | 46.74             | 47.13                 | 622     |
| Organization | 46.85             | 35.29                   | 45.72          | 45.44             | 44.65                 | 327     |
| Person       | 88.66             | 82.79                   | 88.21          | 88.29             | 88.51                 | 4850    |
| Thing        | 71.68             | 65.34                   | 71.88          | 71.68             | 71.81                 | 5993    |
| Time         | 65.35             | 60.38                   | 64.15          | 65.26             | 66.03                 | 1272    |
| avg          | 72.69             | 66.62                   | 72.59          | 72.61             | 72.89                 | 16153   |

## Cited

- If our content is helpful for your research work, please quote our research in your article. 
- If you want to quote our research, you can use this url [S-T-Full-Text-Knowledge-Mining/CSSCI-BERT (github.com)](https://github.com/S-T-Full-Text-Knowledge-Mining/CSSCI-BERT) as an alternative before our paper is published.

## Disclaimer

- The experimental results presented in the report only show the performance under a specific data set and hyperparameter combination, and cannot represent the essence of each model. The experimental results may change due to random number seeds and computing equipment. 
- **Users can use the model arbitrarily within the scope of the license, but we are not responsible for the direct or indirect losses caused by using the content of the project.** 


##  Acknowledgment

- CSSCI_ABS_BERT was trained based on [BERT-Base-Chinese]([google-research/bert: TensorFlow code and pre-trained models for BERT (github.com)](https://github.com/google-research/bert)).
- CSSCI_ABS_roberta and CSSCI_ABS_roberta-wwm was trained based on [RoBERTa-wwm-ext, Chinese]([ymcui/Chinese-BERT-wwm: Pre-Training with Whole Word Masking for Chinese BERT（中文BERT-wwm系列模型） (github.com)](https://github.com/ymcui/Chinese-BERT-wwm)).
