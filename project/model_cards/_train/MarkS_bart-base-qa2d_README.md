---
license: afl-3.0
---

# Generating Declarative Statements from QA Pairs

There are already some rule-based models that can accomplish this task, but I haven't seen any transformer-based models that can do so. Therefore, I trained this model based on `Bart-base` to transform QA pairs into declarative statements.

I compared the this model with other rule base models, including 

> [paper1](https://aclanthology.org/D19-5401.pdf) (2019), which proposes **2 Encoder Pointer-Gen model**

and

> [paper2](https://arxiv.org/pdf/2112.03849.pdf) (2021), which proposes **RBV2 model**

**Here are results compared to 2 Encoder Pointer-Gen model (on testset released by paper1)**

Test on testset

| Model   | 2 Encoder Pointer-Gen(2019) | BART-base  |
| ------- | --------------------------- | ---------- |
| BLEU    | 74.05                       | **78.878** |
| ROUGE-1 | 91.24                       | **91.937** |
| ROUGE-2 | 81.91                       | **82.177** |
| ROUGE-L | 86.25                       | **87.172** |

Test on NewsQA testset

| Model   | 2 Encoder Pointer-Gen | BART       |
| ------- | --------------------- | ---------- |
| BLEU    | 73.29                 | **74.966** |
| ROUGE-1 | **95.38**             | 89.328     |
| ROUGE-2 | **87.18**             | 78.538     |
| ROUGE-L | **93.65**             | 87.583     |

Test on free_base testset

| Model   | 2 Encoder Pointer-Gen | BART       |
| ------- | --------------------- | ---------- |
| BLEU    | 75.41                 | **76.082** |
| ROUGE-1 | **93.46**             | 92.693     |
| ROUGE-2 | **82.29**             | 81.216     |
| ROUGE-L | **87.5**              | 86.834     |



**As paper2 doesn't release its own dataset, it's hard to make a fair comparison. But according to results in paper2, the Bleu and ROUGE score of their model is lower than that of MPG, which is exactly the 2 Encoder Pointer-Gen model.**

| Model        | BLEU | ROUGE-1 | ROUGE-2 | ROUGE-L |
| ------------ | ---- | ------- | ------- | ------- |
| RBV2         | 74.8 | 95.3    | 83.1    | 90.3    |
| RBV2+BERT    | 71.5 | 93.9    | 82.4    | 89.5    |
| RBV2+RoBERTa | 72.1 | 94      | 83.1    | 89.8    |
| RBV2+XLNET   | 71.2 | 93.6    | 82.3    | 89.4    |
| MPG          | 75.8 | 94.4    | 87.4    | 91.6    |

There are reasons to believe that this model performs better than RBV2.

To sum up, this model performs nearly as well as the SOTA rule-based model evaluated with BLEU and ROUGE score. However the sentence pattern is lack of diversity.

(It's worth mentioning that even though I tried my best to conduct objective tests, the testsets I could find were more or less different from what they introduced in the paper.)

## How to use


```python
from transformers import BartTokenizer, BartForConditionalGeneration
tokenizer = BartTokenizer.from_pretrained("MarkS/bart-base-qa2d")
model = BartForConditionalGeneration.from_pretrained("MarkS/bart-base-qa2d")

input_text = "question: what day is it today? answer: Tuesday"
input = tokenizer(input_text, return_tensors='pt')
output = model.generate(input.input_ids)
result = tokenizer.batch_decode(output, skip_special_tokens=True)
```

