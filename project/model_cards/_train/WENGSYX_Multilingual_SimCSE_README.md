# Multilingual SimCSE

#### A contrastive learning model using parallel language pair training

##### By using parallel sentence pairs in different languages, the text is mapped to the same vector space for pre-training similar to Simcse

##### Firstly, the [mDeBERTa](https://huggingface.co/microsoft/mdeberta-v3-base) model is used to load the pre-training parameters, and then the pre-training is carried out based on the [CCMatrix](https://github.com/facebookresearch/LASER/tree/main/tasks/CCMatrix) data set. 

##### Training data: 100 million parallel pairs

##### Taining equipment: 4 * 3090



## Pipline Code

```
from transformers import AutoModel,AutoTokenizer

model = AutoModel.from_pretrained('WENGSYX/Multilingual_SimCSE')
tokenizer = AutoTokenizer.from_pretrained('WENGSYX/Multilingual_SimCSE')

word1 = tokenizer('Hello,world.',return_tensors='pt')
word2 = tokenizer('你好,世界',return_tensors='pt')
out1 = model(**word1).last_hidden_state.mean(1)
out2 = model(**word2).last_hidden_state.mean(1)
print(F.cosine_similarity(out1,out2))
----------------------------------------------------
tensor([0.8758], grad_fn=<DivBackward0>)
```



## Train Code



```
from transformers import AutoModel,AutoTokenizer,AdamW

model = AutoModel.from_pretrained('WENGSYX/Multilingual_SimCSE')
tokenizer = AutoTokenizer.from_pretrained('WENGSYX/Multilingual_SimCSE')
optimizer = AdamW(model.parameters(),lr=1e-5)

def compute_loss(y_pred, t=0.05, device="cuda"):
    idxs = torch.arange(0, y_pred.shape[0], device=device)
    y_true = idxs + 1 - idxs % 2 * 2
    similarities = F.cosine_similarity(y_pred.unsqueeze(1), y_pred.unsqueeze(0), dim=2)
    similarities = similarities - torch.eye(y_pred.shape[0], device=device) * 1e12
    similarities = similarities / t
    loss = F.cross_entropy(similarities, y_true)
    return torch.mean(loss)
    
wordlist = [['Hello,world','你好,世界'],['Pensa che il bianco rappresenti la purezza.','Он думает, что белые символизируют чистоту.']]

input_ids, attention_mask, token_type_ids = [], [], []
for x in wordlist:
    text1 = tokenizer(x[0], padding='max_length', truncation=True, max_length=512)
    input_ids.append(text1['input_ids'])
    attention_mask.append(text1['attention_mask'])
    text2 = tokenizer(x[1], padding='max_length', truncation=True, max_length=512)
    input_ids.append(text2['input_ids'])
    attention_mask.append(text2['attention_mask'])

input_ids = torch.tensor(input_ids,device=device)
attention_mask = torch.tensor(attention_mask,device=device)

output = model(input_ids=input_ids,attention_mask=attention_mask)
output = output.last_hidden_state.mean(1)
loss = compute_loss(output)
loss.backward()

optimizer.step()
optimizer.zero_grad()
```

