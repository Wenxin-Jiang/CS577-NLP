---
language: ja
tags:
- t5
- text2text-generation
- seq2seq
license: cc-by-sa-4.0
datasets:
- wikipedia
- c4
---

# 日本語T5事前学習済みモデル

This is a T5 (Text-to-Text Transfer Transformer) model pretrained on Japanese corpus.

次の日本語コーパス（約890GB）を用いて事前学習を行ったT5 (Text-to-Text Transfer Transformer) モデルです。  

* [Wikipedia](https://ja.wikipedia.org)の日本語ダンプデータ (2020年7月6日時点のもの)
* [mC4](https://github.com/allenai/allennlp/discussions/5056)の日本語コーパス（正確にはc4/multilingualのjaスプリット）

このモデルは事前学習のみを行なったものであり、特定のタスクに利用するにはファインチューニングする必要があります。  
本モデルにも、大規模コーパスを用いた言語モデルにつきまとう、学習データの内容の偏りに由来する偏った（倫理的ではなかったり、有害だったり、バイアスがあったりする）出力結果になる問題が潜在的にあります。
この問題が発生しうることを想定した上で、被害が発生しない用途にのみ利用するよう気をつけてください。


# 転移学習のサンプルコード

https://github.com/sonoisa/t5-japanese のモデル名"t5-base-japanese"を"t5-base-japanese-mC4-Wikipedia"に変更してください。


# ベンチマーク

livedoorニュースコーパスを用いたニュース記事のジャンル予測タスクの精度は次の通りです。

mC4/ja + Wikipediaを用いて事前学習した日本語T5 ([t5-base-japanese-mC4-Wikipedia](https://huggingface.co/sonoisa/t5-base-japanese-mC4-Wikipedia), パラメータ数は222M)

| label       |  precision  |  recall | f1-score | support |
| ----------- | ----------- | ------- | -------- | ------- |
|           0 |      0.91   |   0.93  |    0.92  |     130 |
|           1 |      0.96   |   0.95  |    0.95  |     121 |
|           2 |      0.96   |   0.96  |    0.96  |     123 |
|           3 |      0.87   |   0.90  |    0.89  |      82 |
|           4 |      0.96   |   0.99  |    0.98  |     129 |
|           5 |      0.97   |   0.96  |    0.97  |     141 |
|           6 |      1.00   |   0.98  |    0.99  |     127 |
|           7 |      1.00   |   0.98  |    0.99  |     127 |
|           8 |      0.98   |   0.97  |    0.97  |     120 |
|   accuracy  |             |         |    0.96  |    1100 |
|  macro avg  |      0.96   |   0.96  |    0.96  |    1100 |
| weighted avg |     0.96   |   0.96  |    0.96  |    1100 |


比較対象: OSCAR + CC-100 + Wikipediaを用いて事前学習した日本語T5 ([t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese), パラメータ数は222M)

| label       |  precision  |  recall | f1-score | support |
| ----------- | ----------- | ------- | -------- | ------- |
|           0 |      0.96   |   0.94  |    0.95  |     130 |
|           1 |      0.98   |   0.99  |    0.99  |     121 |
|           2 |      0.96   |   0.96  |    0.96  |     123 |
|           3 |      0.86   |   0.91  |    0.89  |      82 |
|           4 |      0.96   |   0.97  |    0.97  |     129 |
|           5 |      0.96   |   0.96  |    0.96  |     141 |
|           6 |      0.98   |   0.98  |    0.98  |     127 |
|           7 |      1.00   |   0.99  |    1.00  |     127 |
|           8 |      0.99   |   0.97  |    0.98  |     120 |
|   accuracy  |             |         |    0.97  |    1100 |
|  macro avg  |      0.96   |   0.96  |    0.96  |    1100 |
| weighted avg |     0.97   |   0.97  |    0.97  |    1100 |


## 免責事項

本モデルの作者は本モデルを作成するにあたって、その内容、機能等について細心の注意を払っておりますが、モデルの出力が正確であるかどうか、安全なものであるか等について保証をするものではなく、何らの責任を負うものではありません。本モデルの利用により、万一、利用者に何らかの不都合や損害が発生したとしても、モデルやデータセットの作者や作者の所属組織は何らの責任を負うものではありません。利用者には本モデルやデータセットの作者や所属組織が責任を負わないことを明確にする義務があります。


## ライセンス

[CC-BY SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.ja)

[Common Crawlの利用規約](http://commoncrawl.org/terms-of-use/)も守るようご注意ください。
