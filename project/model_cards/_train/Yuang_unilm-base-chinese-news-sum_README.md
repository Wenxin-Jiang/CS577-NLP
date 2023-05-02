---
language:
  - zh
tags:
  - unilm
license: apache-2.0
---

# unilm-base-chinese-news-sum

```sh
pip install git+https://github.com/Liadrinz/transformers-unilm  # 安装兼容HuggingFace的UniLM模型代码
```

```py
from unilm import UniLMTokenizer, UniLMForConditionalGeneration


news_article = (
    "12月23日，河北石家庄。8岁哥哥轻车熟路哄睡弟弟，姿势标准动作熟练。"
    "妈妈杨女士表示：哥哥很喜欢弟弟，因为心思比较细，自己平时带孩子的习惯他都会跟着学习，"
    "哄睡孩子也都会争着来，技巧很娴熟，两人在一块很有爱，自己感到很幸福，平时帮了自己很大的忙，感恩有这么乖的宝宝。"
)

tokenizer = UniLMTokenizer.from_pretrained("Yuang/unilm-base-chinese-news-sum")
model = UniLMForConditionalGeneration.from_pretrained("Yuang/unilm-base-chinese-news-sum")

inputs = tokenizer(news_article, return_tensors="pt")
output_ids = model.generate(**inputs, max_new_tokens=16)
output_text = tokenizer.decode(output_ids[0])
print(output_text)  # "[CLS] <news_article> [SEP] <news_summary> [SEP]"
news_summary = output_text.split("[SEP]")[1].strip()
print(news_summary)
```
