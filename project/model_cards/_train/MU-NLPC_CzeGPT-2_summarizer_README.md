---
language: cs

license: cc-by-nc-sa-4.0
datasets:
- csTenTen17
---

# CzeGPT-2_summarizer
CzeGPT-2 summarizer is a Czech summarizer built upon the <a href="https://huggingface.co/MU-NLPC/CzeGPT-2">CzeGPT-2</a> model. The model has the same architectural dimensions as the GPT-2 small (12 layers, 12 heads, 1024 tokens on input/output, and embedding vectors with 768 dimensions) resulting in 124M trainable parameters. It was fine-tuned and evaluated on the <a href="https://aclanthology.org/L18-1551.pdf">SumeCzech</a> summarization dataset containing about 1M Czech news articles.
The model is trained to generate the summary as long as you let it (or it runs out of sequence length). This leaves a space for developers to set their own constraints.

## Tokenizer
Along, we also provide a Czech trained tokenizer (vocab and merges) with vocab size of 50257 that was used during the pre-training phase and fine-tuning. It is the byte-level BPE tokenizer as used in the original GPT-2 paper.

## Training results
The model was evaluated on the *test* and *ood-test* partitions of the SumeCzech dataset and compared to the best summarizers yet evaluated on this benchmark (the results taken from <a href="https://ufal.mff.cuni.cz/sumeczech">here</a>). 
The abstract generator yields three sentences that roughly correspond to 40 token average length of abstracts in the SumeCzech. This length of summary was also confirmed by tuning on the validation set. 

We manage to reach state-of-the art on most standard metrics.  
 

Test set

| Model | ROUGE<sub>RAW</sub>-1  | ROUGE<sub>RAW</sub>-2 | ROUGE<sub>RAW</sub>-L |
| :---: | :------: | :-----: | :-----: |
| CzeGPT-2 | **18.0**/18.7/**17.8** | **3.5**/**3.7**/**3.5** | **12.6**/13.3/**12.5** |
| First | 13.1/17.9/14.4 | 1.9/2.8/2.1 | 8.8/12.0/9.6 |
| TextRank | 11.1/**20.8**/13.8 | 1.6/3.1/2.0 | 7.1/**13.4**/8.9 |
|Tensor2Tensor | 13.2/10.5/11.3 | 1.2/0.9/1.0 | 10.2/8.1/8.7 |


OOD test set

| Model | ROUGE<sub>RAW</sub>-1  | ROUGE<sub>RAW</sub>-2 | ROUGE<sub>RAW</sub>-L |
| :---: | :------: | :-----: | :-----: |
|CzeGPT-2 | **16.2**/18.5/**16.7** | **3.1**/**3.7**/**3.2** | **11.5**/**13.3**/**11.9** |
|First | 11.1/17.1/12.7 | 1.6/2.7/1.9 | 7.6/11.7/8.7 |
|TextRank | 9.8/**19.9**/12.5 | 1.5/3.3/2.0 | 6.6/**13.3**/8.4 |
|Tensor2Tensor | 12.5/9.4/10.3 | 0.8/0.6/0.6 | 9.8/7.5/8.1 |

The numbers in the tables denote *precision/recall/F1-score*

## Error Analysis
As we think the current standard  ROUGE<sub>RAW</sub> metric is not suitable enough for the summarization task (even though it is the best we have at the time), we performed also a manual error analysis of the generated summaries using human annotators. You can find more about the methodology and results in our paper referenced at the bottom of this card.

## Running the predictions
The repository includes a simple Jupyter Notebook that can help with first steps when using the model.

## Headline generator
See also our model fine-tuned for <a href="https://huggingface.co/MU-NLPC/CzeGPT-2_headline_generator">headline generation task</a>.

## How to cite
@unpublished{hajek_horak2022,<br>
  author = "Adam Hájek and Aleš Horák",<br>
  title  = "CzeGPT-2 – New Model for Czech Summarization Task",<br>
  note   = "preprint available at \url{https://openreview.net/forum?id=H43eQtxZefq}",<br>
  month  = "3",<br>
  year   = "2022",<br>
}