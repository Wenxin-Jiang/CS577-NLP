---
license: apache-2.0
---
<h2>Re-Punctuate:</h2>

Re-Punctuate is a T5 model that attempts to correct Capitalization and Punctuations in the sentences.

<h3>DataSet:</h3>

DialogSum dataset (115056 Records) was used to fine-tune the model for Punctuation and Capitalization correction.

<h3>Usage:</h3>

<pre>

from transformers import T5Tokenizer, TFT5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained('SJ-Ray/Re-Punctuate')
model = TFT5ForConditionalGeneration.from_pretrained('SJ-Ray/Re-Punctuate')

input_text = 'the story of this brave brilliant athlete whose very being was questioned so publicly is one that still captures the imagination'
inputs = tokenizer.encode("punctuate: " + input_text, return_tensors="tf") 
result = model.generate(inputs)

decoded_output = tokenizer.decode(result[0], skip_special_tokens=True)
print(decoded_output)

</pre>
<h4> Example: </h4>
<b>Input:</b>  the story of this brave brilliant athlete whose very being was questioned so publicly is one that still captures the imagination <br>
<b>Output:</b> The story of this brave, brilliant athlete, whose very being was questioned so publicly, is one that still captures the imagination.

<h4> Connect on: <a href="https://www.linkedin.com/in/suraj-kumar-710382a7" target="_blank">LinkedIn : Suraj Kumar</a></h4>