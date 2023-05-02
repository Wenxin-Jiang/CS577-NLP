This model is used to tag the tokens in an input sequence with information about the different signs of syntactic complexity that they contain. For more details, please see Chapters 2 and 3 of my thesis (http://rgcl.wlv.ac.uk/~richard/Evans2020_SentenceSimplificationForTextProcessing.pdf).

It was derived using code written by Dr. Le An Ha at the University of Wolverhampton.

To use this model, the following code snippet may help:


======================================================================  

import torch
from transformers import AutoModelForTokenClassification, AutoTokenizer

SignTaggingModel = AutoModelForTokenClassification.from_pretrained('RJ3vans/SignTagger')
SignTaggingTokenizer = AutoTokenizer.from_pretrained('RJ3vans/SignTagger')

label_list = ["M:N_CCV", "M:N_CIN", "M:N_CLA", "M:N_CLAdv", "M:N_CLN", "M:N_CLP", # This could be obtained from the config file
              "M:N_CLQ", "M:N_CLV", "M:N_CMA1", "M:N_CMAdv", "M:N_CMN1", 
              "M:N_CMN2", "M:N_CMN3", "M:N_CMN4", "M:N_CMP", "M:N_CMP2", 
              "M:N_CMV1", "M:N_CMV2", "M:N_CMV3", "M:N_COMBINATORY", "M:N_CPA", 
              "M:N_ESAdvP", "M:N_ESCCV", "M:N_ESCM", "M:N_ESMA", "M:N_ESMAdvP", 
              "M:N_ESMI", "M:N_ESMN", "M:N_ESMP", "M:N_ESMV", "M:N_HELP", 
              "M:N_SPECIAL", "M:N_SSCCV", "M:N_SSCM", "M:N_SSMA", "M:N_SSMAdvP",
              "M:N_SSMI", "M:N_SSMN", "M:N_SSMP", "M:N_SSMV", "M:N_STQ", 
              "M:N_V", "M:N_nan", "M:Y_CCV", "M:Y_CIN", "M:Y_CLA", "M:Y_CLAdv", 
              "M:Y_CLN", "M:Y_CLP", "M:Y_CLQ", "M:Y_CLV", "M:Y_CMA1", 
              "M:Y_CMAdv", "M:Y_CMN1", "M:Y_CMN2", "M:Y_CMN4", "M:Y_CMP", 
              "M:Y_CMP2", "M:Y_CMV1", "M:Y_CMV2", "M:Y_CMV3", 
              "M:Y_COMBINATORY", "M:Y_CPA", "M:Y_ESAdvP", "M:Y_ESCCV", 
              "M:Y_ESCM", "M:Y_ESMA", "M:Y_ESMAdvP", "M:Y_ESMI", "M:Y_ESMN", 
              "M:Y_ESMP", "M:Y_ESMV", "M:Y_HELP", "M:Y_SPECIAL", "M:Y_SSCCV", 
              "M:Y_SSCM", "M:Y_SSMA", "M:Y_SSMAdvP", "M:Y_SSMI", "M:Y_SSMN", 
              "M:Y_SSMP", "M:Y_SSMV", "M:Y_STQ"]
              
sentence = 'The County Court in Nottingham heard that Roger Gedge, 30, had his leg amputated following the incident outside a rock festival in Wollaton Park, Nottingham, five years ago.'

tokens = SignTaggingTokenizer.tokenize(SignTaggingTokenizer.decode(SignTaggingTokenizer.encode(sentence)))
inputs = SignTaggingTokenizer.encode(sentence, return_tensors="pt")

outputs = SignTaggingModel(inputs)[0]
predictions = torch.argmax(outputs, dim=2)

print([(token, label_list[prediction]) for token, prediction in zip(tokens, predictions[0].tolist())])   

                      
======================================================================

