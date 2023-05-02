---
language:
- "th"
tags:
- "thai"
- "question-answering"
- "dependency-parsing"
datasets:
- "universal_dependencies"
license: "apache-2.0"
pipeline_tag: "question-answering"
inference:
  parameters:
    align_to_words: false
widget:
- text: "กว่า"
  context: "หลายหัวดีกว่าหัวเดียว"
- text: "หลาย"
  context: "หลายหัวดีกว่าหัวเดียว"
- text: "หัว"
  context: "หลาย[MASK]ดีกว่าหัวเดียว"
---

# roberta-base-thai-spm-ud-head

## Model Description

This is a DeBERTa(V2) model pretrained on Thai Wikipedia texts for dependency-parsing (head-detection on Universal Dependencies) as question-answering, derived from [roberta-base-thai-spm](https://huggingface.co/KoichiYasuoka/roberta-base-thai-spm). Use [MASK] inside `context` to avoid ambiguity when specifying a multiple-used word as `question`.

## How to Use

```py
from transformers import AutoTokenizer,AutoModelForQuestionAnswering,QuestionAnsweringPipeline
tokenizer=AutoTokenizer.from_pretrained("KoichiYasuoka/roberta-base-thai-spm-ud-head")
model=AutoModelForQuestionAnswering.from_pretrained("KoichiYasuoka/roberta-base-thai-spm-ud-head")
qap=QuestionAnsweringPipeline(tokenizer=tokenizer,model=model,align_to_words=False)
print(qap(question="กว่า",context="หลายหัวดีกว่าหัวเดียว"))
```

or (with [ufal.chu-liu-edmonds](https://pypi.org/project/ufal.chu-liu-edmonds/))

```py
class TransformersUD(object):
  def __init__(self,bert):
    import os
    from transformers import (AutoTokenizer,AutoModelForQuestionAnswering,
      AutoModelForTokenClassification,AutoConfig,TokenClassificationPipeline)
    self.tokenizer=AutoTokenizer.from_pretrained(bert)
    self.model=AutoModelForQuestionAnswering.from_pretrained(bert)
    x=AutoModelForTokenClassification.from_pretrained
    if os.path.isdir(bert):
      d,t=x(os.path.join(bert,"deprel")),x(os.path.join(bert,"tagger"))
    else:
      from transformers.utils import cached_file
      c=AutoConfig.from_pretrained(cached_file(bert,"deprel/config.json"))
      d=x(cached_file(bert,"deprel/pytorch_model.bin"),config=c)
      s=AutoConfig.from_pretrained(cached_file(bert,"tagger/config.json"))
      t=x(cached_file(bert,"tagger/pytorch_model.bin"),config=s)
    self.deprel=TokenClassificationPipeline(model=d,tokenizer=self.tokenizer,
      aggregation_strategy="simple")
    self.tagger=TokenClassificationPipeline(model=t,tokenizer=self.tokenizer)
  def __call__(self,text):
    import numpy,torch,ufal.chu_liu_edmonds
    w=[(t["start"],t["end"],t["entity_group"]) for t in self.deprel(text)]
    z,n={t["start"]:t["entity"].split("|") for t in self.tagger(text)},len(w)
    r,m=[text[s:e] for s,e,p in w],numpy.full((n+1,n+1),numpy.nan)
    v,c=self.tokenizer(r,add_special_tokens=False)["input_ids"],[]
    for i,t in enumerate(v):
      q=[self.tokenizer.cls_token_id]+t+[self.tokenizer.sep_token_id]
      c.append([q]+v[0:i]+[[self.tokenizer.mask_token_id]]+v[i+1:]+[[q[-1]]])
    b=[[len(sum(x[0:j+1],[])) for j in range(len(x))] for x in c]
    with torch.no_grad():
      d=self.model(input_ids=torch.tensor([sum(x,[]) for x in c]),
        token_type_ids=torch.tensor([[0]*x[0]+[1]*(x[-1]-x[0]) for x in b]))
    s,e=d.start_logits.tolist(),d.end_logits.tolist()
    for i in range(n):
      for j in range(n):
        m[i+1,0 if i==j else j+1]=s[i][b[i][j]]+e[i][b[i][j+1]-1]
    h=ufal.chu_liu_edmonds.chu_liu_edmonds(m)[0]
    if [0 for i in h if i==0]!=[0]:
      i=([p for s,e,p in w]+["root"]).index("root")
      j=i+1 if i<n else numpy.nanargmax(m[:,0])
      m[0:j,0]=m[j+1:,0]=numpy.nan
      h=ufal.chu_liu_edmonds.chu_liu_edmonds(m)[0]
    u="# text = "+text.replace("\n"," ")+"\n"
    for i,(s,e,p) in enumerate(w,1):
      p="root" if h[i]==0 else "dep" if p=="root" else p
      u+="\t".join([str(i),r[i-1],"_",z[s][0][2:],"_","|".join(z[s][1:]),
        str(h[i]),p,"_","_" if i<n and e<w[i][0] else "SpaceAfter=No"])+"\n"
    return u+"\n"

nlp=TransformersUD("KoichiYasuoka/roberta-base-thai-spm-ud-head")
print(nlp("หลายหัวดีกว่าหัวเดียว"))
```

