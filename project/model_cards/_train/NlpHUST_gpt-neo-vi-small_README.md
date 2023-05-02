---
language: vi
tags:
- vi
- vietnamese
- text-generation
- gpt3
- lm
- nlp
datasets:
- vietnamese
widget:
- text: Việt Nam là quốc gia có
pipeline_tag: text-generation
---

# GPT-Neo-small for vietnamese
First GPT for vietnamese
## Model Description
GPT-Neo-vi-small is a transformer model designed using EleutherAI's replication of the GPT-3 architecture.
## Training data
GPT-Neo-vi-smal was trained on the News datasets, a large scale dataset created by from News Website for the purpose of training this model.
### How to use
his example generates a different sequence each time it's run:
```py
from transformers import GPTNeoForCausalLM, GPT2Tokenizer
model = GPTNeoForCausalLM.from_pretrained("NlpHUST/gpt-neo-vi-small")
tokenizer = GPT2Tokenizer.from_pretrained("NlpHUST/gpt-neo-vi-small")
prompt = "Ngay sau Tết Nguyên đán Tân Sửu, hiện tượng giá đất tăng tại nhiều địa phương. Thị trường nhộn nhịp, tạo ra những cơn sóng sốt đất khó tin khiến bộ ngành, địa phương đưa cảnh báo."
input_ids = tokenizer(prompt, return_tensors="pt").input_ids
gen_tokens = model.generate(input_ids, do_sample=True, temperature=1.0, max_length=1024)
gen_text = tokenizer.batch_decode(gen_tokens)[0]
print(gen_text)



```
### Contact information
For personal communication related to this project, please contact Nha Nguyen Van (nha282@gmail.com).