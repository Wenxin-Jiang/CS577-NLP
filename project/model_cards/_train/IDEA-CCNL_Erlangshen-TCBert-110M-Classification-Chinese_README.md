---
language: 
  - zh

license: apache-2.0

tags:
  - classification

inference: false

---

# Erlangshen-TCBert-110M-Classification-Chinese

- Github: [Fengshenbang-LM](https://github.com/IDEA-CCNL/Fengshenbang-LM)
- Docs: [Fengshenbang-Docs](https://fengshenbang-doc.readthedocs.io/)

## 简介 Brief Introduction

110M参数的Topic Classification BERT (TCBert)。

The TCBert with 110M parameters is pre-trained for, not limited to, Chinese topic classification tasks.

## 模型分类 Model Taxonomy

|  需求 Demand  | 任务 Task       | 系列 Series      | 模型 Model    | 参数 Parameter | 额外 Extra |
|  :----:  | :----:  | :----:  | :----:  | :----:  | :----:  |
| 通用 General  | 自然语言理解 NLU | 二郎神 Erlangshen | TCBert      |      110M     |   Chinese     |

## 模型信息 Model Information


为了提高模型在话题分类上的效果，我们收集了大量话题分类数据进行基于prompts的预训练。

To improve the model performance on the topic classification task, we collected numerous topic classification datasets for pre-training based on general prompts.
### 下游效果 Performance

我们为每个数据集设计了两个prompt模板。
We customize two prompts templates for each dataset.

第一个prompt模板：
For ***prompt template 1***:
| Dataset |     Prompt template 1    |
|---------|:------------------------:|
| TNEWS   | 下面是一则关于__的新闻： |
| CSLDCP  | 这一句描述__的内容如下： |
| IFLYTEK | 这一句描述__的内容如下： |

第一个prompt模板的微调实验结果：
The **fine-tuning** results for prompt template 1:
| Model           |  TNEWS | CLSDCP | IFLYTEK |
|-----------------|:------:|:------:|:-------:|
| Macbert-base    | 55.02  | 57.37  |  51.34  |
| Macbert-large   | 55.77  | 58.99  |  50.31  |
| Erlangshen-1.3B | 57.36  | 62.35  |  53.23  |
| TCBert-base<sub>110M-Classification-Chinese     | 55.57  | 58.60  |  49.63  |
| TCBert-large<sub>330M-Classification-Chinese    | 56.17  | 60.06  |  51.34  |
| TCBert-1.3B<sub>1.3B-Classification-Chinese     | 57.41  | 65.10  |  53.75  |
| TCBert-base<sub>110M-Sentence-Embedding-Chinese     | 54.68  | 59.78  |  49.40  |
| TCBert-large<sub>330M-Sentence-Embedding-Chinese    | 55.32  | 62.07  |  51.11  |
| TCBert-1.3B<sub>1.3B-Sentence-Embedding-Chinese     | 57.46  | 65.04  |  53.06  |


第一个prompt模板的句子相似度结果：

The **sentence similarity** results for prompt template 1:

|                 |   TNEWS  |           |   CSLDCP  |           |  IFLYTEK  |           |
|-----------------|:--------:|:---------:|:---------:|:---------:|:---------:|:---------:|
| Model           | referece | whitening | reference | whitening | reference | whitening |
| Macbert-base    |  43.53   |   47.16   |   33.50   |   36.53   |   28.99   |   33.85   |
| Macbert-large   |  46.17   |   49.35   |   37.65   |   39.38   |   32.36   |   35.33   |
| Erlangshen-1.3B |  45.72   |   49.60   |   40.56   |   44.26   |   29.33   |   36.48   |
| TCBert-base<sub>110M-Classification-Chinese     |  48.61   |   51.99   |   43.31   |   45.15   |   33.45   |   37.28   |
| TCBert-large<sub>330M-Classification-Chinese    |  50.50   |   52.79   |   52.89   |   53.89   |   34.93   |   38.31   |
| TCBert-1.3B<sub>1.3B-Classification-Chinese     |  50.80   |   51.59   |   51.93   |   54.12   |   33.96   |   38.08   |
| TCBert-base<sub>110M-Sentence-Embedding-Chinese     |  45.82   |   47.06   |   42.91   |   43.87   |   33.28   |   34.76   |
| TCBert-large<sub>330M-Sentence-Embedding-Chinese    |  50.10   |   50.90   |   53.78   |   53.33   |   37.62   |   36.94   |
| TCBert-1.3B<sub>1.3B-Sentence-Embedding-Chinese     |  50.70   |   53.48   |   52.66   |   54.40   |   36.88   |   38.48   |

第二个prompt模板：

For ***prompt template 2***:
| Dataset |     Prompt template 2    |
|---------|:------------------------:|
| TNEWS   | 接下来的新闻，是跟__相关的内容： |
| CSLDCP  | 接下来的学科，是跟__相关： |
| IFLYTEK |  接下来的生活内容，是跟__相关： |

第二个prompt模板的微调结果：

The **fine-tuning** results for prompt template 2:

| Model           |  TNEWS | CLSDCP | IFLYTEK |
|-----------------|:------:|:------:|:-------:|
| Macbert-base    | 54.78  | 58.38  |  50.83  |
| Macbert-large   | 56.77  | 60.22  |  51.63  |
| Erlangshen-1.3B | 57.81  | 62.80  |  52.77  |
| TCBert-base<sub>110M-Classification-Chinese     | 54.58  | 59.16  |  49.80  |
| TCBert-large<sub>330M-Classification-Chinese    | 56.22  | 61.23  |  50.77  |
| TCBert-1.3B<sub>1.3B-Classification-Chinese      | 57.41  | 64.82  |  53.34  |
| TCBert-base<sub>110M-Sentence-Embedding-Chinese      | 54.68  | 59.78  |  49.40  |
| TCBert-large<sub>330M-Sentence-Embedding-Chinese    | 55.32  | 62.07  |  51.11  |
| TCBert-1.3B<sub>1.3B-Sentence-Embedding-Chinese     | 56.87  | 65.83  |  52.94  |


第二个prompt模板的句子相似度结果：

The **sentence similarity** results for prompt template 2:

|                 |   TNEWS  |           |   CSLDCP  |           |  IFLYTEK  |           |
|-----------------|:--------:|:---------:|:---------:|:---------:|:---------:|:---------:|
| Model           | referece | whitening | reference | whitening | reference | whitening |
| Macbert-base    |  42.29   |   45.22   |   34.23   |   37.48   |   29.62   |   34.13   |
| Macbert-large   |  46.22   |   49.60   |   40.11   |   44.26   |   32.36   |   35.16   |
| Erlangshen-1.3B |  46.17   |   49.10   |   40.45   |   45.88   |   30.36   |   36.88   |
| TCBert-base<sub>110M-Classification-Chinese      |  48.31   |   51.34   |   43.42   |   45.27   |   33.10   |   36.19   |
| TCBert-large<sub>330M-Classification-Chinese    |  51.19   |   51.69   |   52.55   |   53.28   |   34.31   |   37.45   |
| TCBert-1.3B<sub>1.3B-Classification-Chinese      |  52.14   |   52.39   |   51.71   |   53.89   |   33.62   |   38.14   |
| TCBert-base<sub>110M-Sentence-Embedding-Chinese     |  46.72   |   48.86   |   43.19   |   43.53   |   34.08   |   35.79   |
| TCBert-large<sub>330M-Sentence-Embedding-Chinese    |  50.65   |   51.94   |   53.84   |   53.67   |   37.74   |   36.65   |
| TCBert-1.3B<sub>1.3B-Sentence-Embedding-Chinese     |  50.75   |   54.78   |   51.43   |   54.34   |   36.48   |   38.36   |


更多关于TCBERTs的细节，请参考我们的技术报告。基于新的数据，我们会更新TCBERTs，请留意我们仓库的更新。

For more details about TCBERTs, please refer to our paper. We may regularly update TCBERTs upon new coming data, please keep an eye on the repo!

## 使用 Usage
### 使用示例 Usage Examples

```python
# Prompt-based MLM fine-tuning
from transformers import BertForMaskedLM, BertTokenizer
import torch

# Loading models
tokenizer=BertTokenizer.from_pretrained("IDEA-CCNL/Erlangshen-TCBert-110M-Classification-Chinese")
model=BertForMaskedLM.from_pretrained("IDEA-CCNL/Erlangshen-TCBert-110M-Classification-Chinese")

# Prepare the data
inputs = tokenizer("下面是一则关于[MASK][MASK]的新闻：怎样的房子才算户型方正？", return_tensors="pt")
labels = tokenizer("下面是一则关于房产的新闻：怎样的房子才算户型方正？", return_tensors="pt")["input_ids"]
labels = torch.where(inputs.input_ids == tokenizer.mask_token_id, labels, -100)

# Output the loss
outputs = model(**inputs, labels=labels)
loss = outputs.loss

```

```python
# Prompt-based Sentence Similarity
# To extract sentence representations.
from transformers import BertForMaskedLM, BertTokenizer
import torch

# Loading models
tokenizer=BertTokenizer.from_pretrained("IDEA-CCNL/Erlangshen-TCBert-110M-Classification-Chinese")
model=BertForMaskedLM.from_pretrained("IDEA-CCNL/Erlangshen-TCBert-110M-Classification-Chinese")

# Cosine similarity function
cos = torch.nn.CosineSimilarity(dim=0, eps=1e-8)

with torch.no_grad():

    # To extract sentence representations for training data
    training_input = tokenizer("怎样的房子才算户型方正？", return_tensors="pt")
    training_output = BertForMaskedLM(**token_text, output_hidden_states=True)
    training_representation = torch.mean(training_outputs.hidden_states[-1].squeeze(), dim=0)

    # To extract sentence representations for training data
    test_input = tokenizer("下面是一则关于[MASK][MASK]的新闻：股票放量下趺，大资金出逃谁在接盘？", return_tensors="pt")
    test_output = BertForMaskedLM(**token_text, output_hidden_states=True)
    test_representation = torch.mean(training_outputs.hidden_states[-1].squeeze(), dim=0)

# Calculate similarity scores
similarity_score = cos(training_input, test_input)
```

## 引用 Citation

如果您在您的工作中使用了我们的模型，可以引用我们的[技术报告](https://arxiv.org/abs/2211.11304):

If you use for your work, please cite the following paper

```
@article{han2022tcbert,
  title={TCBERT: A Technical Report for Chinese Topic Classification BERT},
  author={Han, Ting and Pan, Kunhao and Chen, Xinyu and Song, Dingjie and Fan, Yuchen and Gao, Xinyu and Gan, Ruyi and Zhang, Jiaxing},
  journal={arXiv preprint arXiv:2211.11304},
  year={2022}
}
```

如果您在您的工作中使用了我们的模型，可以引用我们的[网站](https://github.com/IDEA-CCNL/Fengshenbang-LM/):

You can also cite our [website](https://github.com/IDEA-CCNL/Fengshenbang-LM/):

```text
@misc{Fengshenbang-LM,
  title={Fengshenbang-LM},
  author={IDEA-CCNL},
  year={2021},
  howpublished={\url{https://github.com/IDEA-CCNL/Fengshenbang-LM}},
}
```