
---
language: English   
tags:
- summarization English model
datasets:
- jrc-acquis
widget:
- text: >
    THE COMMISSION OF THE EUROPEAN COMMUNITIES, Having regard to the Treaty establishing 
    the European Community, Having regard to Council Regulation (EC) No 1255/1999 of 17 May 1999 
    on the common organisation of the market in milk and milk products [1], and in particular Article 15 thereof, 
    Whereas: (1) Article 7(1) of Commission Regulation (EC) No 2799/1999 [2] fixes the amount of aid for 
    skimmed milk and skimmed-milk powder intended for animal feed taking into account the factors set out 
    in Article 11(2) of Regulation (EC) No 1255/1999. In view of the developments in the market price of 
    skimmed-milk powder, of the increase in the market prices for competing proteins, and of the reduction 
    of the supply of skimmed-milk powder, the amount of aid should be reduced. (2) Regulation (EC) 
    No 2799/1999 should therefore be amended accordingly. (3) The Management Committee for Milk and 
    Milk Products has not delivered an opinion within the time-limit set by its chairman, 
    HAS ADOPTED THIS REGULATION: Article 1 In Article 7 of Regulation (EC) No 2799/1999, paragraph 1 is replaced by the following: "1. Aid is fixed at: (a) EUR 1,62 per 100 kg of skimmed milk with a protein content of not less than 35,6 % of the non-fatty dry extract; (b) EUR 1,42 per 100 kg of skimmed milk with a protein content of not less than 31,4 % but less than 35,6 % of the non-fatty dry extract; (c) EUR 20,00 per 100 kg of skimmed-milk powder with a protein content of not less than 35,6 % of the non-fatty dry extract; (d) EUR 17,64 per 100 kg of skimmed-milk powder with a protein content of not less than 31,4 % but less than 35,6 % of the non-fatty dry extract." Article 2 This Regulation shall enter into force on the day following its publication in the Official Journal of the European Union. This Regulation shall be binding in its entirety and directly applicable in all Member States. Done at Brussels, 19 April 2006. For the Commission Mariann Fischer Boel Member of the Commission [1] OJ L 160, 26.6.1999, p. 48. Regulation as last amended by Regulation (EC) No 1913/2005 (OJ L 307, 25.11.2005, p. 2). [2] OJ L 340, 31.12.1999, p. 3. 
    Regulation as last amended by Regulation (EC) No 1194/2005 (OJ L 194, 26.7.2005, p. 7).
---

# legal_t5_small_summ_en model

Model for Summarization of legal text written in English. It was first released in
[this repository](https://github.com/agemagician/LegalTrans). This model is trained on three parallel corpus from jrc-acquis.


## Model description

legal_t5_small_summ_en is based on the `t5-small` model and was trained on a large corpus of parallel text. This is a smaller model, which scales the baseline model of t5 down by using `dmodel = 512`, `dff = 2,048`, 8-headed attention, and only 6 layers each in the encoder and decoder. This variant has about 60 million parameters.

## Intended uses & limitations

The model could be used for summarization of legal texts written in English.

### How to use

Here is how to use this model to summarize legal text written in English in PyTorch:

```python
from transformers import AutoTokenizer, AutoModelWithLMHead, TranslationPipeline

pipeline = TranslationPipeline(
model=AutoModelWithLMHead.from_pretrained("SEBIS/legal_t5_small_summ_en"),
tokenizer=AutoTokenizer.from_pretrained(pretrained_model_name_or_path = "SEBIS/legal_t5_small_summ_en", do_lower_case=False, 
                                            skip_special_tokens=True),
    device=0
)

en_text = "THE COMMISSION OF THE EUROPEAN COMMUNITIES, Having regard to the Treaty establishing the European Community, Having regard to Council Regulation (EC) No 1255/1999 of 17 May 1999 on the common organisation of the market in milk and milk products [1], and in particular Article 15 thereof, Whereas: (1) Article 7(1) of Commission Regulation (EC) No 2799/1999 [2] fixes the amount of aid for skimmed milk and skimmed-milk powder intended for animal feed taking into account the factors set out in Article 11(2) of Regulation (EC) No 1255/1999. In view of the developments in the market price of skimmed-milk powder, of the increase in the market prices for competing proteins, and of the reduction of the supply of skimmed-milk powder, the amount of aid should be reduced. (2) Regulation (EC) No 2799/1999 should therefore be amended accordingly. (3) The Management Committee for Milk and Milk Products has not delivered an opinion within the time-limit set by its chairman, HAS ADOPTED THIS REGULATION: Article 1 In Article 7 of Regulation (EC) No 2799/1999, paragraph 1 is replaced by the following: "1. Aid is fixed at: (a) EUR 1,62 per 100 kg of skimmed milk with a protein content of not less than 35,6 % of the non-fatty dry extract; (b) EUR 1,42 per 100 kg of skimmed milk with a protein content of not less than 31,4 % but less than 35,6 % of the non-fatty dry extract; (c) EUR 20,00 per 100 kg of skimmed-milk powder with a protein content of not less than 35,6 % of the non-fatty dry extract; (d) EUR 17,64 per 100 kg of skimmed-milk powder with a protein content of not less than 31,4 % but less than 35,6 % of the non-fatty dry extract." Article 2 This Regulation shall enter into force on the day following its publication in the Official Journal of the European Union. This Regulation shall be binding in its entirety and directly applicable in all Member States. Done at Brussels, 19 April 2006. For the Commission Mariann Fischer Boel Member of the Commission [1] OJ L 160, 26.6.1999, p. 48. Regulation as last amended by Regulation (EC) No 1913/2005 (OJ L 307, 25.11.2005, p. 2). [2] OJ L 340, 31.12.1999, p. 3. Regulation as last amended by Regulation (EC) No 1194/2005 (OJ L 194, 26.7.2005, p. 7). -------------------------------------------------- "

pipeline([en_text], max_length=512)
```

## Training data

The legal_t5_small_summ_en model was trained on [JRC-ACQUIS](https://wt-public.emm4u.eu/Acquis/index_2.2.html) dataset consisting of 22 Thousand texts.

## Training procedure

The model was trained on a single TPU Pod V3-8 for 250K steps in total, using sequence length 512 (batch size 64). It has a total of approximately 220M parameters and was trained using the encoder-decoder architecture. The optimizer used is AdaFactor with inverse square root learning rate schedule for pre-training.
### Preprocessing

An unigram model trained with 88M lines of text from the parallel corpus (of all possible language pairs) to get the vocabulary (with byte pair encoding), which is used with this model.

### Pretraining



## Evaluation results

When the model is used for classification test dataset, achieves the following results:

Test results :

| Model | Rouge1  | Rouge2 | Rouge Lsum |
|:-----:|:-----:|:-----:|:-----:|
|   legal_t5_small_summ_en | 78.11|68.78 |77.0|


### BibTeX entry and citation info

> Created by [Ahmed Elnaggar/@Elnaggar_AI](https://twitter.com/Elnaggar_AI) | [LinkedIn](https://www.linkedin.com/in/prof-ahmed-elnaggar/)
