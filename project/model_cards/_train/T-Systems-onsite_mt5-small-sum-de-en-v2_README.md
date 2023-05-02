---
language:
- de
- en
- multilingual
license: cc-by-nc-sa-4.0
tags:
- summarization
datasets:
- cnn_dailymail
- xsum
- mlsum
- swiss_text_2019
---

# mT5-small-sum-de-en-v2


This is a bilingual summarization model for English and German. It is based on the multilingual T5 model [google/mt5-small](https://huggingface.co/google/mt5-small).

## Training

The training was conducted with the following hyperparameters:

- base model: [google/mt5-small](https://huggingface.co/google/mt5-small)
- source_prefix: `"summarize: "`
- batch size: 3
- max_source_length: 800
- max_target_length: 96
- warmup_ratio: 0.3
- number of train epochs: 10
- gradient accumulation steps: 2
- learning rate: 5e-5

## Datasets and Preprocessing

The datasets were preprocessed as follows:

The summary was tokenized with the [google/mt5-small](https://huggingface.co/google/mt5-small) tokenizer. Then only the records with no more than 94 summary tokens were selected.

The MLSUM dataset has a special characteristic. In the text, the summary is often included completely as one or more sentences. These have been removed from the texts. The reason is that we do not want to train a model that ultimately extracts only sentences as a summary.

This model is trained on the following datasets:

| Name | Language | License
|------|----------|--------
| [CNN Daily - Train](https://github.com/abisee/cnn-dailymail) | en | The license is unclear. The data comes from CNN and Daily Mail. We assume that it may only be used for research purposes and not commercially.
| [Extreme Summarization (XSum) - Train](https://github.com/EdinburghNLP/XSum) | en | The license is unclear. The data comes from BBC. We assume that it may only be used for research purposes and not commercially.
| [MLSUM German - Train](https://github.com/ThomasScialom/MLSUM) | de | Usage of dataset is restricted to non-commercial research purposes only. Copyright belongs to the original copyright holders (see [here](https://github.com/ThomasScialom/MLSUM#mlsum)).
| [SwissText 2019 - Train](https://www.swisstext.org/2019/shared-task/german-text-summarization-challenge.html) | de | The license is unclear. The data was published in the [German Text Summarization Challenge](https://www.swisstext.org/2019/shared-task/german-text-summarization-challenge.html). We assume that they may be used for research purposes and not commercially.

| Language | Size
|------|------
| German | 302,607
| English | 422,228
| Total | 724,835

## Evaluation on MLSUM German Test Set (no beams)

| Model | rouge1 | rouge2 | rougeL | rougeLsum
|-------|--------|--------|--------|----------
| [ml6team/mt5-small-german-finetune-mlsum](https://huggingface.co/ml6team/mt5-small-german-finetune-mlsum) | 18.3607 | 5.3604 | 14.5456 | 16.1946
| [deutsche-telekom/mT5-small-sum-de-en-01](https://huggingface.co/deutsche-telekom/mt5-small-sum-de-en-v1) | 21.7336 | 7.2614 | 17.1323 | 19.3977
| **T-Systems-onsite/mt5-small-sum-de-en-v2 (this)** | **21.7756** | **7.2662** | **17.1444** | **19.4242**

## Evaluation on CNN Daily English Test Set (no beams)

| Model | rouge1 | rouge2 | rougeL | rougeLsum
|-------|--------|--------|--------|----------
| [sshleifer/distilbart-xsum-12-6](https://huggingface.co/sshleifer/distilbart-xsum-12-6) | 26.7664 | 8.8243 | 18.3703 | 23.2614
| [facebook/bart-large-xsum](https://huggingface.co/facebook/bart-large-xsum) | 28.5374 | 9.8565 | 19.4829 | 24.7364
| [mrm8488/t5-base-finetuned-summarize-news](https://huggingface.co/mrm8488/t5-base-finetuned-summarize-news) | 37.576 | 14.7389 | 24.0254 | 34.4634
| [deutsche-telekom/mT5-small-sum-de-en-01](https://huggingface.co/deutsche-telekom/mt5-small-sum-de-en-v1) | 37.6339 | 16.5317 | 27.1418 | 34.9951
| **T-Systems-onsite/mt5-small-sum-de-en-v2 (this)** | **37.8096** | **16.6646** | **27.2239** | **35.1916**

## Evaluation on Extreme Summarization (XSum) English Test Set (no beams)

| Model | rouge1 | rouge2 | rougeL | rougeLsum
|-------|--------|--------|--------|----------
| [mrm8488/t5-base-finetuned-summarize-news](https://huggingface.co/mrm8488/t5-base-finetuned-summarize-news) | 18.6204 | 3.535 | 12.3997 | 15.2111
| [facebook/bart-large-xsum](https://huggingface.co/facebook/bart-large-xsum) | 28.5374 | 9.8565 | 19.4829 | 24.7364
| [deutsche-telekom/mT5-small-sum-de-en-01](https://huggingface.co/deutsche-telekom/mt5-small-sum-de-en-v1) | 32.3416 | 10.6191 | 25.3799 | 25.3908
| T-Systems-onsite/mt5-small-sum-de-en-v2 (this) | 32.4828 | 10.7004| 25.5238 | 25.5369
| [sshleifer/distilbart-xsum-12-6](https://huggingface.co/sshleifer/distilbart-xsum-12-6) | 44.2553 &clubs; | 21.4289 &clubs; | 36.2639 &clubs; | 36.2696 &clubs;

&clubs;: These values seem to be unusually high. It could be that the test set was used in the training data.

## License

Copyright (c) 2021 Philip May, T-Systems on site services GmbH

This work is licensed under the [Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0)](https://creativecommons.org/licenses/by-nc-sa/3.0/) license.
