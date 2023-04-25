Ushbu model, HuggingFace-da RoBERTa transformatorini amalga oshirishga asoslangan. Bizning RoBERTa dasturimiz 12 ta diqqat boshi va 6 ta qatlamdan foydalanadi, natijada 72 ta aniq e'tibor mexanizmlari paydo bo'ladi. Biz har bir kirish satridagi tokenlarning 15 foizini niqoblaydigan RoBERTa-dan dastlabki tekshirish protsedurasini qabul qildik. Biz maksimal 52K tokenli lug'atdan va maksimal 512 ta ketma-ketlik uzunligidan foydalanganmiz. Biz 1M PubChem to'plamlarida 10 ta davr uchun o'qitdik. Loss funksiya 2.9 dan 0.33 gacha tushdi. Ushbu modelni sizga taqdim qilamiz.
<pre><code class="language-python">

@misc {rifkat_davronov_2022,
	author       = { {Adilova Fatima,Rifkat Davronov, Samariddin Kushmuratov, Ruzmat Safarov} },
	title        = { pubchem_1M (Revision 89e2ba6) },
	year         = 2022,
	url          = { https://huggingface.co/rifkat/pubchem_1M },
	doi          = { 10.57967/hf/0177 },
	publisher    = { Hugging Face }
}

</code></pre>