<h1>Model description</h1>

This is a fine-tuned BioBERT model for text pair classification, namely for identifying pairs of clinical trial outcomes' mentions that refeer to the same outcome (e.g. "overall survival in patients with oesophageal squamous cell carcinoma and PD-L1 combined positive score (CPS) of 10 or more" and "overall survival" can be considered to refer to the same outcome, while "overall survival" and "progression-free survival" refer to different outcomes).
This is the second version of the model; the original model development was reported in:

Anna Koroleva, Patrick Paroubek. Measuring semantic similarity of clinical trial outcomes using deep pre-trained language representations. Journal of Biomedical Informatics – X, 2019  https://www.sciencedirect.com/science/article/pii/S2590177X19300575

The original work was conducted within the scope of the Assisted authoring for avoiding inadequate claims in scientific reporting PhD project of the Methods for Research on Research (MiRoR, http://miror-ejd.eu/) program.

Model creator: Anna Koroleva


<h1>Intended uses & limitations</h1>

The model was originally intended to be used as a part of spin (unjustified presentation of trial results) detection pipeline in articles reporting Randomised controlled trials (see Anna Koroleva, Sanjay Kamath, Patrick MM Bossuyt, Patrick Paroubek. DeSpin: a prototype system for detecting spin in biomedical publications. Proceedings of the 19th SIGBioMed Workshop on Biomedical Language Processing. https://aclanthology.org/2020.bionlp-1.5/). It can be used for any task requiring identification of pairs of outcome mentions referring to the same outcome.

The main limitation is that the model was trained on a fairly small sample of data annotated by a single annotator. Annotating more data or involvig more annotators was not possiblw within the PhD project.


<h1>How to use</h1>

The model should be used with the BioBERT tokeniser. A sample code for getting model predictions is below:
```
	from transformers import AutoTokenizer
	from transformers import AutoModelForTokenClassification
	from transformers import AutoModelForSequenceClassification

    tokenizer = AutoTokenizer.from_pretrained('dmis-lab/biobert-v1.1')
    model = AutoModelForSequenceClassification.from_pretrained(r'aakorolyova/outcome_similarity')

	out1 = 'overall survival'
	out2 = 'overall survival in patients with oesophageal squamous cell carcinoma and PD-L1 combined positive score (CPS) of 10 or more'

    tokenized_input = tokenizer(out1, out2, padding="max_length", truncation=True, return_tensors='pt')
    output = model_similarity(**tokenized_input)['logits']
    output = np.argmax(output.detach().numpy(), axis=1)
    print(output)

```

Some more useful functions can be found in or Github repository: https://github.com/aakorolyova/DeSpin-2.0


<h1>Training data</h1>

Training data can be found in https://github.com/aakorolyova/DeSpin-2.0/tree/main/data/Outcome_similarity

<h1>Training procedure</h1>
The model was fine-tuned using Huggingface Trainer API. Training scripts can be found in https://github.com/aakorolyova/DeSpin-2.0

<h1>Evaluation</h1>
Precision: 86.67%

Recall: 92.86%

F1: 89.66%
