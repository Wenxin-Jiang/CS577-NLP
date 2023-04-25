---

language: ja

license: cc-by-sa-4.0

datasets:

- wikipedia

widget:

- text: 東京大学で[MASK]の研究をしています。

---

# ELECTRA base Japanese generator

This is a [ELECTRA](https://github.com/google-research/electra) model pretrained on texts in the Japanese language.

The codes for the pretraining are available at [retarfi/language-pretraining](https://github.com/retarfi/language-pretraining/tree/v1.0).

## Model architecture

The model architecture is the same as ELECTRA base in the [original ELECTRA implementation](https://github.com/google-research/electra); 12 layers, 256 dimensions of hidden states, and 4 attention heads.

## Training Data

The models are trained on the Japanese version of Wikipedia.

The training corpus is generated from the Japanese version of Wikipedia, using Wikipedia dump file as of June 1, 2021. 

The corpus file is 2.9GB, consisting of approximately 20M sentences.

## Tokenization

The texts are first tokenized by MeCab with IPA dictionary and then split into subwords by the WordPiece algorithm.

The vocabulary size is 32768.

## Training

The models are trained with the same configuration as ELECTRA base in the [original ELECTRA paper](https://arxiv.org/abs/2003.10555) except size; 512 tokens per instance, 256 instances per batch, and 766k training steps.

The size of the generator is 1/3 of the size of the discriminator.

## Citation

```
@article{Suzuki-etal-2023-ipm,
  title = {Constructing and analyzing domain-specific language model for financial text mining}
  author = {Masahiro Suzuki and Hiroki Sakaji and Masanori Hirano and Kiyoshi Izumi},
  journal = {Information Processing & Management},
  volume = {60},
  number = {2},
  pages = {103194},
  year = {2023},
  doi = {10.1016/j.ipm.2022.103194}
}
```

## Licenses

The pretrained models are distributed under the terms of the [Creative Commons Attribution-ShareAlike 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## Acknowledgments

This work was supported by JSPS KAKENHI Grant Number JP21K12010.
