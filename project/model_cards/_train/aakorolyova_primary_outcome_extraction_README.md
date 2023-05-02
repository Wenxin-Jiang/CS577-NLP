<h1>Model description</h1>

This is a fine-tuned BioBERT model for extracting primary outcomes from articles reporting clinical trials.
This is the second version of the model; the original model development was reported in:

Anna Koroleva, Sanjay Kamath, Patrick Paroubek. Extracting primary and reported outcomes from articles reporting randomized controlled trials using pre-trained deep language representations. Preprint: https://easychair.org/publications/preprint/qpml

The original work was conducted within the scope of the Assisted authoring for avoiding inadequate claims in scientific reporting PhD project of the Methods for Research on Research (MiRoR, http://miror-ejd.eu/) program.

Model creator: Anna Koroleva


<h1>Intended uses & limitations</h1>

The model is intended to be used for extracting primary outcomes from texts of clinical trials.

The main limitation is that the model was trained on a fairly small (2000 sentences) sample of data annotated by a single annotator. Annotating more data or involvig more annotators was not possiblw within the PhD project.

Another possible issue with the model use if the complex nature of outcomes: a typical description of an outcome can include the outcome name, measurement tool, timepoints, e.g. "Health-Related Quality of Life at 12 months, measured using the Assessment of Quality of Life instrument". Ideally, this should be broken into 3 separate entities ("Health-Related Quality of Life" - outcome", "at 12 months" - timepoint", "the Assessment of Quality of Life instrument" - measurement tool), and relation between the three should be extracted to capture all the outcome-related information. However, in our annotation we annotated this type of examples as a sinale outcome entity.


<h1>How to use</h1>

The model should be used with the BioBERT tokeniser. A sample code for getting model predictions is below:
```

  import numpy as np

  from transformers import AutoTokenizer

  from transformers import AutoModelForTokenClassification


  tokenizer = AutoTokenizer.from_pretrained('dmis-lab/biobert-v1.1')

  model = AutoModelForTokenClassification.from_pretrained(r'aakorolyova/primary_outcome_extraction')


  text = 'Primary endpoints were overall survival in patients with oesophageal squamous cell carcinoma and PD-L1 combined positive score (CPS) of 10 or more, and overall survival and progression-free survival in patients with oesophageal squamous cell carcinoma, PD-L1 CPS of 10 or more, and in all randomised patients.'

  encoded_input = tokenizer(text, padding=True, truncation=True, max_length=2000, return_tensors='pt')

  output = model(**encoded_input)['logits']

  output = np.argmax(output.detach().numpy(), axis=2)

  print(output)
```

Some more useful functions can be found in or Github repository: https://github.com/aakorolyova/DeSpin-2.0


<h1>Training data</h1>

Training data can be found in https://github.com/aakorolyova/DeSpin-2.0/tree/main/data/Primary_Outcomes

<h1>Training procedure</h1>

The model was fine-tuned using Huggingface Trainer API. Training scripts can be found in https://github.com/aakorolyova/DeSpin-2.0

<h1>Evaluation</h1>

Precision: 74.41%

Recall: 88.7%

F1: 80.93%
