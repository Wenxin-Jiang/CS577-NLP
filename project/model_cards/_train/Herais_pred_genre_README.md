---
language:
- zh
tags:
- classification
license: apache-2.0
datasets:
- Custom
metrics:
- rouge
---

This model predicts the time period given a synopsis of about 200 Chinese characters.
The model is trained on TV and Movie datasets and takes simplified Chinese as input.

We trained the model from the "hfl/chinese-bert-wwm-ext" checkpoint.

#### Sample Usage
    from transformers import BertTokenizer, BertForSequenceClassification
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    checkpoint = "Herais/pred_genre"
    tokenizer = BertTokenizer.from_pretrained(checkpoint, 
                                              problem_type="single_label_classification")
    model = BertForSequenceClassification.from_pretrained(checkpoint).to(device)
    
    label2id_genre = {'涉案': 7, '都市': 10, '革命': 12, '农村': 4, '传奇': 0, 
                      '其它': 2, '传记': 1, '青少': 11, '军旅': 3, '武打': 6, 
                      '科幻': 9, '神话': 8, '宫廷': 5}

    id2label_genre = {7: '涉案', 10: '都市', 12: '革命', 4: '农村', 0: '传奇', 
                      2: '其它', 1: '传记', 11: '青少', 3: '军旅', 6: '武打', 
                      9: '科幻', 8: '神话', 5: '宫廷'}

    synopsis = """加油吧！检察官。鲤州市安平区检察院检察官助理蔡晓与徐美津是两个刚入职场的“菜鸟”。\
    他们在老检察官冯昆的指导与鼓励下，凭借着自己的一腔热血与对检察事业的执著追求，克服工作上的种种困难，\
    成功办理电竞赌博、虚假诉讼、水产市场涉黑等一系列复杂案件，惩治了犯罪分子，维护了人民群众的合法权益，\
    为社会主义法治建设贡献了自己的一份力量。在这个过程中，蔡晓与徐美津不仅得到了业务能力上的提升，\
    也领悟了人生的真谛，学会真诚地面对家人与朋友，收获了亲情与友谊，成长为合格的员额检察官，\
    继续为检察事业贡献自己的青春。 """
    
    inputs = tokenizer(synopsis, truncation=True, max_length=512, return_tensors='pt')
    model.eval()
    outputs = model(**input)
        
    label_ids_pred = torch.argmax(outputs.logits, dim=1).to('cpu').numpy()
    labels_pred = [id2label_timeperiod[label] for label in labels_pred]
    
    print(labels_pred)
    # ['涉案']
    
 Citation
 TBA