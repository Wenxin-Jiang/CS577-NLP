---
license: apache-2.0
---

# Model description

This is an [t5-base](https://huggingface.co/t5-base) model, finetuned to generate questions given a table and linked passages using [HybridQA](https://huggingface.co/datasets/hybrid_qa) dataset. It was trained to generate questions from reasoning paths extracted from hybrid input, i.e., a table and the passages linked to the table cells. 

# Overview

*Language model*: t5-base \
*Language*: English \
*Task*: Hybrid Question Generation \
*Data*: HybridQA

# Intented use and limitations
One can use this model to generate questions given a table and linked passages. Biases associated with pre-training of T5 and HybridQA dataset may be present.
