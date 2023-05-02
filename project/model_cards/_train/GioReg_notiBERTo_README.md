language: 
  - it


Si è creato un modello, chiamato notiBERTo, svolgendo la fase di addestramento e utilizzando per la creazione e il tuning dei pesi del modello l’algoritmo non supervisionato di masked-language modeling (MLM); questo non richiede l’utilizzo di testo con etichettatura. L’idea e stata quella di ottenere un modello BERT-based per la lingua italiana focalizzato sul linguaggio tipico utilizzato nei contesti dell’informazione giornalistica online che quindi potesse ricalcare lo stile, il lessico della stampa.

Per i dati in input sono stati utilizzati database disponibili pubblicamente online organizzati dal portale “Wortschatz Leipzig” dell’universita di Lipsia. Il portale offre l’accesso ai “corpora collection Leipzig” dove si trovano 900 collezioni testuali divise per lingua - le lingue presenti sono 250 - e argomento, ottenuti principalmente attraverso data crawling dei siti internet. In particolare sono stati scelti database di collezioni di notizie ottenute attraverso feeds RSS rac colte su base giornaliera e database ottenuti attraverso crawling dai principali siti internet di notizie italiane, suddivisi in sottodatabase in base agli anni di raccolta. Per la creazione di “notiBERTo” sono stati utilizzati database relativi agli anni 2018, 2019, 2020 per un totale di circa 700MB.

