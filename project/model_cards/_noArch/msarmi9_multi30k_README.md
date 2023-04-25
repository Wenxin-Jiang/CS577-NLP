---
license: mit

language:
- de
- en

tags:
- translation
- pytorch

datasets:
- multi30k

metrics:
- bleu

model-index:
- name: multi30k
  results:
  - task:
      type: translation
    dataset:
      type: multi30k
      name: multi30k-de-en
    metrics:
      - type: bleu
        value: 33.468
        name: Test BLEU
        args: n_gram=4
---

# Seq2seq + Attention

Pytorch implementation of [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473). Trained on the [Multi30k-de-en](http://www.statmt.org/wmt16/multimodal-task.html#task1) dataset with sentencepiece as the tokenizer.    

Here's the attention heatmap of a random sample from the test set:

![attention-heatmap](attention-heatmap.png)
