
---
widget:

- text: "Меня зовут Aнгелина компания диджитал бизнес звоним вам по поводу продления лицензии а мы с серым у вас скоро срок заканчивается. My name is Angela digital business company calling you about your license expiration date"
- text: "Добрый меня Максим зовут компания китобизнес удобно говорить. Greetings my name is Maxim I work for Whale Hunter have a minute? "
#  example_title: "Maxim"
- text: "Угу да вижу я эту почту хорошо тогда исправлю на эту будем ждать ответа всего хорошего. Ok I see this email sure I will change it shall wait for response good bye"

---
# Model is trained on client-manager conversations and is able to classify:

## 1) Greeting class, where managers say 'Hi'. 
##  Uses GRE tag

## 2) Introduction class, where managers introduce themselves.
## Uses NAM tag

## 3) Organisation class, where managers' employer is mentioned
## Uses ORG tag

## 4) Farewell class, where managers say 'Good Bye'
## Uses FAR tag

Evaluation metrics: 
'precision': 0.8695652173913043, 
'recall': 0.9523809523809523, 
'f1_score': 0.909090909090909
