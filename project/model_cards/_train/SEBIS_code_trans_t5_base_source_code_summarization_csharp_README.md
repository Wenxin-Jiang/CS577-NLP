---
tags:
- summarization
widget:
- text: "public static DateTime ParseUnixDateTime ( double unixTime ) { var dt = new DateTime ( CODE_INTEGER , CODE_INTEGER , CODE_INTEGER , CODE_INTEGER , CODE_INTEGER , CODE_INTEGER , CODE_INTEGER , System . DateTimeKind . Utc ) ; dt = dt . AddSeconds ( unixTimeStamp ) . ToLocalTime ( ) ; return dt ; }"

---



# CodeTrans model for source code summarization csharp
Pretrained model on programming language csharp using the t5 base model architecture. It was first released in
[this repository](https://github.com/agemagician/CodeTrans). This model is trained on tokenized csharp code functions: it works best with tokenized csharp functions.


## Model description

This CodeTrans model is based on the `t5-base` model. It has its own SentencePiece vocabulary model. It used single-task training on source code summarization csharp dataset.

## Intended uses & limitations

The model could be used to generate the description for the csharp function or be fine-tuned on other csharp code tasks. It can be used on unparsed and untokenized csharp code. However, if the csharp code is tokenized, the performance should be better.

### How to use

Here is how to use this model to generate csharp function documentation using Transformers SummarizationPipeline:

```python
from transformers import AutoTokenizer, AutoModelWithLMHead, SummarizationPipeline

pipeline = SummarizationPipeline(
    model=AutoModelWithLMHead.from_pretrained("SEBIS/code_trans_t5_base_source_code_summarization_csharp"),
    tokenizer=AutoTokenizer.from_pretrained("SEBIS/code_trans_t5_base_source_code_summarization_csharp", skip_special_tokens=True),
    device=0
)

tokenized_code = "public static DateTime ParseUnixDateTime ( double unixTime ) { var dt = new DateTime ( CODE_INTEGER , CODE_INTEGER , CODE_INTEGER , CODE_INTEGER , CODE_INTEGER , CODE_INTEGER , CODE_INTEGER , System . DateTimeKind . Utc ) ; dt = dt . AddSeconds ( unixTimeStamp ) . ToLocalTime ( ) ; return dt ; }"
pipeline([tokenized_code])
```
Run this example in [colab notebook](https://github.com/agemagician/CodeTrans/blob/main/prediction/single%20task/source%20code%20summarization/csharp/base_model.ipynb).
## Training data

The supervised training tasks datasets can be downloaded on [Link](https://www.dropbox.com/sh/488bq2of10r4wvw/AACs5CGIQuwtsD7j_Ls_JAORa/finetuning_dataset?dl=0&subfolder_nav_tracking=1)


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
