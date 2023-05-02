---
language:
- vi
- en
datasets:
- cc100
tags:
- translation

widget:
- text: "vi: VietAI là tổ chức phi lợi nhuận với sứ mệnh ươm mầm tài năng về trí tuệ nhân tạo và xây dựng một cộng đồng các chuyên gia trong lĩnh vực trí tuệ nhân tạo đẳng cấp quốc tế tại Việt Nam."

license: openrail
---

# EnViT5 Translation

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/mtet-multi-domain-translation-for-english/machine-translation-on-iwslt2015-english-1)](https://paperswithcode.com/sota/machine-translation-on-iwslt2015-english-1?p=mtet-multi-domain-translation-for-english)

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/mtet-multi-domain-translation-for-english-and/on-phomt)](https://paperswithcode.com/sota/on-phomt?p=mtet-multi-domain-translation-for-english-and)


State-of-the-art English-Vietnamese and Vietnamese-English Translation models trained on [MTet](https://research.vietai.org/mtet/), [PhoMT](https://github.com/VinAIResearch/PhoMT).




```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


model_name = "VietAI/envit5-translation"
tokenizer = AutoTokenizer.from_pretrained(model_name)  
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

inputs = [
    "vi: VietAI là tổ chức phi lợi nhuận với sứ mệnh ươm mầm tài năng về trí tuệ nhân tạo và xây dựng một cộng đồng các chuyên gia trong lĩnh vực trí tuệ nhân tạo đẳng cấp quốc tế tại Việt Nam.",
    "vi: Theo báo cáo mới nhất của Linkedin về danh sách việc làm triển vọng với mức lương hấp dẫn năm 2020, các chức danh công việc liên quan đến AI như Chuyên gia AI (Artificial Intelligence Specialist), Kỹ sư ML (Machine Learning Engineer) đều xếp thứ hạng cao.",
    "en: Our teams aspire to make discoveries that impact everyone, and core to our approach is sharing our research and tools to fuel progress in the field.",
    "en: We're on a journey to advance and democratize artificial intelligence through open source and open science."
    ]

outputs = model.generate(tokenizer(inputs, return_tensors="pt", padding=True).input_ids.to('cuda'), max_length=512)
print(tokenizer.batch_decode(outputs, skip_special_tokens=True))

# ['en: VietAI is a non-profit organization with the mission of nurturing artificial intelligence talents and building an international - class community of artificial intelligence experts in Vietnam.',
#  'en: According to the latest LinkedIn report on the 2020 list of attractive and promising jobs, AI - related job titles such as AI Specialist, ML Engineer and ML Engineer all rank high.',
#  'vi: Nhóm chúng tôi khao khát tạo ra những khám phá có ảnh hưởng đến mọi người, và cốt lõi trong cách tiếp cận của chúng tôi là chia sẻ nghiên cứu và công cụ để thúc đẩy sự tiến bộ trong lĩnh vực này.',
#  'vi: Chúng ta đang trên hành trình tiến bộ và dân chủ hoá trí tuệ nhân tạo thông qua mã nguồn mở và khoa học mở.']

```

## Results

![image](https://user-images.githubusercontent.com/44376091/195998681-5860e443-2071-4048-8a2b-873dcee14a72.png)

## Citation
```
@misc{https://doi.org/10.48550/arxiv.2210.05610,
  doi = {10.48550/ARXIV.2210.05610},
  author = {Ngo, Chinh and Trinh, Trieu H. and Phan, Long and Tran, Hieu and Dang, Tai and Nguyen, Hieu and Nguyen, Minh and Luong, Minh-Thang},
  title = {MTet: Multi-domain Translation for English and Vietnamese},
  publisher = {arXiv},
  year = {2022},
}
```