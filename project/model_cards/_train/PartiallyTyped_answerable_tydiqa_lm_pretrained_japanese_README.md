# ReadMe

This is a pretrained model based on [rinna/japanese-gpt2-small](https://huggingface.co/rinna/japanese-gpt2-small) that has been trained on [copenlu/answerable_tydiqa](https://huggingface.co/datasets/copenlu/answerable_tydiqa), specifically the text field of the Japanese samples for 2 epochs.

To use the pretrained head, use: `AutoModelForCausalLM.from_pretrained`.

```python
from transformers import AutoModelForCausalLM, T5Tokenizer

model_path = "PartiallyTyped/answerable_tydiqa_lm_pretrained_japanese"
model = AutoModelForCausalLM.from_pretrained(path)
tokenizer = T5Tokenizer.from_pretrained(path)
tokenizer.do_lower_case = True  # due to some bug of tokenizer config loading

```