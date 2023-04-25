---
tags:
- flair
- token-classification
- sequence-tagger-model
language: en
widget:
- text: "Delphi SQL developer"
  example_title: "Example 1"
- text: "Searching for new opportunities as Junior Node.js JavaScript backend developer. Over 15 years of experience in different IT areas. Experience with: Node.js JavaScript MongoDB  HTML CSS Java Lotus Script websocket socket.io Docker babel Webpack MySQL JSON React"
  example_title: "Example 2"
- text: "Experienced Chief Executive Officer with a demonstrated history of working in the wholesale industry. Skilled in Customer Service, Sales, Strategic Planning, and Business Development. Strong business development professional."
  example_title: "Example 3"

---
## English NER in Flair (Ontonotes fast model)
F1-Score: **84.3** (Ontonotes)

Predicts 2 tags:

| tag                        | meaning |
|---------------------------------|-----------|
| SKILL    | skill name | 
| EXPERIENCE | year of experience |
Based on [Flair embeddings](https://www.aclweb.org/anthology/C18-1139/) and LSTM-CRF.