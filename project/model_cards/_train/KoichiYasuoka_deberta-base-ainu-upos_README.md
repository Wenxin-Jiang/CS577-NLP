---
language:
- "ain"
tags:
- "ainu"
- "token-classification"
- "pos"
- "dependency-parsing"
license: "cc-by-sa-4.0"
pipeline_tag: "token-classification"
widget:
- text: "itak=as awa pon rupne aynu ene itaki"
- text: "イタカㇱ アワ ポン ルㇷ゚ネ アイヌ エネ イタキ"
- text: "итакас ава пон рубне айну эне итакі"
---

# deberta-base-ainu-upos

## Model Description

This is a DeBERTa(V2) model pre-trained on Ainu texts (in カタカナ, Roman, and Кириллица) for POS-tagging and dependency-parsing, derived from [deberta-base-ainu](https://huggingface.co/KoichiYasuoka/deberta-base-ainu). Every word is tagged by [UPOS](https://universaldependencies.org/u/pos/) (Universal Part-Of-Speech).

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForTokenClassification
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/deberta-base-ainu-upos")
model=AutoModelForTokenClassification.from_pretrained("KoichiYasuoka/deberta-base-ainu-upos")
```

or

```py
import esupar
nlp=esupar.load("KoichiYasuoka/deberta-base-ainu-upos","ainu")
```

## Reference

安岡孝一: [ローマ字・カタカナ・キリル文字併用アイヌ語RoBERTa・DeBERTaモデルの開発](http://id.nii.ac.jp/1001/00224072/), 情報処理学会研究報告, Vol.2023-CH-131『人文科学とコンピュータ』, No.7 (2023年2月18日), pp.1-7.

## See Also

[esupar](https://github.com/KoichiYasuoka/esupar): Tokenizer POS-tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models

