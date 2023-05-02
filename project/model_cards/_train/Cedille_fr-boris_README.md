---
language: fr
license: mit
tags:
- pytorch
- causal-lm
datasets:
- c4
---

# Cedille AI
Cedille is a project to bring large language models to non-English languages.

## fr-boris
Boris is a 6B parameter autoregressive language model based on the GPT-J architecture and trained using the [mesh-transformer-jax](https://github.com/kingoflolz/mesh-transformer-jax) codebase.

Boris was trained on around 78B tokens of French text from the [C4](https://huggingface.co/datasets/c4) dataset. We started training from GPT-J, which has been trained on [The Pile](https://pile.eleuther.ai/). As a consequence the model still has good performance in English language. Boris makes use of the unmodified GPT-2 tokenizer.

Boris is named after the great French writer [Boris Vian](https://en.wikipedia.org/wiki/Boris_Vian).

# How do I test Cedille?
For the time being, the easiest way to test the model is to use our [publicly accessible playground](https://en.cedille.ai/).

Cedille is a relatively large model and running it in production can get expensive. Consider contacting us for API access at hello@cedille.ai.


## 📊 Cedille paper
Our paper is out now! https://arxiv.org/abs/2202.03371

Thanks for citing our work if you make use of Cedille
```bibtex
@misc{muller2022cedille,
      title={Cedille: A large autoregressive French language model}, 
      author={Martin M{\"{u}}ller and Florian Laurent},
      year={2022},
      eprint={2202.03371},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

## Contact us
For any custom development please contact us at hello@cedille.ai.

## Links
* [Official website](https://en.cedille.ai/)
* [Blog](https://en.cedille.ai/blog)
* [GitHub](https://github.com/coteries/cedille-ai)
* [Twitter](https://twitter.com/CedilleAI)

