# bert-base for KLUE Relation Extraction task.
Fine-tuned klue/bert-base using KLUE RE dataset.
- <a href="https://klue-benchmark.com/">KLUE Benchmark Official Webpage</a>
- <a href="https://github.com/KLUE-benchmark/KLUE">KLUE Official Github</a> 
- <a href="https://github.com/ainize-team/klue-re-workspace">KLUE RE Github</a>
- Run KLUE RE on free GPU : <a href="https://ainize.ai/workspace/create?imageId=hnj95592adzr02xPTqss&git=https://github.com/ainize-team/klue-re-workspace">Ainize Workspace</a>

<br>

# Usage
<pre><code>
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("ainize/klue-bert-base-re")
model = AutoModelForSequenceClassification.from_pretrained("ainize/klue-bert-base-re")

# Add "&ltsubj&gt", "&lt/subj&gt" to both ends of the subject object and "&ltobj&gt", "&lt/obj&gt" to both ends of the object object.
sentence = "&ltsubj&gt손흥민&lt/subj&gt은 &ltobj&gt대한민국&lt/obj&gt에서 태어났다."

encodings = tokenizer(sentence, 
                      max_length=128, 
                      truncation=True, 
                      padding="max_length", 
                      return_tensors="pt")

outputs = model(**encodings)

logits = outputs['logits']

preds = torch.argmax(logits, dim=1)
</code></pre>

<br>

# About us
- <a href="https://ainize.ai/teachable-nlp">Teachable NLP</a> - Train NLP models with your own text without writing any code
- <a href="https://ainize.ai/">Ainize</a> - Deploy ML project using free gpu