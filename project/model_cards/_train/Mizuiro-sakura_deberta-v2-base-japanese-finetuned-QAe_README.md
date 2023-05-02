---
license: mit
language: ja
library_name: transformers
tags: 
    - pytorch
    - deberta
    - deberta-v2
    - question-answering
    - question answering
    - squad
datasets: 
    - wikipedia
    - cc100
    - oscar
metrics: 
    - accuracy

---

# このモデルはdeberta-v2-base-japaneseをファインチューニングしてQAタスクに用いれるようにしたものです。
このモデルはdeberta-v2-base-japaneseを運転ドメインQAデータセット（DDQA）（　https://nlp.ist.i.kyoto-u.ac.jp/index.php?Driving%20domain%20QA%20datasets　）を用いてファインチューニングしたものです。

Question-Answeringタスク（SQuAD）に用いることができます。

# This model is fine-tuned model for Question-Answering which is based on deberta-v2-base-japanese
This model is fine-tuned by using DDQA dataset.

You could use this model for Question-Answering tasks.

# How to use 使い方
transformersおよびpytorch、sentencepiece、Juman++をインストールしてください。
以下のコードを実行することで、Question-Answeringタスクを解かせることができます。  please execute this code.
```python
import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

tokenizer = AutoTokenizer.from_pretrained('ku-nlp/deberta-v2-base-japanese')
model=AutoModelForQuestionAnswering.from_pretrained('Mizuiro-sakura/deberta-v2-base-japanese-finetuned-QAe') # 学習済みモデルの読み込み

text={
    'context':'私の名前はEIMIです。好きな食べ物は苺です。 趣味は皆さんと会話することです。',
    'question' :'好きな食べ物は何ですか'
}

input_ids=tokenizer.encode(text['question'],text['context']) # tokenizerで形態素解析しつつコードに変換する
output= model(torch.tensor([input_ids])) # 学習済みモデルを用いて解析
prediction = tokenizer.decode(input_ids[torch.argmax(output.start_logits): torch.argmax(output.end_logits)]) # 答えに該当する部分を抜き取る
print(prediction)
```
# モデルの精度 accuracy of model
Exact Match(厳密一致) : 0.8038277511961722

f1 : 0.8959389668095072


# deberta-v2-base-japaneseとは？
日本語Wikipedeia（3.2GB）および、cc100(85GB)、oscar(54GB)を用いて訓練されたモデルです。
京都大学黒橋研究室が公表されました。

# Model description
This is a Japanese DeBERTa V2 base model pre-trained on Japanese Wikipedia, the Japanese portion of CC-100, and the Japanese portion of OSCAR.

# Acknowledgments 謝辞
モデルを公開してくださった京都大学黒橋研究室には感謝いたします。
I would like to thank Kurohashi Lab at Kyoto University.
