from transformers import MT5ForConditionalGeneration, AutoTokenizer
model = MT5ForConditionalGeneration.from_pretrained("Parth/mT5-question-generator")
tokenizer = AutoTokenizer.from_pretrained("google/mt5-base")
