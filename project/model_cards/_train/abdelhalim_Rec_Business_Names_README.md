---
datasets:
- BSD-1
tags:
- Text2Text Generation
- Business names
- Recommendation system
metrics:
- Rouge 

---

**Context**

Most of the business name generator systems based on Rule based approach and only take as input a name or keyword not context. The present trained model its aim is to take in a summary for a business idea (1-2 sentences, could be even keywords) and generate a viable business name for users.

**Introduction**

The goal is to create an AI service which is helpful to people and yet could turn into a small business. After fiddling around with T5, I have realized it has an immense creative potential that could prove useful in creative text generation. So, after scraping around 350.000 websites from different Domain list, I have fine-tuned T5 small parameter on this dataset. Results are much depends to the context and creative at the same time.
T5 small is already pre-trained language model which is capable of creating text with a near human quality. It's able to understand the context of a given prefix to generate text. When fine tuned based on the domain names and their meta context, it was able to understand the relation between domain name and the content of the website.

**Dataset**

t5 small needs lots of data to be trained properly. Quality of the data that we will use for fine tuning will have a direct effect on the model quality therefore we need to make sure the data we are scraping from the websites are as clean as possible. The dateset will be under request.

# Usage
In order to use the model in your Python script just copy the following code:
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM 

tokenizer = AutoTokenizer.from_pretrained("abdelhalim/Rec_Business_Names")
model = AutoModelForSeq2SeqLM.from_pretrained("abdelhalim/Rec_Business_Names")

encoder_input_str = "fourniture and decor brand"
number_of_business_names = 10

input_ids = tokenizer(encoder_input_str, return_tensors="pt").input_ids

outputs = model.generate(
    input_ids,
    num_beams=number_of_business_names,
    num_return_sequences=number_of_business_names,
    no_repeat_ngram_size=1,
    remove_invalid_values=True,
)

for i in range(len(outputs)):
  print(tokenizer.decode(outputs[i], skip_special_tokens=True))
  
#Output
edgy.com
Furnace.com
Decorsy.com
Furnacea.com
Decorse.com
Furniture.com
edgys.com
Furnishing.com
Lavender.com
edgya.com

 ```