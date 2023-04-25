---
language: 
  - en
tags:
- masked-lm
- pytorch
pipeline-tag: "fill-mask"
mask-token: "[MASK]"
widget:
- text: "The present [MASK] provides a torque sensor that is small and highly rigid and for which high production efficiency is possible."
- text: "The present invention relates to [MASK] accessories and pertains particularly to a brake light unit for bicycles."
- text: "The present invention discloses a space-bound-free [MASK] and its coordinate determining circuit for determining a coordinate of a stylus pen."
- text: "The illuminated [MASK] includes a substantially translucent canopy supported by a plurality of ribs pivotally swingable towards and away from a shaft."
license: apache-2.0
metrics:
- perplexity

---

# BERT for Patents

BERT for Patents is a model trained by Google on 100M+ patents (not just US patents). It is based on BERT<sub>LARGE</sub>.

If you want to learn more about the model, check out the [blog post](https://cloud.google.com/blog/products/ai-machine-learning/how-ai-improves-patent-analysis), [white paper](https://services.google.com/fh/files/blogs/bert_for_patents_white_paper.pdf) and [GitHub page](https://github.com/google/patents-public-data/blob/master/models/BERT%20for%20Patents.md) containing the original TensorFlow checkpoint.

---

### Projects using this model (or variants of it):
- [Patents4IPPC](https://github.com/ec-jrc/Patents4IPPC) (carried out by [Pi School](https://picampus-school.com/) and commissioned by the [Joint Research Centre (JRC)](https://ec.europa.eu/jrc/en) of the European Commission)
