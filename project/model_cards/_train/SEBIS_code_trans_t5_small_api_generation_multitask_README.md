---
tags:
- summarization
widget:
- text: "parse the uses licence node of this package , if any , and returns the license definition if theres"

---


# CodeTrans model for api recommendation generation
Pretrained model for api recommendation generation using the t5 small model architecture. It was first released in
[this repository](https://github.com/agemagician/CodeTrans). 


## Model description

This CodeTrans model is based on the `t5-small` model. It has its own SentencePiece vocabulary model. It used multi-task training on 13 supervised tasks in the software development domain and 7 unsupervised datasets.

## Intended uses & limitations

The model could be used to generate api usage for the java programming tasks. 

### How to use

Here is how to use this model to generate java function documentation using Transformers SummarizationPipeline:

```python
from transformers import AutoTokenizer, AutoModelWithLMHead, SummarizationPipeline

pipeline = SummarizationPipeline(
    model=AutoModelWithLMHead.from_pretrained("SEBIS/code_trans_t5_small_api_generation_multitask"),
    tokenizer=AutoTokenizer.from_pretrained("SEBIS/code_trans_t5_small_api_generation_multitask", skip_special_tokens=True),
    device=0
)

tokenized_code = "parse the uses licence node of this package , if any , and returns the license definition if theres"
pipeline([tokenized_code])
```
Run this example in [colab notebook](https://github.com/agemagician/CodeTrans/blob/main/prediction/multitask/pre-training/api%20generation/small_model.ipynb).
## Training data

The supervised training tasks datasets can be downloaded on [Link](https://www.dropbox.com/sh/488bq2of10r4wvw/AACs5CGIQuwtsD7j_Ls_JAORa/finetuning_dataset?dl=0&subfolder_nav_tracking=1)


## Training procedure

### Multi-task Pretraining

The model was trained on a single TPU Pod V3-8 for 500,000 steps in total, using sequence length 512 (batch size 4096).
It has a total of approximately 220M parameters and was trained using the encoder-decoder architecture.
The optimizer used is AdaFactor with inverse square root learning rate schedule for pre-training.


## Evaluation results

For the code documentation tasks, different models achieves the following results on different programming languages (in BLEU score):

Test results :

|   Language / Model   |      Java      |
| -------------------- | :------------: |
|   CodeTrans-ST-Small    |     68.71      |
|   CodeTrans-ST-Base     |     70.45      |
|   CodeTrans-TF-Small    |     68.90      |
|   CodeTrans-TF-Base     |     72.11      |
|   CodeTrans-TF-Large    |     73.26      |
|   CodeTrans-MT-Small    |     58.43      |
|   CodeTrans-MT-Base     |     67.97      |
|   CodeTrans-MT-Large    |     72.29      |
|   CodeTrans-MT-TF-Small |     69.29      |
|   CodeTrans-MT-TF-Base  |     72.89      |
|   CodeTrans-MT-TF-Large |   **73.39**    |
|   State of the art   |     54.42      |



> Created by [Ahmed Elnaggar](https://twitter.com/Elnaggar_AI) | [LinkedIn](https://www.linkedin.com/in/prof-ahmed-elnaggar/) and Wei Ding | [LinkedIn](https://www.linkedin.com/in/wei-ding-92561270/)

