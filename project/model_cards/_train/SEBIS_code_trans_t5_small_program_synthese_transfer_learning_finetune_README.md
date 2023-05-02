---
tags:
- summarization
widget:
- text: "you are given an array of numbers a and a number b , compute the difference of elements in a and b"

---


# CodeTrans model for program synthesis

## Table of Contents
- [Model Details](#model-details)
- [How to Get Started With the Model](#how-to-get-started-with-the-model)
- [Uses](#uses)
- [Risks, Limitations and Biases](#risks-limitations-and-biases)
- [Training](#training)
- [Evaluation](#evaluation)
- [Environmental Impact](#environmental-impact)
- [Citation Information](#citation-information)

## Model Details
- **Model Description:** This CodeTrans model is based on the `t5-small` model. It has its own SentencePiece vocabulary model. It used transfer-learning pre-training on 7 unsupervised datasets in the software development domain. It is then fine-tuned on the program synthesis task for the lisp inspired DSL code.
- **Developed by:** [Ahmed Elnaggar](https://www.linkedin.com/in/prof-ahmed-elnaggar/),[Wei Ding](https://www.linkedin.com/in/wei-ding-92561270/)
- **Model Type:** Summarization
- **Language(s):** English
- **License:** Unknown
- **Resources for more information:**
	- [Research Paper](https://arxiv.org/pdf/2104.02443.pdf)
    - [GitHub Repo](https://github.com/agemagician/CodeTrans)


## How to Get Started With the Model

Here is how to use this model to generate lisp inspired DSL code using Transformers SummarizationPipeline:

```python
from transformers import AutoTokenizer, AutoModelWithLMHead, SummarizationPipeline

pipeline = SummarizationPipeline(
    model=AutoModelWithLMHead.from_pretrained("SEBIS/code_trans_t5_small_program_synthese_transfer_learning_finetune"),
    tokenizer=AutoTokenizer.from_pretrained("SEBIS/code_trans_t5_small_program_synthese_transfer_learning_finetune", skip_special_tokens=True),
    device=0
)

tokenized_code = "you are given an array of numbers a and a number b , compute the difference of elements in a and b"
pipeline([tokenized_code])
```
Run this example in [colab notebook](https://github.com/agemagician/CodeTrans/blob/main/prediction/multitask/transfer%20learning%20fine-tuning/small_model.ipynb).
## Training data

The supervised training tasks datasets can be downloaded on [Link](https://www.dropbox.com/sh/488bq2of10r4wvw/AACs5CGIQuwtsD7j_Ls_JAORa/finetuning_dataset?dl=0&subfolder_nav_tracking=1)




## Uses

#### Direct Use

The model could be used to generate lisp inspired DSL code given the human language description tasks.

## Risks, Limitations and Biases


As detailed in this model’s [publication](https://arxiv.org/pdf/2104.02443.pdf), this model makes use of the data-set [One Billion Word Language Model Benchmark corpus](https://www.researchgate.net/publication/259239818_One_Billion_Word_Benchmark_for_Measuring_Progress_in_Statistical_Language_Modeling) in order to gather the self-supervised English data samples. 

Significant research has explored bias and fairness issues with language models (see, e.g., [Sheng et al. (2021)](https://aclanthology.org/2021.acl-long.330.pdf) and [Bender et al. (2021)](https://dl.acm.org/doi/pdf/10.1145/3442188.3445922)).
As such, it should be noted that language models that are pretrained from text corpus such as the One Billion Word Word Language Model Benchmark corpus have been further explored (e.g by  [Ngo, Helen & Araújo et al(2021)](https://www.researchgate.net/publication/355582954_No_News_is_Good_News_A_Critique_of_the_One_Billion_Word_Benchmark) reports that the One Billion Word Word Language Model Benchmark corpus
> “generate text in the linguistic style of news, without any grounding in the real world. In addition to potential harms from models which are inadvertently optimized for generating fake news.” 

The aforementioned publication continues to warn that the One Billion Word Word Language Model Benchmark corpus
> contains sentences which contain words commonly found on blocklists. While these sentences may have plausibly been used in expository contexts within the article, the destructive sentence-level preprocessing and shuffling applied to lm1b [One Billion Word Word Language Model Benchmark corpus] removes all long-range structure from the text and makes it infeasible to track the context and intent of individual examples. 

[Ngo, Helen & Araújo et al(2021)](https://www.researchgate.net/publication/355582954_No_News_is_Good_News_A_Critique_of_the_One_Billion_Word_Benchmark)

## Training

#### Training Data

The supervised training tasks datasets can be downloaded on [Link](https://www.dropbox.com/sh/488bq2of10r4wvw/AACs5CGIQuwtsD7j_Ls_JAORa/finetuning_dataset?dl=0&subfolder_nav_tracking=1)

The authors provide additionally notes about the vocabulary used, in the [associated paper](https://arxiv.org/pdf/2104.02443.pdf): 

> We used the SentencePiece model (Kudo, 2018) to construct the vocabulary for this research, as well as to decode and encode the input/output.


## Training procedure

#### Preprocessing

##### Transfer-learning Pretraining

The model was trained on a single TPU Pod V3-8 for 500,000 steps in total, using sequence length 512 (batch size 4096).
It has a total of approximately 220M parameters and was trained using the encoder-decoder architecture.
The optimizer used is AdaFactor with inverse square root learning rate schedule for pre-training.

###### Fine-tuning

This model was then fine-tuned on a single TPU Pod V2-8 for 5,000 steps in total, using sequence length 512 (batch size 256), using only the dataset only containing lisp inspired DSL data.


## Evaluation

#### Results

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


## Environmental Impact

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700). We present the hardware type based on the [associated paper](https://arxiv.org/pdf/2105.09680.pdf).


- **Hardware Type:** Nvidia RTX 8000 GPUs

- **Hours used:** Unknown

- **Cloud Provider:** GCC TPU v2-8 and v3-8. 

- **Compute Region:** Unknown

- **Carbon Emitted:** Unknown 

## Citation Information

```bibtex
@misc{elnaggar2021codetrans,
      title={CodeTrans: Towards Cracking the Language of Silicon's Code Through Self-Supervised Deep Learning and High Performance Computing}, 
      author={Ahmed Elnaggar and Wei Ding and Llion Jones and Tom Gibbs and Tamas Feher and Christoph Angerer and Silvia Severini and Florian Matthes and Burkhard Rost},
      year={2021},
      eprint={2104.02443},
      archivePrefix={arXiv},
      primaryClass={cs.SE}
}
```


