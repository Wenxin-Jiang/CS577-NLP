---
tags:
- generated_from_trainer
datasets:
- thaiqa_squad
model-index:
- name: wangchanberta-base-att-spm-uncased-finetuned-th-squad
  results: []
widget:
- text: "สโมสรเรอัลมาดริดก่อตั้งขึ้นในปีใด"
  context: "สโมสรฟุตบอลเรอัลมาดริด (สเปน: Real Madrid Club de Fútbol) เป็นสโมสรฟุตบอลที่มีชื่อเสียงในประเทศสเปน ตั้งอยู่ที่กรุงมาดริด ปัจจุบันเล่นอยู่ในลาลิกา ก่อตั้งขึ้นใน ค.ศ. 1902 โดยเป็นหนึ่งในสโมสรที่ประสบความสำเร็จมากที่สุดในทวีปยุโรป เรอัลมาดริดเป็นสมาชิกของกลุ่ม 14 ซึ่งเป็นกลุ่มสโมสรชั้นนำของยูฟ่า และยังเป็นหนึ่งในสามสโมสรผู้ร่วมก่อตั้งลาลิกาซึ่งไม่เคยตกชั้นจากลีกสูงสุดนับตั้งแต่ ค.ศ. 1929 มีคู่อริคือสโมสรบาร์เซโลนา และ อัตเลติโกเดมาดริด มีสนามเหย้าคือซานเตียโก เบร์นาเบว" 
- text: "รักบี้ถือกำเนิดขึ้นในปีใด"
  context: "รักบี้ เป็นกีฬาชนิดหนึ่งถือกำเนิดขึ้นจากโรงเรียนรักบี้ (Rugby School) ในเมืองรักบี้ ในเขตวอร์วิกเชียร์ ประเทศอังกฤษ เริ่มต้นจาก ในปี ค.ศ. 1826 ขณะนั้นเป็นการแข่งขัน ฟุตบอล ภายในของโรงเรียนรักบี้ ซึ่งตั้งอยู่ ณ เมืองรักบี้ ประเทศอังกฤษ ผู้เล่นคนหนึ่งชื่อ วิลเลียม เวบบ์ เอลลิส (William Webb Ellis) ได้ทำผิดกติกาการแข่งขันที่วางไว้ โดยวิ่งอุ้มลูกบอลซึ่งตัวเขาเองไม่ได้เป็นผู้เล่นในตำแหน่งผู้รักษาประตู และได้วิ่งอุ้มลูกบอลไปจนถึงเส้นประตูฝ่ายตรงข้าม เขาจะจงใจหรือไม่ก็ตามแต่ แต่การเล่นที่นอกลู่นอกทางของเขาได้เป็นที่พูดถึงอย่างแพร่หลาย ในหมู่ผู้เล่นและผู้ดูจนแพร่กระจายไปตามโรงเรียนต่างๆในอังกฤษ โดยเฉพาะในหมู่นักเรียนของโรงเรียนเคมบริดจ์ ได้นำเอาวิธีการเล่นของ นายเอลลีส ไปจัดการแข่งขันโดยเรียกชื่อเกมชนิดใหม่นี้ว่า รักบี้เกมส์ (Rugby Games) ภายหลังจากนั้นก็เป็นที่นิยมเล่นกันมากขึ้น ทั้งได้มีการเปลี่ยนแปลงแก้ไขการเล่นเรื่อยมาในประเทศอังกฤษ"
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wangchanberta-base-att-spm-uncased-finetuned-th-squad

This model is a fine-tuned version of [airesearch/wangchanberta-base-att-spm-uncased](https://huggingface.co/airesearch/wangchanberta-base-att-spm-uncased) on the thaiqa_squad dataset.


### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3


### Framework versions

- Transformers 4.13.0
- Pytorch 1.10.0+cu111
- Datasets 1.16.1
- Tokenizers 0.10.3


