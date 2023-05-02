---
language: id
widget:
- text: "Kapan Einstein melepas kewarganegaraan Jerman?"
  context: "Setelah menghabiskan waktu satu tahun di Praha, Einstein tinggal di Swiss antara tahun 1895 dan 1914, melepas kewarganegaraan Jermannya pada tahun 1896, dan lulus sarjana dari sekolah politeknik federal Swiss (kelak Eidgenössische Technische Hochschule, ETH) di Zürich pada tahun 1900."
---

# IndoBERT-Lite base fine-tuned on Translated SQuAD v2

[IndoBERT-Lite](https://huggingface.co/indobenchmark/indobert-lite-base-p2) trained by [Indo Benchmark](https://www.indobenchmark.com/) and fine-tuned on [Translated SQuAD 2.0](https://github.com/Wikidepia/indonesia_dataset/tree/master/question-answering/SQuAD) for **Q&A** downstream task.

## Model in action

Fast usage with **pipelines**:

```python
from transformers import BertTokenizerFast, pipeline

tokenizer = BertTokenizerFast.from_pretrained(
    'Wikidepia/indobert-lite-squad'
)
qa_pipeline = pipeline(
    "question-answering",
    model="Wikidepia/indobert-lite-squad",
    tokenizer=tokenizer
)

qa_pipeline({
    'context': "Setelah menghabiskan waktu satu tahun di Praha, Einstein tinggal di Swiss antara tahun 1895 dan 1914, melepas kewarganegaraan Jermannya pada tahun 1896, dan lulus sarjana dari sekolah politeknik federal Swiss (kelak Eidgenössische Technische Hochschule, ETH) di Zürich pada tahun 1900.",
    'question': "Kapan Einstein melepas kewarganegaraan Jerman?"
})
```

# Output:

```json
{
   "score":0.9799205660820007,
   "start":147,
   "end":151,
   "answer":"1896"
}
```

README copied from [mrm8488's repository](https://huggingface.co/mrm8488/bert-tiny-finetuned-squadv2)
