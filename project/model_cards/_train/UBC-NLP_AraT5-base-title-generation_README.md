---
language: 
  - ar
tags:
  - Arabic T5
  - MSA
  - Twitter
  - Arabic Dialect
  - Arabic Machine Translation
  - Arabic Text Summarization
  - Arabic News Title and Question Generation
  - Arabic Paraphrasing and Transliteration
  - Arabic Code-Switched Translation
---

# AraT5-base-title-generation 
# AraT5: Text-to-Text Transformers for Arabic Language Generation

<img src="https://huggingface.co/UBC-NLP/AraT5-base/resolve/main/AraT5_CR_new.png" alt="AraT5" width="45%" height="35%" align="right"/>

This is the repository accompanying our paper [AraT5: Text-to-Text Transformers for Arabic Language Understanding and Generation](https://aclanthology.org/2022.acl-long.47/). In this is the repository we Introduce **AraT5<sub>MSA</sub>**, **AraT5<sub>Tweet</sub>**, and **AraT5**: three powerful Arabic-specific text-to-text Transformer based models;


---
# How to use AraT5 models
Below is an example for fine-tuning **AraT5-base** for News Title Generation on the Aranews dataset 
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("UBC-NLP/AraT5-base-title-generation")  
model = AutoModelForSeq2SeqLM.from_pretrained("UBC-NLP/AraT5-base-title-generation")

Document = "تحت رعاية صاحب السمو الملكي الأمير سعود بن نايف بن عبدالعزيز أمير المنطقة الشرقية اختتمت غرفة الشرقية مؤخرا، الثاني من مبادرتها لتأهيل وتدريب أبناء وبنات المملكة ضمن مبادرتها المجانية للعام 2019 حيث قدمت 6 برامج تدريبية نوعية. وثمن رئيس مجلس إدارة الغرفة، عبدالحكيم العمار الخالدي، رعاية سمو أمير المنطقة الشرقية للمبادرة، مؤكدا أن دعم سموه لجميع أنشطة ."

encoding = tokenizer.encode_plus(Document,pad_to_max_length=True, return_tensors="pt")
input_ids, attention_masks = encoding["input_ids"], encoding["attention_mask"]


outputs = model.generate(
    input_ids=input_ids, attention_mask=attention_masks,
    max_length=256,
    do_sample=True,
    top_k=120,
    top_p=0.95,
    early_stopping=True,
    num_return_sequences=5
)

for id, output in enumerate(outputs):
    title = tokenizer.decode(output, skip_special_tokens=True,clean_up_tokenization_spaces=True)
    print("title#"+str(id), title)
```
**The input news document**

<div style="white-space : pre-wrap !important;word-break: break-word; direction:rtl; text-align: right">
تحت رعاية صاحب السمو الملكي الأمير سعود بن نايف بن عبدالعزيز أمير المنطقة الشرقية اختتمت غرفة الشرقية مؤخرا، الثاني من مبادرتها لتأهيل وتدريب أبناء وبنات المملكة ضمن مبادرتها المجانية للعام 2019 حيث قدمت 6 برامج تدريبية نوعية. وثمن رئيس مجلس إدارة الغرفة، عبدالحكيم العمار الخالدي، رعاية سمو أمير المنطقة الشرقية للمبادرة، مؤكدا أن دعم سموه لجميع أنشطة .
  <br>
</div>
 

**The generated titles**
```
title#0 غرفة الشرقية تختتم المرحلة الثانية من مبادرتها لتأهيل وتدريب أبناء وبنات المملكة
title#1 غرفة الشرقية تختتم الثاني من مبادرة تأهيل وتأهيل أبناء وبناتنا
title#2 سعود بن نايف يختتم ثانى مبادراتها لتأهيل وتدريب أبناء وبنات المملكة
title#3 أمير الشرقية يرعى اختتام برنامج برنامج تدريب أبناء وبنات المملكة
title#4 سعود بن نايف يرعى اختتام مبادرة تأهيل وتدريب أبناء وبنات المملكة
```

# AraT5 Models Checkpoints 

AraT5 Pytorch and TensorFlow checkpoints are available on the Huggingface website for direct download and use ```exclusively for research```. ```For commercial use, please contact the authors via email @ (muhammad.mageed[at]ubc[dot]ca).```

| **Model**   | **Link** | 
|---------|:------------------:|
|  **AraT5-base** |     [https://huggingface.co/UBC-NLP/AraT5-base](https://huggingface.co/UBC-NLP/AraT5-base)       | 
| **AraT5-msa-base**  |     [https://huggingface.co/UBC-NLP/AraT5-msa-base](https://huggingface.co/UBC-NLP/AraT5-msa-base)     |     
| **AraT5-tweet-base**  |   [https://huggingface.co/UBC-NLP/AraT5-tweet-base](https://huggingface.co/UBC-NLP/AraT5-tweet-base)    |      
| **AraT5-msa-small** |     [https://huggingface.co/UBC-NLP/AraT5-msa-small](https://huggingface.co/UBC-NLP/AraT5-msa-small)   |     
| **AraT5-tweet-small**|    [https://huggingface.co/UBC-NLP/AraT5-tweet-small](https://huggingface.co/UBC-NLP/AraT5-tweet-small) |  

# BibTex

If you use our models (Arat5-base, Arat5-msa-base, Arat5-tweet-base, Arat5-msa-small, or Arat5-tweet-small ) for your scientific publication, or if you find the resources in this repository useful, please cite our paper as follows (to be updated):
```bibtex
@inproceedings{nagoudi-etal-2022-arat5,
    title = "{A}ra{T}5: Text-to-Text Transformers for {A}rabic Language Generation",
    author = "Nagoudi, El Moatez Billah  and
      Elmadany, AbdelRahim  and
      Abdul-Mageed, Muhammad",
    booktitle = "Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = may,
    year = "2022",
    address = "Dublin, Ireland",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.acl-long.47",
    pages = "628--647",
    abstract = "Transfer learning with a unified Transformer framework (T5) that converts all language problems into a text-to-text format was recently proposed as a simple and effective transfer learning approach. Although a multilingual version of the T5 model (mT5) was also introduced, it is not clear how well it can fare on non-English tasks involving diverse data. To investigate this question, we apply mT5 on a language with a wide variety of dialects{--}Arabic. For evaluation, we introduce a novel benchmark for ARabic language GENeration (ARGEN), covering seven important tasks. For model comparison, we pre-train three powerful Arabic T5-style models and evaluate them on ARGEN. Although pre-trained with {\textasciitilde}49 less data, our new models perform significantly better than mT5 on all ARGEN tasks (in 52 out of 59 test sets) and set several new SOTAs. Our models also establish new SOTA on the recently-proposed, large Arabic language understanding evaluation benchmark ARLUE (Abdul-Mageed et al., 2021). Our new models are publicly available. We also link to ARGEN datasets through our repository: https://github.com/UBC-NLP/araT5.",
}
```

## Acknowledgments
We gratefully acknowledge support from the Natural Sciences and Engineering Research Council  of Canada, the  Social  Sciences and  Humanities  Research  Council  of  Canada, Canadian  Foundation for  Innovation,  [ComputeCanada](www.computecanada.ca) and [UBC ARC-Sockeye](https://doi.org/10.14288/SOCKEYE). We  also  thank  the  [Google TensorFlow Research Cloud (TFRC)](https://www.tensorflow.org/tfrc) program for providing us with free TPU access.
