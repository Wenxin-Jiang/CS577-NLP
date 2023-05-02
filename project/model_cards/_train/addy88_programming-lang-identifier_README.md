This model is funetune version of Codebert in roberta. On CodeSearchNet.
###
Quick start:

from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("addy88/programming-lang-identifier")

model = AutoModelForSequenceClassification.from_pretrained("addy88/programming-lang-identifier")

input_ids = tokenizer.encode(CODE_TO_IDENTIFY)
logits = model(input_ids)[0]

language_idx = logits.argmax() # index for the resulting label
###