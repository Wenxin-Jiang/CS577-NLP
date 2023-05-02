---
language:
 - en
tags:
- table-to-text
- tabular
- Narratable
datasets:
- totto
widget:
- text: "<s><page_title> John Higgins </page_title> <section_title> Minor-ranking finals: 6 (3 titles, 3 runners-up) </section_title> <table> <row> <c> Outcome </c> <c> No. <row_header> Outcome </row_header> </c> <c> Year <row_header> Outcome </row_header> <row_header> No. </row_header> </c> <c> Championship <row_header> Outcome </row_header> <row_header> No. </row_header> <row_header> Year </row_header> </c> <c> Opponent in the final <row_header> Outcome </row_header> <row_header> No. </row_header> <row_header> Year </row_header> <row_header> Championship </row_header> </c> <c> Score <row_header> Outcome </row_header> <row_header> No. </row_header> <row_header> Year </row_header> <row_header> Championship </row_header> <row_header> Opponent in the final </row_header> </c> </row> <row> <c> Winner <col_header> Outcome </col_header> </c> <c> 1. <col_header> No. </col_header> </c> <c> 2010 <col_header> Year </col_header> </c> <c> Ruhr Championship <col_header> Championship </col_header> </c> <c> England Shaun Murphy <col_header> Opponent in the final </col_header> </c> <c> 4–2 <col_header> Score </col_header> </c> </row> <row> <c> Runner-up <col_header> Outcome </col_header> </c> <c> 1. <col_header> No. </col_header> </c> <c> 2010 <col_header> Year </col_header> </c> <c> Prague Classic <col_header> Championship </col_header> </c> <c> England Michael Holt <col_header> Opponent in the final </col_header> </c> <c> 3–4 <col_header> Score </col_header> </c> </row> <row> <c> Runner-up <col_header> Outcome </col_header> </c> <c> 2. <col_header> No. </col_header> </c> <c> 2011 <col_header> Year </col_header> </c> <c> Players Tour Championship – Event 5 <col_header> Championship </col_header> </c> <c> England Andrew Higginson <col_header> Opponent in the final </col_header> </c> <c> 1–4 <col_header> Score </col_header> </c> </row> <row> <c> Winner <col_header> Outcome </col_header> </c> <c> 2. <col_header> No. </col_header> </c> <c> 2012 <col_header> Year </col_header> </c> <c> Kay Suzanne Memorial Trophy <col_header> Championship </col_header> </c> <c> England Judd Trump <col_header> Opponent in the final </col_header> </c> <c> 4–2 <col_header> Score </col_header> </c> </row> <row> <c> Runner-up <col_header> Outcome </col_header> </c> <c> 3. <col_header> No. </col_header> </c> <c> 2012 <col_header> Year </col_header> </c> <c> Bulgarian Open <col_header> Championship </col_header> </c> <c> England Judd Trump <col_header> Opponent in the final </col_header> </c> <c> 0–4 <col_header> Score </col_header> </c> </row> <row> <highlighted_cell> Winner <col_header> Outcome </col_header> </highlighted_cell> <c> 3. <col_header> No. </col_header> </c> <highlighted_cell> 2013 <col_header> Year </col_header> </highlighted_cell> <highlighted_cell> Bulgarian Open <col_header> Championship </col_header> </highlighted_cell> <highlighted_cell> Australia Neil Robertson <col_header> Opponent in the final </col_header> </highlighted_cell> <highlighted_cell> 4–1 <col_header> Score </col_header> </highlighted_cell> </row> </table>\n\n"

inference:
  parameters:
    max_length: 500
    
---

# BLOOM (0.56B) fine-tuned on ToTTo for Table-to-text 📋 ➡️ 🔤 aka NARRATABLE

This model is a fine-tuned version of [bigscience/bloom-560m](https://huggingface.co/bigscience/bloom-560m) on the **ToTTo** [dataset](https://huggingface.co/datasets/totto).


## The model 🧠

It is a 560M params version of [**BLOOM** 🌸](https://bigscience.huggingface.co/blog/bloom)

## The dataset 📚

**ToTTo** is an open-domain English table-to-text dataset with over 120,000 training examples that proposes a controlled generation task: given a Wikipedia table and a set of highlighted table cells, produce a one-sentence description.

During the dataset creation process, tables from English Wikipedia are matched with (noisy) descriptions. Each table cell mentioned in the description is highlighted and the descriptions are iteratively cleaned and corrected to faithfully reflect the content of the highlighted cells.


### Evaluation results

| Metric | Value |
|:-------:|:-----:|
| rouge1  | 0.56  |
| rouge2  | 0.33  |
| rougeL  | 0.48  |
| rougeLsum  | 0.48  |
| sacrebleu  |  20.87  |
| meteor  | 0.49 |


## Usage

```py
from datasets import load_dataset
from transformers import BloomTokenizerFast, BloomForCausalLM

valid_dataset = load_dataset('totto', split='validation')

from preprocess import preprocess # This file is included in the repo

# Now we linearize the tables
valid_dataset = valid_dataset.map(preprocess) 

model_ckpt = "mrm8488/bloom-560m-finetuned-totto-table-to-text"

tokenizer = BloomTokenizerFast.from_pretrained(ckpt)
model = BloomForCausalLM.from_pretrained(ckpt).to("cuda")


def explain_hl_cells(text):
    inputs = tokenizer(text, return_tensors='pt')
    input_ids = inputs.input_ids.to("cuda")
    attention_mask = inputs.attention_mask.to("cuda")
    output = model.generate(input_ids, attention_mask=attention_mask, max_length=2048, eos_token_id=tokenizer.eos_token_id)

    return tokenizer.decode(output[0], skip_special_tokens=False)

example = valid_dataset[1]

print(explain_hl_cells(example['linearized_table'])
``` 

<video loop="" autoplay="" controls="" src="https://huggingface.co/Narrativaai/bloom-560m-finetuned-totto-table-to-text/resolve/main/video_totto.mp4"></video>


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1


Created by: [Narrativa](https://www.narrativa.com/)

#### About **Narrativa**:

Narrativa is an internationally recognized **content services company** that uses its proprietary **artificial intelligence** and **machine learning** platforms to build and deploy **digital content solutions** for enterprises. Its technology suite, consisting of data extraction, data analysis, natural language processing (NLP) and natural language generation (NLG) tools, all seamlessly work together to power a lineup of smart content creation, automated business intelligence reporting and process optimization products for a variety of industries.
Contact us to learn more about our solutions!