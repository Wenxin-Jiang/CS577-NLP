---
language: de
license: mit
datasets:
- wikipedia
- OPUS
- OpenLegalData
- oscar
---

# German BERT large

Released, Oct 2020, this is a German BERT language model trained collaboratively by the makers of the original German BERT (aka "bert-base-german-cased") and the dbmdz BERT (aka bert-base-german-dbmdz-cased). In our [paper](https://arxiv.org/pdf/2010.10906.pdf), we outline the steps taken to train our model and show that it outperforms its predecessors.  

## Overview  
**Paper:** [here](https://arxiv.org/pdf/2010.10906.pdf)  
**Architecture:** BERT large  
**Language:** German  

## Performance  
```
GermEval18 Coarse: 80.08
GermEval18 Fine:   52.48
GermEval14:        88.16
```

See also:  
deepset/gbert-base    
deepset/gbert-large    
deepset/gelectra-base    
deepset/gelectra-large    
deepset/gelectra-base-generator    
deepset/gelectra-large-generator    

## Authors
**Branden Chan:** branden.chan@deepset.ai    
**Stefan Schweter:** stefan@schweter.eu        
**Timo Möller:** timo.moeller@deepset.ai    

## About us
<div class="grid lg:grid-cols-2 gap-x-4 gap-y-3">
    <div class="w-full h-40 object-cover mb-2 rounded-lg flex items-center justify-center">
         <img alt="" src="https://raw.githubusercontent.com/deepset-ai/.github/main/deepset-logo-colored.png" class="w-40"/>
     </div>
     <div class="w-full h-40 object-cover mb-2 rounded-lg flex items-center justify-center">
         <img alt="" src="https://raw.githubusercontent.com/deepset-ai/.github/main/haystack-logo-colored.png" class="w-40"/>
     </div>
</div>

[deepset](http://deepset.ai/) is the company behind the open-source NLP framework [Haystack](https://haystack.deepset.ai/) which is designed to help you build production ready NLP systems that use: Question answering, summarization, ranking etc.


Some of our other work: 
- [Distilled roberta-base-squad2 (aka "tinyroberta-squad2")]([https://huggingface.co/deepset/tinyroberta-squad2)
- [German BERT (aka "bert-base-german-cased")](https://deepset.ai/german-bert)
- [GermanQuAD and GermanDPR datasets and models (aka "gelectra-base-germanquad", "gbert-base-germandpr")](https://deepset.ai/germanquad)

## Get in touch and join the Haystack community

<p>For more info on Haystack, visit our <strong><a href="https://github.com/deepset-ai/haystack">GitHub</a></strong> repo and <strong><a href="https://docs.haystack.deepset.ai">Documentation</a></strong>. 

We also have a <strong><a class="h-7" href="https://haystack.deepset.ai/community">Discord community open to everyone!</a></strong></p>

[Twitter](https://twitter.com/deepset_ai) | [LinkedIn](https://www.linkedin.com/company/deepset-ai/) | [Discord](https://haystack.deepset.ai/community) | [GitHub Discussions](https://github.com/deepset-ai/haystack/discussions) | [Website](https://deepset.ai)

By the way: [we're hiring!](http://www.deepset.ai/jobs)