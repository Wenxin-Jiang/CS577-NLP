---
tags:
- summarization
widget:
- text: "protected String renderUri ( URI uri ) { return uri . toASCIIString ( ) ; }"

---


# CodeTrans model for code comment generation java
Pretrained model on programming language java using the t5 base model architecture. It was first released in
[this repository](https://github.com/agemagician/CodeTrans). This model is trained on tokenized java code functions: it works best with tokenized java functions.


## Model description

This CodeTrans model is based on the `t5-base` model. It has its own SentencePiece vocabulary model. It used single-task training on Code Comment Generation dataset.

## Intended uses & limitations

The model could be used to generate the description for the java function or be fine-tuned on other java code tasks. It can be used on unparsed and untokenized java code. However, if the java code is tokenized, the performance should be better.

### How to use

Here is how to use this model to generate java function documentation using Transformers SummarizationPipeline:

```python
from transformers import AutoTokenizer, AutoModelWithLMHead, SummarizationPipeline

pipeline = SummarizationPipeline(
    model=AutoModelWithLMHead.from_pretrained("SEBIS/code_trans_t5_base_code_comment_generation_java"),
    tokenizer=AutoTokenizer.from_pretrained("SEBIS/code_trans_t5_base_code_comment_generation_java", skip_special_tokens=True),
    device=0
)

tokenized_code = "protected String renderUri ( URI uri ) { return uri . toASCIIString ( ) ; }"
pipeline([tokenized_code])
```
Run this example in [colab notebook](https://github.com/agemagician/CodeTrans/blob/main/prediction/single%20task/code%20comment%20generation/base_model.ipynb).
## Training data

The supervised training tasks datasets can be downloaded on [Link](https://www.dropbox.com/sh/488bq2of10r4wvw/AACs5CGIQuwtsD7j_Ls_JAORa/finetuning_dataset?dl=0&subfolder_nav_tracking=1)


## Evaluation results

For the code documentation tasks, different models achieves the following results on different programming languages (in BLEU score):

Test results :

|   Language / Model   |      Java      |
| -------------------- | :------------: |
|   CodeTrans-ST-Small    |     37.98      |
|   CodeTrans-ST-Base     |     38.07      |
|   CodeTrans-TF-Small    |     38.56      |
|   CodeTrans-TF-Base     |     39.06      |
|   CodeTrans-TF-Large    |   **39.50**    |
|   CodeTrans-MT-Small    |     20.15      |
|   CodeTrans-MT-Base     |     27.44      |
|   CodeTrans-MT-Large    |     34.69      |
|   CodeTrans-MT-TF-Small |     38.37      |
|   CodeTrans-MT-TF-Base  |     38.90      |
|   CodeTrans-MT-TF-Large |     39.25      |
|   State of the art   |     38.17      |



> Created by [Ahmed Elnaggar](https://twitter.com/Elnaggar_AI) | [LinkedIn](https://www.linkedin.com/in/prof-ahmed-elnaggar/) and Wei Ding | [LinkedIn](https://www.linkedin.com/in/wei-ding-92561270/)
