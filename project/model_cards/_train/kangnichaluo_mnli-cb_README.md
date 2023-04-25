learning rate: 3e-5  
training epochs: 5  
batch size: 8  
seed: 42  
model: bert-base-uncased  
The model is pretrained on MNLI (we use kangnichaluo/mnli-2 directly) and then finetuned on CB which is converted into two-way nli classification (predict entailment or not-entailment class)