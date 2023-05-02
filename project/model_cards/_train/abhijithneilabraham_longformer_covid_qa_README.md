# Dataset
---
---

datasets:
- covid_qa_deepset
---

--- 
Covid 19 question answering data obtained from [covid_qa_deepset](https://huggingface.co/datasets/covid_qa_deepset).  
# Original Repository
Repository for the fine tuning, inference and evaluation scripts can be found [here](https://github.com/abhijithneilabraham/Covid-QA).  
# Model in action
```
import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

tokenizer = AutoTokenizer.from_pretrained("abhijithneilabraham/longformer_covid_qa")
model = AutoModelForQuestionAnswering.from_pretrained("abhijithneilabraham/longformer_covid_qa")

question = "In this way, what do the mRNA-destabilising RBPs constitute ?"

text = 
"""
 In this way, mRNA-destabilising RBPs constitute a 'brake' on the immune system, which may ultimately be toggled therapeutically. I anticipate continued efforts in this area will lead to new methods of regaining control over inflammation in autoimmunity, selectively enhancing immunity in immunotherapy, and modulating RNA synthesis and virus replication during infection.

Another mRNA under post-transcriptional regulation by Regnase-1 and Roquin is Furin, which encodes a conserved proprotein convertase crucial in human health and disease. Furin, along with other PCSK family members, is widely implicated in immune regulation, cancer and the entry, maturation or release of a broad array of evolutionarily diverse viruses including human papillomavirus (HPV), influenza (IAV), Ebola (EboV), dengue (DenV) and human immunodeficiency virus (HIV). Here, Braun and Sauter review the roles of furin in these processes, as well as the history and future of furin-targeting therapeutics. 7 They also discuss their recent work revealing how two IFN-cinducible factors exhibit broad-spectrum inhibition of IAV, measles (MV), zika (ZikV) and HIV by suppressing furin activity. 8 Over the coming decade, I expect to see an ever-finer spatiotemporal resolution of host-oriented therapies to achieve safe, effective and broad-spectrum yet costeffective therapies for clinical use.

The increasing abundance of affordable, sensitive, high-throughput genome sequencing technologies has led to a recent boom in metagenomics and the cataloguing of the microbiome of our world. The MinION nanopore sequencer is one of the latest innovations in this space, enabling direct sequencing in a miniature form factor with only minimal sample preparation and a consumer-grade laptop computer. Nakagawa and colleagues here report on their latest experiments using this system, further improving its performance for use in resource-poor contexts for meningitis diagnoses. 9 While direct sequencing of viral genomic RNA is challenging, this system was recently used to directly sequence an RNA virus genome (IAV) for the first time. 10 I anticipate further improvements in the performance of such devices over the coming decade will transform virus surveillance efforts, the importance of which was underscored by the recent EboV and novel coronavirus (nCoV / COVID-19) outbreaks, enabling rapid deployment of antiviral treatments that take resistance-conferring mutations into account.

Decades of basic immunology research have provided a near-complete picture of the main armaments in the human antiviral arsenal. Nevertheless, this focus on mammalian defences and pathologies has sidelined examination of the types and roles of viruses and antiviral defences that exist throughout our biosphere. One case in point is the CRISPR/Cas antiviral immune system of prokaryotes, which is now repurposed as a revolutionary gene-editing biotechnology in plants and animals. 11 Another is the ancient lineage of nucleocytosolic large DNA viruses (NCLDVs), which are emerging human pathogens that possess enormous genomes of up to several megabases in size encoding hundreds of proteins with unique and unknown functions. 12 Moreover, hundreds of human-and avian-infective viruses such as IAV strain H5N1 are known, but recent efforts indicate the true number may be in the millions and many harbour zoonotic potential. 13 It is increasingly clear that host-virus interactions have generated truly vast yet poorly understood and untapped biodiversity. Closing this Special Feature, Watanabe and Kawaoka elaborate on neo-virology, an emerging field engaged in cataloguing and characterising this biodiversity through a global consortium. 14 I predict these efforts will unlock a vast wealth of currently unexplored biodiversity, leading to biotechnologies and treatments that leverage the host-virus interactions developed throughout evolution.

When biomedical innovations fall into the 'Valley of Death', patients who are therefore not reached all too often fall with them. Being entrusted with the resources and expectation to conceive, deliver and communicate dividends to society is both cherished and eagerly pursued at every stage of our careers. Nevertheless, the road to research translation is winding and is built on a foundation of basic research. Supporting industry-academia collaboration and nurturing talent and skills in the Indo-Pacific region are two of the four pillars of the National Innovation and Science Agenda. 2 These frame Australia's Medical Research and Innovation Priorities, which include antimicrobial resistance, global health and health security, drug repurposing and translational research infrastructure, 15 capturing many of the key elements of this CTI Special Feature. Establishing durable international relationships that integrate diverse expertise is essential to delivering these outcomes. To this end, NHMRC has recently taken steps under the International Engagement Strategy 16 to increase cooperation with its counterparts overseas. These include the Japan Agency for Medical Research and Development (AMED), tasked with translating the biomedical research output of that country. Given the reciprocal efforts at accelerating bilateral engagement currently underway, 17 the prospects for new areas of international cooperation and mobility have never been more exciting nor urgent. With the above in mind, all contributions to this CTI Special Feature I have selected from research presented by fellow invitees to the 2018 Awaji International Forum on Infection and Immunity (AIFII) and 2017 Consortium of Biological Sciences (ConBio) conferences in Japan. Both Australia and Japan have strong traditions in immunology and related disciplines, and I predict that the quantity, quality and importance of our bilateral cooperation will accelerate rapidly over the short to medium term. By expanding and cooperatively leveraging our respective research strengths, our efforts may yet solve the many pressing disease, cost and other sustainability issues of our time.
"""

encoding = tokenizer(question, text, return_tensors="pt")
input_ids = encoding["input_ids"]

# default is local attention everywhere
# the forward method will automatically set global attention on question tokens
attention_mask = encoding["attention_mask"]

start_scores, end_scores = model(input_ids, attention_mask=attention_mask)
all_tokens = tokenizer.convert_ids_to_tokens(input_ids[0].tolist())

answer_tokens = all_tokens[torch.argmax(start_scores) :torch.argmax(end_scores)+1]
answer = tokenizer.decode(tokenizer.convert_tokens_to_ids(answer_tokens))
# output => a 'brake' on the immune system 
```