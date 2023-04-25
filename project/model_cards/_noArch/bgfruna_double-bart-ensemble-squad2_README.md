---
language: en
tags:
- pytorch
- question-answering
datasets:
- squad_v2
- squad2
license: cc-by-4.0
metrics:
- squad_v2
- exact
- f1
widget:
- text: "By what main attribute are computational problems classified utilizing computational complexity theory?"
  context: "Computational complexity theory is a branch of the theory of computation in theoretical computer science that focuses on classifying computational problems according to their inherent difficulty, and relating those classes to each other. A computational problem is understood to be a task that is in principle amenable to being solved by a computer, which is equivalent to stating that the problem may be solved by mechanical application of mathematical steps, such as an algorithm."
---

# Performance
This ensemble was evaluated on [SQuAD 2.0](https://huggingface.co/datasets/squad_v2) with the following results:

```
{'HasAns_exact': 52.5472334682861,
 'HasAns_f1': 67.94939813758602,
 'HasAns_total': 5928,
 'NoAns_exact': 91.75777964676199,
 'NoAns_f1': 91.75777964676199,
 'NoAns_total': 5945,
 'best_exact': 72.16373283921503,
 'best_exact_thresh': 0.0,
 'best_f1': 79.85378860941708,
 'best_f1_thresh': 0.0,
 'exact': 72.1805777815211,
 'f1': 79.87063355172326,
 'total': 11873
 }
 ```