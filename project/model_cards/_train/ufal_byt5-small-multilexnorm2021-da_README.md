---
language: da
datasets:
- mc4
- wikipedia
- multilexnorm
tags:
- lexical normalization
license: apache-2.0

---

# Fine-tuned ByT5-small for MultiLexNorm (Danish version)

![model image](https://github.com/ufal/multilexnorm2021/raw/master/img/overall.png)

This is the official release of the fine-tuned models for **the winning entry** to the [*W-NUT 2021: Multilingual Lexical Normalization (MultiLexNorm)* shared task](https://noisy-text.github.io/2021/multi-lexnorm.html), which evaluates lexical-normalization systems on 12 social media datasets in 11 languages.

Our system is based on [ByT5](https://arxiv.org/abs/2105.13626), which we first pre-train on synthetic data and then fine-tune on authentic normalization data. It achieves the best performance by a wide margin in intrinsic evaluation, and also the best performance in extrinsic evaluation through dependency parsing. In addition to these fine-tuned models, we also release the source files on [GitHub](https://github.com/ufal/multilexnorm2021) and an interactive demo on [Google Colab](https://colab.research.google.com/drive/1rxpI8IlKk-D2crFqi2hdzbTBIezqgsCg?usp=sharing).


## How to use

The model was *not* fine-tuned in a standard sentence-to-sentence setting – instead, it was tailored to the token-to-token definition of MultiLexNorm data. Please refer to [**the interactive demo on Colab notebook**](https://colab.research.google.com/drive/1rxpI8IlKk-D2crFqi2hdzbTBIezqgsCg?usp=sharing) to learn how to use these models.


## How to cite

```bibtex
@inproceedings{wnut-ufal,
  title= "{ÚFAL} at {MultiLexNorm} 2021: Improving Multilingual Lexical Normalization by Fine-tuning {ByT5}",
  author = "Samuel, David and Straka, Milan",
  booktitle = "Proceedings of the 7th Workshop on Noisy User-generated Text (W-NUT 2021)",
  year = "2021",
  publisher = "Association for Computational Linguistics",
  address = "Punta Cana, Dominican Republic"
}
```


## ByT5 - Small

ByT5 is a tokenizer-free version of [Google's T5](https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html) and generally follows the architecture of [MT5](https://huggingface.co/google/mt5-small).

ByT5 was only pre-trained on [mC4](https://www.tensorflow.org/datasets/catalog/c4#c4multilingual) excluding any supervised training with an average span-mask of 20 UTF-8 characters. Therefore, this model has to be fine-tuned before it is useable on a downstream task.

ByT5 works especially well on noisy text data,*e.g.*, `google/byt5-small` significantly outperforms [mt5-small](https://huggingface.co/google/mt5-small) on [TweetQA](https://arxiv.org/abs/1907.06292).

Paper: [ByT5: Towards a token-free future with pre-trained byte-to-byte models](https://arxiv.org/abs/2105.13626)

Authors: *Linting Xue, Aditya Barua, Noah Constant, Rami Al-Rfou, Sharan Narang, Mihir Kale, Adam Roberts, Colin Raffel* 
