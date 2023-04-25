---
license: other
---
---
datasets:
- squad
tags:
- question-generation
widget:
- text: "The Technikum was conceived in the early 1900s by the German-Jewish fund Ezrah as a school of [HL]engineering and sciences[HL].[SEP]"
---

# Transformer QG on SQuAD
HLQG is Proposed by [Ying-Hong Chan & Yao-Chung Fan. (2019). A Re-current BERT-based Model for Question Generation.](https://www.aclweb.org/anthology/D19-5821/)

**This is a Reproduce Version from distilled squad dataset**

More detail: [p208p2002/Transformer-QG-on-SQuAD](https://github.com/p208p2002/Transformer-QG-on-SQuAD)

## Usage
### Input Format
```
C' = [c1, c2, ..., [HL], a1, ..., a|A|, [HL], ..., c|C|]
```