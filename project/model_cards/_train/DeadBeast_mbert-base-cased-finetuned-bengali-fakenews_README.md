---
language: bengali
license: apache-2.0
datasets:
- BanFakeNews
---

# **mBERT-base-cased-finetuned-bengali-fakenews**

This model is a fine-tune checkpoint of mBERT-base-cased over **[Bengali-fake-news Dataset](https://www.kaggle.com/cryptexcode/banfakenews)** for Text classification. This model reaches an accuracy of 96.3 with an f1-score of 79.1 on the dev set.

### **How to use?**

**Task**: binary-classification

- LABEL_1: Authentic (*Authentic means news is authentic*)
- LABEL_0: Fake (*Fake means news is fake*)

```
from transformers import pipeline
print(pipeline("sentiment-analysis",model="DeadBeast/mbert-base-cased-finetuned-bengali-fakenews",tokenizer="DeadBeast/mbert-base-cased-finetuned-bengali-fakenews")("অভিনেতা আফজাল শরীফকে ২০ লাখ টাকার অনুদান অসুস্থ অভিনেতা আফজাল শরীফকে চিকিৎসার জন্য ২০ লাখ টাকা অনুদান দিয়েছেন প্রধানমন্ত্রী শেখ হাসিনা।"))
```