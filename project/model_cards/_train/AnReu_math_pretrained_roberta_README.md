---
language: 
  - en
tags:
- mathematics
- math-aware
datasets:
- MathematicalStackExchange
---

# Math-aware RoBERTa

This repository contains our pre-trained RoBERTa-based model for ARQMath 3. It was initialised from RoBERTa-base and further pre-trained on Math StackExchange in only one stage. We also added more LaTeX tokens to the tokenizer to enable a better tokenization of mathematical formulas. This model is not yet fine-tuned on a specific task. 

For further details, please read our paper: http://ceur-ws.org/Vol-3180/paper-07.pdf. 



# Usage

You can use this model to further fine-tune it on any math-aware task you have in mind, e.g., classification, question-answering, etc. . Please note, that the model in this repository is only pre-trained and not fine-tuned.


# Citation

If you find this model useful, consider citing our paper:
```
@article{reusch2022transformer,
  title={Transformer-Encoder and Decoder Models for Questions on Math},
  author={Reusch, Anja and Thiele, Maik and Lehner, Wolfgang},
  year={2022},
  organization={CLEF}
}
```
