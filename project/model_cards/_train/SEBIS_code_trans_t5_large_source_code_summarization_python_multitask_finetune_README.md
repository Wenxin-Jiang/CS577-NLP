---
tags:
- summarization
widget:
- text: '''with open ( CODE_STRING , CODE_STRING ) as in_file : buf = in_file . readlines ( )  with open ( CODE_STRING , CODE_STRING ) as out_file : for line in buf :          if line ==   " ; Include this text   " :              line = line +   " Include below  "          out_file . write ( line ) '''

---



# CodeTrans model for source code summarization python
Pretrained model on programming language python using the t5 large model architecture. It was first released in
[this repository](https://github.com/agemagician/CodeTrans). This model is trained on tokenized python code functions: it works best with tokenized python functions.


## Model description

This CodeTrans model is based on the `t5-large` model. It has its own SentencePiece vocabulary model. It used multi-task training on 13 supervised tasks in the software development domain and 7 unsupervised datasets. It is then fine-tuned on the source code summarization task for the python code snippets.



## Intended uses & limitations

The model could be used to generate the description for the python function or be fine-tuned on other python code tasks. It can be used on unparsed and untokenized python code. However, if the python code is tokenized, the performance should be better.

### How to use

Here is how to use this model to generate python function documentation using Transformers SummarizationPipeline:

```python
from transformers import AutoTokenizer, AutoModelWithLMHead, SummarizationPipeline

pipeline = SummarizationPipeline(
    model=AutoModelWithLMHead.from_pretrained("SEBIS/code_trans_t5_large_source_code_summarization_python_multitask_finetune"),
    tokenizer=AutoTokenizer.from_pretrained("SEBIS/code_trans_t5_large_source_code_summarization_python_multitask_finetune", skip_special_tokens=True),
    device=0
)

tokenized_code = '''with open ( CODE_STRING , CODE_STRING ) as in_file : buf = in_file . readlines ( )  with open ( CODE_STRING , CODE_STRING ) as out_file : for line in buf :          if line ==   " ; Include this text   " :              line = line +   " Include below  "          out_file . write ( line ) '''
pipeline([tokenized_code])
```
Run this example in [colab notebook](https://github.com/agemagician/CodeTrans/blob/main/prediction/multitask/fine-tuning/source%20code%20summarization/python/large_model.ipynb).
## Training data

The supervised training tasks datasets can be downloaded on [Link](https://www.dropbox.com/sh/488bq2of10r4wvw/AACs5CGIQuwtsD7j_Ls_JAORa/finetuning_dataset?dl=0&subfolder_nav_tracking=1)


## Training procedure

### Multi-task Pretraining

The model was trained on a single TPU Pod V3-8 for 500,000 steps in total, using sequence length 512 (batch size 4096).
It has a total of approximately 220M parameters and was trained using the encoder-decoder architecture.
The optimizer used is AdaFactor with inverse square root learning rate schedule for pre-training.

### Fine-tuning

This model was then fine-tuned on a single TPU Pod V2-8 for 100 steps in total, using sequence length 512 (batch size 256), using only the dataset only containing python code.


## Evaluation results

For the source code summarization tasks, different models achieves the following results on different programming languages (in BLEU score):

Test results :

|   Language / Model   |     Python     |       SQL      |       C#       |
| -------------------- | :------------: | :------------: | :------------: |
|   CodeTrans-ST-Small    |      8.45      |     17.55      |     19.74      |
|   CodeTrans-ST-Base     |      9.12      |     15.00      |     18.65      | 
|   CodeTrans-TF-Small    |     10.06      |     17.71      |     20.40      |
|   CodeTrans-TF-Base     |     10.94      |     17.66      |     21.12      |
|   CodeTrans-TF-Large    |     12.41      |     18.40      |     21.43      |
|   CodeTrans-MT-Small    |     13.11      |     19.15      |     22.39      |
|   CodeTrans-MT-Base     |   **13.37**    |     19.24      |     23.20      |
|   CodeTrans-MT-Large    |     13.24      |     19.40      |   **23.57**    |
|   CodeTrans-MT-TF-Small |     12.10      |     18.25      |     22.03      |
|   CodeTrans-MT-TF-Base  |     10.64      |     16.91      |     21.40      |
|   CodeTrans-MT-TF-Large |     12.14      |   **19.98**    |     21.10      |
|   CODE-NN   |       --       |     18.40      |     20.50      |


> Created by [Ahmed Elnaggar](https://twitter.com/Elnaggar_AI) | [LinkedIn](https://www.linkedin.com/in/prof-ahmed-elnaggar/) and Wei Ding | [LinkedIn](https://www.linkedin.com/in/wei-ding-92561270/)


