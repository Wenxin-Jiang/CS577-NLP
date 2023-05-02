---
license: mit
language: ja
tags:
    - luke
    - pytorch
    - transformers
    - ner
    - 固有表現抽出
    - named entity recognition
    - named-entity-recognition
    
---

# このモデルはluke-japanese-baseをファインチューニングして、固有表現抽出（NER）に用いれるようにしたものです。
このモデルはluke-japanese-baseを
Wikipediaを用いた日本語の固有表現抽出データセット(ストックマーク社、https://github.com/stockmarkteam/ner-wikipedia-dataset )を用いてファインチューニングしたものです。

固有表現抽出（NER）タスクに用いることができます。

# This model is fine-tuned model for Named-Entity-Recognition(NER) which is based on luke-japanese-base

This model is fine-tuned by using Wikipedia dataset.

You could use this model for NER tasks.

# モデルの精度 accuracy of model
                        precision   recall    f1-score   support

     その他の組織名       0.76      0.77      0.77       238
       イベント名       　0.83      0.90      0.87       215
          人名      　    0.88      0.91      0.90       546
          地名            0.84      0.83      0.83       440
      政治的組織名        0.80      0.84      0.82       263
         施設名           0.78      0.83      0.80       241
         法人名           0.88      0.90      0.89       487
         製品名           0.74      0.80      0.77       252

        micro avg          0.83      0.86      0.84      2682
        macro avg         0.81      0.85      0.83      2682
      weighted avg        0.83      0.86      0.84      2682


# How to use 使い方
sentencepieceとtransformersをインストールして (pip install sentencepiece , pip install transformers) 
以下のコードを実行することで、NERタスクを解かせることができます。
please execute this code.
```python
from transformers import MLukeTokenizer,pipeline, LukeForTokenClassification

tokenizer = MLukeTokenizer.from_pretrained('Mizuiro-sakura/luke-japanese-base-finetuned-ner')
model=LukeForTokenClassification.from_pretrained('Mizuiro-sakura/luke-japanese-base-finetuned-ner') # 学習済みモデルの読み込み

text=('昨日は東京で買い物をした')

ner=pipeline('ner', model=model, tokenizer=tokenizer)

result=ner(text)
print(result)
```


# what is Luke?　Lukeとは？[1]
LUKE (Language Understanding with Knowledge-based Embeddings) is a new pre-trained contextualized representation of words and entities based on transformer. LUKE treats words and entities in a given text as independent tokens, and outputs contextualized representations of them. LUKE adopts an entity-aware self-attention mechanism that is an extension of the self-attention mechanism of the transformer, and considers the types of tokens (words or entities) when computing attention scores.

LUKE achieves state-of-the-art results on five popular NLP benchmarks including SQuAD v1.1 (extractive question answering), CoNLL-2003 (named entity recognition), ReCoRD (cloze-style question answering), TACRED (relation classification), and Open Entity (entity typing). luke-japaneseは、単語とエンティティの知識拡張型訓練済み Transformer モデルLUKEの日本語版です。LUKE は単語とエンティティを独立したトークンとして扱い、これらの文脈を考慮した表現を出力します。

# Acknowledgments　謝辞
Lukeの開発者である山田先生とStudio ousiaさんには感謝いたします。 I would like to thank Mr.Yamada @ikuyamada and Studio ousia @StudioOusia.

# Citation
[1]@inproceedings{yamada2020luke, title={LUKE: Deep Contextualized Entity Representations with Entity-aware Self-attention}, author={Ikuya Yamada and Akari Asai and Hiroyuki Shindo and Hideaki Takeda and Yuji Matsumoto}, booktitle={EMNLP}, year={2020} }




