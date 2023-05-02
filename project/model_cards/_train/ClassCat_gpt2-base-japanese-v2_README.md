---
language: ja
license: cc-by-sa-4.0
datasets:
- wikipedia
- cc100
widget:
- text: 天気予報によれば明日は
- text: 私の今日の昼飯は
- text: サッカー日本代表はベルギーに
- text: 日本人サッカー選手が W 杯で
---

## GPT2 Japanese base model version 2

### Prerequisites

transformers==4.19.2

### Model architecture

This model uses GPT2 base setttings except vocabulary size.

### Tokenizer

Using BPE tokenizer with vocabulary size 60,000.

### Training Data 

* [wiki40b/ja](https://www.tensorflow.org/datasets/catalog/wiki40b#wiki40bja) (Japanese Wikipedia)
* Subset of [CC-100/ja](https://data.statmt.org/cc-100/) : Monolingual Datasets from Web Crawl Data

### Usage

```python
from transformers import pipeline
generator = pipeline('text-generation', model='ClassCat/gpt2-base-japanese-v2')
generator("今度の連休の天気は", max_length=50, num_return_sequences=5)
```


## (Japanese description) GPT2 日本語 ベースモデル・バージョン 2

### 前提条件

transformers==4.19.2

### モデル・アーキテクチャ

このモデルは GPT2 ベースモデルの設定を (語彙サイズ以外は) 使用しています。

### トークナイザー

語彙サイズ 60,000 の BPE トークナイザーを使用しています。

### 訓練データ

* [wiki40b/ja](https://www.tensorflow.org/datasets/catalog/wiki40b#wiki40bja) (日本語 Wikipedia)
* [CC-100/ja](https://data.statmt.org/cc-100/) のサブセット : Web クロールデータからの単一言語データセット。


### 使用方法

```python
from transformers import pipeline
generator = pipeline('text-generation', model='ClassCat/gpt2-base-japanese-v2')
generator("今度の連休の天気は", max_length=50, num_return_sequences=5)
```
