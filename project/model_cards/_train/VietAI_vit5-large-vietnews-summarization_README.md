---
language: vi
datasets:
- cc100
tags:
- summarization

license: mit

widget:
- text: "vietnews: VietAI là tổ chức phi lợi nhuận với sứ mệnh ươm mầm tài năng về trí tuệ nhân tạo và xây dựng một cộng đồng các chuyên gia trong lĩnh vực trí tuệ nhân tạo đẳng cấp quốc tế tại Việt Nam."
---

# ViT5-large Finetuned on `vietnews` Abstractive Summarization


State-of-the-art pretrained Transformer-based encoder-decoder model for Vietnamese.
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/vit5-pretrained-text-to-text-transformer-for/abstractive-text-summarization-on-vietnews)](https://paperswithcode.com/sota/abstractive-text-summarization-on-vietnews?p=vit5-pretrained-text-to-text-transformer-for)


## How to use
For more details, do check out [our Github repo](https://github.com/vietai/ViT5) and [eval script](https://github.com/vietai/ViT5/blob/main/eval/Eval_vietnews_sum.ipynb). 

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
​
tokenizer = AutoTokenizer.from_pretrained("VietAI/vit5-large-vietnews-summarization")  
model = AutoModelForSeq2SeqLM.from_pretrained("VietAI/vit5-large-vietnews-summarization")
model.cuda()
​
sentence = "VietAI là tổ chức phi lợi nhuận với sứ mệnh ươm mầm tài năng về trí tuệ nhân tạo và xây dựng một cộng đồng các chuyên gia trong lĩnh vực trí tuệ nhân tạo đẳng cấp quốc tế tại Việt Nam."
text =  "vietnews: " + sentence + " </s>"
encoding = tokenizer(text, return_tensors="pt")
input_ids, attention_masks = encoding["input_ids"].to("cuda"), encoding["attention_mask"].to("cuda")
outputs = model.generate(
    input_ids=input_ids, attention_mask=attention_masks,
    max_length=256,
    early_stopping=True
)
for output in outputs:
    line = tokenizer.decode(output, skip_special_tokens=True, clean_up_tokenization_spaces=True)
    print(line)
```

## Citation
```
@inproceedings{phan-etal-2022-vit5,
    title = "{V}i{T}5: Pretrained Text-to-Text Transformer for {V}ietnamese Language Generation",
    author = "Phan, Long and Tran, Hieu and Nguyen, Hieu and Trinh, Trieu H.",
    booktitle = "Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies: Student Research Workshop",
    year = "2022",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.naacl-srw.18",
    pages = "136--142",
}
```