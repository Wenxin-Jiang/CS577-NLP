---
language: zh
tags:
- roberta-wwm
license: apache-2.0
datasets:
- finance
---

在众多业务中，越来越频繁的使用预训练语言模型（Pre-trained Language Models），为了在金融场景下各任务中取得更好效果，我们发布了jdt-fin-roberta-wwm模型

## 模型
* `base模型`：12-layer, 768-hidden, 12-heads, 110M parameters  

| 模型简称 | 语料 | 京盘下载 |
| - | - | - |
| fin-roberta-wwm | 金融语料 | - |

## 快速加载
### 使用Huggingface-Transformers
依托于[Huggingface-Transformers](https://github.com/huggingface/transformers)，可轻松调用以上模型。
```
tokenizer = BertTokenizer.from_pretrained("MODEL_NAME")
model = BertModel.from_pretrained("MODEL_NAME")
```
**注意：本目录中的所有模型均使用BertTokenizer以及BertModel加载，请勿使用RobertaTokenizer/RobertaModel！**
其中`MODEL_NAME`对应列表如下：

| 模型名 | MODEL_NAME |
| - | - |
| fin-roberta-wwm | wangfan/jdt-fin-roberta-wwm |

