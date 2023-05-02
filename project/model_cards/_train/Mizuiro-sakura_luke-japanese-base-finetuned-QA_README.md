---
license: mit
language: ja
tags:
    - luke
    - question-answering
    - squad
    - pytorch
    - transformers
    - question answering
    
---

# このモデルはluke-japanese-base-liteをファインチューニングして、Question-Answeringに用いれるようにしたものです。
このモデルはluke-japanese-base-liteを運転ドメインQAデータセット（DDQA）（　https://nlp.ist.i.kyoto-u.ac.jp/index.php?Driving%20domain%20QA%20datasets　）を用いてファインチューニングしたものです。

Question-Answeringタスク（SQuAD）に用いることができます。

# This model is fine-tuned model for Question-Answering which is based on luke-japanese-base-lite

This model is fine-tuned by using DDQA dataset.

You could use this model for Question-Answering tasks.

# モデルの精度 accuracy of model
'em(厳密一致)': 0.845933014354067, 'f1': 0.9197176274789681

# How to use 使い方
sentencepieceとtransformersをインストールして
(pip install sentencepiece , pip install transformers)
以下のコードを実行することで、Question-Answeringタスクを解かせることができます。
please execute this code.
```python
import torch
from transformers import AutoTokenizer, LukeForQuestionAnswering

tokenizer = AutoTokenizer.from_pretrained('Mizuiro-sakura/luke-japanese-base-finetuned-QA')
model=LukeForQuestionAnswering.from_pretrained('Mizuiro-sakura/luke-japanese-base-finetuned-QA') # 学習済みモデルの読み込み
text={
    'context':'私の名前はEIMIです。好きな食べ物は苺です。 趣味は皆さんと会話することです。',
    'question' :'好きな食べ物は何ですか'
}

input_ids=tokenizer.encode(text['question'],text['context']) # tokenizerで形態素解析しつつコードに変換する
output= model(torch.tensor([input_ids])) # 学習済みモデルを用いて解析
prediction = tokenizer.decode(input_ids[torch.argmax(output.start_logits): torch.argmax(output.end_logits)]) # 答えに該当する部分を抜き取る
print(prediction)
```


# what is Luke?　Lukeとは？[1]
LUKE (Language Understanding with Knowledge-based Embeddings) is a new pre-trained contextualized representation of words and entities based on transformer. LUKE treats words and entities in a given text as independent tokens, and outputs contextualized representations of them. LUKE adopts an entity-aware self-attention mechanism that is an extension of the self-attention mechanism of the transformer, and considers the types of tokens (words or entities) when computing attention scores.

LUKE achieves state-of-the-art results on five popular NLP benchmarks including SQuAD v1.1 (extractive question answering), CoNLL-2003 (named entity recognition), ReCoRD (cloze-style question answering), TACRED (relation classification), and Open Entity (entity typing). luke-japaneseは、単語とエンティティの知識拡張型訓練済み Transformer モデルLUKEの日本語版です。LUKE は単語とエンティティを独立したトークンとして扱い、これらの文脈を考慮した表現を出力します。

# Acknowledgments　謝辞
Lukeの開発者である山田先生とStudio ousiaさんには感謝いたします。 I would like to thank Mr.Yamada @ikuyamada and Studio ousia @StudioOusia.

# Citation
[1]@inproceedings{yamada2020luke, title={LUKE: Deep Contextualized Entity Representations with Entity-aware Self-attention}, author={Ikuya Yamada and Akari Asai and Hiroyuki Shindo and Hideaki Takeda and Yuji Matsumoto}, booktitle={EMNLP}, year={2020} }



