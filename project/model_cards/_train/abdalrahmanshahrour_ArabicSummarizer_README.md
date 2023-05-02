---
language: 
  - ar
tags:
  - AraBERT
  - BERT
  - BERT2BERT
  - MSA
  - Arabic Text Summarization
  - Arabic News Title Generation
  - Arabic Paraphrasing
widget:
 - text: "شهدت مدينة طرابلس، مساء أمس الأربعاء، احتجاجات شعبية وأعمال شغب لليوم الثالث على التوالي، وذلك بسبب تردي الوضع المعيشي والاقتصادي. واندلعت مواجهات عنيفة وعمليات كر وفر ما بين الجيش اللبناني والمحتجين استمرت لساعات، إثر محاولة فتح الطرقات المقطوعة، ما أدى إلى إصابة العشرات من الطرفين."
---

# An Arabic abstractive text summarization model
A BERT2BERT-based model whose parameters are initialized with AraBERT weights and which has been fine-tuned on a dataset of 84,764 paragraph-summary pairs.

More details on the fine-tuning of this model will be released later.

The model can be used as follows:
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from arabert.preprocess import ArabertPreprocessor

model_name="abdalrahmanshahrour/ArabicSummarizer"
preprocessor = ArabertPreprocessor(model_name="")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
pipeline = pipeline("text2text-generation",model=model,tokenizer=tokenizer)

text = "شهدت مدينة طرابلس، مساء أمس الأربعاء، احتجاجات شعبية وأعمال شغب لليوم الثالث على التوالي، وذلك بسبب تردي الوضع المعيشي والاقتصادي. واندلعت مواجهات عنيفة وعمليات كر وفر ما بين الجيش اللبناني والمحتجين استمرت لساعات، إثر محاولة فتح الطرقات المقطوعة، ما أدى إلى إصابة العشرات من الطرفين."
text = preprocessor.preprocess(text)

result = pipeline(text,
            pad_token_id=tokenizer.eos_token_id,
            num_beams=3,
            repetition_penalty=3.0,
            max_length=200,
            length_penalty=1.0,
            no_repeat_ngram_size = 3)[0]['generated_text']
result
>>> 'مواجهات في طرابلس لليوم الثالث على التوالي'
```

## Contact:
<abdalrahman_shahrour@outlook.com>
