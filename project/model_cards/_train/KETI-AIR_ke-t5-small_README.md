---
license: apache-2.0
language: [en, ko]
tags:
  - t5
eos_token: "</s>"
widget:
  - text: 아버지가 방에 들어가신다.</s>
---

# ke-t5 base

Pretrained T5 Model on Korean and English. See [Github](https://github.com/AIRC-KETI/ke-t5) and [Paper](https://aclanthology.org/2021.findings-emnlp.33/) [Korean paper](https://koreascience.kr/article/CFKO202130060717834.pdf) for more details.

## How to use

```python
from transformers import AutoModel, AutoTokenizer

model = AutoModel.from_pretrained("KETI-AIR/ke-t5-small")
tokenizer = AutoTokenizer.from_pretrained("KETI-AIR/ke-t5-small")
```

## BibTeX entry and citation info

```bibtex
@inproceedings{kim-etal-2021-model-cross,
    title = "A Model of Cross-Lingual Knowledge-Grounded Response Generation for Open-Domain Dialogue Systems",
    author = "Kim, San  and
      Jang, Jin Yea  and
      Jung, Minyoung  and
      Shin, Saim",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2021",
    month = nov,
    year = "2021",
    address = "Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-emnlp.33",
    doi = "10.18653/v1/2021.findings-emnlp.33",
    pages = "352--365",
    abstract = "Research on open-domain dialogue systems that allow free topics is challenging in the field of natural language processing (NLP). The performance of the dialogue system has been improved recently by the method utilizing dialogue-related knowledge; however, non-English dialogue systems suffer from reproducing the performance of English dialogue systems because securing knowledge in the same language with the dialogue system is relatively difficult. Through experiments with a Korean dialogue system, this paper proves that the performance of a non-English dialogue system can be improved by utilizing English knowledge, highlighting the system uses cross-lingual knowledge. For the experiments, we 1) constructed a Korean version of the Wizard of Wikipedia dataset, 2) built Korean-English T5 (KE-T5), a language model pre-trained with Korean and English corpus, and 3) developed a knowledge-grounded Korean dialogue model based on KE-T5. We observed the performance improvement in the open-domain Korean dialogue model even only English knowledge was given. The experimental results showed that the knowledge inherent in cross-lingual language models can be helpful for generating responses in open dialogue systems.",
}
```