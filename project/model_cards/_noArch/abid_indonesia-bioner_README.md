---
tags:
- flair
- token-classification
- sequence-tagger-model
language:
- id
- en
license: bsd-3-clause
widget:
- text: 'Dok saya mau tanya kenapa ya kulit saya kering bersisik gitu dok. Apalagi bagian tumit sampai nglupas terus gatal. Penyebabnya apa y dok terus cara mengobatinya gimana? Terima kasi'
- text: 'halo dok saya mau bertanya saya sering merasa cemas resah dan takut akan semua yg saya lakukan dan kejar , padahal aktifitas sehari hari berjalan lancar pdahal saya di kantor cukup terbilang sebagai karyawan terbaik tetapi saya merasa terbebani dengan cemas dan rasa takut itu sendiri'
- text: 'Does anyone else feel like their losing there mind with all the hormonal changes? One minute Im all happy and then Im crying. Tumor was seen in 2014 and I was never told. Lots of other surgeries, they have already told me surgery needs to done. This would be around my 20th surgery. Alot of different parts of body have been medically altered and this time its all my chose on what i want to do. Im opting to just let it all go and let god do what he needs to with me. Im not scared for myself but for my family and people I love.'

---
## Biomedical Entity Recognition in Bahasa Indonesia

Summary:
- Trained using manually annotated data from alodokter.com (online health QA platform) using UMLS guideline (see https://rdcu.be/cNxV3) 
- Recognize disorders (DISO) and anatomy (ANAT) entities
- Achieve best F1 macro score 0.81
- Based on XLM-Roberta. So, cross lingual recognition might work.

## CITATION
This work is done with generous support from Safitri Juanita, Dr. Diana Purwitasari and Dr. Mauridhi Hery Purnomo from Institut Teknologi Sepuluh Nopember, Indonesia.

Citation for academic purpose will be provided later.

For demo, please go to the HF space demo: https://huggingface.co/spaces/abid/id-bioner-demo