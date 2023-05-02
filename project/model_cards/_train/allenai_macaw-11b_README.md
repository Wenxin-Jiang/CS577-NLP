---
language: en
widget:
- text: $answer$ ; $mcoptions$ ; $question$ = What is the color of a cloudy sky?
license: apache-2.0
---

# macaw-11b

## Model description

Macaw (<b>M</b>ulti-<b>a</b>ngle <b>c</b>(q)uestion <b>a</b>ns<b>w</b>ering) is a ready-to-use model capable of 
general question answering, 
showing robustness outside the domains it was trained on. It has been trained in "multi-angle" fashion, 
which means it can handle a flexible set of input and output "slots" 
(question, answer, multiple-choice options, context, and explanation) .

Macaw was built on top of [T5](https://github.com/google-research/text-to-text-transfer-transformer) and comes in 
three sizes: [macaw-11b](https://huggingface.co/allenai/macaw-11b), [macaw-3b](https://huggingface.co/allenai/macaw-3b), 
and [macaw-large](https://huggingface.co/allenai/macaw-large), as well as an answer-focused version featured on 
various leaderboards [macaw-answer-11b](https://huggingface.co/allenai/macaw-answer-11b).

See https://github.com/allenai/macaw for more details.

## Intended uses & limitations

#### How to use

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("allenai/macaw-11b")
model = AutoModelForSeq2SeqLM.from_pretrained("allenai/macaw-11b")
input_string = "$answer$ ; $mcoptions$ ; $question$ = What is the color of a cloudy sky?"
input_ids = tokenizer.encode(input_string, return_tensors="pt")
output = model.generate(input_ids, max_length=200)

>>> tokenizer.batch_decode(output, skip_special_tokens=True)
['$answer$ = gray ; $mcoptions$ = (A) blue (B) white (C) grey (D) black']
```

### BibTeX entry and citation info

```bibtex
@article{Tafjord2021Macaw,
  title={General-Purpose Question-Answering with {M}acaw},
  author={Oyvind Tafjord and Peter Clark},
  journal={ArXiv},
  year={2021},
  volume={abs/2109.02593}
}
```