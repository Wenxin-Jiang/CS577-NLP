---
language:
- multilingual
- af
- am
- ar
- ast
- az
- ba
- be
- bg
- bn
- br
- bs
- ca
- ceb
- cs
- cy
- da
- de
- el
- en
- es
- et
- fa
- ff
- fi
- fr
- fy
- ga
- gd
- gl
- gu
- ha
- he
- hi
- hr
- ht
- hu
- hy
- id
- ig
- ilo
- is
- it
- ja
- jv
- ka
- kk
- km
- kn
- ko
- lb
- lg
- ln
- lo
- lt
- lv
- mg
- mk
- ml
- mn
- mr
- ms
- my
- ne
- nl
- 'no'
- ns
- oc
- or
- pa
- pl
- ps
- pt
- ro
- ru
- sd
- si
- sk
- sl
- so
- sq
- sr
- ss
- su
- sv
- sw
- ta
- th
- tl
- tn
- tr
- uk
- ur
- uz
- vi
- wo
- xh
- yi
- yo
- zh
- zu
license: mit
tags:
- small100
- translation
- flores101
- gsarti/flores_101
- tico19
- gmnlp/tico19
- tatoeba
datasets:
- tico19
- flores101
- tatoeba
---

# SMALL-100 Model

SMaLL-100 is a compact and fast massively multilingual machine translation model covering more than 10K language pairs, that achieves competitive results with M2M-100 while being much smaller and faster. It is introduced in [this paper](https://arxiv.org/abs/2210.11621)(accepted to EMNLP2022), and initially released in [this repository](https://github.com/alirezamshi/small100).

The model architecture and config are the same as [M2M-100](https://huggingface.co/facebook/m2m100_418M/tree/main) implementation, but the tokenizer is modified to adjust language codes. So, you should load the tokenizer locally from [tokenization_small100.py](https://huggingface.co/alirezamsh/small100/blob/main/tokenization_small100.py) file for the moment.

**Demo**: https://huggingface.co/spaces/alirezamsh/small100

**Note**: SMALL100Tokenizer requires sentencepiece, so make sure to install it by:

```pip install sentencepiece```

- **Supervised Training**

SMaLL-100 is a seq-to-seq model for the translation task. The input to the model is ```source:[tgt_lang_code] + src_tokens + [EOS]``` and ```target: tgt_tokens + [EOS]```. 

An example of supervised training is shown below:

```
from transformers import M2M100ForConditionalGeneration
from tokenization_small100 import SMALL100Tokenizer

model = M2M100ForConditionalGeneration.from_pretrained("alirezamsh/small100")
tokenizer = M2M100Tokenizer.from_pretrained("alirezamsh/small100", tgt_lang="fr")

src_text = "Life is like a box of chocolates."
tgt_text = "La vie est comme une boîte de chocolat."

model_inputs = tokenizer(src_text, text_target=tgt_text, return_tensors="pt")

loss = model(**model_inputs).loss  # forward pass
```

Training data can be provided upon request.

- **Generation**

Beam size of 5, and maximum target length of 256 is used for the generation.

```
from transformers import M2M100ForConditionalGeneration
from tokenization_small100 import SMALL100Tokenizer

hi_text = "जीवन एक चॉकलेट बॉक्स की तरह है।"
chinese_text = "生活就像一盒巧克力。"

model = M2M100ForConditionalGeneration.from_pretrained("alirezamsh/small100")
tokenizer = SMALL100Tokenizer.from_pretrained("alirezamsh/small100")

# translate Hindi to French
tokenizer.tgt_lang = "fr"
encoded_hi = tokenizer(hi_text, return_tensors="pt")
generated_tokens = model.generate(**encoded_hi)
tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
# => "La vie est comme une boîte de chocolat."

# translate Chinese to English
tokenizer.tgt_lang = "en"
encoded_zh = tokenizer(chinese_text, return_tensors="pt")
generated_tokens = model.generate(**encoded_zh)
tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
# => "Life is like a box of chocolate."
```

- **Evaluation**

Please refer to [original repository](https://github.com/alirezamshi/small100) for spBLEU computation.

- **Languages Covered**

Afrikaans (af), Amharic (am), Arabic (ar), Asturian (ast), Azerbaijani (az), Bashkir (ba), Belarusian (be), Bulgarian (bg), Bengali (bn), Breton (br), Bosnian (bs), Catalan; Valencian (ca), Cebuano (ceb), Czech (cs), Welsh (cy), Danish (da), German (de), Greeek (el), English (en), Spanish (es), Estonian (et), Persian (fa), Fulah (ff), Finnish (fi), French (fr), Western Frisian (fy), Irish (ga), Gaelic; Scottish Gaelic (gd), Galician (gl), Gujarati (gu), Hausa (ha), Hebrew (he), Hindi (hi), Croatian (hr), Haitian; Haitian Creole (ht), Hungarian (hu), Armenian (hy), Indonesian (id), Igbo (ig), Iloko (ilo), Icelandic (is), Italian (it), Japanese (ja), Javanese (jv), Georgian (ka), Kazakh (kk), Central Khmer (km), Kannada (kn), Korean (ko), Luxembourgish; Letzeburgesch (lb), Ganda (lg), Lingala (ln), Lao (lo), Lithuanian (lt), Latvian (lv), Malagasy (mg), Macedonian (mk), Malayalam (ml), Mongolian (mn), Marathi (mr), Malay (ms), Burmese (my), Nepali (ne), Dutch; Flemish (nl), Norwegian (no), Northern Sotho (ns), Occitan (post 1500) (oc), Oriya (or), Panjabi; Punjabi (pa), Polish (pl), Pushto; Pashto (ps), Portuguese (pt), Romanian; Moldavian; Moldovan (ro), Russian (ru), Sindhi (sd), Sinhala; Sinhalese (si), Slovak (sk), Slovenian (sl), Somali (so), Albanian (sq), Serbian (sr), Swati (ss), Sundanese (su), Swedish (sv), Swahili (sw), Tamil (ta), Thai (th), Tagalog (tl), Tswana (tn), Turkish (tr), Ukrainian (uk), Urdu (ur), Uzbek (uz), Vietnamese (vi), Wolof (wo), Xhosa (xh), Yiddish (yi), Yoruba (yo), Chinese (zh), Zulu (zu)

# Citation

If you use this model for your research, please cite the following work:
```
@inproceedings{mohammadshahi-etal-2022-small,
    title = "{SM}a{LL}-100: Introducing Shallow Multilingual Machine Translation Model for Low-Resource Languages",
    author = "Mohammadshahi, Alireza  and
      Nikoulina, Vassilina  and
      Berard, Alexandre  and
      Brun, Caroline  and
      Henderson, James  and
      Besacier, Laurent",
    booktitle = "Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.emnlp-main.571",
    pages = "8348--8359",
    abstract = "In recent years, multilingual machine translation models have achieved promising performance on low-resource language pairs by sharing information between similar languages, thus enabling zero-shot translation. To overcome the {``}curse of multilinguality{''}, these models often opt for scaling up the number of parameters, which makes their use in resource-constrained environments challenging. We introduce SMaLL-100, a distilled version of the M2M-100(12B) model, a massively multilingual machine translation model covering 100 languages. We train SMaLL-100 with uniform sampling across all language pairs and therefore focus on preserving the performance of low-resource languages. We evaluate SMaLL-100 on different low-resource benchmarks: FLORES-101, Tatoeba, and TICO-19 and demonstrate that it outperforms previous massively multilingual models of comparable sizes (200-600M) while improving inference latency and memory usage. Additionally, our model achieves comparable results to M2M-100 (1.2B), while being 3.6x smaller and 4.3x faster at inference.",
}

@inproceedings{mohammadshahi-etal-2022-compressed,
    title = "What Do Compressed Multilingual Machine Translation Models Forget?",
    author = "Mohammadshahi, Alireza  and
      Nikoulina, Vassilina  and
      Berard, Alexandre  and
      Brun, Caroline  and
      Henderson, James  and
      Besacier, Laurent",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2022",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.findings-emnlp.317",
    pages = "4308--4329",
    abstract = "Recently, very large pre-trained models achieve state-of-the-art results in various natural language processing (NLP) tasks, but their size makes it more challenging to apply them in resource-constrained environments. Compression techniques allow to drastically reduce the size of the models and therefore their inference time with negligible impact on top-tier metrics. However, the general performance averaged across multiple tasks and/or languages may hide a drastic performance drop on under-represented features, which could result in the amplification of biases encoded by the models. In this work, we assess the impact of compression methods on Multilingual Neural Machine Translation models (MNMT) for various language groups, gender, and semantic biases by extensive analysis of compressed models on different machine translation benchmarks, i.e. FLORES-101, MT-Gender, and DiBiMT. We show that the performance of under-represented languages drops significantly, while the average BLEU metric only slightly decreases. Interestingly, the removal of noisy memorization with compression leads to a significant improvement for some medium-resource languages. Finally, we demonstrate that compression amplifies intrinsic gender and semantic biases, even in high-resource languages.",
}

```