---
license: cc-by-4.0
language: 
- pl
datasets:
- Wikipedia
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
widget:
- source_sentence: "Uczenie maszynowe jest konsekwencją rozwoju idei sztucznej inteligencji i metod jej wdrażania praktycznego."
  sentences:
    - "Głębokie uczenie maszynowe jest sktukiem wdrażania praktycznego metod sztucznej inteligencji oraz jej rozwoju."
    - "Kasparow zarzucił firmie IBM oszustwo, kiedy odmówiła mu dostępu do historii wcześniejszych gier Deep Blue. "
    - "Samica o długości ciała 10–11 mm, szczoteczki na tylnych nogach służące do zbierania pyłku oraz włoski na końcu odwłoka jaskrawo pomarańczowoczerwone. "
  example_title: "Uczenie maszynowe"
---
<img src="https://public.3.basecamp.com/p/rs5XqmAuF1iEuW6U7nMHcZeY/upload/download/VL-NLP-short.png" alt="logo voicelab nlp" style="width:300px;"/>

# SHerbert large - Polish SentenceBERT
SentenceBERT is a modification of the pretrained BERT network that use siamese and triplet network structures to derive semantically meaningful sentence embeddings that can be compared using cosine-similarity. Training was based on the original paper [Siamese BERT models for the task of semantic textual similarity (STS)](https://arxiv.org/abs/1908.10084) with a slight modification of how the training data was used. The goal of the model is to generate different embeddings based on the semantic and topic similarity of the given text.

> Semantic textual similarity analyzes how similar two pieces of texts are.

Read more about how the model was prepared in our [blog post](https://voicelab.ai/blog/).

The base trained model is a Polish HerBERT. HerBERT is a BERT-based Language Model. For more details, please refer to: "HerBERT: Efficiently Pretrained Transformer-based Language Model for Polish".

# Corpus
Te model was trained solely on [Wikipedia](https://dumps.wikimedia.org/).


# Tokenizer

As in the original HerBERT implementation, the training dataset was tokenized into subwords using a character level byte-pair encoding (CharBPETokenizer) with a vocabulary size of 50k tokens. The tokenizer itself was trained with a tokenizers library. 

We kindly encourage you to use the Fast version of the tokenizer, namely HerbertTokenizerFast.

# Usage

 ```python
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics import pairwise

sbert = AutoModel.from_pretrained("Voicelab/sbert-large-cased-pl")
tokenizer = AutoTokenizer.from_pretrained("Voicelab/sbert-large-cased-pl")

s0 = "Uczenie maszynowe jest konsekwencją rozwoju idei sztucznej inteligencji i metod jej wdrażania praktycznego."
s1 = "Głębokie uczenie maszynowe jest sktukiem wdrażania praktycznego metod sztucznej inteligencji oraz jej rozwoju."
s2 = "Kasparow zarzucił firmie IBM oszustwo, kiedy odmówiła mu dostępu do historii wcześniejszych gier Deep Blue. "

tokens = tokenizer([s0, s1, s2], 
                    padding=True, 
                    truncation=True,
                    return_tensors='pt')
x = sbert(tokens["input_ids"],
            tokens["attention_mask"]).pooler_output

# similarity between sentences s0 and s1
print(pairwise.cosine_similarity(x[0], x[1])) # Result: 0.8011128

# similarity between sentences s0 and s2
print(pairwise.cosine_similarity(x[0], x[2])) # Result: 0.58822715
    
 ```
# Results

| Model                    | Accuracy   | Source                                                   |
|--------------------------|------------|----------------------------------------------------------|
| SBERT-WikiSec-base (EN)  | 80.42%     | https://arxiv.org/abs/1908.10084                         |
| SBERT-WikiSec-large (EN) | 80.78%     | https://arxiv.org/abs/1908.10084                         |
| sbert-base-cased-pl       | 82.31%     | https://huggingface.co/Voicelab/sbert-base-cased-pl    |
| **sbert-large-cased-pl**  | **84.42%** | **https://huggingface.co/Voicelab/sbert-large-cased-pl** |

# License

CC BY 4.0

# Citation

If you use this model, please cite the following paper:


# Authors

The model was trained by NLP Research Team at Voicelab.ai.

You can contact us [here](https://voicelab.ai/contact/).