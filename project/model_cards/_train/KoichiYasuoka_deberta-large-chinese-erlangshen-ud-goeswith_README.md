---
language:
- "zh"
tags:
- "chinese"
- "token-classification"
- "pos"
- "dependency-parsing"
datasets:
- "universal_dependencies"
license: "apache-2.0"
pipeline_tag: "token-classification"
---

# deberta-large-chinese-erlangshen-ud-goeswith

## Model Description

This is a DeBERTa(V2) model pre-trained on Chinese texts (both simplified and traditional) for POS-tagging and dependency-parsing (using `goeswith` for subwords), derived from [deberta-large-chinese-erlangshen-upos](https://huggingface.co/KoichiYasuoka/deberta-large-chinese-erlangshen-upos).

## How to Use

```py
class UDgoeswith(object):
  def __init__(self,bert):
    from transformers import AutoTokenizer,AutoModelForTokenClassification
    self.tokenizer=AutoTokenizer.from_pretrained(bert)
    self.model=AutoModelForTokenClassification.from_pretrained(bert)
  def __call__(self,text):
    import numpy,torch,ufal.chu_liu_edmonds
    w=self.tokenizer(text,return_offsets_mapping=True)
    v=w["input_ids"]
    x=[v[0:i]+[self.tokenizer.mask_token_id]+v[i+1:]+[j] for i,j in enumerate(v[1:-1],1)]
    with torch.no_grad():
      e=self.model(input_ids=torch.tensor(x)).logits.numpy()[:,1:-2,:]
    r=[1 if i==0 else -1 if j.endswith("|root") else 0 for i,j in sorted(self.model.config.id2label.items())]
    e+=numpy.where(numpy.add.outer(numpy.identity(e.shape[0]),r)==0,0,numpy.nan)
    g=self.model.config.label2id["X|_|goeswith"]
    r=numpy.tri(e.shape[0])
    for i in range(e.shape[0]):
      for j in range(i+2,e.shape[1]):
        r[i,j]=r[i,j-1] if numpy.nanargmax(e[i,j-1])==g else 1
    e[:,:,g]+=numpy.where(r==0,0,numpy.nan)
    m=numpy.full((e.shape[0]+1,e.shape[1]+1),numpy.nan)
    m[1:,1:]=numpy.nanmax(e,axis=2).transpose()
    p=numpy.zeros(m.shape)
    p[1:,1:]=numpy.nanargmax(e,axis=2).transpose()
    for i in range(1,m.shape[0]):
      m[i,0],m[i,i],p[i,0]=m[i,i],numpy.nan,p[i,i]
    h=ufal.chu_liu_edmonds.chu_liu_edmonds(m)[0]
    if [0 for i in h if i==0]!=[0]:
      m[:,0]+=numpy.where(m[:,0]==numpy.nanmax(m[[i for i,j in enumerate(h) if j==0],0]),0,numpy.nan)
      m[[i for i,j in enumerate(h) if j==0]]+=[0 if i==0 or j==0 else numpy.nan for i,j in enumerate(h)]
      h=ufal.chu_liu_edmonds.chu_liu_edmonds(m)[0]
    u="# text = "+text+"\n"
    v=[(s,e) for s,e in w["offset_mapping"] if s<e]
    for i,(s,e) in enumerate(v,1):
      q=self.model.config.id2label[p[i,h[i]]].split("|")
      u+="\t".join([str(i),text[s:e],"_",q[0],"_","|".join(q[1:-1]),str(h[i]),q[-1],"_","_" if i<len(v) and e<v[i][0] else "SpaceAfter=No"])+"\n"
    return u+"\n"

nlp=UDgoeswith("KoichiYasuoka/deberta-large-chinese-erlangshen-ud-goeswith")
print(nlp("我把这本书看完了"))
```

with [ufal.chu-liu-edmonds](https://pypi.org/project/ufal.chu-liu-edmonds/).
Or without ufal.chu-liu-edmonds:

```
from transformers import pipeline
nlp=pipeline("universal-dependencies","KoichiYasuoka/deberta-large-chinese-erlangshen-ud-goeswith",trust_remote_code=True,aggregation_strategy="simple")
print(nlp("我把这本书看完了"))
```

