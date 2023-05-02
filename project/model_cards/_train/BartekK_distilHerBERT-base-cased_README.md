---
language: pl
tags:
- distilherbert
---

## distilHerBERT
distilHerBERT-base is a BERT-based Language Model trained on Polish subset of [cc100](https://huggingface.co/datasets/cc100) dataset using Masked Language Modelling (MLM) and [distillation procedure](https://arxiv.org/abs/1910.01108) from model [HerBERT](https://huggingface.co/allegro/herbert-base-cased) with dynamic masking of whole words.
We provide one of the models (S4) described in the report from final project on the subject of (Deep) Natural Language Processing, which was carried out at MIMUW in 2021/2022: [Distillation_of_HerBERT](https://github.com/BartekKrzepkowski/DistilHerBERT-base_vol2/blob/master/report/Final_Report___Distillation_of_HerBERT.pdf).

The model was trained using fp16 and the data parallelism method (ZeRO Stage 2), using the deep learning optimization library - DeepSpeed.

Model training and experiments were conducted with transformers in version 4.20.1.


## Tokenizer
The training dataset was tokenized into subwords using a character level byte-pair encoding (``CharBPETokenizer``) with
a vocabulary size of 50k tokens. The tokenizer itself was trained with a [tokenizers](https://github.com/huggingface/tokenizers) library. 

We kindly encourage you to use the ``Fast`` version of the tokenizer, namely ``HerbertTokenizerFast``.

## Usage
Example code:
```python
from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("BartekK/distilHerBERT-base-cased")
model = AutoModelForMaskedLM.from_pretrained("BartekK/distilHerBERT-base-cased")

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

## Acknowledgements
We want to thank <br>
Spyridon Mouselinos - for suggesting literature to help with the project <br>
and <br>
Piotr Rybak - for sharing information on training the HerBERT models

## Authors
The model was trained by:

Bartłomiej Krzepkowski, <br>
Dominika Bankiewicz, <br>
Rafał Michaluk, <br>
Jacek Ciszewski.

If you have questions please contact me: <a href="mailto:bartekkrzepkowski@gmail.com">bartekkrzepkowski@gmail.com</a>

The code can be found here: [distilHerBERT-base repo](https://github.com/BartekKrzepkowski/DistilHerBERT-base_vol2/tree/master).