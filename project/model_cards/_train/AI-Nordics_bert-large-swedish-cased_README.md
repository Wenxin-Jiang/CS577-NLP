---
language: sv
---

# A Swedish Bert model

## Model description
This model follows the Bert Large model architecture as implemented in [Megatron-LM framework](https://github.com/NVIDIA/Megatron-LM). It was trained with a batch size of 512 in 600k steps. The model contains following parameters:
<figure>

| Hyperparameter       | Value      |
|----------------------|------------|
| \\(n_{parameters}\\) | 340M |
| \\(n_{layers}\\)     | 24    |
| \\(n_{heads}\\)      | 16         |
| \\(n_{ctx}\\)        | 1024       |
| \\(n_{vocab}\\)        | 30592       |


## Training data
The model is pretrained on a Swedish text corpus of around 85 GB from a variety of sources as shown below.
<figure>

| Dataset       | Genre      | Size(GB)|
|----------------------|------|------|
| Anföranden      | Politics  |0.9|
|DCEP|Politics|0.6|
|DGT|Politics|0.7|
|Fass|Medical|0.6|
|Författningar|Legal|0.1|
|Web data|Misc|45.0|
|JRC|Legal|0.4|
|Litteraturbanken|Books|0.3O|
|SCAR|Misc|28.0|
|SOU|Politics|5.3|
|Subtitles|Drama|1.3|
|Wikipedia|Facts|1.8|


## Intended uses & limitations
The raw model can be used for the usual tasks of masked language modeling or next sentence prediction. It is also often fine-tuned on a downstream task to improve its performance in a specific domain/task.
<br>
<br>

## How to use

```python
from transformers import AutoTokenizer, AutoModelForMaskedLM
tokenizer = AutoTokenizer.from_pretrained("AI-Nordics/bert-large-swedish-cased")
model = AutoModelForMaskedLM.from_pretrained("AI-Nordics/bert-large-swedish-cased")

