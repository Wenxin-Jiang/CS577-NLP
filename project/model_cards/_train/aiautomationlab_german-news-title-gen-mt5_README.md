---
language: 
  - de
tags:
  - summarization
  - arxiv:2005.00661
  - arxiv:2111.09525
  - arxiv:2112.08542
  - arxiv:2104.04302
  - arxiv:2109.09209
license: mit
metrics:
  - rouge
widget:
- text: "Als Reaktion auf die Brandserie wurde am Mittwoch bei der Kriminalpolizei Würzburg eine Ermittlungskommission eingerichtet. Ich habe den Eindruck, der Brandstifter wird dreister, kommentiert Rosalinde Schraud, die Bürgermeisterin von Estenfeld, die Brandserie. Gerade die letzten beiden Brandstiftungen seien ungewöhnlich gewesen, da sie mitten am Tag und an frequentierten Straßen stattgefunden haben.Kommt der Brandstifter aus Estenfeld?Norbert Walz ist das letzte Opfer des Brandstifters von Estenfeld. Ein Unbekannter hat am Dienstagnachmittag sein Gartenhaus angezündet.Was da in seinem Kopf herumgeht, was da passiert – das ist ja unglaublich! Das kann schon jemand aus dem Ort sein, weil sich derjenige auskennt.Norbert Walz aus Estenfeld.Dass es sich beim Brandstifter wohl um einen Bürger ihrer Gemeinde handele, will die erste Bürgermeisterin von Estenfeld, Rosalinde Schraud, nicht bestätigen: In der Bevölkerung gibt es natürlich Spekulationen, an denen ich mich aber nicht beteiligen will. Laut Schraud reagiert die Bürgerschaft mit vermehrter Aufmerksamkeit auf die Brände: Man guckt mehr in die Nachbarschaft. Aufhören wird die Brandserie wohl nicht, solange der Täter nicht gefasst wird.Es wäre nicht ungewöhnlich, dass der Täter aus der Umgebung von Estenfeld stammt. Wir bitten deshalb Zeugen, die sachdienliche Hinweise sowohl zu den Bränden geben können, sich mit unserer Kriminalpolizei in Verbindung zu setzen.Philipp Hümmer, Sprecher des Polizeipräsidiums UnterfrankenFür Hinweise, die zur Ergreifung des Täters führen, hat das Bayerische Landeskriminalamt eine Belohnung von 2.000 Euro ausgesetzt."
  example_title: "Example article"
inference:
  parameters:
    num_beams: 5
---

# German news title gen

This is a model for the task of news headline generation in German. 

While this task is very similar to summarization, there remain differences like length, structure, and language style, which cause state-of-the-art summarization models not to be suited best for headline generation and demand further fine tuning on this task.

For this model, [mT5-base](https://huggingface.co/google/mt5-base) by Google is used as a foundation model. 

**The model is still work in progress**

## Dataset & preprocessing
The model was finetuned on a corpus of news articles from [BR24](https://www.br.de/) published between  2015 and 2021. The texts are in german language and cover a range of different news topics like politics, sports, and culture, with a focus on topics that are relevant to the people living in Bavaria (Germany).

In a preprocessing step, article-headline pairs matching any of the following criteria were filtered out:
- very short articles (number of words in text lower than 3x the number of words in the headline).
- articles with headlines containing only words that are not contained in the text (lemmatized and excluding stopwords).
- articles with headlines that are just the name of a known text format (e.g. "Das war der Tag" a format summarizing the most important topics of the day)

Further the prefix `summarize: ` was added to all articles to make use of the pretrained summarization capabilities of mT5.

After filtering the corpus contained 89098 article-headline pairs, of which 87306 were used for training, 902 for validation, and 890 for testing.

## Training 
After multiple test runs of finetuning the present model was further trained using the following parameters:
- foundation-model: mT5-base
- input_prefix: "summarize: "
- num_train_epochs: 10
- learning_rate: 5e-5
- warmup_ratio: 0.3
- lr_scheduler_type: constant_with_warmup
- per_device_train_batch_size: 3
- gradient_accumulation_steps: 2
- fp16: False

Every 5000 steps a checkpoint is stored and evaluated on the validation set. After the training, the checkpoint with the best cross-entropy loss on the validation set is saved as the final model.

## Usage

Because the model was fine tuned on mT5, the usage is analogous to the T5 model ([see docs](https://huggingface.co/docs/transformers/model_doc/t5)). Another option for using the model for inference is the huggingface [summarization pipeline](https://huggingface.co/docs/transformers/v4.23.1/en/main_classes/pipelines#transformers.SummarizationPipeline).

In both cases the prefix `summarize: ` has to be added to the input texts. 

For obtaining higher quality headlines it is recommended to increase the beam size for genereation. In the evaluations conducted for this model a beam size of 5 was used.

### Example: Direct model evaluation

```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model_id = ""
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

text = "Als Reaktion auf die Brandserie wurde am Mittwoch bei der Kriminalpolizei Würzburg eine Ermittlungskommission eingerichtet. Ich habe den Eindruck, der Brandstifter wird dreister, kommentiert Rosalinde Schraud, die Bürgermeisterin von Estenfeld, die Brandserie. Gerade die letzten beiden Brandstiftungen seien ungewöhnlich gewesen, da sie mitten am Tag und an frequentierten Straßen stattgefunden haben.Kommt der Brandstifter aus Estenfeld?Norbert Walz ist das letzte Opfer des Brandstifters von Estenfeld. Ein Unbekannter hat am Dienstagnachmittag sein Gartenhaus angezündet.Was da in seinem Kopf herumgeht, was da passiert – das ist ja unglaublich! Das kann schon jemand aus dem Ort sein, weil sich derjenige auskennt.Norbert Walz aus Estenfeld.Dass es sich beim Brandstifter wohl um einen Bürger ihrer Gemeinde handele, will die erste Bürgermeisterin von Estenfeld, Rosalinde Schraud, nicht bestätigen: In der Bevölkerung gibt es natürlich Spekulationen, an denen ich mich aber nicht beteiligen will. Laut Schraud reagiert die Bürgerschaft mit vermehrter Aufmerksamkeit auf die Brände: Man guckt mehr in die Nachbarschaft. Aufhören wird die Brandserie wohl nicht, solange der Täter nicht gefasst wird.Es wäre nicht ungewöhnlich, dass der Täter aus der Umgebung von Estenfeld stammt. Wir bitten deshalb Zeugen, die sachdienliche Hinweise sowohl zu den Bränden geben können, sich mit unserer Kriminalpolizei in Verbindung zu setzen.Philipp Hümmer, Sprecher des Polizeipräsidiums UnterfrankenFür Hinweise, die zur Ergreifung des Täters führen, hat das Bayerische Landeskriminalamt eine Belohnung von 2.000 Euro ausgesetzt."

input_text = "summarize: " + text
input_ids = tokenizer(input_text, return_tensors="pt").input_ids

outputs = model.generate(input_ids, num_beams=5)
generated_headline = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(generated_headline)
```

### Example: Model evaluation using huggingface pipeline
```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

model_id = ""
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
headline_generator = pipeline(
    "summarization",
    model=model,
    tokenizer=tokenizer,
    num_beams=5
)

text = "Als Reaktion auf die Brandserie wurde am Mittwoch bei der Kriminalpolizei Würzburg eine Ermittlungskommission eingerichtet. Ich habe den Eindruck, der Brandstifter wird dreister, kommentiert Rosalinde Schraud, die Bürgermeisterin von Estenfeld, die Brandserie. Gerade die letzten beiden Brandstiftungen seien ungewöhnlich gewesen, da sie mitten am Tag und an frequentierten Straßen stattgefunden haben.Kommt der Brandstifter aus Estenfeld?Norbert Walz ist das letzte Opfer des Brandstifters von Estenfeld. Ein Unbekannter hat am Dienstagnachmittag sein Gartenhaus angezündet.Was da in seinem Kopf herumgeht, was da passiert – das ist ja unglaublich! Das kann schon jemand aus dem Ort sein, weil sich derjenige auskennt.Norbert Walz aus Estenfeld.Dass es sich beim Brandstifter wohl um einen Bürger ihrer Gemeinde handele, will die erste Bürgermeisterin von Estenfeld, Rosalinde Schraud, nicht bestätigen: In der Bevölkerung gibt es natürlich Spekulationen, an denen ich mich aber nicht beteiligen will. Laut Schraud reagiert die Bürgerschaft mit vermehrter Aufmerksamkeit auf die Brände: Man guckt mehr in die Nachbarschaft. Aufhören wird die Brandserie wohl nicht, solange der Täter nicht gefasst wird.Es wäre nicht ungewöhnlich, dass der Täter aus der Umgebung von Estenfeld stammt. Wir bitten deshalb Zeugen, die sachdienliche Hinweise sowohl zu den Bränden geben können, sich mit unserer Kriminalpolizei in Verbindung zu setzen.Philipp Hümmer, Sprecher des Polizeipräsidiums UnterfrankenFür Hinweise, die zur Ergreifung des Täters führen, hat das Bayerische Landeskriminalamt eine Belohnung von 2.000 Euro ausgesetzt."
input_text = "summarize: " + text

generated_headline = headline_generator(input_text)[0]["summary_text"]
print(generated_headline)

```


## Limitations
Like most state-of-the-art summarization models this model has issues with the factuality of the generated texts [^factuality]. **It is therefore strongly advised having a human fact-check the generated headlines.**

An analysis of possible biases reproduced by the present model, regardless of whether they originate from our finetuning or the underlying mT5 model, is beyond the scope of this work. We assume that biases exist within the model and an analysis will be a task for future work

As the model was trained on news articles from the time range 2015-2021, further biases and factual errors could emerge due to topic shifts in news articles and changes in the (e.g. political) situation.

##  Evaluation

The model was evaluated on a held-out test set consisting of 890 article-headline pairs.

For each model the headlines were generated using beam search with a beam width of 5.

### Quantitative

| model | Rouge1 | Rouge2 | RougeL | RougeLsum |
|-|-|-|-|-|
| [T-Systems-onsite/mt5-small-sum-de-en-v2](https://huggingface.co/T-Systems-onsite/mt5-small-sum-de-en-v2)| 0.107 | 0.0297 | 0.098 | 0.098 |
| aiautomationlab/german-news-title-gen-mt5 | 0.3131 | 0.0873 | 0.1997 | 0.1997 |

For evaluating the factuality of the generated headlines concerning the input text, we use 3 state-of-the-art metrics for summary evaluation (the parameters were chosen according to the recommendations from the respective papers or GitHub repositories). Because these metrics are only available for the English language the texts and generated headlines were translated from German to English using the [DeepL API](https://www.deepl.com/en/docs-api/) in an additional preprocessing step for this factuality evaluation.

- **SummaC-CZ** [^summac]  
  Yields a score between -1 and 1, representing the difference between entailment probability and contradiction probability (-1: the headline is not entailed in text and is completely contradicted by it, 1: the headline is fully entailed in text and not contradicted by it).

  Parameters:
  - `model_name`: [vitc](https://huggingface.co/tals/albert-xlarge-vitaminc-mnli)
- **QAFactEval** [^qafacteval]  
  Using Lerc Quip score, which is reported to perform best in the corresponding paper. The score yields a value between 0 and 5 representing the overlap between answers based on the headline and text to questions generated from the headline (0: no overlap, 5: perfect overlap).

  Parameters:
  - `use_lerc_quip`: True

- **DAE (dependency arc entailment)** [^dae]  
  Yields a binary value of either 0 or 1, representing whether all dependency arcs in the headline are entailed in the text (0: at least one dependency arc is not entailed, 1: all dependency arcs are entailed).

  Parameters:
  - model checkpoint: DAE_xsum_human_best_ckpt
  - `model_type`: model_type
  - `max_seq_length`: 512


Each metric is calculated for all article-headline pairs in the test set and the respective mean score over the test set is reported.

| model | SummacCZ | QAFactEval | DAE | 
|-|-|-|-|
| [T-Systems-onsite/mt5-small-sum-de-en-v2](https://huggingface.co/T-Systems-onsite/mt5-small-sum-de-en-v2) | 0.6969 | 3.3023 | 0.8292 |
| aiautomationlab/german-news-title-gen-mt5 | 0.4419 | 1.9265 | 0.7438 |

It can be observed that our model scores consistently lower than the T-Systems one. Following human evaluation, it seems that to match the structure and style specific to headlines the headline generation model has to be more abstractive than a model for summarization which leads to a higher frequency of hallucinations in the generated output.

### Qualitative
A qualitative evaluation conducted by members of the BR AI + Automation Lab showed that the model succeeds in producing headlines that match the language and style of news headlines, but also confirms that there are issues with the factual consistency common to state-of-the-art summarization models.

## Future work

Future work on this model will focus on generating headlines with higher factual consistency regarding the text. Ideas to achieve this goal include:
- Use of coreference resolution as additional preprocessing step for making the relations within the text more explicit to the model.
- Use of contrastive learning [^contrastive_learning]
- Use of different models for different news topics, as different topics seem to be prone to different types of errors, more specialized models may be able to improve performance.
- Use of factuality metric models for reranking beam search candidates in the generation step.
- Perform analysis of biases included in the model



[^factuality]: Maynez, Joshua, Shashi Narayan, Bernd Bohnet, and Ryan McDonald. “On Faithfulness and Factuality in Abstractive Summarization.” In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, 1906–19. Online: Association for Computational Linguistics, 2020. https://doi.org/10.18653/v1/2020.acl-main.173.

[^summac]: Laban, Philippe, Tobias Schnabel, Paul N. Bennett, and Marti A. Hearst. “SummaC: Re-Visiting NLI-Based Models for Inconsistency Detection in Summarization.” Transactions of the Association for Computational Linguistics 10 (February 9, 2022): 163–77. https://doi.org/10.1162/tacl_a_00453.  
Code: https://github.com/tingofurro/summac

[^qafacteval]: Fabbri, Alexander R., Chien-Sheng Wu, Wenhao Liu, and Caiming Xiong. “QAFactEval: Improved QA-Based Factual Consistency Evaluation for Summarization.” arXiv, April 29, 2022. https://doi.org/10.48550/arXiv.2112.08542.  
Code: https://github.com/salesforce/QAFactEval

[^dae]: Goyal, Tanya, and Greg Durrett. “Annotating and Modeling Fine-Grained Factuality in Summarization.” arXiv, April 9, 2021. http://arxiv.org/abs/2104.04302.  
Code: https://github.com/tagoyal/factuality-datasets

[^contrastive_learning]: Cao, Shuyang, and Lu Wang. “CLIFF: Contrastive Learning for Improving Faithfulness and Factuality in Abstractive Summarization.” In Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing, 6633–49. Online and Punta Cana, Dominican Republic: Association for Computational Linguistics, 2021. https://doi.org/10.18653/v1/2021.emnlp-main.532.


