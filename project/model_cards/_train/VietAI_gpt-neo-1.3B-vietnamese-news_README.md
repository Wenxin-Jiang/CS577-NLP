---
language: 
  - vi
tags:
- pytorch
- causal-lm
- gpt
---

# GPT-Neo 1.3B on Vietnamese News

Details will be available soon.

For more information, please contact anhduongng.1001@gmail.com (Dương) / imthanhlv@gmail.com (Thành) / nguyenvulebinh@gmail.com (Bình).

### How to use 
```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("VietAI/gpt-neo-1.3B-vietnamese-news")
model = AutoModelForCausalLM.from_pretrained("VietAI/gpt-neo-1.3B-vietnamese-news", low_cpu_mem_usage=True)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu") 
model.to(device)

prompt = "Tiềm năng của trí tuệ nhân tạo" # your input sentence
input_ids = tokenizer(prompt, return_tensors="pt")['input_ids'].to(device)

gen_tokens = model.generate(
        input_ids,
        max_length=max_length,
        do_sample=True,
        temperature=0.9,
        top_k=20,
    )

gen_text = tokenizer.batch_decode(gen_tokens)[0]
print(gen_text)
```