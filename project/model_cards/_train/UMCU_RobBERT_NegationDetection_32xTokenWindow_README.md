---
language: nl
license: mit
---

# MedRoBERTa.nl finetuned for negation

## Description
This model is a finetuned RoBERTa-based model called RobBERT, this model is pre-trained on the Dutch section of OSCAR. All code used for the creation of RobBERT can be found here https://github.com/iPieter/RobBERT. The publication associated with the negation detection task can be found at https://arxiv.org/abs/2209.00470. The code for finetuning the model can be found at https://github.com/umcu/negation-detection.

## Intended use
The model is finetuned for negation detection on Dutch clinical text. Since it is a domain-specific model trained on medical data, it is meant to be used on medical NLP tasks for Dutch. This particular model is trained on a 32-max token windows surrounding the concept-to-be negated. Note that we also trained a biLSTM which can be incorporated in [MedCAT](https://github.com/CogStack/MedCAT).

## Minimal example

```python
tokenizer = AutoTokenizer\
             .from_pretrained("UMCU/MedRoBERTa.nl_NegationDetection")
model = AutoModelForTokenClassification\
            .from_pretrained("UMCU/MedRoBERTa.nl_NegationDetection")

some_text = "De patient was niet aanspreekbaar en hij zag er grauw uit. \
Hij heeft de inspanningstest echter goed doorstaan." 
inputs = tokenizer(some_text, return_tensors='pt')
output = model.forward(inputs)
probas = torch.nn.functional.softmax(output.logits[0]).detach().numpy()

#  koppel aan tokens
input_tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
target_map = {0: 'B-Negated', 1:'B-NotNegated',2:'I-Negated',3:'I-NotNegated'}
results = [{'token': input_tokens[idx],
                 'proba_negated': proba_arr[0]+proba_arr[2],
                 'proba_not_negated': proba_arr[1]+proba_arr[3]
                 }  
                 for idx,proba_arr in enumerate(probas)]

```

It is perhaps good to note that we assume the [Inside-Outside-Beginning](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) format.


## Data
The pre-trained model was trained the Dutch section of OSCAR (about 39GB), and is described here: http://dx.doi.org/10.18653/v1/2020.findings-emnlp.292.

## Authors

RobBERT: Pieter Delobelle, Thomas Winters, Bettina Berendt,
Finetuning: Bram van Es, Sebastiaan Arends.

## Contact

If you are having problems with this model please add an issue on our git: https://github.com/umcu/negation-detection/issues

## Usage

If you use the model in your work please refer either to 
https://doi.org/10.5281/zenodo.6980076 or https://doi.org/10.48550/arXiv.2209.00470

## References
Paper: Pieter Delobelle, Thomas Winters, Bettina Berendt (2020), RobBERT: a Dutch RoBERTa-based Language Model, Findings of the Association for Computational Linguistics: EMNLP 2020

Paper: Bram van Es, Leon C. Reteig, Sander C. Tan, Marijn Schraagen, Myrthe M. Hemker, Sebastiaan R.S. Arends, Miguel A.R. Rios, Saskia Haitjema (2022): Negation detection in Dutch clinical texts: an evaluation of rule-based and machine learning methods, Arxiv
