---
license: apache-2.0
language:
- en
tags:
- text-generation
- non-autoregressive-generation
- early-exit
---

# ELMER
The ELMER model was proposed in [**ELMER: A Non-Autoregressive Pre-trained Language Model for Efficient and Effective Text Generation**](https://arxiv.org/abs/2210.13304) by Junyi Li, Tianyi Tang, Wayne Xin Zhao, Jian-Yun Nie and Ji-Rong Wen.

The detailed information and instructions can be found [https://github.com/RUCAIBox/ELMER](https://github.com/RUCAIBox/ELMER).

## Model Description
ELMER is an efficient and effective PLM for NAR text generation, which generates tokens at different layers by leveraging the early exit technique.

The architecture of ELMER is a variant of the standard Transformer encoder-decoder and poses three technical contributions:

1. For decoder, we replace the original masked multi-head attention with bi-directional multi-head attention akin to the encoder. Therefore, ELMER dynamically adjusts the output length by emitting an end token "[EOS]" at any position.
2. Leveraging early exit, ELMER injects "off-ramps" at each decoder layer, which make predictions with intermediate hidden states. If ELMER exits at the $l$-th layer, we copy the $l$-th hidden states to the subsequent layers.
3. ELMER utilizes a novel pre-training objective, layer permutation language modeling (LPLM), to pre-train on the large-scale corpus. LPLM permutes the exit layer for each token from 1 to the maximum layer $L$.

## Examples
To fine-tune ELMER on non-autoregressive text generation:
```python
>>> from transformers import BartTokenizer as ElmerTokenizer
>>> from transformers import BartForConditionalGeneration as ElmerForConditionalGeneration

>>> tokenizer = ElmerTokenizer.from_pretrained("RUCAIBox/elmer")
>>> model = ElmerForConditionalGeneration.from_pretrained("RUCAIBox/elmer")
```

## Citation
```bibtex
@article{lijunyi2022elmer,
  title={ELMER: A Non-Autoregressive Pre-trained Language Model for Efficient and Effective Text Generation},
  author={Li, Junyi and Tang, Tianyi and Zhao, Wayne Xin and Nie, Jian-Yun and Wen, Ji-Rong},
  booktitle={EMNLP 2022},
  year={2022}
}
```