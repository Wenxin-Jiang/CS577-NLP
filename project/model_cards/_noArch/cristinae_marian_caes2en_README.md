---
language: 
- ca 
- es
- en
tags:
- translation
---

### Preprocessing
1. Normalisation and tokenisation with moses scripts
2. truecased with model docgWP.tcmodel.[LAN] and moses scripts
3. bped with model model.caesen40k.bpe and subword-nmt
- Note: no prepended tag for multilinguality

### Training Data
1. Bilingual es-ca: DOGC, Wikimatrix, OpenSubtitles, JW300, GlobalVoices
* Bilingual es-ca: Translations using systems trained with 1. of Oscar and Wikipedia
2. Bilingual es-en, ca-en: United Nations, Europarl, Wikimatrix, OpenSubtitles, JW300
* Bilingual es-en, ca-en: Translations using systems trained with 1. of the missing pairs

- Final training data size for the ca/es-en: 44M parallel sentences
- Finetuned with 1.5M real parallel data (without backtranslations)

### Model
Transformer big with guided alignments. Relevant parameters:

--beam-size 6 

--normalize 0.6 

--enc-depth 6  --dec-depth 6  --transformer-heads 8

--transformer-preprocess n  --transformer-postprocess da 

--transformer-dropout 0.1 

--label-smoothing 0.1 

--dim-emb 1024  --transformer-dim-ffn 4096 

--transformer-dropout-attention 0.1 

--transformer-dropout-ffn 0.1 

--learn-rate 0.00015 --lr-warmup 8000 --lr-decay-inv-sqrt 8000 

--optimizer-params 0.9 0.998 1e-09 

--clip-norm 5 

--tied-embeddings 

--exponential-smoothing 

--transformer-guided-alignment-layer 1 --guided-alignment-cost mse --guided-alignment-weight 0.1


## Evaluation

### Test set

https://github.com/PLXIV/Gebiotoolkit/tree/master/gebiocorpus_v2

### ca2en
 BLEU|#:1|bs:1000|rs:12345|c:mixed|e:no|tok:13a|s:exp|v:2.0.0 = 47.8 (μ = 47.8 ± 0.9)

 chrF|#:1|bs:1000|rs:12345|c:mixed|e:yes|nc:6|nw:0|s:no|v:2.0.0 = 69.9 (μ = 69.9 ± 0.7)

### es2en
BLEU|#:1|bs:1000|rs:12345|c:mixed|e:no|tok:13a|s:exp|v:2.0.0 = 48.9 (μ = 48.9 ± 0.9) 

chrF2|#:1|bs:1000|rs:12345|c:mixed|e:yes|nc:6|nw:0|s:no|v:2.0.0 = 70.5 (μ = 70.5 ± 0.7)

