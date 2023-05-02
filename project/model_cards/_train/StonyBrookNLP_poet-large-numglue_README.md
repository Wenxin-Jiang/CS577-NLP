---
tags:
- question-answering, multi-step-reasoning, multi-hop-reasoning
thumbnail: https://raw.githubusercontent.com/StonyBrookNLP/teabreac/main/teabreac_icon.png
license: cc-by-4.0
---

# What's this?

This is one of the models reported in the paper: ["Teaching Broad Reasoning Skills for Multi-Step QA by Generating Hard Contexts".](https://arxiv.org/abs/2205.12496).

This paper proposes a procedure to synthetically generate a QA dataset, TeaBReaC, for pretraining language models for robust multi-step reasoning. Pretraining plain LMs like Bart, T5 and numerate LMs like NT5, PReasM, POET on TeaBReaC leads to improvemed downstream performance on several multi-step QA datasets. Please checkout out the paper for the details.

We release the following models:

- **A:** Base Models finetuned on target datasets: `{base_model}-{target_dataset}`
- **B:** Base models pretrained on TeaBReaC: `teabreac-{base_model}`
- **C:** Base models pretrained on TeaBReaC and then finetuned on target datasets: `teabreac-{base_model}-{target_dataset}`

The `base_model` above can be from: `bart-large`, `t5-large`, `t5-3b`, `nt5-small`, `preasm-large`.
The `target_dataset` above can be from: `drop`, `tatqa`, `iirc-gold`, `iirc-retrieved`, `numglue`.

The **A** models are only released for completeness / reproducibility. In your end application you probably just want to use either **B** or **C**.

# How to use it?

Please checkout the details in our [github repository](https://github.com/stonybrooknlp/teabreac), but in a nutshell:

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from digit_tokenization import enable_digit_tokenization # digit_tokenization.py from https://github.com/stonybrooknlp/teabreac

model_name = "StonyBrookNLP/poet-large-numglue"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False) # Fast doesn't work with digit tokenization
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
enable_digit_tokenization(tokenizer)
input_texts = [
    "answer_me: Who scored the first touchdown of the game?" +
    "context: ... Oakland would get the early lead in the first quarter as quarterback JaMarcus Russell completed a 20-yard touchdown pass to rookie wide receiver Chaz Schilens..."
    # Note: some models have slightly different qn/ctxt format. See the github repo.
]
input_ids = tokenizer(
    input_texts, return_tensors="pt",
    truncation=True, max_length=800,
    add_special_tokens=True, padding=True,
)["input_ids"]
generated_ids = model.generate(input_ids, min_length=1,  max_length=50)
generated_predictions = tokenizer.batch_decode(generated_ids, skip_special_tokens=False)
generated_predictions = [
    tokenizer.fix_decoded_text(generated_prediction) for generated_prediction in generated_predictions
]
# => ["Chaz Schilens"]
```