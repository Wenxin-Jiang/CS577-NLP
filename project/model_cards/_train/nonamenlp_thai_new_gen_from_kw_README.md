# Generate News in Thai language by keywords.

MODEL_NAME = 'nonamenlp/news_gen' 

TOKENIZER_NAME = "nonamenlp/news_gen"

trained_model = MT5ForConditionalGeneration.from_pretrained(MODEL_NAME, return_dict=True)

tokenizer = T5Tokenizer.from_pretrained(TOKENIZER_NAME)