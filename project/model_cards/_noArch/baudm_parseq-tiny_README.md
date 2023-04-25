---
language:
- en
license: apache-2.0
tags:
- image-to-text
---

# PARSeq tiny v1.0

PARSeq model pre-trained on various real [STR datasets](https://github.com/baudm/parseq/blob/main/Datasets.md) at image size 128x32 with a patch size of 8x4.

## Model description

PARSeq (Permuted Autoregressive Sequence) models unify the prevailing modeling/decoding schemes in Scene Text Recognition (STR). In particular, with a single model, it allows for context-free non-autoregressive inference (like CRNN and ViTSTR), context-aware autoregressive inference (like TRBA), and bidirectional iterative refinement (like ABINet).

![model image](https://github.com/baudm/parseq/raw/main/.github/system.png)

## Intended uses & limitations

You can use the model for STR on images containing Latin characters (62 case-sensitive alphanumeric + 32 punctuation marks).

### How to use

*TODO*

### BibTeX entry and citation info

```bibtex
@InProceedings{bautista2022parseq,
  author={Bautista, Darwin and Atienza, Rowel},
  title={Scene Text Recognition with Permuted Autoregressive Sequence Models},
  booktitle={Proceedings of the 17th European Conference on Computer Vision (ECCV)},
  month={10},
  year={2022},
  publisher={Springer International Publishing},
  address={Cham}
}
```
