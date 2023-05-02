---
license: mit
tags:
- generated_from_trainer
model-index:
- name: afro-xlmr-large
  results: []
language:
- en
- fr
- ar
- ha
- ig
- yo
- rn
- rw
- sn
- xh
- zu
- om
- am
- so
- st
- ny
- mg
- sw
- af
---


# afro-xlmr-large

AfroXLMR-large was created by MLM adaptation of XLM-R-large model on 17 African languages (Afrikaans, Amharic, Hausa, Igbo, Malagasy, Chichewa, Oromo, Nigerian-Pidgin, Kinyarwanda, Kirundi, Shona, Somali, Sesotho, Swahili, isiXhosa, Yoruba, and isiZulu) covering the major African language families and 3 high resource languages (Arabic, French, and English). 

## Eval results on MasakhaNER (F-score)
language| XLM-R-miniLM| XLM-R-base |XLM-R-large | afro-xlmr-large |  afro-xlmr-base | afro-xlmr-small | afro-xlmr-mini
-|-|-|-|-|-|-|-
amh |69.5|70.6|76.2|79.7|76.1|70.1|69.7
hau |74.5|89.5|90.5|91.4|91.2|91.4|87.7
ibo |81.9|84.8|84.1|87.7|87.4|86.6|83.5
kin |68.6|73.3|73.8|79.1|78.0|77.5|74.1
lug |64.7|79.7|81.6|86.7|82.9|83.2|77.4
luo |11.7|74.9|73.6|78.1|75.1|75.4|17.5
pcm |83.2|87.3|89.0|91.0|89.6|89.0|85.5
swa |86.3|87.4|89.4|90.4|88.6|88.7|86.0
wol |51.7|63.9|67.9|69.6|67.4|65.9|59.0
yor |72.0|78.3|78.9|85.2|82.1|81.3|75.1
avg |66.4|79.0|80.5|83.9|81.8|80.9|71.6


### BibTeX entry and citation info
```
@inproceedings{alabi-etal-2022-adapting,
    title = "Adapting Pre-trained Language Models to {A}frican Languages via Multilingual Adaptive Fine-Tuning",
    author = "Alabi, Jesujoba O.  and
      Adelani, David Ifeoluwa  and
      Mosbach, Marius  and
      Klakow, Dietrich",
    booktitle = "Proceedings of the 29th International Conference on Computational Linguistics",
    month = oct,
    year = "2022",
    address = "Gyeongju, Republic of Korea",
    publisher = "International Committee on Computational Linguistics",
    url = "https://aclanthology.org/2022.coling-1.382",
    pages = "4336--4349",
    abstract = "Multilingual pre-trained language models (PLMs) have demonstrated impressive performance on several downstream tasks for both high-resourced and low-resourced languages. However, there is still a large performance drop for languages unseen during pre-training, especially African languages. One of the most effective approaches to adapt to a new language is language adaptive fine-tuning (LAFT) {---} fine-tuning a multilingual PLM on monolingual texts of a language using the pre-training objective. However, adapting to target language individually takes large disk space and limits the cross-lingual transfer abilities of the resulting models because they have been specialized for a single language. In this paper, we perform multilingual adaptive fine-tuning on 17 most-resourced African languages and three other high-resource languages widely spoken on the African continent to encourage cross-lingual transfer learning. To further specialize the multilingual PLM, we removed vocabulary tokens from the embedding layer that corresponds to non-African writing scripts before MAFT, thus reducing the model size by around 50{\%}. Our evaluation on two multilingual PLMs (AfriBERTa and XLM-R) and three NLP tasks (NER, news topic classification, and sentiment classification) shows that our approach is competitive to applying LAFT on individual languages while requiring significantly less disk space. Additionally, we show that our adapted PLM also improves the zero-shot cross-lingual transfer abilities of parameter efficient fine-tuning methods.",
}

```