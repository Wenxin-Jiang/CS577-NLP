---
language:
- ar
- en
- multilingual
license: mit
tags:
- bert
- roberta
- exbert
datasets:
- arabic_billion_words
- cc100
- gigaword
- oscar
- wikipedia
---

# An English-Arabic Bilingual Encoder

```
from transformers import AutoModelForMaskedLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("jhu-clsp/roberta-large-eng-ara-128k")
model = AutoModelForMaskedLM.from_pretrained("jhu-clsp/roberta-large-eng-ara-128k")
```

`roberta-large-eng-ara-128k` is an English�Arabic bilingual encoders of 24-layer Transformers (d\_model= 1024), the same size as XLM-R large. We use the same Common Crawl corpus as XLM-R for pretraining. Additionally, we also use English and Arabic Wikipedia, Arabic Gigaword (Parker et al., 2011), Arabic OSCAR (Ortiz Su�rez et al., 2020), Arabic News Corpus (El-Khair, 2016), and Arabic OSIAN (Zeroual et al.,2019). In total, we train with 9.2B words of Arabic text and 26.8B words of English text, more than either XLM-R (2.9B words/23.6B words) or GigaBERT v4 (Lan et al., 2020) (4.3B words/6.1B words). We build an English�Arabic joint vocabulary using SentencePiece (Kudo and Richardson, 2018) with size of 128K. We additionally enforce coverage of all Arabic characters after normalization.

## Pretraining Detail

We pretrain each encoder with a batch size of 2048 sequences and 512 sequence length for 250K steps from scratch roughly 1/24 the amount of pretraining compute of XLM-R. Training takes 8 RTX6000 GPUs roughly three weeks. We follow the pretraining recipe of RoBERTa (Liu et al., 2019) and XLM-R. We omit the next sentence prediction task and use a learning rate of 2e-4, Adam optimizer, and linear warmup of 10K steps then decay linearly to 0, multilingual sampling alpha of 0.3, and the fairseq (Ott et al., 2019) implementation.

## Citation

Please cite this paper for reference:

```bibtex
@inproceedings{yarmohammadi-etal-2021-everything,
    title = "Everything Is All It Takes: A Multipronged Strategy for Zero-Shot Cross-Lingual Information Extraction",
    author = "Yarmohammadi, Mahsa  and
      Wu, Shijie  and
      Marone, Marc  and
      Xu, Haoran  and
      Ebner, Seth  and
      Qin, Guanghui  and
      Chen, Yunmo and
      Guo, Jialiang and
      Harman, Craig  and
      Murray, Kenton and
      White, Aaron Steven  and
      Dredze, Mark and
      Van Durme, Benjamin",
    booktitle = "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
    year = "2021",
}
```
