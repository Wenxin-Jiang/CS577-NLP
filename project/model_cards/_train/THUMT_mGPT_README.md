
# mGPT

mGPT is pre-trained on the [mC4 dataset](https://huggingface.co/datasets/mc4) using a causal language modeling objective. It was introduced in this [paper](https://arxiv.org/abs/2110.06609) and first released on this page.

## Model description

mGPT is a Transformer-based model which pre-trained on massive multilingual data covering over 101 languages. Similar to GPT-2, It was pre-trained on the raw texts only, with no human labeling. We use the same tokenization and vocabulary as the [mT5 model](https://huggingface.co/google/mt5-base).

## Intended uses

You can use the raw model for text generation or using prompts for adapting it to a downstream task.

## How to use

You can use this model directly with a pipeline for text generation.  Here is how to use this model to get the features of a given text in PyTorch:

```python
from transformers import MT5Tokenizer, GPT2LMHeadModel, TextGenerationPipeline

tokenizer = MT5Tokenizer.from_pretrained("THUMT/mGPT")
model = GPT2LMHeadModel.from_pretrained("THUMT/mGPT")

pipeline = TextGenerationPipeline(model=model, tokenizer=tokenizer)
text = "Replace me by any text you'd like."
text = pipeline(text, do_sample=True,  max_length=1024)[0]["generated_text"]
```

## Preprocessing

The texts are tokenized using `sentencepiece` and a vocabulary size of 250,100. The inputs are sequences of 1,024 consecutive tokens. We use `<extra_id_0>` to separate lines in a document.

## BibTeX entry and citation info

```bibtex
@misc{tan2021msp,
    title={MSP: Multi-Stage Prompting for Making Pre-trained Language Models Better Translators},
    author={Zhixing Tan and Xiangwen Zhang and Shuo Wang and Yang Liu},
    year={2021},
    eprint={2110.06609},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```
