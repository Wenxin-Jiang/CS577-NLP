<h1>Model description</h1>

This is a fine-tuned BioBERT model for extracting primary and secondary outcomes from articles reporting clinical trials.

This model is a version of https://huggingface.co/aakorolyova/primary_outcome_extraction. We have not annotated any secondary outcome during the related PhD project. To be able to extract secondary outcomes, we manually annotated secondary outcomes in the existing annotated sentences with primary outcomes (only a small percentage of sentences contains secondary outcomes) and performed automatic data augmentation by replacing "primary"/"main"/"principal" by "secondary" and changing tags from B/I-Prim to B/I-Sec in the primary outcomes data.

Model creator: Anna Koroleva


<h1>Intended uses & limitations</h1>

The model is intended to be used for extracting primary and secondary outcomes from texts of clinical trials.

The main limitation is that the model was trained on a mix of manually annotated and automatically augmented data, which might lead to inaccuracies in prediction.


<h1>How to use</h1>

The model should be used with the BioBERT tokeniser. A sample code for getting model predictions is below:
```
  import numpy as np
  from transformers import AutoTokenizer
  from transformers import AutoModelForTokenClassification
  tokenizer = AutoTokenizer.from_pretrained('dmis-lab/biobert-v1.1')
  model = AutoModelForTokenClassification.from_pretrained(r'aakorolyova/primary_and_secondary_outcome_extraction')
  text = 'Primary endpoint was overall survival in patients with oesophageal squamous cell carcinoma and PD-L1 combined positive score (CPS) of 10 or more, secondary endpoints were overall survival and progression-free survival in patients with oesophageal squamous cell carcinoma, PD-L1 CPS of 10 or more, and in all randomised patients.'
  encoded_input = tokenizer(text, padding=True, truncation=True, max_length=2000, return_tensors='pt')
  output = model(**encoded_input)['logits']
  output = np.argmax(output.detach().numpy(), axis=2)
  print(output)
```

Some more useful functions can be found in or Github repository: https://github.com/aakorolyova/DeSpin-2.0


<h1>Training data</h1>

Training data can be found in https://github.com/aakorolyova/DeSpin-2.0/tree/main/data/Primary_Secondary_Outcomes

<h1>Training procedure</h1>
The model was fine-tuned using Huggingface Trainer API. Training scripts can be found in https://github.com/aakorolyova/DeSpin-2.0

<h1>Evaluation</h1>
Primary outcomes: 

Precision: 92.22

Recall: 94.86

F1: 93.52

Secondary outcomes: 

Precision: 91.43

Recall: 91.87

F1: 91.65 

Overall precision: 91.79

Overall recall: 93.23

Overall F1: 92.51
