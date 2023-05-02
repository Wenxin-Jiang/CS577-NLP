---
language: pl
tags:
- herbert
license: cc-by-4.0
---

# HerBERT 
**[HerBERT](https://en.wikipedia.org/wiki/Zbigniew_Herbert)** is a BERT-based Language Model trained on Polish corpora
using Masked Language Modelling (MLM) and Sentence Structural Objective (SSO) with dynamic masking of whole words. For more details, please refer to: [HerBERT: Efficiently Pretrained Transformer-based Language Model for Polish](https://www.aclweb.org/anthology/2021.bsnlp-1.1/).

Model training and experiments were conducted with [transformers](https://github.com/huggingface/transformers) in version 2.9.

## Corpus
HerBERT was trained on six different corpora available for Polish language:

| Corpus | Tokens | Documents |
| :------ | ------: | ------: |
| [CCNet Middle](https://github.com/facebookresearch/cc_net) | 3243M  | 7.9M |
| [CCNet Head](https://github.com/facebookresearch/cc_net) | 2641M  | 7.0M |
| [National Corpus of Polish](http://nkjp.pl/index.php?page=14&lang=1)| 1357M  | 3.9M |
| [Open Subtitles](http://opus.nlpl.eu/OpenSubtitles-v2018.php) | 1056M  | 1.1M 
| [Wikipedia](https://dumps.wikimedia.org/) | 260M  | 1.4M |
| [Wolne Lektury](https://wolnelektury.pl/) | 41M  | 5.5k |

## Tokenizer
The training dataset was tokenized into subwords using a character level byte-pair encoding (``CharBPETokenizer``) with
a vocabulary size of 50k tokens. The tokenizer itself was trained with a [tokenizers](https://github.com/huggingface/tokenizers) library. 

We kindly encourage you to use the ``Fast`` version of the tokenizer, namely ``HerbertTokenizerFast``.

## Usage
Example code:
```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("allegro/herbert-base-cased")
model = AutoModel.from_pretrained("allegro/herbert-base-cased")

output = model(
    **tokenizer.batch_encode_plus(
        [
            (
                "A potem szedł środkiem drogi w kurzawie, bo zamiatał nogami, ślepy dziad prowadzony przez tłustego kundla na sznurku.",
                "A potem leciał od lasu chłopak z butelką, ale ten ujrzawszy księdza przy drodze okrążył go z dala i biegł na przełaj pól do karczmy."
            )
        ],
    padding='longest',
    add_special_tokens=True,
    return_tensors='pt'
    )
)
```

## License
CC BY 4.0

## Citation
If you use this model, please cite the following paper:
```
@inproceedings{mroczkowski-etal-2021-herbert,
    title = "{H}er{BERT}: Efficiently Pretrained Transformer-based Language Model for {P}olish",
    author = "Mroczkowski, Robert  and
      Rybak, Piotr  and
      Wr{\\'o}blewska, Alina  and
      Gawlik, Ireneusz",
    booktitle = "Proceedings of the 8th Workshop on Balto-Slavic Natural Language Processing",
    month = apr,
    year = "2021",
    address = "Kiyv, Ukraine",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2021.bsnlp-1.1",
    pages = "1--10",
}
```

## Authors
The model was trained by [**Machine Learning Research Team at Allegro**](https://ml.allegro.tech/) and [**Linguistic Engineering Group at Institute of Computer Science, Polish Academy of Sciences**](http://zil.ipipan.waw.pl/).

You can contact us at: <a href="mailto:klejbenchmark@allegro.pl">klejbenchmark@allegro.pl</a>