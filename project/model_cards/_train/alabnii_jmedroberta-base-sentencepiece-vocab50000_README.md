---
language: ja
license: cc-by-nc-sa-4.0
tags:
- roberta
- medical
mask_token: "[MASK]"
widget:
- text: "この患者は[MASK]と診断された。"
---

# alabnii/jmedroberta-base-sentencepiece-vocab50000

## Model description

This is a Japanese RoBERTa base model pre-trained on academic articles in medical sciences collected by Japan Science and Technology Agency (JST).

This model is released under the [Creative Commons 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/deed) (CC BY-NC-SA 4.0).

#### Reference

Ja:

```
@InProceedings{sugimoto_nlp2023_jmedroberta,
    author =    "杉本海人 and 壹岐太一 and 知田悠生 and 金沢輝一 and 相澤彰子",
    title =     "J{M}ed{R}o{BERT}a: 日本語の医学論文にもとづいた事前学習済み言語モデルの構築と評価",
    booktitle = "言語処理学会第29回年次大会",
    year =      "2023",
    url =       "https://www.anlp.jp/proceedings/annual_meeting/2023/pdf_dir/P3-1.pdf"
}
```

En:

```
@InProceedings{sugimoto_nlp2023_jmedroberta,
    author =    "Sugimoto, Kaito and Iki, Taichi and Chida, Yuki and Kanazawa, Teruhito and Aizawa, Akiko",
    title =     "J{M}ed{R}o{BERT}a: a Japanese Pre-trained Language Model on Academic Articles in Medical Sciences (in Japanese)",
    booktitle = "Proceedings of the 29th Annual Meeting of the Association for Natural Language Processing",
    year =      "2023",
    url =       "https://www.anlp.jp/proceedings/annual_meeting/2023/pdf_dir/P3-1.pdf"
}
```

## Datasets used for pre-training

- abstracts (train: 1.6GB (10M sentences), validation: 0.2GB (1.3M sentences))
- abstracts & body texts (train: 0.2GB (1.4M sentences))

## How to use

**Input text must be converted to full-width characters（全角）in advance.**

You can use this model for masked language modeling as follows:
```python
from transformers import AutoModelForMaskedLM, AutoTokenizer

model = AutoModelForMaskedLM.from_pretrained("alabnii/jmedroberta-base-sentencepiece-vocab50000")
model.eval()
tokenizer = AutoTokenizer.from_pretrained("alabnii/jmedroberta-base-sentencepiece-vocab50000")

texts = ['この患者は[MASK]と診断された。']
inputs = tokenizer.batch_encode_plus(texts, return_tensors='pt')
outputs = model(**inputs)
tokenizer.convert_ids_to_tokens(outputs.logits[0][1:-1].argmax(axis=-1))
# ['▁この', '患者は', 'ＳＬＥ', '▁', 'と診断された', '。']
```

Alternatively, you can employ [Fill-mask pipeline](https://huggingface.co/tasks/fill-mask).

```python
from transformers import pipeline
fill = pipeline("fill-mask", model="alabnii/jmedroberta-base-sentencepiece-vocab50000", top_k=10)
fill("この患者は[MASK]と診断された。")
#[{'score': 0.021247705444693565,
#  'token': 3592,
#  'token_str': 'ＳＬＥ',
#  'sequence': 'この患者はＳＬＥ と診断された。'},
# {'score': 0.012531018815934658,
#  'token': 16813,
#  'token_str': 'ＭＳＡ',
#  'sequence': 'この患者はＭＳＡ と診断された。'},
# {'score': 0.01097362581640482,
#  'token': 41130,
#  'token_str': 'ＭＥＬＡＳ',
#  'sequence': 'この患者はＭＥＬＡＳ と診断された。'},
# ...
```

You can fine-tune this model on downstream tasks.

**See also sample Colab notebooks:** https://colab.research.google.com/drive/1D-FNO01XX82pL3So5GWfi2gVo338aAMo?usp=sharing

## Tokenization

Each sentence is tokenized into tokens by [SentencePiece (Unigram)](https://huggingface.co/course/chapter6/7).

## Vocabulary

The vocabulary consists of 50000 tokens induced by [SentencePiece (Unigram)](https://huggingface.co/course/chapter6/7).

## Training procedure

The following hyperparameters were used during pre-training:

- learning_rate: 0.0001
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- total_train_batch_size: 256
- total_eval_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 20000
- training_steps: 2000000
- mixed_precision_training: Native AMP

## Note: Why do we call our model RoBERTa, not BERT?

As the config file suggests, our model is based on HuggingFace's `BertForMaskedLM` class. However, we consider our model as **RoBERTa** for the following reasons:

- We kept training only with max sequence length (= 512) tokens.
- We removed the next sentence prediction (NSP) training objective.
- We introduced dynamic masking (changing the masking pattern in each training iteration).

## Acknowledgements

This work was supported by Japan Japan Science and Technology Agency (JST) AIP Trilateral AI Research (Grant Number: JPMJCR20G9), and Joint Usage/Research Center for Interdisciplinary Large-scale Information Infrastructures (JHPCN) (Project ID: jh221004), in Japan.  
In this research work, we used the "[mdx: a platform for the data-driven future](https://mdx.jp/)".