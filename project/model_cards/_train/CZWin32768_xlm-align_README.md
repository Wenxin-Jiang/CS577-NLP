# XLM-Align

**Improving Pretrained Cross-Lingual Language Models via Self-Labeled Word Alignment** (ACL-2021, [paper](https://arxiv.org/pdf/2106.06381.pdf), [github](https://github.com/CZWin32768/XLM-Align))

XLM-Align is a pretrained cross-lingual language model that supports 94 languages. See details in our [paper](https://arxiv.org/pdf/2106.06381.pdf).

## Example

```
model = = AutoModel.from_pretrained("CZWin32768/xlm-align")
```

## Evaluation Results

XTREME cross-lingual understanding tasks:

| Model | POS | NER  | XQuAD | MLQA | TyDiQA | XNLI | PAWS-X | Avg |
|:----:|:----:|:----:|:----:|:-----:|:----:|:-----:|:----:|:----:|
| XLM-R_base | 75.6 | 61.8 | 71.9 / 56.4 | 65.1 / 47.2 | 55.4 / 38.3 | 75.0 | 84.9 | 66.4 |
| XLM-Align | **76.0** | **63.7** | **74.7 / 59.0** | **68.1 / 49.8**  |  **62.1 / 44.8** | **76.2**  | **86.8**  | **68.9** |

## MD5

```
b9d214025837250ede2f69c9385f812c  config.json
6005db708eb4bab5b85fa3976b9db85b  pytorch_model.bin
bf25eb5120ad92ef5c7d8596b5dc4046  sentencepiece.bpe.model
eedbd60a7268b9fc45981b849664f747  tokenizer.json
```

## About

Contact: chizewen\@outlook.com

BibTeX:

```
@article{xlmalign,
  title={Improving Pretrained Cross-Lingual Language Models via Self-Labeled Word Alignment},
  author={Zewen Chi and Li Dong and Bo Zheng and Shaohan Huang and Xian-Ling Mao and Heyan Huang and Furu Wei},
  journal={arXiv preprint arXiv:2106.06381},
  year={2021}
}
```