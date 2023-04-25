---
inference: false
language:
- bg
license: mit
datasets:
- oscar
- chitanka
- wikipedia
tags:
- torch
---

# GPT-2

Pretrained model on Bulgarian language using a causal language modeling (CLM) objective. It was introduced in
[this paper](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
and first released at [this page](https://openai.com/blog/better-language-models/).

## Model description

This is the **SMALL** version compressed via [progressive module replacing](https://arxiv.org/abs/2002.02925).

The compression was executed on Bulgarian text from [OSCAR](https://oscar-corpus.com/post/oscar-2019/), [Chitanka](https://chitanka.info/) and [Wikipedia](https://bg.wikipedia.org/).

## Intended uses & limitations

You can use the raw model for: 
- text generation
- auto-complete
- spelling correction

Or fine-tune it to a downstream task.

### How to use

Here is how to use this model in PyTorch:

```python
>>> from transformers import AutoModel, AutoTokenizer
>>>
>>> model_id = "rmihaylov/gpt2-small-theseus-bg"
>>> tokenizer = AutoTokenizer.from_pretrained(model_id)
>>> model = AutoModel.from_pretrained(model_id, trust_remote_code=True)
>>>
>>> input_ids = tokenizer.encode(
>>>     "Здравей,", 
>>>     add_special_tokens=False, 
>>>     return_tensors='pt')
>>>
>>> output_ids = model.generate(
>>>     input_ids, 
>>>     do_sample=True, 
>>>     max_length=50, 
>>>     top_p=0.92, 
>>>     pad_token_id=2,
>>>     top_k=0)
>>>
>>> output = tokenizer.decode(output_ids[0])
>>>
>>> output = output.replace('<|endoftext|>', '\n\n\n')
>>> output = output.replace('<|unknown|>', '')
>>> output = output.replace('▁', ' ')
>>> output = output.replace('<|n|>', '\n')
>>>
>>> print(output)

Здравей, извинявай, но не мога да заспя. 
 Джини се обърна и забеляза колко са прегърнати. 
 — Почакай, Джини. Не мога да повярвам, че е възможно! Толкова искам да те видя. 
 — Обеща
```

### Limitations and bias

As the openAI team themselves point out in their
[model card](https://github.com/openai/gpt-2/blob/master/model_card.md#out-of-scope-use-cases):

> Because large-scale language models like GPT-2 do not distinguish fact from fiction, we don’t support use-cases
> that require the generated text to be true.
>
> Additionally, language models like GPT-2 reflect the biases inherent to the systems they were trained on, so we do
> not recommend that they be deployed into systems that interact with humans > unless the deployers first carry out a
> study of biases relevant to the intended use-case. We found no statistically significant difference in gender, race,
> and religious bias probes between 774M and 1.5B, implying all versions of GPT-2 should be approached with similar
> levels of caution around use cases that are sensitive to biases around human attributes.