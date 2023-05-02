---
language: cs

license: cc-by-nc-sa-4.0
datasets:
- csTenTen17
---

# CzeGPT-2 headline generator
CzeGPT-2_headline_generator is a Czech summarizer built upon the <a href="https://huggingface.co/MU-NLPC/CzeGPT-2">CzeGPT-2</a> model. The model has the same architectural dimensions as the GPT-2 small (12 layers, 12 heads, 1024 tokens on input/output, and embedding vectors with 768 dimensions) resulting in 124M trainable parameters. It was fine-tuned and evaluated on the <a href="https://aclanthology.org/L18-1551.pdf">SumeCzech</a> summarization dataset containing about 1M Czech news articles.

## Tokenizer
Along, we also provide a Czech trained tokenizer (vocab and merges) with vocab size of 50257 that was used during the pre-training phase and fine-tuning. It is the byte-level BPE tokenizer as used in the original GPT-2 paper.

## Training results
The model was evaluated on the *test* and *ood-test* partitions of the SumeCzech dataset and compared to the best summarizers yet evaluated on this benchmark (the results taken from <a href="https://ufal.mff.cuni.cz/sumeczech">here</a>). 
The headline generator is trained to decide itself when to stop (generate an <|endoftext|> token). If you want a variable summary length, refer to our <a href="https://huggingface.co/MU-NLPC/CzeGPT-2_summarizer">summary generator</a>

We manage to exceed current state-of-the art on all standard metrics.
 

Test set

| Model | ROUGE<sub>RAW</sub>-1  | ROUGE<sub>RAW</sub>-2 | ROUGE<sub>RAW</sub>-L |
| :---: | :------: | :-----: | :-----: |
| CzeGPT-2 | **17.3**/**17.0**/**16.7** | **4.4**/**4.3**/**4.2** | **15.5**/**15.2**/**14.9**|
| First | 7.4/13.5/8.9 | 1.1/2.2/1.3 | 6.5/11.7/7.7 |
| TextRank | 6.0/16.5/8.3 | 0.8/2.3/1.1 | 5.0/13.8/6.9 |
|Tensor2Tensor | 8.8/7.0/7.5 | 0.8/0.6/0.7 | 8.1/6.5/7.0 |
|NE Density | 6.6/10.7/7.3 | 0.8/1.4/0.9 | 5.9/9.4/6.4 |
|Seq2Seq | 16.1/14.1/14.6 | 2.5/2.1/2.2 | 14.6/12.8/13.2|
|Seq2Seq<sub>NER</sub> | 16.2/14.1/14.7 | 2.5/2.1/2.2 | 14.7/12.8/13.3|


OOD test set

| Model | ROUGE<sub>RAW</sub>-1  | ROUGE<sub>RAW</sub>-2 | ROUGE<sub>RAW</sub>-L |
| :---: | :------: | :-----: | :-----: |
|CzeGPT-2 | **17.9**/**17.6**/**17.2** | **5.9**/**5.7**/**5.5** | **16.4**/**16.2**/**15.8** |
|First | 6.7/13.6/8.3 | 1.3/2.8/1.6 | 5.9/12.0/7.4 |
|TextRank | 5.8/16.9/8.1 | 1.1/3.4/1.5 | 5.0/14.5/6.9 |
|Tensor2Tensor | 6.3/5.1/5.5 | 0.5/0.4/0.4 | 5.9/4.8/5.1 |
|NE Density | 6.3/11.4/7.1 | 1.3/2.3/1.4 | 5.7/10.2/6.3 |
|Seq2Seq | 13.1/11.8/12.0 | 2.0/1.7/1.8 | 12.1/11.0/11.2 |
|Seq2SeqNER | 16.2/14.1/14.7 | 2.5/2.1/2.2 | 14.7/12.8/13.3 |

The numbers in the tables denote *precision/recall/F1-score*

## Error Analysis
As we think the current standard  ROUGE<sub>RAW</sub> metric is not suitable enough for the summarization task (even though it is the best we have at the time), we performed also a manual error analysis of the generated summaries using human annotators. You can find more about the methodology and results in our paper referenced at the bottom of this card.

## Running the predictions
The repository includes a simple Jupyter Notebook that can help with first steps when using the model.

## Summary generator
See also our model fine-tuned for <a href="https://huggingface.co/MU-NLPC/CzeGPT-2_summarizer">summary generation task</a>.

## How to cite
@unpublished{hajek_horak2022,<br>
  author = "Adam Hájek and Aleš Horák",<br>
  title  = "CzeGPT-2 – New Model for Czech Summarization Task",<br>
  note   = "preprint available at \url{https://openreview.net/forum?id=H43eQtxZefq}",<br>
  month  = "3",<br>
  year   = "2022",<br>
}