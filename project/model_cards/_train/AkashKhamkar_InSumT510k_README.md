---
license: afl-3.0
---
---
About : 
This model can be used for text summarization.

 
  
The dataset on which it was fine tuned consisted of 10,323 articles.

The Data Fields : 

- "Headline" : title of the article
- "articleBody" : the main article content
- "source" : the link to the readmore page.

The data splits were : 

- Train : 8258.
- Vaildation : 2065.


### How to use along with pipeline
```python
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2Seq

tokenizer = AutoTokenizer.from_pretrained("AkashKhamkar/InSumT510k")

model = AutoModelForSeq2SeqLM.from_pretrained("AkashKhamkar/InSumT510k")

summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

summarizer("Text for summarization...", min_length=5, max_length=50)
```

language:
- English
  
library_name: Pytorch  

tags:
- Summarization 
- T5-base
- Conditional Modelling  
- 


