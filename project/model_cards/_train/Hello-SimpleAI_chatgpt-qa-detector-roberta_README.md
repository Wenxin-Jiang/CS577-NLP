---
datasets:
- Hello-SimpleAI/HC3
language:
- en
pipeline_tag: text-classification
tags:
- chatgpt
---

# Model Card for `Hello-SimpleAI/chatgpt-qa-detector-roberta`

This model is trained on `question-answer` pairs of **the filtered full-text** from [Hello-SimpleAI/HC3](https://huggingface.co/datasets/Hello-SimpleAI/HC3).

More details refer to [arxiv: 2301.07597](https://arxiv.org/abs/2301.07597) and Gtihub project [Hello-SimpleAI/chatgpt-comparison-detection](https://github.com/Hello-SimpleAI/chatgpt-comparison-detection).


The base checkpoint is [roberta-base](https://huggingface.co/roberta-base).
We train it with all [Hello-SimpleAI/HC3](https://huggingface.co/datasets/Hello-SimpleAI/HC3) data (without held-out) for 1 epoch.

(1-epoch is consistent with the experiments in [our paper](https://arxiv.org/abs/2301.07597).)

## Citation

Checkout this papaer [arxiv: 2301.07597](https://arxiv.org/abs/2301.07597)

```
@article{guo-etal-2023-hc3,
    title = "How Close is ChatGPT to Human Experts? Comparison Corpus, Evaluation, and Detection",
    author = "Guo, Biyang  and
      Zhang, Xin  and
      Wang, Ziyuan  and
      Jiang, Minqi  and
      Nie, Jinran  and
      Ding, Yuxuan  and
      Yue, Jianwei  and
      Wu, Yupeng",
    journal={arXiv preprint arxiv:2301.07597}
    year = "2023",
}
```
