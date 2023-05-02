---
datasets: 
  - ZeyadAhmed/Arabic-SQuADv2.0
language: 
  - ar
metrics: 
  - 
    name: exact_match
    type: exact_match
    value: 65.12
  - 
    name: F1
    type: f1
    value: 71.49

---

# AraElectra for Question Answering on Arabic-SQuADv2

This is the [AraElectra](https://huggingface.co/aubmindlab/araelectra-base-discriminator) model, fine-tuned using the [Arabic-SQuADv2.0](https://huggingface.co/datasets/ZeyadAhmed/Arabic-SQuADv2.0) dataset. It's been trained on question-answer pairs, including unanswerable questions, for the task of Question Answering. with help of [AraElectra Classifier](https://huggingface.co/ZeyadAhmed/AraElectra-Arabic-SQuADv2-CLS) to predicted unanswerable question.

 ## Overview
**Language model:** AraElectra <br>
**Language:** Arabic <br>
**Downstream-task:** Extractive QA  
**Training data:** Arabic-SQuADv2.0  
**Eval data:** Arabic-SQuADv2.0 <br>
**Test data:** Arabic-SQuADv2.0 <br>
**Code:** [See More Info on Github](https://github.com/zeyadahmed10/Arabic-MRC)  
**Infrastructure**: 1x Tesla K80 

## Hyperparameters

```
batch_size = 8
n_epochs = 4
base_LM_model = "AraElectra"
learning_rate = 3e-5
optimizer = AdamW
padding = dynamic
``` 

## Online Demo on Arabic Wikipedia and User Provided Contexts
See model in action hosted on streamlit [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/wissamantoun/arabic-wikipedia-qa-streamlit/main)

## Usage
For best results use the AraBert [preprocessor](https://github.com/aub-mind/arabert/blob/master/preprocess.py) by aub-mind
```python
from transformers import ElectraForQuestionAnswering, ElectraForSequenceClassification, AutoTokenizer, pipeline
from preprocess import ArabertPreprocessor
prep_object = ArabertPreprocessor("araelectra-base-discriminator")
question = prep_object('ما هي جامعة الدول العربية ؟')
context = prep_object('''
جامعة الدول العربية هيمنظمة إقليمية تضم دولاً عربية في آسيا وأفريقيا.
ينص ميثاقها على التنسيق بين الدول الأعضاء في الشؤون الاقتصادية، ومن ضمنها العلاقات التجارية الاتصالات، العلاقات الثقافية، الجنسيات ووثائق وأذونات السفر والعلاقات الاجتماعية والصحة. المقر الدائم لجامعة الدول العربية يقع في القاهرة، عاصمة مصر (تونس من 1979 إلى 1990). 
''')
# a) Get predictions
qa_modelname = 'ZeyadAhmed/AraElectra-Arabic-SQuADv2-QA'
cls_modelname = 'ZeyadAhmed/AraElectra-Arabic-SQuADv2-CLS'
qa_pipe = pipeline('question-answering', model=qa_modelname, tokenizer=qa_modelname)
QA_input = {
    'question': question,
    'context': context
}
CLS_input = {
    'text': question,
    'text_pair': context
}
qa_res = qa_pipe(QA_input)
cls_res = cls_pipe(CLS_iput)
threshold = 0.5 #hyperparameter can be tweaked
## note classification results label0 probability it can be answered label1 probability can't be answered 
## if label1 probability > threshold then consider the output of qa_res is empty string else take the qa_res
# b) Load model & tokenizer
qa_model = ElectraForQuestionAnswering.from_pretrained(qa_modelname)
cls_model = ElectraForSequenceClassification.from_pretrained(cls_modelname)
tokenizer = AutoTokenizer.from_pretrained(qa_modelname)
```

## Performance
Evaluated on the Arabic-SQuAD 2.0 test set with the [official eval script](https://worksheets.codalab.org/rest/bundles/0x6b567e1cf2e041ec80d7098f031c5c9e/contents/blob/) except changing in the preprocessing a little to fit the arabic language [the modified eval script](https://github.com/zeyadahmed10/Arabic-MRC/blob/main/evaluatev2.py).

```
"exact": 65.11555277951281,
"f1": 71.49042547237256,,

"total": 9606,
"HasAns_exact": 56.14535768645358,
"HasAns_f1": 67.79623803036668,
"HasAns_total": 5256,
"NoAns_exact": 75.95402298850574,
"NoAns_f1": 75.95402298850574,
"NoAns_total": 4350
```
