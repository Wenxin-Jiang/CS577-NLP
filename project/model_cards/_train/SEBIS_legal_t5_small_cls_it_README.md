
---
language: Italian   
tags:
- classification Italian model
datasets:
- jrc-acquis
widget:
- text: "Regolamento (CE) n. 435/2005 della Commissione del 17 marzo 2005 relativo all'applicazione di un coefficiente di riduzione ai certificati di restituzione per le merci non comprese nell'allegato I del trattato come statuito all'articolo 8, paragrafo 5, del regolamento (CE) n. 1520/2000 LA COMMISSIONE DELLE COMUNITÀ EUROPEE, visto il trattato che istituisce la Comunità europea, visto il regolamento (CE) n. 3448/93 del Consiglio, del 6 dicembre 1993, sul regime di scambi per talune merci ottenute dalla trasformazione di prodotti agricoli [1], visto il regolamento (CE) n. 1520/2000 della Commissione, del 13 luglio 2000, che stabilisce, per taluni prodotti agricoli esportati sotto forma di merci non comprese nell'allegato I del trattato, le modalità comuni di applicazione relative al versamento delle restituzioni all'esportazione e i criteri per stabilirne l'importo [2], in particolare l'articolo 8, paragrafo 5, considerando quanto segue: (1) Dalle comunicazioni degli Stati membri di cui all'articolo 8, paragrafo 2, del regolamento (CE) n. 1520/2000 si evince che l'importo totale delle domande ricevute ammonta a 178002906 EUR, mentre l'importo disponibile per la tranche di titoli di restituzione di cui all'articolo 8, paragrafo 4, del regolamento (CE) n. 1520/2000 ammonta a 68116869 EUR. (2) Un coefficiente di riduzione è calcolato sulla base dell'articolo 8, paragrafi 3 e 4, del regolamento (CE) n. 1520/2000. Siffatto coefficiente dovrebbe pertanto essere applicato agli importi richiesti sotto forma di certificati di restituzione per il periodo dal 1o aprile 2005 come stabilito all'articolo 8, paragrafo 6, del regolamento (CE) n. 1520/2000, HA ADOTTATO IL PRESENTE REGOLAMENTO: Articolo 1 Gli importi delle domande di certificati di restituzione per il periodo dal 1o aprile 2005 sono soggetti a un coefficiente di riduzione pari a 0,618. Articolo 2 Il presente regolamento entra in vigore il 18 marzo 2005. Il presente regolamento è obbligatorio in tutti i suoi elementi e direttamente applicabile in ciascuno degli Stati membri. Fatto a Bruxelles, il 17 marzo 2005. Per la Commissione Günter Verheugen Vicepresidente [1] GU L 318 del 20.12.1993, pag. 18. Regolamento modificato da ultimo dal regolamento (CE) n. 2580/2000 (GU L 298 del 25.11.2000, pag. 5). [2] GU L 177 del 15.7.2000, pag. 1. Regolamento modificato da ultimo dal regolamento (CE) n. 886/2004 (GU L 168 del 1.5.2004, pag. 14). --------------------------------------------------"

---

# legal_t5_small_cls_it model

Model for classification of legal text written in Italian. It was first released in
[this repository](https://github.com/agemagician/LegalTrans). This model is trained on three parallel corpus from jrc-acquis.


## Model description

legal_t5_small_cls_it is based on the `t5-small` model and was trained on a large corpus of parallel text. This is a smaller model, which scales the baseline model of t5 down by using `dmodel = 512`, `dff = 2,048`, 8-headed attention, and only 6 layers each in the encoder and decoder. This variant has about 60 million parameters.

## Intended uses & limitations

The model could be used for classification of legal texts written in Italian.

### How to use

Here is how to use this model to classify legal text written in Italian in PyTorch:

```python
from transformers import AutoTokenizer, AutoModelWithLMHead, TranslationPipeline

pipeline = TranslationPipeline(
model=AutoModelWithLMHead.from_pretrained("SEBIS/legal_t5_small_cls_it"),
tokenizer=AutoTokenizer.from_pretrained(pretrained_model_name_or_path = "SEBIS/legal_t5_small_cls_it", do_lower_case=False, 
                                            skip_special_tokens=True),
    device=0
)

it_text = "Regolamento (CE) n. 435/2005 della Commissione del 17 marzo 2005 relativo all'applicazione di un coefficiente di riduzione ai certificati di restituzione per le merci non comprese nell'allegato I del trattato come statuito all'articolo 8, paragrafo 5, del regolamento (CE) n. 1520/2000 LA COMMISSIONE DELLE COMUNITÀ EUROPEE, visto il trattato che istituisce la Comunità europea, visto il regolamento (CE) n. 3448/93 del Consiglio, del 6 dicembre 1993, sul regime di scambi per talune merci ottenute dalla trasformazione di prodotti agricoli [1], visto il regolamento (CE) n. 1520/2000 della Commissione, del 13 luglio 2000, che stabilisce, per taluni prodotti agricoli esportati sotto forma di merci non comprese nell'allegato I del trattato, le modalità comuni di applicazione relative al versamento delle restituzioni all'esportazione e i criteri per stabilirne l'importo [2], in particolare l'articolo 8, paragrafo 5, considerando quanto segue: (1) Dalle comunicazioni degli Stati membri di cui all'articolo 8, paragrafo 2, del regolamento (CE) n. 1520/2000 si evince che l'importo totale delle domande ricevute ammonta a 178002906 EUR, mentre l'importo disponibile per la tranche di titoli di restituzione di cui all'articolo 8, paragrafo 4, del regolamento (CE) n. 1520/2000 ammonta a 68116869 EUR. (2) Un coefficiente di riduzione è calcolato sulla base dell'articolo 8, paragrafi 3 e 4, del regolamento (CE) n. 1520/2000. Siffatto coefficiente dovrebbe pertanto essere applicato agli importi richiesti sotto forma di certificati di restituzione per il periodo dal 1o aprile 2005 come stabilito all'articolo 8, paragrafo 6, del regolamento (CE) n. 1520/2000, HA ADOTTATO IL PRESENTE REGOLAMENTO: Articolo 1 Gli importi delle domande di certificati di restituzione per il periodo dal 1o aprile 2005 sono soggetti a un coefficiente di riduzione pari a 0,618. Articolo 2 Il presente regolamento entra in vigore il 18 marzo 2005. Il presente regolamento è obbligatorio in tutti i suoi elementi e direttamente applicabile in ciascuno degli Stati membri. Fatto a Bruxelles, il 17 marzo 2005. Per la Commissione Günter Verheugen Vicepresidente [1] GU L 318 del 20.12.1993, pag. 18. Regolamento modificato da ultimo dal regolamento (CE) n. 2580/2000 (GU L 298 del 25.11.2000, pag. 5). [2] GU L 177 del 15.7.2000, pag. 1. Regolamento modificato da ultimo dal regolamento (CE) n. 886/2004 (GU L 168 del 1.5.2004, pag. 14). --------------------------------------------------"

pipeline([it_text], max_length=512)
```

## Training data

The legal_t5_small_cls_it model was trained on [JRC-ACQUIS](https://wt-public.emm4u.eu/Acquis/index_2.2.html) dataset consisting of 23 Thousand texts.

## Training procedure


The model was trained on a single TPU Pod V3-8 for 250K steps in total, using sequence length 512 (batch size 64). It has a total of approximately 220M parameters and was trained using the encoder-decoder architecture. The optimizer used is AdaFactor with inverse square root learning rate schedule for pre-training.

### Preprocessing

An unigram model trained with 88M lines of text from the parallel corpus (of all possible language pairs) to get the vocabulary (with byte pair encoding), which is used with this model.

### Pretraining



## Evaluation results

When the model is used for classification test dataset, achieves the following results:

Test results :

| Model | F1 score |
|:-----:|:-----:|
|   legal_t5_small_cls_it | 0.6296|


### BibTeX entry and citation info

> Created by [Ahmed Elnaggar/@Elnaggar_AI](https://twitter.com/Elnaggar_AI) | [LinkedIn](https://www.linkedin.com/in/prof-ahmed-elnaggar/)
