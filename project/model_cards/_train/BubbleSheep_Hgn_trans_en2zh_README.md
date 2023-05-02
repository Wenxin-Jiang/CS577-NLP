---
language: 
  - en
  - zh
thumbnail: "url to a thumbnail used in social sharing"
tags:
- translation
license: apache-2.0
datasets:
- THUOCL清华大学开放中文词库
metrics:
- bleu

---
# Model Details
- **Model Description:**
This model has been pre-trained for English-Chinese Translation, and use datasets of THUOCL to fine tune the model.
- **source group**: English 
- **target group**: Chinese 
- **Parent Model:** Helsinki-NLP/opus-mt-en-zh, see https://huggingface.co/Helsinki-NLP/opus-mt-en-zh
- **Model Type:** Translation
#### Training Data
- 清华大学中文开放词库(THUOCL)
- **Data link**: http://thuocl.thunlp.org/
## How to Get Started With the Model

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("BubbleSheep/Hgn_trans_en2zh")

model = AutoModelForSeq2SeqLM.from_pretrained("BubbleSheep/Hgn_trans_en2zh")

```

