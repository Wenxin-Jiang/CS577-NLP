**Dataset**

ToTTo is an open-domain English Table-to-Text dataset with over 120,000 training examples that proposes a controlled generation task: given a Wikipedia table, a set of highlighted table cells, page title and section title as inputs, it produces a one-sentence description summarising the key details from the inputs. This dataset can be taken from hugging face (https://huggingface.co/datasets/totto). 

**Model**

The pre-trained Text-to-Text "t5-base" model is fine-tuned with the Table-to-Text ToTTo dataset(downstream task) for the complete train dataset split of around 120,761 examples. During the fine-tuning process for this downstream task, BertScore metric was used as an evaluation metric instead of the standard BLEU metric.