---
license: gpl
---
Ady Endre style GPT network. 
Some details about the network: 
-It's based on a hungarian language model that was also trained from scratch with casual language modelling.
-The language model was trained 1,5x times on a big part of the Hungarian Wikipedia, then trained on all of Ady Endre's poems. 
-The model has a GPT2-like architecture with a few small tweaks.
-The network has about 258M parameters.


*To get optimal result its recommended to run the model with a text-generation pipeline using the following options: 
* no_repeat_ngram_size=2 
* top_k=50
* num_beams = 2
* max_length = 50<

