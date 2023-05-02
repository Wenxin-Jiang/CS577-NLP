---
license: mit
language: ja
library_name: transformers
tags: 
    - pytorch
    - deberta
    - deberta-v2
    - named entity recognition
    - named-entity-recognition
    - ner
datasets: 
    - wikipedia
    - cc100
    - oscar
metrics: 
    - accuracy

---

# このモデルはdeberta-v2-base-japaneseをファインチューニングして固有表現抽出（NER）に用いれるようにしたものです。
このモデルはdeberta-v2-base-japaneseを Wikipediaを用いた日本語の固有表現抽出データセット(ストックマーク社、https://github.com/stockmarkteam/ner-wikipedia-dataset )を用いてファインチューニングしたものです。

# This model is fine-tuned model for Named Entity Recognition (NER) which is based on deberta-v2-base-japanese
This model is fine-tuned by using Wikipedia dataset.

You could use this model for NER tasks.

# How to use 使い方
transformersおよびpytorch、sentencepiece、Juman++をインストールしてください。
以下のコードを実行することで、固有表現抽出タスクを解かせることができます。  please execute this code.
```python
from transformers import AutoTokenizer,pipeline, AutoModelForTokenClassification
tokenizer = AutoTokenizer.from_pretrained('Mizuiro-sakura/deberta-v2-base-japanese-finetuned-ner')
model=AutoModelForTokenClassification.from_pretrained('Mizuiro-sakura/deberta-v2-base-japanese-finetuned-ner') # 学習済みモデルの読み込み

text=('昨日は東京で買い物をした')

ner=pipeline('ner', model=model, tokenizer=tokenizer)

result=ner(text)
print(result)
```
# モデルの精度 accuracy of model
                     precision   recall  f1-score   support

     その他の組織名       0.73      0.75      0.74      238
        イベント名        0.81      0.81      0.81      215
         人名            0.84      0.87      0.85      547
         地名            0.83      0.83      0.83      446
      政治的組織名        0.82      0.85      0.83      263
         施設名          0.74      0.86      0.80      241
         法人名          0.81      0.82      0.82      487
         製品名          0.68      0.73      0.71      252

       micro avg        0.79      0.82      0.81      2689
       macro avg        0.78      0.81      0.80      2689
     weighted avg       0.79      0.82      0.81      2689

# deberta-v2-base-japaneseとは？
日本語Wikipedeia（3.2GB）および、cc100(85GB)、oscar(54GB)を用いて訓練されたモデルです。
京都大学黒橋研究室が公表されました。

# Model description
This is a Japanese DeBERTa V2 base model pre-trained on Japanese Wikipedia, the Japanese portion of CC-100, and the Japanese portion of OSCAR.

# Acknowledgments 謝辞
モデルを公開してくださった京都大学黒橋研究室には感謝いたします。

I would like to thank Kurohashi Lab at Kyoto University.

