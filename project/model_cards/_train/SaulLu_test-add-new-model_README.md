# HTLM

Pretraining Dataset: 23TB of simplified HTML extracted from common crawl dumps

Paper: [HTLM: Hyper-Text Pre-Training and Prompting of Language Models](https://arxiv.org/abs/2107.06955)

Authors: Armen Aghajanyan, Dmytro Okhonko, Mike Lewis, Mandar Joshi, Hu Xu, Gargi Ghosh, Luke Zettlemoyer

Disclaimer: The team releasing BERT did not write a model card for this model so this model card has been written by the Hugging Face team.

## Abstract

We introduce HTLM, a hyper-text language model trained on a large-scale web crawl. Modeling hyper-text has a number of advantages: (1) it is easily gathered at scale, (2) it provides rich document-level and end-task-adjacent supervision (e.g. class and id attributes often encode document category information), and (3) it allows for new structured prompting that follows the established semantics of HTML (e.g. to do zero-shot summarization by infilling title tags for a webpage that contains the input text). We show that pretraining with a BART-style denoising loss directly on simplified HTML provides highly effective transfer for a wide range of end tasks and supervision levels. HTLM matches or exceeds the performance of comparably sized text-only LMs for zero-shot prompting and fine-tuning for classification benchmarks, while also setting new state-of-the-art performance levels for zero-shot summarization. We also find that hyper-text prompts provide more value to HTLM, in terms of data efficiency, than plain text prompts do for existing LMs, and that HTLM is highly effective at auto-prompting itself, by simply generating the most likely hyper-text formatting for any available training data. We will release all code and models to support future HTLM research. 

## Usage

For the moment you can use it as is to do a classic Mask Filling task (see snippet bellow) or fine-tune it on a downstream task.

```
from transformers import BartTokenizer, BartForConditionalGeneration

TXT = "My friends are <mask> but they eat too many carbs."
model_name = "SaulLu/test-add-new-model"

tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

input_ids = tokenizer([TXT], return_tensors='pt')['input_ids']
logits = model(input_ids).logits
masked_index = (input_ids[0] == tokenizer.mask_token_id).nonzero().item()
probs = logits[0, masked_index].softmax(dim=0)
values, predictions = probs.topk(5)
tokenizer.decode(predictions).split()
```