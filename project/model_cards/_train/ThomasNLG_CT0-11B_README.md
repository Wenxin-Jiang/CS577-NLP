---
language: en
license: apache-2.0
widget:
- text: "A is the son's of B's uncle. What is the family relationship between A and B?"
- text: "Reorder the words in this sentence: justin and name bieber years is my am I 27 old."
- text: "Task: copy but say the opposite.\n
PSG won its match against Barca."
- text: "Is this review positive or negative? Review: Best cast iron skillet you will every buy."
  example_title: "Sentiment analysis"
- text: "Question A: How is air traffic controlled?
\nQuestion B: How do you become an air traffic controller?\nPick one: these questions are duplicates or not duplicates."
- text: "Barack Obama nominated Hilary Clinton as his secretary of state on Monday. He chose her because she had foreign affairs experience as a former First Lady.
\nIn the previous sentence, decide who 'her' is referring to."
  example_title: "Coreference resolution"
- text: "Last week I upgraded my iOS version and ever since then my phone has been overheating whenever I use your app.\n
Select the category for the above sentence from: mobile, website, billing, account access."
- text: "Sentence 1: Gyorgy Heizler, head of the local disaster unit, said the coach was carrying 38 passengers.\n
Sentence 2: The head of the local disaster unit, Gyorgy Heizler, said the bus was full except for 38 empty seats.\n\n
Do sentences 1 and 2 have the same meaning?"
  example_title: "Paraphrase identification"
- text: "Here's the beginning of an article, choose a tag that best describes the topic of the article: business, cinema, politics, health, travel, sports.\n\n
The best and worst fo 007 as 'No time to die' marks Daniel Craig's exit.\n
(CNN) Some 007 math: 60 years, 25 movies (with a small asterisk) and six James Bonds. For a Cold War creation, Ian Fleming's suave spy has certainly gotten around, but despite different guises in the tuxedo and occasional scuba gear, when it comes to Bond ratings, there really shouldn't be much argument about who wore it best."
- text: "Max: Know any good websites to buy clothes from?\n
Payton: Sure :) LINK 1, LINK 2, LINK 3\n
Max: That's a lot of them!\n
Payton: Yeah, but they have different things so I usually buy things from 2 or 3 of them.\n
Max: I'll check them out. Thanks.\n\n
Who or what are Payton and Max referring to when they say 'them'?"
- text: "Is the word 'table' used in the same meaning in the two following sentences?\n\n
Sentence A: you can leave the books on the table over there.\n
Sentence B: the tables in this book are very hard to read."
- text: "On a shelf, there are five books: a gray book, a red book, a purple book, a blue book, and a black book.\n
The red book is to the right of the gray book. The black book is to the left of the blue book. The blue book is to the left of the gray book. The purple book is the second from the right.\n\n
Which book is the leftmost book?"
  example_title: "Logic puzzles"
- text: "The two men running to become New York City's next mayor will face off in their first debate Wednesday night.\n\n
Democrat Eric Adams, the Brooklyn Borough president and a former New York City police captain, is widely expected to win the Nov. 2 election against Republican Curtis Sliwa, the founder of the 1970s-era Guardian Angels anti-crime patril.\n\n
Who are the men running for mayor?"
  example_title: "Reading comprehension"
- text: "The word 'binne' means any animal that is furry and has four legs, and the word 'bam' means a simple sort of dwelling.\n\n
Which of the following best characterizes binne bams?\n
- Sentence 1: Binne bams are for pets.\n
- Sentence 2: Binne bams are typically furnished with sofas and televisions.\n
- Sentence 3: Binne bams are luxurious apartments.\n
- Sentence 4: Binne bams are places where people live."
---
**How do I pronounce the name of the model?** CT0 should be pronounced "C T Zero" (like in "Continual T5 for zero-shot")
# Model Description
CT0 is an extention of T0, a model showing great zero-shot task generalization on English natural language prompts, outperforming GPT-3 on many tasks, while being 16x smaller. 

```bibtex
@misc{scialom2022Continual,
      title={Fine-tuned Language Models are Continual Learners},
      author={Thomas Scialom and Tuhin Chakrabarty and Smaranda Muresan},
      year={2022},
      eprint={2205.12393},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```