---
language: 
  - en
tags:
- retrieval
- math-retrieval
datasets:
- MathematicalStackExchange
- ARQMath
---

# ALBERT for ARQMath 3

This repository contains our best model for ARQMath 3, the math_10 model. It was initialised from ALBERT-base-v2 and further pre-trained on Math StackExchange in three different stages. We also added more LaTeX tokens to the tokenizer to enable a better tokenization of mathematical formulas. math_10 was fine-tuned on a classification task to determine whether a given question (sequence 1) matches a given answer (sequence 2). The classification output can be used for ranking the best answers. For further details, please read our paper: http://ceur-ws.org/Vol-3180/paper-07.pdf. 


## Other Models for ARQMath 3
We plan on also publishing the other fine-tuned models as well as the base models. Links to these repositories will be added here soon.

| Model       | Initialised from | Pre-training               | Fine-Tuned                          | Link |
|-------------|------------------|----------------------------|-------------------------------------|------|
| roberta_10  | RoBERTa          | MathSE (1)                 | yes, N=10 MathSE                    |      |
| base_10     | ALBERT           | MathSE (1)                 | yes, N=10 MathSE                    |      |
| math_10_add | ALBERT           | MathSE (1)-(3)             | yes, N=10 MathSE and annotated data |      |
| Khan_SE_10  | ALBERT           | MathSE (1)                 | yes, N=10 MathSE                    |      |
| roberta     | RoBERTa          | MathSE (1)                 | no                                  | [AnReu/math_pretrained_roberta](https://huggingface.co/AnReu/math_pretrained_roberta)     |
| math albert | ALBERT           | MathSE (1)-(3)             | no                                  | [AnReu/math_albert](https://huggingface.co/AnReu/math_albert) |
| base        | ALBERT           | MathSE (1)                 | no                                  |      |
| Khan_SE     | ALBERT           | MathSE (1) mixed with Khan | no                                  |      |

### Update

We have also further pre-trained a BERT-base-cased model in the same way as our ALBERT model. You can find it here: [AnReu/math_pretrained_bert](https://huggingface.co/AnReu/math_pretrained_bert).

# Usage

```python
# based on https://huggingface.co/docs/transformers/main/en/task_summary#sequence-classification
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("AnReu/albert-for-arqmath-3")

model = AutoModelForSequenceClassification.from_pretrained("AnReu/albert-for-arqmath-3")

classes = ["non relevant", "relevant"]

sequence_0 = "How can I calculate x in $3x = 5$"
sequence_1 = "Just divide by 3: $x = \\frac{5}{3}$"
sequence_2 = "The general rule for squaring a sum is $(a+b)^2=a^2+2ab+b^2$"

# The tokenizer will automatically add any model specific separators (i.e. <CLS> and <SEP>) and tokens to
# the sequence, as well as compute the attention masks.
irrelevant = tokenizer(sequence_0, sequence_2, return_tensors="pt")
relevant = tokenizer(sequence_0, sequence_1, return_tensors="pt")

irrelevant_classification_logits = model(**irrelevant).logits
relevant_classification_logits = model(**relevant).logits

irrelevant_results = torch.softmax(irrelevant_classification_logits, dim=1).tolist()[0]
relevant_results = torch.softmax(relevant_classification_logits, dim=1).tolist()[0]

# Should be irrelevant
for i in range(len(classes)):
    print(f"{classes[i]}: {int(round(irrelevant_results[i] * 100))}%")

# Should be relevant
for i in range(len(classes)):
    print(f"{classes[i]}: {int(round(relevant_results[i] * 100))}%")

```

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