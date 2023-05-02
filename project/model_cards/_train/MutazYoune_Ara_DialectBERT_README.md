---
language: ar
datasets:
- HARD-Arabic-Dataset
---
# Ara-dialect-BERT
We used a pretrained model to further train it on [HARD-Arabic-Dataset](https://github.com/elnagara/HARD-Arabic-Dataset), the weights were initialized using [CAMeL-Lab](https://huggingface.co/CAMeL-Lab/bert-base-camelbert-msa-eighth) "bert-base-camelbert-msa-eighth" model


### Usage
The model weights can be loaded using `transformers` library by HuggingFace.
```python
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("MutazYoune/Ara_DialectBERT")
model = AutoModel.from_pretrained("MutazYoune/Ara_DialectBERT")
```
Example using `pipeline`:
```python
from transformers import pipeline
fill_mask = pipeline(
    "fill-mask",
    model="MutazYoune/Ara_DialectBERT",
    tokenizer="MutazYoune/Ara_DialectBERT"
)
fill_mask("الفندق جميل و لكن [MASK] بعيد")
```
```python
{'sequence': 'الفندق جميل و لكن الموقع بعيد', 'score': 0.28233852982521057, 'token': 3221, 'token_str': 'الموقع'}
{'sequence': 'الفندق جميل و لكن موقعه بعيد', 'score': 0.24436227977275848, 'token': 19218, 'token_str': 'موقعه'}
{'sequence': 'الفندق جميل و لكن المكان بعيد', 'score': 0.15372352302074432, 'token': 5401, 'token_str': 'المكان'}
{'sequence': 'الفندق جميل و لكن الفندق بعيد', 'score': 0.029026474803686142, 'token': 11133, 'token_str': 'الفندق'}
{'sequence': 'الفندق جميل و لكن مكانه بعيد', 'score': 0.024554792791604996, 'token': 10701, 'token_str': 'مكانه'}
