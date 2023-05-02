---
language: fr        # <-- my language
widget:
 - text: "J'aime ta coiffure"
   example_title: "NOT TOXIC 1" 
 - text: "Va te faire foutre"
   example_title: "TOXIC 1"
 - text: "Quel mauvais temps, n'est-ce pas ?"
   example_title: "NOT TOXIC 2" 
 - text: "J'espère que tu vas mourir, connard !"
   example_title: "TOXIC 2"
 - text: "j'aime beaucoup ta veste"   
   example_title: "NOT TOXIC 3"

license: other
---
This model was trained for toxicity labeling. Label_1 means TOXIC, Label_0 means NOT TOXIC

The model was fine-tuned based off [the CamemBERT language model](https://huggingface.co/camembert-base).

The accuracy is 93% on the test split during training and 79% on a manually picked (and thus harder) sample of 200 sentences (100 label 1, 100 label 0) at the end of the training.

The model was finetuned on 32k sentences. The train data was the translations of the English data (around 30k sentences) from [the multilingual_detox dataset](https://github.com/s-nlp/multilingual_detox) by [Skolkovo Institute](https://huggingface.co/SkolkovoInstitute) using [the opus-mt-en-fr translation model](https://huggingface.co/Helsinki-NLP/opus-mt-en-fr) by [Helsinki-NLP](https://huggingface.co/Helsinki-NLP) and the data from [the jigsaw dataset](https://www.kaggle.com/competitions/jigsaw-multilingual-toxic-comment-classification/data) on kaggle.