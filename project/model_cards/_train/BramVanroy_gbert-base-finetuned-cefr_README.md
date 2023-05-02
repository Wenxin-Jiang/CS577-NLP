---
language:
- de
license: mit
tags:
- cefr
- proficiency assessment
- written text
datasets:
- merlin
- disko 
metrics:
- accuracy
- f1
- precision
- qwk
- recall

model-index:
- name: gbert-base-finetuned-cefr
  results:
  - task: 
      type: text-classification
      name: CEFR proficiency prediction
    metrics:
      - type: accuracy
        value: 0.8297872340425532
      - type: f1
        value: 0.831662518023171
      - type: precision
        value: 0.8379770347855454
      - type: qwk
        value: 0.9497893050032643
      - type: recall
        value: 0.8297872340425532

widget:
- text: "Samstag der 13. Februar Hallo ! Ich habe eine Fragen . Ich habe Probleme hören “ eu ” und “ cht ” . Wie sage ich “ also ” und “ to bake ” auf Deutsche ? Ich bin nicht gut aber ich lerne . Ich studiere Kunstgeschichte . Ich liebe Kunst und Geschichte . Mathamatik und Deutsche ich schierig aber nützlich . Es regnet heute . Die Woche ist interessant ."
- text: "Lieber . Ingo . Wie gehts es Ich will 3 Zimmer Wohnung Mieten . Ich kann nicht so viel Miete bezahlen Ich hab kein Geld . Ich muss eine wohnung Mieten . Viel Danke - Maria"
- text: "Hallo Liebe Daniela , ich möchte am Samstag um 15.00 Uhr im Schwimmbad gehen . In Stadt X ist ein neue Schwimmbad und ich möchte da gehen . _ Diese Schwimmbad ist so groß und sehr schön . Möchtest du mit mir gehen ? Weiß du dass ich liebe schwimmen , aber zusammen ist besser . Nimm bitte ein Tüch , speciall Schuhe , ein Schampoo und etwas zu trinken . Ruft mir an oder schreibt wenn möchtest du gehen mit mir . Mit freundlichen Grüße Julia"
---