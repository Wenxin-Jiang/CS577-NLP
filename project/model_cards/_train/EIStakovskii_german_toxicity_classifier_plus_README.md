---
language: de        # <-- my language
widget:
 - text: "Guten morgen, meine Liebe"
   example_title: "NOT TOXIC 1"
 - text: "Ich scheiß drauf."
   example_title: "TOXIC 1"
 - text: "Ich liebe dich"
   example_title: "NOT TOXIC 2" 
 - text: "Ich hab die Schnauze voll von diesen Irren."
   example_title: "TOXIC 2" 
 - text: "Ich wünsche Ihnen einen schönen Tag!"   
   example_title: "NOT TOXIC 3"
 - text: "Nigger"
   example_title: "TOXIC 3" 
 - text: "Du bist schon wieder zu spät!"   
   example_title: "NOT TOXIC 4"
 - text: "Beweg deinen AArschhh hier rüber"
   example_title: "TOXIC 4" 
   
license: other
---
This model was trained for toxicity labeling. Label_1 means TOXIC, Label_0 means NOT TOXIC

The model was fine-tuned based off the already existing sentiment classifier oliverguhr/german-sentiment-bert . The aforementioned classifier performed poorly (44% accuracy on my test sample), so I trained the current toxicity classifier. It was noted that the same performance achieved training on the [dbmdz/bert-base-german-cased model](https://huggingface.co/dbmdz/bert-base-german-cased).

The accuracy is 91% on the test split during training and 83% on a manually picked (and thus harder) sample of 200 sentences (100 label 1, 100 label 0) at the end of the training. 

The model was finetuned on 37k sentences. The train data was the translations of the English data (around 30k sentences) from [the multilingual_detox dataset](https://github.com/s-nlp/multilingual_detox) by [Skolkovo Institute](https://huggingface.co/SkolkovoInstitute) using [the opus-mt-en-de translation model](https://huggingface.co/Helsinki-NLP/opus-mt-en-de) by [Helsinki-NLP](https://huggingface.co/Helsinki-NLP) and semi-manually collected data (around 7 k) by crawling [the dict.cc web dictionary](https://www.dict.cc/) and [the Reverso Context](https://context.reverso.net/translation/).