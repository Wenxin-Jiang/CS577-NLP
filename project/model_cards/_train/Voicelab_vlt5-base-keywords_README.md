---
license: cc-by-4.0
language: 
- pl
- en
datasets:
- posmac
pipeline_tag: text2text-generation
pipeline_kwargs:
- no_repeat_ngram_size=3
- num_beams=4
tags:
- keywords-generation
- text-classifiation
- other
widget:
- text: "Keywords: Our vlT5 model is a keyword generation model based on encoder-decoder architecture using Transformer blocks presented by google (https://huggingface.co/t5-base). The vlT5 was trained on scientific articles corpus to predict a given set of keyphrases based on the concatenation of the article’s abstract and title. It generates precise, yet not always complete keyphrases that describe the content of the article based only on the abstract."
  example_title: "English 1"
- text: "Keywords: Decays the learning rate of each parameter group by gamma every step_size epochs. Notice that such decay can happen simultaneously with other changes to the learning rate from outside this scheduler. When last_epoch=-1, sets initial lr as lr."
  example_title: "English 2"
- text: "Keywords: Przełomem w dziedzinie sztucznej inteligencji i maszynowego uczenia się było powstanie systemu eksperckiego Dendral na Uniwersytecie Stanforda w 1965. System ten powstał w celu zautomatyzowania analizy i identyfikacji molekuł związków organicznych, które dotychczas nie były znane chemikom. Wyniki badań otrzymane dzięki systemowi Dendral były pierwszym w historii odkryciem dokonanym przez komputer, które zostały opublikowane w prasie specjalistycznej."
  example_title: "Polish"
- text: "Keywords: El análisis de un economista calcula que, a pesar del aumento del gasto general, la Navidad es una pérdida de peso muerto según la teoría microeconómica ortodoxa, debido al efecto de dar regalos. Esta pérdida se calcula como la diferencia entre lo que el donante gastó en el artículo y lo que el receptor del regalo habría pagado por el artículo. Se estima que en 2001, Navidad resultó en una pérdida de peso muerto de $ 4 mil millones solo en los EE. UU.1​ Debido a factores de complicación, este análisis se utiliza a veces para discutir posibles fallas en la teoría microeconómica actual. Otras pérdidas de peso muerto incluyen los efectos de la Navidad en el medio ambiente y el hecho de que los regalos materiales a menudo se perciben como elefantes blancos, lo que impone costos de mantenimiento y almacenamiento y contribuye al desorden."
  example_title: "Spanish"
metrics:
- f1
- precision
- recall

---
<img src="https://public.3.basecamp.com/p/rs5XqmAuF1iEuW6U7nMHcZeY/upload/download/VL-NLP-short.png" alt="logo voicelab nlp" style="width:300px;"/>

# Keyword Extraction from Short Texts with T5

 > Our vlT5 model is a keyword generation model based on encoder-decoder architecture using Transformer blocks presented by Google ([https://huggingface.co/t5-base](https://huggingface.co/t5-base)). The vlT5 was trained on scientific articles corpus to predict a given set of keyphrases based on the concatenation of the article’s abstract and title. It generates precise, yet not always complete keyphrases that describe the content of the article based only on the abstract.

**Keywords generated with vlT5-base-keywords:** encoder-decoder architecture, keyword generation

Results on demo model (different generation method, one model per language):

 > Our vlT5 model is a keyword generation model based on encoder-decoder architecture using Transformer blocks presented by Google ([https://huggingface.co/t5-base](https://huggingface.co/t5-base)). The vlT5 was trained on scientific articles corpus to predict a given set of keyphrases based on the concatenation of the article’s abstract and title. It generates precise, yet not always complete keyphrases that describe the content of the article based only on the abstract.

**Keywords generated with vlT5-base-keywords:** encoder-decoder architecture, vlT5, keyword generation, scientific articles corpus

## vlT5

The biggest advantage is the transferability of the vlT5 model, as it works well on all domains and types of text. The downside is that the text length and the number of keywords are similar to the training data: the text piece of an abstract length generates approximately 3 to 5 keywords. It works both extractive and abstractively. Longer pieces of text must be split into smaller chunks, and then propagated to the model.

### Overview
- **Language model:** [t5-base](https://huggingface.co/t5-base)   
- **Language:** pl, en (but works relatively well with others)
- **Training data:** POSMAC
- **Online Demo:** Visit our online demo for better results [https://nlp-demo-1.voicelab.ai/](https://nlp-demo-1.voicelab.ai/)
- **Paper:** [Keyword Extraction from Short Texts with a Text-To-Text Transfer Transformer, ACIIDS 2022](https://arxiv.org/abs/2209.14008)

# Corpus

The model was trained on a POSMAC corpus. Polish Open Science Metadata Corpus (POSMAC) is a collection of  216,214 abstracts of scientific publications compiled in the CURLICAT project.


| Domains                                                  | Documents | With keywords |
| -------------------------------------------------------- | --------: | :-----------: |
| Engineering and technical sciences                       |    58 974 |    57 165    |
| Social sciences                                          |    58 166 |    41 799    |
| Agricultural sciences                                    |    29 811 |    15 492    |
| Humanities                                               |    22 755 |    11 497    |
| Exact and natural sciences                               |    13 579 |     9 185     |
| Humanities, Social sciences                              |    12 809 |     7 063     |
| Medical and health sciences                              |     6 030 |     3 913     |
| Medical and health sciences, Social sciences             |       828 |      571      |
| Humanities, Medical and health sciences, Social sciences |       601 |      455      |
| Engineering and technical sciences, Humanities           |       312 |      312      |

# Tokenizer

As in the original plT5 implementation, the training dataset was tokenized into subwords using a sentencepiece unigram model with vocabulary size of 50k tokens. 

# Usage

```python
from transformers import T5Tokenizer, T5ForConditionalGeneration

model = T5ForConditionalGeneration.from_pretrained("Voicelab/vlt5-base-keywords")
tokenizer = T5Tokenizer.from_pretrained("Voicelab/vlt5-base-keywords")

task_prefix = "Keywords: "
inputs = [
    "Christina Katrakis, who spoke to the BBC from Vorokhta in western Ukraine, relays the account of one family, who say Russian soldiers shot at their vehicles while they were leaving their village near Chernobyl in northern Ukraine. She says the cars had white flags and signs saying they were carrying children.",
    "Decays the learning rate of each parameter group by gamma every step_size epochs. Notice that such decay can happen simultaneously with other changes to the learning rate from outside this scheduler. When last_epoch=-1, sets initial lr as lr.",
    "Hello, I'd like to order a pizza with salami topping.",
]

for sample in inputs:
    input_sequences = [task_prefix + sample]
    input_ids = tokenizer(
        input_sequences, return_tensors="pt", truncation=True
    ).input_ids
    output = model.generate(input_ids, no_repeat_ngram_size=3, num_beams=4)
    predicted = tokenizer.decode(output[0], skip_special_tokens=True)
    print(sample, "\n --->", predicted)

```
# Inference
Our results showed that the best generation results were achieved with `no_repeat_ngram_size=3, num_beams=4`


# Results



| Method      | Rank |   Micro   |            |            | Macro |       |       |
| ----------- | ---: | :--------: | ---------: | ---------: | :---: | ----: | ----: |
|             |      |     P     |          R |         F1 |   P   |     R |    F1 |
| extremeText |    1 |   0.175   |      0.038 |      0.063 | 0.007 | 0.004 | 0.005 |
|             |    3 |   0.117   |      0.077 |      0.093 | 0.011 | 0.011 | 0.011 |
|             |    5 |   0.090   |      0.099 |      0.094 | 0.013 | 0.016 | 0.015 |
|             |   10 |   0.060   |      0.131 |      0.082 | 0.015 | 0.025 | 0.019 |
| vlT5kw      |    1 | **0.345** |      0.076 |      0.124 | 0.054 | 0.047 | 0.050 |
|             |    3 |   0.328   |      0.212 |      0.257 | 0.133 | 0.127 | 0.129 |
|             |    5 |   0.318   | **0.237** | **0.271** | 0.143 | 0.140 | 0.141 |
| KeyBERT     |    1 |   0.030   |      0.007 |      0.011 | 0.004 | 0.003 | 0.003 |
|             |    3 |   0.015   |      0.010 |      0.012 | 0.006 | 0.004 | 0.005 |
|             |    5 |   0.011   |      0.012 |      0.011 | 0.006 | 0.005 | 0.005 |
| TermoPL     |    1 |   0.118   |      0.026 |      0.043 | 0.004 | 0.003 | 0.003 |
|             |    3 |   0.070   |      0.046 |      0.056 | 0.006 | 0.005 | 0.006 |
|             |    5 |   0.051   |      0.056 |      0.053 | 0.007 | 0.007 | 0.007 |
|             |  all |   0.025   |      0.339 |      0.047 | 0.017 | 0.030 | 0.022 |
| extremeText |    1 |   0.210   |      0.077 |      0.112 | 0.037 | 0.017 | 0.023 |
|             |    3 |   0.139   |      0.152 |      0.145 | 0.045 | 0.042 | 0.043 |
|             |    5 |   0.107   |      0.196 |      0.139 | 0.049 | 0.063 | 0.055 |
|             |   10 |   0.072   |      0.262 |      0.112 | 0.041 | 0.098 | 0.058 |
| vlT5kw      |    1 | **0.377** |      0.138 |      0.202 | 0.119 | 0.071 | 0.089 |
|             |    3 |   0.361   |      0.301 |      0.328 | 0.185 | 0.147 | 0.164 |
|             |    5 |   0.357   | **0.316** | **0.335** | 0.188 | 0.153 | 0.169 |
| KeyBERT     |    1 |   0.018   |      0.007 |      0.010 | 0.003 | 0.001 | 0.001 |
|             |    3 |   0.009   |      0.010 |      0.009 | 0.004 | 0.001 | 0.002 |
|             |    5 |   0.007   |      0.012 |      0.009 | 0.004 | 0.001 | 0.002 |
| TermoPL     |    1 |   0.076   |      0.028 |      0.041 | 0.002 | 0.001 | 0.001 |
|             |    3 |   0.046   |      0.051 |      0.048 | 0.003 | 0.001 | 0.002 |
|             |    5 |   0.033   |      0.061 |      0.043 | 0.003 | 0.001 | 0.002 |
|             |  all |   0.021   |      0.457 |      0.040 | 0.004 | 0.008 | 0.005 |

# License

CC BY 4.0

# Citation

If you use this model, please cite the following paper:

[Piotr Pęzik, Agnieszka Mikołajczyk-Bareła, Adam Wawrzyński, Bartłomiej Nitoń, Maciej Ogrodniczuk, Keyword Extraction from Short Texts with a Text-To-Text Transfer Transformer, ACIIDS 2022](https://arxiv.org/abs/2209.14008)


# Authors

The model was trained by NLP Research Team at Voicelab.ai.

You can contact us [here](https://voicelab.ai/contact/).
