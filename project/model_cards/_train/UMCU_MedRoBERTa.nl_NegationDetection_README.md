---
language: nl
license: mit
---

# MedRoBERTa.nl finetuned for negation

## Description
This model is a finetuned RoBERTa-based model pre-trained from scratch on Dutch hospital notes sourced from Electronic Health Records. All code used for the creation of MedRoBERTa.nl can be found at https://github.com/cltl-students/verkijk_stella_rma_thesis_dutch_medical_language_model. The publication associated with the negation detection task can be found at https://arxiv.org/abs/2209.00470. The code for finetuning the model can be found at https://github.com/umcu/negation-detection.


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

## Intended use
The model is finetuned for negation detection on Dutch clinical text. Since it is a domain-specific model trained on medical data, it is meant to be used on medical NLP tasks for Dutch. This particular model is trained on a 512-max token windows surrounding the concept-to-be negated. Note that we also trained a biLSTM which can be incorporated in [MedCAT](https://github.com/CogStack/MedCAT).

## Data
The pre-trained model was trained on nearly 10 million hospital notes from the Amsterdam University Medical Centres. The training data was anonymized before starting the pre-training procedure. 

The finetuning was performed on the Erasmus Dutch Clinical Corpus (EDCC), and can be obtained through Jan Kors (j.kors@erasmusmc.nl). The EDCC is described here: https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-014-0373-3

## Authors

MedRoBERTa.nl: Stella Verkijk, Piek Vossen,
Finetuning: Bram van Es, Sebastiaan Arends.

## Contact

If you are having problems with this model please add an issue on our git: https://github.com/umcu/negation-detection/issues

## Usage

If you use the model in your work please refer either to 
https://doi.org/10.5281/zenodo.6980076 or https://doi.org/10.48550/arXiv.2209.00470

## References
Paper: Verkijk, S. & Vossen, P. (2022) MedRoBERTa.nl: A Language Model for Dutch Electronic Health Records. Computational Linguistics in the Netherlands Journal, 11.

Paper: Bram van Es, Leon C. Reteig, Sander C. Tan, Marijn Schraagen, Myrthe M. Hemker, Sebastiaan R.S. Arends, Miguel A.R. Rios, Saskia Haitjema (2022): Negation detection in Dutch clinical texts: an evaluation of rule-based and machine learning methods, Arxiv
