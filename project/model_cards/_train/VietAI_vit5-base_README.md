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

# ViT5-base

State-of-the-art pretrained Transformer-based encoder-decoder model for Vietnamese.

## How to use
For more details, do check out [our Github repo](https://github.com/vietai/ViT5). 

[Finetunning Example can be found here](https://github.com/vietai/ViT5/tree/main/finetunning_huggingface).

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
​
tokenizer = AutoTokenizer.from_pretrained("VietAI/vit5-base")  
model = AutoModelForSeq2SeqLM.from_pretrained("VietAI/vit5-base")
model.cuda()
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