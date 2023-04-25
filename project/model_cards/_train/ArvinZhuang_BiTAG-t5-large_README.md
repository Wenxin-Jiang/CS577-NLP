---
inference:
  parameters:
    do_sample: True
    max_length: 500
    top_p: 0.9
    top_k: 20
    temperature: 1
    num_return_sequences: 10
    
widget:
- text: "abstract: We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers. Unlike recent language representation models, BERT is designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT model can be fine-tuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial task-specific architecture modifications. BERT is conceptually simple and empirically powerful. It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% (4.6% absolute improvement), SQuAD v1.1 question answering Test F1 to 93.2 (1.5 point absolute improvement) and SQuAD v2.0 Test F1 to 83.1 (5.1 point absolute improvement)."
  example_title: "BERT abstract"
---

```
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model = AutoModelForSeq2SeqLM.from_pretrained("ArvinZhuang/BiTAG-t5-large")
tokenizer = AutoTokenizer.from_pretrained("ArvinZhuang/BiTAG-t5-large")

text = "abstract: [your abstract]"  # use 'title:' as the prefix for title_to_abs task.
input_ids = tokenizer.encode(text, return_tensors='pt')

outputs = model.generate(
    input_ids,
    do_sample=True,
    max_length=500,
    top_p=0.9,
    top_k=20,
    temperature=1,
    num_return_sequences=10,
)

print("Output:\n" + 100 * '-')
for i, output in enumerate(outputs):
    print("{}: {}".format(i+1, tokenizer.decode(output, skip_special_tokens=True)))

```
GitHub: https://github.com/ArvinZhuang/BiTAG