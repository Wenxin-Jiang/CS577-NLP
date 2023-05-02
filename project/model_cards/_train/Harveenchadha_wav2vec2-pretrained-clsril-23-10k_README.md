## Overview

We present a CLSRIL-23 (Cross Lingual Speech Representations on Indic Languages), a self supervised learning based audio pre-trained model which learns cross
lingual speech representations from raw audio across **23 Indic languages**. It is built on top of wav2vec
2.0 which is solved by training a contrastive task over masked latent speech representations and
jointly learns the quantization of latents shared across all languages.

[Arxiv Link](https://arxiv.org/pdf/2107.07402.pdf)

[Original Repo](https://github.com/Open-Speech-EkStep/vakyansh-models) contains models in fairseq format.

## Languages in the pretraining dataset

| Language  | Data (In Hrs) |
|-----------|---------------|
|  Assamese | 254.9         |
|  Bengali  | 331.3         |
|   Bodo    | 26.9          |
|   Dogri   | 17.1          |
|  English  | 819.7         |
|  Gujarati | 336.7         |
|   Hindi   | 4563.7        |
|  Kannada  | 451.8         |
|  Kashmiri | 67.8          |
|  Konkani  | 36.8          |
|  Maithili | 113.8         |
| Malayalam | 297.7         |
|  Manipuri | 171.9         |
|  Marathi  | 458.2         |
|   Nepali  | 31.6          |
|    Odia   | 131.4         |
|  Punjabi  | 486.05        |
|  Sanskrit | 58.8          |
|  Santali  | 6.56          |
|   Sindhi  | 16            |
|   Tamil   | 542.6         |
|   Telugu  | 302.8         |
|    Urdu   | 259.68        |

## Repo for training:

[Experimentation](https://github.com/Open-Speech-EkStep/vakyansh-wav2vec2-experimentation) platform built on top of fairseq.
