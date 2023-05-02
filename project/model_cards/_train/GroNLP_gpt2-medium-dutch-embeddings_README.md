---
language: nl
tags:
- adaption
- recycled
- gpt2-medium
pipeline_tag: text-generation
---

# GPT-2 recycled for Dutch (medium, adapted lexical embeddings)
[Wietse de Vries](https://www.semanticscholar.org/author/Wietse-de-Vries/144611157) •
[Malvina Nissim](https://www.semanticscholar.org/author/M.-Nissim/2742475)

## Model description

This model is based on the medium OpenAI GPT-2 ([`gpt2-medium`](https://huggingface.co/gpt2-medium)) model.

The Transformer layer weights in this model are identical to the original English, model but the lexical layer has been retrained for a Dutch vocabulary.

For details, check out our paper on [arXiv](https://arxiv.org/abs/2012.05628) and the code on [Github](https://github.com/wietsedv/gpt2-recycle).


## Related models

### Dutch
 - [`gpt2-small-dutch-embeddings`](https://huggingface.co/GroNLP/gpt2-small-dutch-embeddings): Small model size with only retrained lexical embeddings.
 - [`gpt2-small-dutch`](https://huggingface.co/GroNLP/gpt2-small-dutch):  Small model size with retrained lexical embeddings and additional fine-tuning of the full model. (**Recommended**)
 - [`gpt2-medium-dutch-embeddings`](https://huggingface.co/GroNLP/gpt2-medium-dutch-embeddings): Medium model size with only retrained lexical embeddings.

### Italian
 - [`gpt2-small-italian-embeddings`](https://huggingface.co/GroNLP/gpt2-small-italian-embeddings): Small model size with only retrained lexical embeddings.
 - [`gpt2-small-italian`](https://huggingface.co/GroNLP/gpt2-small-italian):  Small model size with retrained lexical embeddings and additional fine-tuning of the full model. (**Recommended**)
 - [`gpt2-medium-italian-embeddings`](https://huggingface.co/GroNLP/gpt2-medium-italian-embeddings): Medium model size with only retrained lexical embeddings.


## How to use

```python
from transformers import pipeline

pipe = pipeline("text-generation", model="GroNLP/gpt2-medium-dutch-embeddings")
```

```python
from transformers import AutoTokenizer, AutoModel, TFAutoModel

tokenizer = AutoTokenizer.from_pretrained("GroNLP/gpt2-medium-dutch-embeddings")
model = AutoModel.from_pretrained("GroNLP/gpt2-medium-dutch-embeddings")  # PyTorch
model = TFAutoModel.from_pretrained("GroNLP/gpt2-medium-dutch-embeddings")  # Tensorflow
```

## BibTeX entry

```bibtex
@misc{devries2020good,
      title={As good as new. How to successfully recycle English GPT-2 to make models for other languages}, 
      author={Wietse de Vries and Malvina Nissim},
      year={2020},
      eprint={2012.05628},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```