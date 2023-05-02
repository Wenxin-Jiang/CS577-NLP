---
language: th
widget:
- text: "สโมสรฟุตบอลเชลซีเล่นอยู่ในลีกอะไร"
  context: "สโมสรฟุตบอลเชลซี (อังกฤษ: Chelsea Football Club) เป็นสโมสรฟุตบอลอาชีพที่ตั้งอยู่ในเขตฟูลัม, ลอนดอน ซึ่งเล่นอยู่ในพรีเมียร์ลีก ลีกสูงสุดของฟุตบอลอังกฤษ ก่อตั้งขึ้นใน ค.ศ. 1905 มีสนามเหย้าคือสแตมฟอร์ดบริดจ์ เป็นหนึ่งในสโมสรที่ประสบความสำเร็จมากที่สุดของอังกฤษ[3][4][5] ในการแข่งขันภายในประเทศ เชลซีชนะเลิศลีกสูงสุด 6 สมัย, เอฟเอคัพ 8 สมัย, ลีกคัพ 5 สมัย และ เอฟเอคอมมิวนิตีชีลด์ 4 สมัย และในการแข่งขันระหว่างประเทศ พวกเขาชนะเลิศยูฟ่าแชมเปียนส์ลีก 2 สมัย, ยูฟ่าคัพวินเนอร์สคัพ 2 สมัย, ยูฟ่ายูโรปาลีก 2 สมัย, ยูฟ่าซูเปอร์คัพ 2 สมัย และฟุตบอลชิงแชมป์สโมสรโลก 1 สมัย"
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->


# wangchanberta-wiki-qa-finetuned-squad

This model is a fine-tuned version of [airesearch/wangchanberta-base-wiki-20210520-spm-finetune-qa](https://huggingface.co/airesearch/wangchanberta-base-wiki-20210520-spm-finetune-qa) on the iapp_wiki_qa_squad dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
