Pre-trained evaluator in EMNLP 2022 paper

*[Towards a Unified Multi-Dimensional Evaluator for Text Generation](https://arxiv.org/abs/2210.07197)*

## Introduction

**Multi-dimensional evaluation** is the dominant paradigm for human evaluation in Natural Language Generation (NLG), i.e., evaluating the generated text from multiple explainable dimensions, such as coherence and fluency.

However, automatic evaluation in NLG is still dominated by similarity-based metrics (e.g., ROUGE, BLEU), but they are not sufficient to portray the difference between the advanced generation models.

Therefore, we propose **UniEval** to bridge this gap so that a more comprehensive and fine-grained evaluation of NLG systems can be achieved.

## Pre-trained Evaluator

**unieval-intermediate** is a pre-trained Boolean Answer Generator after performing intermediate multi-task learning. On top of this checkpoint, you can also train a custom evaluator for a specific NLG task.

## Usage 

Please refer to [our GitHub repository](https://github.com/maszhongming/UniEval).