---
language:
- "vi"
tags:
- "vietnamese"
- "token-classification"
- "pos"
- "dependency-parsing"
datasets:
- "universal_dependencies"
license: "cc-by-sa-4.0"
pipeline_tag: "token-classification"
widget:
- text: "Hai cái đầu thì tốt hơn một"
---

# phobert-large-vietnamese-ud-goeswith

## Model Description

This is a PhoBERT model pre-trained on Vietnamese texts for POS-tagging and dependency-parsing (using `goeswith` for subwords), derived from [phobert-large](https://huggingface.co/vinai/phobert-large).

## How to Use

```py
class UDgoeswithViNLP(object):
  def __init__(self,bert):
    from transformers import AutoTokenizer,AutoModelForTokenClassification
    from ViNLP import word_tokenize
    self.tokenizer=AutoTokenizer.from_pretrained(bert)
    self.model=AutoModelForTokenClassification.from_pretrained(bert)
    self.vinlp=word_tokenize
  def __call__(self,text):
    import numpy,torch,ufal.chu_liu_edmonds
    t=self.vinlp(text)
    w=self.tokenizer(t,add_special_tokens=False)["input_ids"]
    z=[]
    for i,j in enumerate(t):
      if j.find("_")>0 and [k for k in w[i] if k==self.tokenizer.unk_token_id]!=[]:
          w[i]=self.tokenizer(j.replace("_"," "))["input_ids"][1:-1]
      if [k for k in w[i] if k==self.tokenizer.unk_token_id]!=[]:
        w[i]=[self.tokenizer.unk_token_id]
        z.append(j)
    v=[self.tokenizer.cls_token_id]+sum(w,[])+[self.tokenizer.sep_token_id]
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
    q=[self.model.config.id2label[p[i,j]].split("|") for i,j in enumerate(h)]
    t=[i.replace("_"," ") for i in t]
    if len(t)!=len(v)-2:
      t=[z.pop(0) if i==self.tokenizer.unk_token else i.replace("_"," ") for i in self.tokenizer.convert_ids_to_tokens(v[1:-1])]
      for i,j in reversed(list(enumerate(q[2:],2))):
        if j[-1]=="goeswith" and set([k[-1] for k in q[h[i]+1:i+1]])=={"goeswith"}:
          h=[b if i>b else b-1 for a,b in enumerate(h) if i!=a]
          t[i-2]=(t[i-2][0:-2] if t[i-2].endswith("@@") else t[i-2]+" ")+t.pop(i-1)
          q.pop(i)
      t=[i[0:-2].strip() if i.endswith("@@") else i.strip() for i in t]
    for i,j in enumerate(t,1):
      u+="\t".join([str(i),j,"_",q[i][0],"_","|".join(q[i][1:-1]),str(h[i]),q[i][-1],"_","_"])+"\n"
    return u+"\n"

nlp=UDgoeswithViNLP("KoichiYasuoka/phobert-large-vietnamese-ud-goeswith")
print(nlp("Hai cái đầu thì tốt hơn một."))
```

with [ufal.chu-liu-edmonds](https://pypi.org/project/ufal.chu-liu-edmonds/) and [ViNLP](https://pypi.org/project/ViNLP/).
Or without them:

```
from transformers import pipeline
nlp=pipeline("universal-dependencies","KoichiYasuoka/phobert-large-vietnamese-ud-goeswith",trust_remote_code=True,aggregation_strategy="simple")
print(nlp("Hai cái đầu thì tốt hơn một."))
```

