# Query Generation
This model is the t5-base model from [docTTTTTquery](https://github.com/castorini/docTTTTTquery).

The T5-base model was trained on the [MS MARCO Passage Dataset](https://github.com/microsoft/MSMARCO-Passage-Ranking), which consists of about 500k real search queries from Bing together with the relevant passage.

The model can be used for query generation to learn semantic search models without requiring annotated training data: [Synthetic Query Generation](https://github.com/UKPLab/sentence-transformers/tree/master/examples/unsupervised_learning/query_generation).


## Usage

```python
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained('model-name')
model = T5ForConditionalGeneration.from_pretrained('model-name')

para = "Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."

input_ids = tokenizer.encode(para, return_tensors='pt')
outputs = model.generate(
	input_ids=input_ids,
	max_length=64,
	do_sample=True,
	top_p=0.95,
	num_return_sequences=3)

print("Paragraph:")
print(para)

print("\nGenerated Queries:")
for i in range(len(outputs)):
	query = tokenizer.decode(outputs[i], skip_special_tokens=True)
	print(f'{i + 1}: {query}')
```