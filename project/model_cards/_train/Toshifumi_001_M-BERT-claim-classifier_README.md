---
tags:
- generated_from_keras_callback
model-index:
- name: 001_M-BERT-claim-classifier
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# この「クレーム判別」モデルの使い方

このモデルは、当該クレームがどのプロダクトについてのものかを判別します。右側の"Hosted inference API" 直下のBOXにお好きなクレームを入力し、"Compute"ボタンをクリックして下さい。30〜60秒前後で答えが返ってきます。答えは以下の５つのlabelのいずれかです。
入力は最大300〜400文字、日本語・英語他100カ国語以上に対応してます。教育用ですので、機密情報は入力しないで下さい。

# 5つのlabelの定義:

- LABEL_0 : Bank account or service (銀行口座・サービス)
- LABEL_1 : Checking or savings account（当座預金・普通預金）
- LABEL_2 : Consumer Loan（消費者ローン）
- LABEL_3 : Credit card（クレジットカード）
- LABEL_4 : Mortgage（住宅ローン）

### 入力例 　（正解　4: 'Mortgage'）
「私の夫と私はローンデポを通じてローンのRefiローンを申請し、その後承認されました。私たちはそれが次週になると言われているプロセスで前進することにしました。 両当事者と鑑定評価で実行されました。私たちの料金は次の週に有効であることが開示されました。貸出金の担当者によって連絡しました。ローンが45日以内に閉じなかった場合、当社の元のレートオファーが拡張されます。ロックレートが期限切れになったことを示すXXXXから別のコミュニケーション（Eメール）を受け取り、新しい料金を取得する必要があります。」





# How to use this "claim classification" model

This model determines which product the claim is about. Enter your favorite claim in the box directly under "Hosted inference API" on the right, and click the "Compute" button. You will receive an answer within 30-60 seconds. The answer is one of the following five labels. You can enter a maximum of 400 to 500 characters, and it supports Japanese, English, and more than 100 languages.

# Warning 
This is for educational purposes only, please do not enter confidential information.


# Definition of 5 labels

- LABEL_0 : Bank account or service 
- LABEL_1 : Checking or savings account
- LABEL_2 : Consumer Loan
- LABEL_3 : Credit card
- LABEL_4 : Mortgage


# Input example (correct answer 4: 'Mortgage')

I drew an advance of $2900.00 from my HELOC that I have with Wells Fargo. I have auto pay with Wells Fargo and a scheduled payment of $100.00 was taken from mychecking ac. I entered the bank, CA branch and paid $2800.00 to pay off the advance. Since that time, various transactions have been posted to this account. There is a principal adj debit in the amount of $170.00 followed by a principal reversal in the amount of $91.


# 001_M-BERT-claim-classifier

It achieves the following results on the evaluation set:


## Model description

bert-base-multilingual-cased

## Intended uses & limitations

This is solely for educational purposes. This cannot be used for investments or businesses in practice.  I do not accept any responsibility or liability for loss or damage occasioned to any person or property through using materials, instructions, methods, algorithm or ideas contained herein, or acting or refraining from acting as a result of such use.  I expressly disclaim all implied warranties, including merchantability or fitness for any particular purpose. There will be no duty on me to correct any errors or defects in the codes and the software.

## Training and evaluation data

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': 1e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: float32

### Training results

### Framework versions

- Transformers 4.25.1
- TensorFlow 2.9.2
- Datasets 2.8.0
- Tokenizers 0.13.2
