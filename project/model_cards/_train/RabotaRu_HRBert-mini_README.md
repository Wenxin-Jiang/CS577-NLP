---

language: ["ru", "en", "be", "bg", "uk", "ro", "kz", "tg", "tat", "sv", "sl", "sr", "uz", "es", "fi"]

tags:

- russian

- fill-mask

- pretraining

- embeddings

- masked-lm


license: mit

widget:

- text: "<mask> на склад"

---

!!! 
At the moment, the model is distilled, a version from one of the first checkpoints is available for download.
We plan to post the full model in the next few days.
!!!

This is a distilled HRBert model for an mlm task.


Sentence embeddings can be produced as follows:

```python

# pip install transformers

from transformers import pipeline


fill_mask = pipeline(
    "fill-mask",
    model='RabotaRu/HRBert-mini',
    tokenizer='RabotaRu/HRBert-mini'
)

fill_mask('<mask> на склад')
```