---
license: mit
datasets:
- Wannita/PyCoder
- Wannita/PyCoder-Type
metrics:
- accuracy
- bleu
- meteor
- exact_match
- rouge
library_name: transformers
pipeline_tag: text-generation
tags:
- code
- code completion
---
# PyCoder

This repository contains the model for the paper [Syntax-Aware On-the-Fly Code Completion](https://arxiv.org/abs/2211.04673)

The sample code to run the model can be found in directory: "`assets/notebooks/inference.ipynb`" in our GitHub: https://github.com/awsm-research/pycoder.

PyCoder is an auto code completion model which leverage a Multi-Task Training technique (MTT) to cooperatively
learn the code prediction task and the type prediction task. For the type prediction
task, we propose to leverage the standard Python token
type information (e.g., String, Number, Name, Keyword),
which is readily available and lightweight, instead of using
the AST information which requires source code to be parsable for an extraction, limiting its ability to perform on-the-fly code completion (see Section 2.3 in our paper). 

More information can be found in our paper.

If you use our code or PyCoder, please cite our paper.

<pre><code>@article{takerngsaksiri2022syntax,
  title={Syntax-Aware On-the-Fly Code Completion},
  author={Takerngsaksiri, Wannita and Tantithamthavorn, Chakkrit and Li, Yuan-Fang},
  journal={arXiv preprint arXiv:2211.04673},
  year={2022}
}</code></pre>

---
license: mit
datasets:
- Wannita/PyCoder
metrics:
- accuracy
library_name: transformers
pipeline_tag: text-generation
---