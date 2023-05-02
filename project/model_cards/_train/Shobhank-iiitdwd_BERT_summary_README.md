---
language: en
license: apache-2.0
datasets:
- cnn_dailymail
tags:
- summarization
model-index:
- name: patrickvonplaten/bert2bert_cnn_daily_mail
  results:
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: cnn_dailymail
      type: cnn_dailymail
      config: 3.0.0
      split: test
    metrics:
    - name: ROUGE-1
      type: rouge
      value: 41.2808
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 18.6853
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 28.191
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 38.0871
      verified: true
    - name: loss
      type: loss
      value: 2.3451855182647705
      verified: true
    - name: gen_len
      type: gen_len
      value: 73.8332
      verified: true
---

Bert2Bert Summarization with 🤗EncoderDecoder Framework
This model is a warm-started *BERT2BERT* model fine-tuned on the *CNN/Dailymail* summarization dataset.

The model achieves a **18.22** ROUGE-2 score on *CNN/Dailymail*'s test dataset.
