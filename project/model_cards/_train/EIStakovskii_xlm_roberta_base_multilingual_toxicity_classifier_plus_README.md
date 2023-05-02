---
language: multilingual          # <-- my language
widget:
 - text: "J'aime ta coiffure"
 - text: "Va te faire foutre"
 - text: "Quel mauvais temps, n'est-ce pas ?"
 - text: "J'espère que tu vas mourir, connard !"
 - text: "j'aime beaucoup ta veste"
 - text: "Guten morgen, meine Liebe"
 - text: "Ich scheiß drauf."
 - text: "Ich liebe dich"
 - text: "Ich hab die Schnauze voll von diesen Irren."
 - text: "Ich wünsche Ihnen einen schönen Tag!"
 - text: "Сука тупая"
 - text: "Какая прекрасная погода!"
 - text: "Я ненавижу тебя козёл!"
 - text: "Хлеб всему голова"
 - text: "Вот же ублюдок...."
 - text: "Go fuck yoursefl, asshole"
 - text: "I don't really like this idea"
 - text: "Look at this dickhead tho"
 - text: "Usually, she is more open about that"
 - text: "Why you have to always fuck everything up????"
 - text: "I like this car"
         
   

license: other
---

This model was trained for multilingual toxicity labeling. Label_1 means TOXIC, Label_0 means NOT TOXIC. 

The model was fine-tuned based off the xlm_roberta_base model for 4 languages: EN, RU, FR, DE 

The validation accuracy is 92%. 

The model was finetuned on the total sum of 100933k sentences. The train data for English and Russian came from https://github.com/s-nlp/multilingual_detox, French data comprised the translated to French data from https://github.com/s-nlp/multilingual_detox as well as all the French data from the Jigsaw dataset, the German data was similarly composed using translations and semi-manual data collection techniquies, in particular for offensive words and phrases were crawled the dict.cc dictionary (https://www.dict.cc/) and the Reverso Context (https://context.reverso.net/translation/).