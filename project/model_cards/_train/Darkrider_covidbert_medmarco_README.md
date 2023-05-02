Fine-tuned CovidBERT on Med-Marco Dataset for passage ranking 

# CovidBERT-MedNLI

This is the model **CovidBERT** trained by DeepSet on AllenAI's [CORD19 Dataset](https://pages.semanticscholar.org/coronavirus-research) of scientific articles about coronaviruses.

The model uses the original BERT wordpiece vocabulary and was subsequently fine-tuned on the [SNLI](https://nlp.stanford.edu/projects/snli/) and the [MultiNLI](https://www.nyu.edu/projects/bowman/multinli/) datasets using the [`sentence-transformers` library](https://github.com/UKPLab/sentence-transformers/) to produce universal sentence embeddings [1] using the **average pooling strategy** and a **softmax loss**.

It is further fine-tuned Med-Marco Dataset. MacAvaney et.al in their [paper](https://arxiv.org/abs/2010.05987) titled “SLEDGE-Z: A Zero-Shot Baseline for COVID-19 Literature Search” used MedSyn a lexicon of layperson and expert terminology for various medical conditions to filter for medical questions. One can also replace this by UMLs ontologies but the beauty of MedSyn is that the terms are more general human conversation lingo and not terms based on scientific literature.


Parameter details for the original training on CORD-19 are available on [DeepSet's MLFlow](https://public-mlflow.deepset.ai/#/experiments/2/runs/ba27d00c30044ef6a33b1d307b4a6cba)

**Base model**: `deepset/covid_bert_base` from HuggingFace's `AutoModel`.

