---
language: da
tags:
- danish
- bert
- masked-lm
- Certainly
license: cc-by-4.0
datasets:
- common_crawl
- wikipedia
- dindebat.dk
- hestenettet.dk
- danishOpenSubtitles
pipeline_tag: fill-mask
widget:
- text: "København er [MASK] i Danmark."
---

# Danish BERT (version 2, uncased) by [Certainly](https://certainly.io/) (previously known as BotXO).

All credit goes to [Certainly](https://certainly.io/) (previously known as BotXO), who developed Danish BERT. For data and training details see their [GitHub repository](https://github.com/certainlyio/nordic_bert) or [this article](https://www.certainly.io/blog/danish-bert-model/). You can also visit their [organization page](https://huggingface.co/Certainly) on Hugging Face.

It is both available in TensorFlow and Pytorch format. 

The original TensorFlow version can be downloaded using [this link](https://www.dropbox.com/s/19cjaoqvv2jicq9/danish_bert_uncased_v2.zip?dl=1).


Here is an example on how to load Danish BERT in PyTorch using the [🤗Transformers](https://github.com/huggingface/transformers) library:



```python
from transformers import AutoTokenizer, AutoModelForPreTraining

tokenizer = AutoTokenizer.from_pretrained("Maltehb/danish-bert-botxo")
model = AutoModelForPreTraining.from_pretrained("Maltehb/danish-bert-botxo")

```
