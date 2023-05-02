---
language: vi
datasets:
- cc100
tags:
- summarization
- translation
- question-answering

license: mit
---

# EnViT5-base

State-of-the-art pretrained Transformer-based encoder-decoder model for Vietnamese and English used in [MTet's paper](https://arxiv.org/abs/2210.05610).

## How to use
For more details, do check out [our Github repo](https://github.com/vietai/mtet). 

[Finetunning examples can be found here](https://github.com/vietai/ViT5/tree/main/finetunning_huggingface).

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
​
tokenizer = AutoTokenizer.from_pretrained("VietAI/envit5-base")  
model = AutoModelForSeq2SeqLM.from_pretrained("VietAI/envit5-base")
model.cuda()


# need prefix for en: and vi: sentences
inputs = [
    "vi: VietAI là tổ chức phi lợi nhuận với sứ mệnh ươm mầm tài năng về trí tuệ nhân tạo và xây dựng một cộng đồng các chuyên gia trong lĩnh vực trí tuệ nhân tạo đẳng cấp quốc tế tại Việt Nam.",
    "vi: Theo báo cáo mới nhất của Linkedin về danh sách việc làm triển vọng với mức lương hấp dẫn năm 2020, các chức danh công việc liên quan đến AI như Chuyên gia AI (Artificial Intelligence Specialist), Kỹ sư ML (Machine Learning Engineer) đều xếp thứ hạng cao.",
    "en: Our teams aspire to make discoveries that impact everyone, and core to our approach is sharing our research and tools to fuel progress in the field.",
    "en: We're on a journey to advance and democratize artificial intelligence through open source and open science."
    ]

outputs = model.generate(tokenizer(inputs, return_tensors="pt", padding=True).input_ids.to('cuda'), max_length=512)
print(tokenizer.batch_decode(outputs, skip_special_tokens=True))

```

## Citation
```
@misc{mtet,
  doi = {10.48550/ARXIV.2210.05610},
  url = {https://arxiv.org/abs/2210.05610},
  author = {Ngo, Chinh and Trinh, Trieu H. and Phan, Long and Tran, Hieu and Dang, Tai and Nguyen, Hieu and Nguyen, Minh and Luong, Minh-Thang},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {MTet: Multi-domain Translation for English and Vietnamese},
  publisher = {arXiv},
  year = {2022},
  copyright = {Creative Commons Attribution 4.0 International}
}

```