---
license: mit
widget:
- text: "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data."
- text: "Text-to-image generation has traditionally focused on finding better modeling assumptions for training on a fixed dataset. These assumptions might involve complex architectures, auxiliary losses, or side information such as object part labels or segmentation masks supplied during training. We describe a simple approach for this task based on a transformer that autoregressively models the text and image tokens as a single stream of data. With sufficient data and scale, our approach is competitive with previous domain-specific models when evaluated in a zero-shot fashion."
---

[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AI-Growth-Lab/SciNerTopic/blob/main/notebooks/Sci_NERTopic.ipynb)

![](https://raw.githubusercontent.com/AI-Growth-Lab/SciNerTopic/main/vis/punchcard_nlp.jpg)

NER model based on `allenai/scibert_scivocab_cased`
Fine-tuned using the [SciERC Dataset](http://nlp.cs.washington.edu/sciIE/) to identify scientific terms:

- Task: Applications, problems to solve, systems to construct.
E.g. information extraction, machine reading system, image segmentation, etc.
- Method: Methods , models, systems to use, or tools, components of a system, frameworks.
E.g. language model, CORENLP, POS parser, kernel method, etc.
• Evaluation Metric: Metrics, measures, or entities that can express the quality of a system/method.
E.g. F1, BLEU, Precision, Recall, ROC curve, mean reciprocal rank, mean-squared error, robustness,
time complexity, etc.
- Material: Data, datasets, resources, Corpus, Knowledge base.
E.g. image data, speech data, stereo images, bilingual dictionary, paraphrased questions, CoNLL,
Panntreebank, WordNet, Wikipedia, etc.
- Other Scientific Terms: Phrases that are scientific terms but do not fall into any of the above classes
E.g. physical or geometric constraints, qualitative prior knowledge, discourse structure, syntactic rule,
discourse structure, tree, node, tree kernel, features, noise, criteria
- Generic: General terms or pronouns that may refer to an entity but are not themselves informative,
often used as connection words.
E.g model, approach, prior knowledge, them, it...


## Training
- Learning Rate: 1e-05
- Epochs: 10,

## Performance
- Eval Loss: 0.401
- Precision 0.577
- Recall: 0.632
- F1: 0.603

![](https://github.com/AI-Growth-Lab/SciNerTopic/raw/main/vis/ner-model-confusion.png)


## Colab

Check out how this model is used for NER-enhanced topic modelling, inspired by [BERTopic](https://maartengr.github.io/BERTopic).

[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AI-Growth-Lab/SciNerTopic/blob/main/notebooks/Sci_NERTopic.ipynb)

![](https://github.com/AI-Growth-Lab/SciNerTopic/raw/main/vis/sciner-map.jpg)

## Use
```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("RJuro/SciNERTopic")
model_trf = AutoModelForTokenClassification.from_pretrained("RJuro/SciNERTopic")

nlp = pipeline("ner", model=model_trf, tokenizer=tokenizer, aggregation_strategy='average')
```

## Cite this model
```latex
@misc {roman_jurowetzki_2022,
	author       = { {Roman Jurowetzki, Hamid Bekamiri} },
	title        = { SciNERTopic - NER enhanced transformer-based topic modelling for scientific text },
	year         = 2022,
	url          = { https://huggingface.co/RJuro/SciNERTopic },
	doi          = { 10.57967/hf/0095 },
	publisher    = { Hugging Face }
}
```