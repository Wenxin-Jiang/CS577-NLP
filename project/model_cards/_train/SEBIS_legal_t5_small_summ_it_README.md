
---
language: Italian   
tags:
- summarization Italian model
datasets:
- jrc-acquis
widget:
- text: "LA COMMISSIONE DELLE COMUNITÀ EUROPEE, visto il trattato che istituisce la Comunità europea, visto il regolamento (CEE) n. 2082/92 del Consiglio, del 14 luglio 1992, relativo alle attestazioni di specificità dei prodotti agricoli ed alimentari(1), in particolare l'articolo 9, paragrafo 1, considerando quanto segue: (1) A norma dell'articolo 7 del regolamento (CEE) n. 2082/92, la Finlandia ha trasmesso alla Commissione una domanda di registrazione della denominazione %quot%Kalakukko%quot% quale attestazione di specificità. (2) La dicitura %quot%specialità tradizionale garantita%quot% può applicarsi soltanto a denominazioni figuranti nel summenzionato albo. (3) Nessuna dichiarazione di opposizione, ai sensi dell'articolo 8 del summenzionato regolamento, è stata trasmessa alla Commissione a seguito della pubblicazione nella Gazzetta ufficiale delle Comunità europee(2) della denominazione figurante nell'allegato del presente regolamento. (4) Di conseguenza, la denominazione di cui all'allegato può essere iscritta nell'albo delle attestazioni di specificità e beneficiare pertanto della protezione a livello comunitario quale specialità tradizionale garantita nella Comunità in virtù dell'articolo 13, paragrafo 2, del regolamento (CEE) n. 2082/92. (5) L'allegato del presente regolamento completa l'allegato del regolamento (CE) n. 2301/97 della Commissione(3), modificato da ultimo dal regolamento (CE) n. 688/2002(4), HA ADOTTATO IL PRESENTE REGOLAMENTO: Articolo 1 La denominazione di cui all'allegato del presente regolamento è aggiunta all'allegato del regolamento (CE) n. 2301/97 e iscritta nell'albo delle attestazioni di specificità, conformemente all'articolo 9, paragrafo 1, del regolamento (CEE) n. 2082/92. Tale denominazione è protetta ai sensi dell'articolo 13, paragrafo 2, del summenzionato regolamento. Articolo 2 Il presente regolamento entra in vigore il ventesimo giorno successivo alla pubblicazione nella Gazzetta ufficiale delle Comunità europee. Il presente regolamento è obbligatorio in tutti i suoi elementi e direttamente applicabile in ciascuno degli Stati membri. Fatto a Bruxelles, il 15 luglio 2002. Per la Commissione Franz Fischler Membro della Commissione (1) GU L 208 del 24.7.1992, pag. 9. (2) GU C 235 del 21.8.2001, pag. 12. (3) GU L 319 del 21.11.1997, pag. 8. (4) GU L 106 del 23.4.2002, pag. 7. ALLEGATO Prodotti della panetteria, della pasticceria, della confetteria o della biscotteria - Kalakukko "

---

# legal_t5_small_summ_it model

Model for Summarization of legal text written in Italian. It was first released in
[this repository](https://github.com/agemagician/LegalTrans). This model is trained on three parallel corpus from jrc-acquis.


## Model description

legal_t5_small_summ_it is based on the `t5-small` model and was trained on a large corpus of parallel text. This is a smaller model, which scales the baseline model of t5 down by using `dmodel = 512`, `dff = 2,048`, 8-headed attention, and only 6 layers each in the encoder and decoder. This variant has about 60 million parameters.

## Intended uses & limitations

The model could be used for summarization of legal texts written in Italian.

### How to use

Here is how to use this model to summarize legal text written in Italian in PyTorch:

```python
from transformers import AutoTokenizer, AutoModelWithLMHead, TranslationPipeline

pipeline = TranslationPipeline(
model=AutoModelWithLMHead.from_pretrained("SEBIS/legal_t5_small_summ_it"),
tokenizer=AutoTokenizer.from_pretrained(pretrained_model_name_or_path = "SEBIS/legal_t5_small_summ_it", do_lower_case=False, 
                                            skip_special_tokens=True),
    device=0
)

it_text = "LA COMMISSIONE DELLE COMUNITÀ EUROPEE, visto il trattato che istituisce la Comunità europea, visto il regolamento (CEE) n. 2082/92 del Consiglio, del 14 luglio 1992, relativo alle attestazioni di specificità dei prodotti agricoli ed alimentari(1), in particolare l'articolo 9, paragrafo 1, considerando quanto segue: (1) A norma dell'articolo 7 del regolamento (CEE) n. 2082/92, la Finlandia ha trasmesso alla Commissione una domanda di registrazione della denominazione %quot%Kalakukko%quot% quale attestazione di specificità. (2) La dicitura %quot%specialità tradizionale garantita%quot% può applicarsi soltanto a denominazioni figuranti nel summenzionato albo. (3) Nessuna dichiarazione di opposizione, ai sensi dell'articolo 8 del summenzionato regolamento, è stata trasmessa alla Commissione a seguito della pubblicazione nella Gazzetta ufficiale delle Comunità europee(2) della denominazione figurante nell'allegato del presente regolamento. (4) Di conseguenza, la denominazione di cui all'allegato può essere iscritta nell'albo delle attestazioni di specificità e beneficiare pertanto della protezione a livello comunitario quale specialità tradizionale garantita nella Comunità in virtù dell'articolo 13, paragrafo 2, del regolamento (CEE) n. 2082/92. (5) L'allegato del presente regolamento completa l'allegato del regolamento (CE) n. 2301/97 della Commissione(3), modificato da ultimo dal regolamento (CE) n. 688/2002(4), HA ADOTTATO IL PRESENTE REGOLAMENTO: Articolo 1 La denominazione di cui all'allegato del presente regolamento è aggiunta all'allegato del regolamento (CE) n. 2301/97 e iscritta nell'albo delle attestazioni di specificità, conformemente all'articolo 9, paragrafo 1, del regolamento (CEE) n. 2082/92. Tale denominazione è protetta ai sensi dell'articolo 13, paragrafo 2, del summenzionato regolamento. Articolo 2 Il presente regolamento entra in vigore il ventesimo giorno successivo alla pubblicazione nella Gazzetta ufficiale delle Comunità europee. Il presente regolamento è obbligatorio in tutti i suoi elementi e direttamente applicabile in ciascuno degli Stati membri. Fatto a Bruxelles, il 15 luglio 2002. Per la Commissione Franz Fischler Membro della Commissione (1) GU L 208 del 24.7.1992, pag. 9. (2) GU C 235 del 21.8.2001, pag. 12. (3) GU L 319 del 21.11.1997, pag. 8. (4) GU L 106 del 23.4.2002, pag. 7. ALLEGATO Prodotti della panetteria, della pasticceria, della confetteria o della biscotteria - Kalakukko "

pipeline([it_text], max_length=512)
```

## Training data

The legal_t5_small_summ_it model was trained on [JRC-ACQUIS](https://wt-public.emm4u.eu/Acquis/index_2.2.html) dataset consisting of 22 Thousand texts.

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
|   legal_t5_small_summ_it | 75.07|65.53 |73.85|


### BibTeX entry and citation info

> Created by [Ahmed Elnaggar/@Elnaggar_AI](https://twitter.com/Elnaggar_AI) | [LinkedIn](https://www.linkedin.com/in/prof-ahmed-elnaggar/)
