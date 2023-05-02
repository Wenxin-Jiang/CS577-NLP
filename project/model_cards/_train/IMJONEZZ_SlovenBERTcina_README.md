#Slovak RoBERTA Masked Language Model

###83Mil Parameters in small model

Medium and Large models coming soon!

RoBERTA pretrained tokenizer vocab and merges included.

---

##Training params:
- **Dataset**:
  8GB Slovak Monolingual dataset including ParaCrawl (monolingual), OSCAR, and several gigs of my own findings and cleaning.
- **Preprocessing**:
  Tokenized with a pretrained ByteLevelBPETokenizer trained on the same dataset. Uncased, with s, pad, /s, unk, and mask special tokens.
- **Evaluation results**:
  - Mnoho ľudí tu<mask>
    * žije.
    * žijú.
    * je.
    * trpí.
  - Ako sa<mask>
    * máte
    * máš
    * má
    * hovorí
  - Plážová sezóna pod Zoborom patrí medzi<mask> obdobia.
    * ročné
    * najkrajšie
    * najobľúbenejšie
    * najnáročnejšie
    
- **Limitations**:
  The current model is fairly small, although it works very well. This model is meant to be finetuned on downstream tasks e.g. Part-of-Speech tagging, Question Answering, anything in GLUE or SUPERGLUE.
  
- **Credit**:
  If you use this or any of my models in research or professional work, please credit me - Christopher Brousseau in said work.