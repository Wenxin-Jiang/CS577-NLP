---
tags:
- summarization
widget:
- text: "you are given an array of numbers a and a number b , compute the difference of elements in a and b"

---


# CodeTrans model for program synthesis
Pretrained model on programming language lisp inspired DSL using the t5 large model architecture. It was first released in
[this repository](https://github.com/agemagician/CodeTrans). 


## Model description

This CodeTrans model is based on the `t5-large` model. It has its own SentencePiece vocabulary model. It used multi-task training on 13 supervised tasks in the software development domain and 7 unsupervised datasets.

## Intended uses & limitations

The model could be used to generate lisp inspired DSL code given the human language description tasks.

### How to use

Here is how to use this model to generate lisp inspired DSL code using Transformers SummarizationPipeline:

```python
from transformers import AutoTokenizer, AutoModelWithLMHead, SummarizationPipeline

pipeline = SummarizationPipeline(
    model=AutoModelWithLMHead.from_pretrained("SEBIS/code_trans_t5_large_program_synthese_multitask"),
    tokenizer=AutoTokenizer.from_pretrained("SEBIS/code_trans_t5_large_program_synthese_multitask", skip_special_tokens=True),
    device=0
)

tokenized_code = "you are given an array of numbers a and a number b , compute the difference of elements in a and b"
pipeline([tokenized_code])
```
Run this example in [colab notebook](https://github.com/agemagician/CodeTrans/blob/main/prediction/multitask/pre-training/program%20synthesis/large_model.ipynb).
## Training data

The supervised training tasks datasets can be downloaded on [Link](https://www.dropbox.com/sh/488bq2of10r4wvw/AACs5CGIQuwtsD7j_Ls_JAORa/finetuning_dataset?dl=0&subfolder_nav_tracking=1)


## Training procedure

### Multi-task Pretraining

The model was trained on a single TPU Pod V3-8 for 220,000 steps in total, using sequence length 512 (batch size 4096).
It has a total of approximately 220M parameters and was trained using the encoder-decoder architecture.
The optimizer used is AdaFactor with inverse square root learning rate schedule for pre-training.


## Evaluation results

For the code documentation tasks, different models achieves the following results on different programming languages (in BLEU score):

Test results :

|   Language / Model   |      LISP      |
| -------------------- | :------------: |
|   CodeTrans-ST-Small    |     89.43      |
|   CodeTrans-ST-Base     |     89.65      |
|   CodeTrans-TF-Small    |     90.30      |
|   CodeTrans-TF-Base     |     90.24      |
|   CodeTrans-TF-Large    |     90.21      |
|   CodeTrans-MT-Small    |     82.88      |
|   CodeTrans-MT-Base     |     86.99      |
|   CodeTrans-MT-Large    |     90.27      |
|   CodeTrans-MT-TF-Small |   **90.31**    |
|   CodeTrans-MT-TF-Base  |     90.30      |
|   CodeTrans-MT-TF-Large |     90.17      |
|   State of the art   |     85.80      |



> Created by [Ahmed Elnaggar](https://twitter.com/Elnaggar_AI) | [LinkedIn](https://www.linkedin.com/in/prof-ahmed-elnaggar/) and Wei Ding | [LinkedIn](https://www.linkedin.com/in/wei-ding-92561270/)

