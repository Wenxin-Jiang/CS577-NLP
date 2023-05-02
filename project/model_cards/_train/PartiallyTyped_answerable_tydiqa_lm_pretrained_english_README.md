# ReadMe

This is a pretrained model based on [gpt2](https://huggingface.co/gpt2) that has been trained on [copenlu/answerable_tydiqa](https://huggingface.co/datasets/copenlu/answerable_tydiqa), specifically the text field of the English samples for 2 epochs.

To use the pretrained head, use: `AutoModelForCausalLM.from_pretrained`.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("PartiallyTyped/answerable_tydiqa_lm_pretrained_japenese")
tokenizer = AutoTokenizer.from_pretrained("rinna/japanese-gpt2-small")

```
