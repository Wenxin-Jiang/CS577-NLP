Pre-trained evaluator in EMNLP 2022 paper

*[Towards a Unified Multi-Dimensional Evaluator for Text Generation](https://arxiv.org/abs/2210.07197)*

## Introduction

**Multi-dimensional evaluation** is the dominant paradigm for human evaluation in Natural Language Generation (NLG), i.e., evaluating the generated text from multiple explainable dimensions, such as coherence and fluency.

However, automatic evaluation in NLG is still dominated by similarity-based metrics (e.g., ROUGE, BLEU), but they are not sufficient to portray the difference between the advanced generation models.

Therefore, we propose **UniEval** to bridge this gap so that a more comprehensive and fine-grained evaluation of NLG systems can be achieved.

## Pre-trained Evaluator

**unieval-sum** is the pre-trained evaluator for the text summarization task. It can evaluate the model output from four dimensions:
- *coherence*
- *consistency*
- *fluency*
- *relevance*

It can also be transferred to the new dimensions and generation tasks, such as *naturalness* and *informativeness* for data-to-text.

## Usage 

Please refer to [our GitHub repository](https://github.com/maszhongming/UniEval).