---
tags:
- summarization
widget:
- text: "new file mode 100644 index 000000000 . . 892fda21b Binary files / dev / null and b / src / plugins / gateway / lib / joscar . jar differ"

---


# CodeTrans model for git commit message generation
Pretrained model on git commit using the t5 base model architecture. It was first released in
[this repository](https://github.com/agemagician/CodeTrans). This model is trained on tokenized git commit: it works best with tokenized git commit.


## Model description

This CodeTrans model is based on the `t5-base` model. It has its own SentencePiece vocabulary model.  It used multi-task training on 13 supervised tasks in the software development domain and 7 unsupervised datasets.

## Intended uses & limitations

The model could be used to generate the git commit message for the git commit changes or be fine-tuned on other relevant tasks. It can be used on unparsed and untokenized commit changes. However, if the change is tokenized, the performance should be better.

### How to use

Here is how to use this model to generate git commit message using Transformers SummarizationPipeline:

```python
from transformers import AutoTokenizer, AutoModelWithLMHead, SummarizationPipeline

pipeline = SummarizationPipeline(
    model=AutoModelWithLMHead.from_pretrained("SEBIS/code_trans_t5_base_commit_generation_multitask"),
    tokenizer=AutoTokenizer.from_pretrained("SEBIS/code_trans_t5_base_commit_generation_multitask", skip_special_tokens=True),
    device=0
)

tokenized_code = "new file mode 100644 index 000000000 . . 892fda21b Binary files / dev / null and b / src / plugins / gateway / lib / joscar . jar differ"
pipeline([tokenized_code])
```
Run this example in [colab notebook](https://github.com/agemagician/CodeTrans/blob/main/prediction/multitask/pre-training/commit%20generation/base_model.ipynb).
## Training data

The supervised training tasks datasets can be downloaded on [Link](https://www.dropbox.com/sh/488bq2of10r4wvw/AACs5CGIQuwtsD7j_Ls_JAORa/finetuning_dataset?dl=0&subfolder_nav_tracking=1)


## Training procedure

### Multi-task Pretraining

The model was trained on a single TPU Pod V3-8 for 480,000 steps in total, using sequence length 512 (batch size 4096).
It has a total of approximately 220M parameters and was trained using the encoder-decoder architecture.
The optimizer used is AdaFactor with inverse square root learning rate schedule for pre-training.


## Evaluation results

For the git commit message generation task, different models achieves the following results on different programming languages (in BLEU score):

Test results :

|   Language / Model   |      Java      |
| -------------------- | :------------: |
|   CodeTrans-ST-Small    |     39.61      |
|   CodeTrans-ST-Base     |     38.67      |
|   CodeTrans-TF-Small    |     44.22      |
|   CodeTrans-TF-Base     |     44.17      |
|   CodeTrans-TF-Large    |   **44.41**    |
|   CodeTrans-MT-Small    |     36.17      |
|   CodeTrans-MT-Base     |     39.25      |
|   CodeTrans-MT-Large    |     41.18      |
|   CodeTrans-MT-TF-Small |     43.96      |
|   CodeTrans-MT-TF-Base  |     44.19      |
|   CodeTrans-MT-TF-Large |     44.34      |
|   State of the art   |     32.81      |



> Created by [Ahmed Elnaggar](https://twitter.com/Elnaggar_AI) | [LinkedIn](https://www.linkedin.com/in/prof-ahmed-elnaggar/) and Wei Ding | [LinkedIn](https://www.linkedin.com/in/wei-ding-92561270/)

