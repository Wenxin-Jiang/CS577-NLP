---
language:
- de
- en
pipeline_tag: sentence-similarity
tags:
- semantic textual similarity
- sts
- semantic search
- sentence similarity
- paraphrasing
- sentence-transformer
- feature-extraction
- transformers
---

# Model card for PM-AI/sts_paraphrase_xlm-roberta-base_de-en

## Model summary
Transformer model for **Semantic Textual Similarity (STS)** for _German_ and _Englisch_ sentences/texts.
The embeddings output can be used for **semantic search**, **paraphrasing** and **retrieval** with _cosine similarity_.
The Model is applicable to _Englisch-German-Mixed_ sentences/texts but also for _Englisch only_ and _German only_.

The model can be easily used with [Sentence Transformer](https://github.com/UKPLab/sentence-transformers) library.

## Training
This model is based on a training approach from 2020 by Philip May, who published the [T-Systems-onsite/cross-en-de-roberta-sentence-transformer](https://huggingface.co/T-Systems-onsite/cross-en-de-roberta-sentence-transformer) model.
We updated this approach by a new base model for fine-tuning and some extensions to the training data.
These changes are discussed in the next sections.

### Training Data
The model is based on training with samples from [STSb](https://huggingface.co/datasets/stsb_multi_mt), [SICK](https://huggingface.co/datasets/mteb/sickr-sts) and [Priya22 semantic textual relatedness](https://github.com/Priya22/semantic-textual-relatedness) datasets.
They contain about 76.000 sentence pairs in total.
These sentence pairs are based on _German-German_, _English-English_ and _German-English mixed_.
The training object is to optimize for _cosine similarity loss_ based on a human annoted sentence similarity score.
In terms of content, the samples are based on rather simple sentences.

When the TSystems model was published, only the STSb dataset was used for STS training.
Therefore it is included in our model, but expanded to include SICK and Priya22 semantic textual relatedness:
 - SICK was partly used in STSb, but our custom translation using [DeepL](https://www.deepl.com/) leads to slightly different phrases. This approach allows more examples to be included in the training.
 - The Priya22 semantic textual relatedness dataset published in 2022 was also translated into German via DeepL and added to the training data. Since it does not have a train-test-split, it was created independently at a ratio of 80:20.

All training and test data (STSb, Sick, Priya22) were checked for duplicates within and with each other and removed if found.
Because the test data is prioritized, duplicated entries between test-train are exclusively removed from train split.
The final used datasets can be viewed here: [datasets_sts_paraphrase_xlm-roberta-base_de-en](https://gitlab.com/sense.ai.tion-public/datasets_sts_paraphrase_xlm-roberta-base_de-en)

### Training
Befor fine-tuning for STS we made the English paraphrasing model [paraphrase-distilroberta-base-v1](https://huggingface.co/sentence-transformers/paraphrase-distilroberta-base-v1) usable for German by applying **[Knowledge Distillation](https://arxiv.org/abs/2004.09813)** (_Teacher-Student_ approach).
The TSystems model used version 1, which is based on 7 different datasets and contains around 24.6 million samples.
We are using version 2 with 12 datasets and about 83.3 million examples.
Details for this process here: [PM-AI/paraphrase-distilroberta-base-v2_de-en](https://huggingface.co/PM-AI/paraphrase-distilroberta-base-v2_de-en)

For fine-tuning we are using SBERT's [training_stsbenchmark_continue_training.py](https://github.com/UKPLab/sentence-transformers/blob/b86eec31cf0a102ad786ba1ff31bfeb4998d3ca5/examples/training/sts/training_stsbenchmark_continue_training.py) training script.
One thing has been changed in this training script: when a sentence pair consists of identical utterances the score is set to 5.0 (maximum).
It makes no sense to say identical sentences have a score of 4.8 or 4.9.

#### Parameterization of training
- **Script:** [training_stsbenchmark_continue_training.py](https://github.com/UKPLab/sentence-transformers/blob/b86eec31cf0a102ad786ba1ff31bfeb4998d3ca5/examples/training/sts/training_stsbenchmark_continue_training.py)
- **Datasets:** [datasets_sts_paraphrase_xlm-roberta-base_de-en/all_cross_train_unique.csv](https://gitlab.com/sense.ai.tion-public/datasets_sts_paraphrase_xlm-roberta-base_de-en)
- **GPU:** NVIDIA A40 (Driver Version: 515.48.07; CUDA Version: 11.7)
- **Batch Size:** 32
- **Base Model:** [PM-AI/paraphrase-distilroberta-base-v2_de-en](PM-AI/paraphrase-distilroberta-base-v2_de-en)
- **Loss Function:** Cosine Similarity
- **Learning Rate:** 2e-5
- **Epochs:** 3
- **Evaluation Samples:** 500
- **Evaluation Steps:** 1000
- **Warmup Steps:** 10%

### Evaluation <a name="evaluation"></a>

Now the performance is measured cross-lingually as well as for German and English only.
In addition, the test samples used are evaluated individually for each data set (STSb, SICK, Priya22), as well as in a large combined test data set (all).
This subdivision per data set allows for a fair overall assessment, since external models are not built on the same data basis as the model presented here.
The data is not evenly distributed in either training or testing!

**❗Some models are only usable for one language (because they are monolingual). They will almost not perform at all in the other two tables. Still, they are good models in certain applications❗**

The first table shows the evaluation results for **cross-lingual (German-English-Mixed)** based on _Spearman_:
**model**|**STSb**|**SICK**|**Priya22**|**all**|
:-----:|:-----:|:-----:|:-----:|:-----:
[PM-AI/sts_paraphrase_xlm-roberta-base_de-en (ours)](https://huggingface.co/PM-AI/sts_paraphrase_xlm-roberta-base_de-en) | 0.8672 <br /> 🏆 | 0.8639 <br /> 🏆 | 0.8354 <br /> 🏆 | 0.8711 <br /> 🏆
[T-Systems-onsite/cross-en-de-roberta-sentence-transformer](https://huggingface.co/T-Systems-onsite/cross-en-de-roberta-sentence-transformer) | 0.8525 | 0.7642 | 0.7998 | 0.8216
[PM-AI/paraphrase-distilroberta-base-v2_de-en (ours, no fine-tuning)](PM-AI/paraphrase-distilroberta-base-v2_de-en) | 0.8225 | 0.7579 | 0.8255 | 0.8109
[sentence-transformers/paraphrase-multilingual-mpnet-base-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2) | 0.8310 | 0.7529 | 0.8184 | 0.8102
[sentence-transformers/stsb-xlm-r-multilingual](https://huggingface.co/sentence-transformers/stsb-xlm-r-multilingual) | 0.8194 | 0.7703 | 0.7566 | 0.7998
[sentence-transformers/paraphrase-xlm-r-multilingual-v1](https://huggingface.co/sentence-transformers/paraphrase-xlm-r-multilingual-v1) | 0.7985 | 0.7217 | 0.7975 | 0.7838
[sentence-transformers/xlm-r-distilroberta-base-paraphrase-v1](https://huggingface.co/sentence-transformers/xlm-r-distilroberta-base-paraphrase-v1) | 0.7985 | 0.7217 | 0.7975 | 0.7838
[sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2) | 0.7823 | 0.7090 | 0.7830 | 0.7834
[sentence-transformers/distiluse-base-multilingual-cased-v1](https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v1) | 0.7449 | 0.6941 | 0.7607 | 0.7534
[sentence-transformers/distiluse-base-multilingual-cased-v2](https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v2) | 0.7517 | 0.6950 | 0.7619 | 0.7496
[sentence-transformers/distilbert-multilingual-nli-stsb-quora-ranking](https://huggingface.co/sentence-transformers/distilbert-multilingual-nli-stsb-quora-ranking) | 0.7211 | 0.6650 | 0.7382 | 0.7200
[Sahajtomar/German-semantic](https://huggingface.co/Sahajtomar/German-semantic) | 0.7170 | 0.5871 | 0.7204 | 0.6802
[symanto/sn-xlm-roberta-base-snli-mnli-anli-xnli](https://huggingface.co/symanto/sn-xlm-roberta-base-snli-mnli-anli-xnli) | 0.6488 | 0.5489 | 0.6688 | 0.6303
[sentence-transformers/sentence-t5-large](https://huggingface.co/sentence-transformers/sentence-t5-large) | 0.6849 | 0.6063 | 0.7360 | 0.5843
[sentence-transformers/sentence-t5-base](https://huggingface.co/sentence-transformers/sentence-t5-base) | 0.6013 | 0.5213 | 0.6671 | 0.5068
[sentence-transformers/gtr-t5-large](https://huggingface.co/sentence-transformers/gtr-t5-large) | 0.5881 | 0.5168 | 0.6674 | 0.4984
[deepset/gbert-large-sts](https://huggingface.co/deepset/gbert-large-sts) | 0.3842 | 0.3537 | 0.4105 | 0.4362
[sentence-transformers/gtr-t5-base](https://huggingface.co/sentence-transformers/gtr-t5-base) | 0.5204 | 0.4346 | 0.6008 | 0.4276
[textattack/bert-base-uncased-STS-B](https://huggingface.co/textattack/bert-base-uncased-STS-B) | 0.0669 | 0.1135 | 0.0105 | 0.1514
[symanto/xlm-roberta-base-snli-mnli-anli-xnli](https://huggingface.co/symanto/xlm-roberta-base-snli-mnli-anli-xnli) | 0.1694 | 0.0440 | 0.0521 | 0.1156

The second table shows the evaluation results for **German only** based on _Spearman_:
**model**|**STSb**|**SICK**|**Priya22**|**all**|
:-----:|:-----:|:-----:|:-----:|:-----:
[PM-AI/sts_paraphrase_xlm-roberta-base_de-en (ours)](https://huggingface.co/PM-AI/sts_paraphrase_xlm-roberta-base_de-en) | 0.8658 <br /> 🏆 | 0.8775 <br /> 🏆 | 0.8432 <br /> 🏆 | 0.8747 <br /> 🏆
[T-Systems-onsite/cross-en-de-roberta-sentence-transformer](https://huggingface.co/T-Systems-onsite/cross-en-de-roberta-sentence-transformer) | 0.8547 | 0.8047 | 0.8068 | 0.8327
[Sahajtomar/German-semantic](https://huggingface.co/Sahajtomar/German-semantic) | 0.8485 | 0.7915 | 0.8139 | 0.8280
[sentence-transformers/paraphrase-multilingual-mpnet-base-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2) | 0.8360 | 0.7941 | 0.8237 | 0.8178
[PM-AI/paraphrase-distilroberta-base-v2_de-en (ours, no fine-tuning)](PM-AI/paraphrase-distilroberta-base-v2_de-en) | 0.8297 | 0.7930 | 0.8341 | 0.8170
[sentence-transformers/stsb-xlm-r-multilingual](https://huggingface.co/sentence-transformers/stsb-xlm-r-multilingual) | 0.8190 | 0.8027 | 0.7674 | 0.8072
[sentence-transformers/paraphrase-xlm-r-multilingual-v1](https://huggingface.co/sentence-transformers/paraphrase-xlm-r-multilingual-v1) | 0.8079 | 0.7844 | 0.8126 | 0.8034
[sentence-transformers/xlm-r-distilroberta-base-paraphrase-v1](https://huggingface.co/sentence-transformers/xlm-r-distilroberta-base-paraphrase-v1) | 0.8079 | 0.7844 | 0.8126 | 0.8034
[sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2) | 0.7891 | 0.7830 | 0.8010 | 0.7981
[sentence-transformers/distiluse-base-multilingual-cased-v1](https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v1) | 0.7705 | 0.7612 | 0.7899 | 0.7780
[sentence-transformers/sentence-t5-large](https://huggingface.co/sentence-transformers/sentence-t5-large) | 0.7771 | 0.7724 | 0.7829 | 0.7727
[sentence-transformers/sentence-t5-base](https://huggingface.co/sentence-transformers/sentence-t5-base) | 0.7361 | 0.7613 | 0.7643 | 0.7602
[sentence-transformers/distiluse-base-multilingual-cased-v2](https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v2) | 0.7467 | 0.7494 | 0.7684 | 0.7584
[sentence-transformers/distilbert-multilingual-nli-stsb-quora-ranking](https://huggingface.co/sentence-transformers/distilbert-multilingual-nli-stsb-quora-ranking) | 0.7419 | 0.7420 | 0.7692 | 0.7566
[sentence-transformers/gtr-t5-large](https://huggingface.co/sentence-transformers/gtr-t5-large) | 0.7252 | 0.7201 | 0.7613 | 0.7447
[sentence-transformers/gtr-t5-base](https://huggingface.co/sentence-transformers/gtr-t5-base) | 0.7058 | 0.6943 | 0.7462 | 0.7271
[symanto/sn-xlm-roberta-base-snli-mnli-anli-xnli](https://huggingface.co/symanto/sn-xlm-roberta-base-snli-mnli-anli-xnli) | 0.7284 | 0.7136 | 0.7109 | 0.6997
[deepset/gbert-large-sts](https://huggingface.co/deepset/gbert-large-sts) | 0.6576 | 0.7141 | 0.6769 | 0.6959
[textattack/bert-base-uncased-STS-B](https://huggingface.co/textattack/bert-base-uncased-STS-B) | 0.4427 | 0.6023 | 0.4380 | 0.5380
[symanto/xlm-roberta-base-snli-mnli-anli-xnli](https://huggingface.co/symanto/xlm-roberta-base-snli-mnli-anli-xnli) | 0.4154 | 0.5048 | 0.3478 | 0.4540

And last but not least our third table which shows the evaluation results for **English only** based on _Spearman_:
**model**|**STSb**|**SICK**|**Priya22**|**all**|
:-----:|:-----:|:-----:|:-----:|:-----:
[PM-AI/sts_paraphrase_xlm-roberta-base_de-en (ours)](https://huggingface.co/PM-AI/sts_paraphrase_xlm-roberta-base_de-en) | 0.8768 <br /> 🏆 | 0.8705 <br /> 🏆 | 0.8402 | 0.8748 <br /> 🏆
[sentence-transformers/paraphrase-multilingual-mpnet-base-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2) | 0.8682 | 0.8065 | 0.8430 | 0.8378
[PM-AI/paraphrase-distilroberta-base-v2_de-en (ours, no fine-tuning)](PM-AI/paraphrase-distilroberta-base-v2_de-en) | 0.8597 | 0.8105 | 0.8399 | 0.8363
[T-Systems-onsite/cross-en-de-roberta-sentence-transformer](https://huggingface.co/T-Systems-onsite/cross-en-de-roberta-sentence-transformer) | 0.8660 | 0.7897 | 0.8097 | 0.8308
[sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2) | 0.8441 | 0.8059 | 0.8175 | 0.8300
[sentence-transformers/sentence-t5-base](https://huggingface.co/sentence-transformers/sentence-t5-base) | 0.8551 | 0.8063 | 0.8434 | 0.8235
[sentence-transformers/sentence-t5-large](https://huggingface.co/sentence-transformers/sentence-t5-large) | 0.8536 | 0.8097 | 0.8475 <br /> 🏆 | 0.8191
[sentence-transformers/stsb-xlm-r-multilingual](https://huggingface.co/sentence-transformers/stsb-xlm-r-multilingual) | 0.8503 | 0.8009 | 0.7675 | 0.8162
[sentence-transformers/paraphrase-xlm-r-multilingual-v1](https://huggingface.co/sentence-transformers/paraphrase-xlm-r-multilingual-v1) | 0.8350 | 0.7645 | 0.8211 | 0.8050
[sentence-transformers/xlm-r-distilroberta-base-paraphrase-v1](https://huggingface.co/sentence-transformers/xlm-r-distilroberta-base-paraphrase-v1) | 0.8350 | 0.7645 | 0.8211 | 0.8050
[sentence-transformers/distiluse-base-multilingual-cased-v2](https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v2) | 0.8075 | 0.7534 | 0.7908 | 0.7828
[sentence-transformers/distiluse-base-multilingual-cased-v1](https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v1) | 0.8061 | 0.7421 | 0.7923 | 0.7784
[Sahajtomar/German-semantic](https://huggingface.co/Sahajtomar/German-semantic) | 0.8061 | 0.7098 | 0.7709 | 0.7712
[sentence-transformers/distilbert-multilingual-nli-stsb-quora-ranking](https://huggingface.co/sentence-transformers/distilbert-multilingual-nli-stsb-quora-ranking) | 0.7866 | 0.7477 | 0.7700 | 0.7691
[sentence-transformers/gtr-t5-large](https://huggingface.co/sentence-transformers/gtr-t5-large) | 0.7763 | 0.7258 | 0.8124 | 0.7675
[sentence-transformers/gtr-t5-base](https://huggingface.co/sentence-transformers/gtr-t5-base) | 0.7961 | 0.7129 | 0.8147 | 0.7669
[symanto/sn-xlm-roberta-base-snli-mnli-anli-xnli](https://huggingface.co/symanto/sn-xlm-roberta-base-snli-mnli-anli-xnli) | 0.7799 | 0.7415 | 0.7335 | 0.7376
[deepset/gbert-large-sts](https://huggingface.co/deepset/gbert-large-sts) | 0.5703 | 0.6011 | 0.5673 | 0.6060
[textattack/bert-base-uncased-STS-B](https://huggingface.co/textattack/bert-base-uncased-STS-B) | 0.4978 | 0.6099 | 0.5505 | 0.5754
[symanto/xlm-roberta-base-snli-mnli-anli-xnli](https://huggingface.co/symanto/xlm-roberta-base-snli-mnli-anli-xnli) | 0.3830 | 0.5180 | 0.3056 | 0.4414

**❗It is crucial to understand that:**
- Only our model has seen training data from STSb, SICK and Priya22 combined, which is one reason for better results. The model has simply been trained to be more sensitive to these type of samples.
- The datasets are not proportionally aligned in terms of their number of examples. For example, Priya22 is significantly underrepresented.
- The compared models are of different sizes, which affects resource consumption (CPU, RAM) and inference speed (benchmark). So-called "large" models usually perform better, but also cost more (resources, monetary value) than e.g. "base" models.
- Multilingual models are usually made multilingual by Knowledge Distillation, starting from a monolingual state. Therefore, they usually perform somewhat better in the original language.

### Acknowledgment

This work is a collaboration between [Technical University of Applied Sciences Wildau (TH Wildau)](https://en.th-wildau.de/) and [sense.ai.tion GmbH](https://senseaition.com/).
You can contact us via:
* [Philipp Müller (M.Eng.)](https://www.linkedin.com/in/herrphilipps); Author
* [Prof. Dr. Janett Mohnke](mailto:icampus@th-wildau.de); TH Wildau
* [Dr. Matthias Boldt, Jörg Oehmichen](mailto:info@senseaition.com); sense.AI.tion GmbH 

This work was funded by the European Regional Development Fund (EFRE) and the State of Brandenburg. Project/Vorhaben: "ProFIT: Natürlichsprachliche Dialogassistenten in der Pflege".

<div style="display:flex">
     <div style="padding-left:20px;">
          <a href="https://efre.brandenburg.de/efre/de/"><img src="https://huggingface.co/datasets/PM-AI/germandpr-beir/resolve/main/res/EFRE-Logo_rechts_oweb_en_rgb.jpeg" alt="Logo of European Regional Development Fund (EFRE)" width="200"/></a>
     </div>
     <div style="padding-left:20px;">
          <a href="https://www.senseaition.com"><img src="https://senseaition.com/wp-content/uploads/thegem-logos/logo_c847aaa8f42141c4055d4a8665eb208d_3x.png" alt="Logo of senseaition GmbH" width="200"/></a>
     </div>
     <div style="padding-left:20px;">
          <a href="https://www.th-wildau.de"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/TH_Wildau_Logo.png/640px-TH_Wildau_Logo.png" alt="Logo of TH Wildau" width="180"/></a>
     </div>
</div>