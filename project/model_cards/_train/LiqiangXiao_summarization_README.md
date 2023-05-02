## Copy-or-Rewrite
This repository contains the code of paper "Copy or Rewrite: Hybrid Summarization with Hierarchical Reinforcement Learning". A model built for human-like summarization task and trained with Actor-critic Reinforcement Learning. This work significantly improved the ROUGE scores on CNN/DM dataset by 1.7 and augmented the informativity and readability of generated summaries. It implemented a more human-like workflow for summarization task solving the information loss problem. It contains a novel hierarchical transformer module to represent article in both word and sentence level, a new reinforcement learning method that can effectively train two-step model.

## Model description 
Copy-or-Rewrite is a model to improve the workflow of summarization models. Existing methods that adopt an extract-then-abstract strategy have achieved impressive results, yet they suffer from the information loss in the abstraction step because they compress all the selected sentences without distinguish. Especially when the whole sentence is summary-worthy, salient content would be lost by compression. To address this problem, we pro- pose HYSUM, a hybrid framework for summarization that can flexibly switch between copying sentence and rewriting sentence according to the degree of redundancy. In this way, our approach can effectively combine the advantages of two branches of summarization, juggling informativity and conciseness. Moreover, we based on Hierarchical Reinforcement Learning, propose an end-to-end reinforcing method to bridge together the extraction module and rewriting module, which can enhance the cooperation between them. Automatic evaluation shows that our approach significantly outperforms the state-of-the-arts on the CNN/DailyMail corpus. Human evaluation also demonstrates that our generated summaries are more informative and concise than popular models.

## Intended uses & limitations
With this repository, you can generate informative and concise summaries for input articles. For other tasks, you may used the hierarchical representation module to effectively represent the article. The parameters of the model is pre-trained on CNN/DM dataset. You may need to fine-tune it other your own dataset when needed.

## How to use

    from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
    
    tokenizer = AutoTokenizer.from_pretrained("LiqiangXiao/summarization")
    
    model = AutoModelForSeq2SeqLM.from_pretrained("LiqiangXiao/summarization")
    

## Training data
This model used the non-anonymous version of CNN/Daily Mail dataset. 

## BibTeX entry and citation info
    @inproceedings{DBLP:conf/aaai/XiaoWHJ20,
      author    = {Liqiang Xiao and
                   Lu Wang and
                   Hao He and
                   Yaohui Jin},
      title     = {Copy or Rewrite: Hybrid Summarization with Hierarchical Reinforcement
                   Learning},
      booktitle = {The Thirty-Fourth {AAAI} Conference on Artificial Intelligence, {AAAI}
                   2020, The Thirty-Second Innovative Applications of Artificial Intelligence
                   Conference, {IAAI} 2020, The Tenth {AAAI} Symposium on Educational
                   Advances in Artificial Intelligence, {EAAI} 2020, New York, NY, USA,
                   February 7-12, 2020},
      pages     = {9306--9313},
      publisher = {{AAAI} Press},
      year      = {2020},
      url       = {https://aaai.org/ojs/index.php/AAAI/article/view/6470},
      timestamp = {Tue, 02 Feb 2021 08:00:14 +0100},
      biburl    = {https://dblp.org/rec/conf/aaai/XiaoWHJ20.bib},
      bibsource = {dblp computer science bibliography, https://dblp.org}
    }
