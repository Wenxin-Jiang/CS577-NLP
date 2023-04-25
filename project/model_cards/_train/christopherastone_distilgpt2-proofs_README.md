---
widget:
- text: "Let MATH be given."
- text: "If MATH is a nonempty"
- text: "By the inductive hypothesis,"
---
[DistilGPT2](https://huggingface.co/distilgpt2)  English language model fine-tuned on mathematical proofs extracted from [arXiv.org](https://arxiv.org) LaTeX sources from 1992 to 2020.

 Proofs have been cleaned up a bit. In particular, they use
 * `CITE` for any citation
 * `REF` for any reference
 * `MATH` for any LaTeX mathematical formula
 * `CASE:` for any `\item` or labeled subcase.