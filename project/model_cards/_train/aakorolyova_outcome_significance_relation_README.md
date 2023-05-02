<h1>Model description</h1>

This is a fine-tuned BioBERT model for extracting the relation between clinical trial outcome and its significance level. The task is framed as sentence classification:

- you first need to extract the entities - outcomes and significance levels. For outcomes, you could use the model https://huggingface.co/aakorolyova/reported_outcome_extraction. For significance levels, we have previously used a rule-based approach that worked well; we plan to make the code available in https://github.com/aakorolyova/DeSpin-2.0 soon.

- then, for each pair of outcome and significance level, you mask the entity texts as @OUTCOME$ and @SIGNIFICANCE$

- you run the prediction on the sentence with the masked outcome-significance level pair to get the label (0 if the entities are unrelated, 1 if they are related).

For example, the sentence "Intubation conditions (succinylcholine 8.3 ± 0.8; rocuronium 8.2 ± 0.9; P = 0.7) and failed first intubation attempts (succinylcholine 32/200; rocuronium 36/201; P = 1.0) did not differ between the groups." contains several outcomes ("Intubation conditions", "failed first intubation attempts") and significance levels ("P = 0.7", "P = 1.0"). Masked sentence for each pair and the expected label are as follows:

```
@OUTCOME$ (succinylcholine 8.3 ± 0.8; rocuronium 8.2 ± 0.9; @SIGNIFICANCE$) and failed first intubation attempts (succinylcholine 32/200; rocuronium 36/201; P = 1.0) did not differ between the groups.	1

@OUTCOME$ (succinylcholine 8.3 ± 0.8; rocuronium 8.2 ± 0.9; P = 0.7) and failed first intubation attempts (succinylcholine 32/200; rocuronium 36/201; @SIGNIFICANCE$) did not differ between the groups.        0

Intubation conditions (succinylcholine 8.3 ± 0.8; rocuronium 8.2 ± 0.9; P = 0.7) and @OUTCOME$ (succinylcholine 32/200; rocuronium 36/201; @SIGNIFICANCE$) did not differ between the groups.	1

Intubation conditions (succinylcholine 8.3 ± 0.8; rocuronium 8.2 ± 0.9; @SIGNIFICANCE$) and @OUTCOME$ (succinylcholine 32/200; rocuronium 36/201; P = 1.0) did not differ between the groups.	0
```

This is the second version of the model; the original model development was reported in:

Anna Koroleva, Patrick Paroubek. Extracting relations between outcome and significance level in Randomized Controlled Trials (RCTs) publications. Proceedings of ACL BioNLP workshop, 2019  https://aclanthology.org/W19-5038/

The original work was conducted within the scope of the Assisted authoring for avoiding inadequate claims in scientific reporting PhD project of the Methods for Research on Research (MiRoR, http://miror-ejd.eu/) program.

Model creator: Anna Koroleva


<h1>Intended uses & limitations</h1>

The model was originally intended to be used as a part of spin (unjustified presentation of trial results) detection pipeline in articles reporting Randomised controlled trials (see Anna Koroleva, Sanjay Kamath, Patrick MM Bossuyt, Patrick Paroubek. DeSpin: a prototype system for detecting spin in biomedical publications. Proceedings of the 19th SIGBioMed Workshop on Biomedical Language Processing. https://aclanthology.org/2020.bionlp-1.5/). It can also be used separately, for predicting outcome - significance level relation.

The main limitation is that the model was trained on a fairly small sample of data annotated by a single annotator. Annotating more data or involvig more annotators was not possible within the PhD project.


<h1>How to use</h1>

The model should be used with the BioBERT tokeniser. A sample code for getting model predictions is below:
```
	import numpy as np
	from transformers import AutoModelForTokenClassification
	from transformers import AutoModelForSequenceClassification

	tokenizer = AutoTokenizer.from_pretrained('dmis-lab/biobert-v1.1')
	model = AutoModelForSequenceClassification.from_pretrained("aakorolyova/outcome_significance_relation")
	
	text1 = "@OUTCOME$ (succinylcholine 8.3 ± 0.8; rocuronium 8.2 ± 0.9; @SIGNIFICANCE$) and failed first intubation attempts (succinylcholine 32/200; rocuronium 36/201; P = 1.0) did not differ between the groups."
	text2 = "@OUTCOME$ (succinylcholine 8.3 ± 0.8; rocuronium 8.2 ± 0.9; P = 0.7) and failed first intubation attempts (succinylcholine 32/200; rocuronium 36/201; @SIGNIFICANCE$) did not differ between the groups."
	
	tokenized_input1 = tokenizer(text1, padding="max_length", truncation=True, return_tensors='pt')
	output1 = model(**tokenized_input1)['logits']
	output1 = np.argmax(output1.detach().numpy(), axis=1)
	print(output1)

	tokenized_input2 = tokenizer(text2, padding="max_length", truncation=True, return_tensors='pt')
	output2 = model(**tokenized_input2)['logits']
	output2 = np.argmax(output2.detach().numpy(), axis=1)
	print(output2)
```

Some more useful functions can be found in or Github repository: https://github.com/aakorolyova/DeSpin-2.0


<h1>Training data</h1>

Training data can be found in https://github.com/aakorolyova/DeSpin-2.0/tree/main/data/Outcome_significance_relation

<h1>Training procedure</h1>
The model was fine-tuned using Huggingface Trainer API. Training scripts can be found in https://github.com/aakorolyova/DeSpin-2.0

<h1>Evaluation</h1>

Precision: 94.96%

Recall: 96.35%

F1: 95.65%
