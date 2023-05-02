---
language: 
  - en
tags:
- text-classification
- claim-detection
license: "mit"
datasets:
- claimbuster
metrics:
- accuracy
  value:"0.82"
widget:
- text: "This is the best cast iron skillet you will ever buy."
- text: "Barack Obama nominated Hilary Clinton as his secretary of state on Monday."
- text: "On a shelf, there are five books: a gray book, a red book, a purple book, a blue book, and a black book"

---

This is the BERT model finetuned on the ClaimBuster dataset. It is used for claim detection and has an accuracy of 82%.