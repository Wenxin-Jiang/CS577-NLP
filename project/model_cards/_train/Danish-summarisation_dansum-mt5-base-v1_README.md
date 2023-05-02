---
language: 
  - da
tags:
- summarization
widget:
- text: "De strejkende SAS-piloter melder sig nu klar til gøre en undtagelse fra strejken for at hente strandede chartergæster hjem fra flere ferieområder.

Undtagelsen skal gælde nogle uger frem, men piloterne vil under ingen omstændigheder have nye gæster med sig ned til de samme destinationer.

Det skriver SAS Pilot Group i en pressemeddelelse.

- Vi forstår, at det er uundgåeligt, at vores passagerer bliver ramt af strejken. Men vi piloter er altid fokuseret på at opføre os ansvarligt med passagersikkerheden som højeste prioritet, siger Martin Lindgren, der er formand for SAS Pilot Group i Norden.

Men for at hjælpe strandede gæster kræver de strejkende piloter samtidig, at SAS' trækker sin lockout af piloterne tilbage.

Samtidig ser SAS Pilot Group det som en forudsætning, at SAS ikke får hjælp fra andre flyselskaber til at flyve nye passagerer til de samme destinationer, som piloterne tilbyder at flyve gæster hjem fra, skriver fagforeningen."
  example_title: "Example 1"
- text: "Mere end 21.000 krigsforbrydelser. Så mange efterforsker de ukrainske myndigheder lige nu ifølge den ukrainske rigsadvokat, Iryna Venediktova.

Hun oplyser til britiske BBC, at der bliver anmeldt mellem 200 og 300 nye sager om dagen.

Forbrydelserne er ifølge Venediktova svære at efterforske, fordi det kan være vanskeligt at komme frem til de relevante områder og mennesker.

Men hun understreger overfor BBC, at russiske soldater, der har dræbt, tortureret eller voldtaget civile, bør forstå, at det kun er et spørgsmål om tid, før de alle vil komme for retten.

Rusland er blevet anklaget for en lang række krigsforbrydelser, siden landet invaderede Ukraine den 24. februar, men afviser alle anklager."
  example_title: "Example 2"
  
- text: "Det nye studie Cognitive Science på Aarhus Universitet, som i år havde Østjyllands højeste adgangskrav på 11,7 i karaktergennemsnit, udklækker det første hold bachelorer til sommer.

Men når de skal læse videre på kandidaten må de til udlandet, hvis ikke de vil skifte til et andet fag. Aarhus Universitet kan nemlig ikke nå at oprette en kandidat i Cognitive Science til næste sommer, hvor det første hold bachelorer er færdige.

Det rammer blandt andre Julie Sohn, der startede på uddannelsen i sommeren 2015, og derfor kun mangler et år, før hun er bachelor.

- Jeg synes, at det er ærgerligt, at vi som nye studerende på et populært studie ikke kan tage en kandidat i Danmark, siger hun.

Bacheloruddannelsen i Cognitive Science blev oprettet af Aarhus Universitet i 2015, og uddannelsen kombinerer viden om menneskelig adfærd med avanceret statistik. Da der endnu ikke er oprettet en kandidatuddannelse indenfor dette område, har Julie Sohn i stedet mulighed for at læse en kandidatgrad i for eksempel informationsvidenskab.

Hun vil dog hellere fortsætte på Cognitive Science, og derfor overvejer hun nu at læse videre i udlandet.

- Det ser ud til, at det er den eneste mulighed, hvis man gerne vil læse videre på noget, der faktisk passer ind til vores studie, siger hun.

Nye regler giver forsinkelse
På Aarhus Universitet havde man håbet på at have kandidatuddannelsen klar, når det første hold bachelorer bliver færdige til sommer. Arbejdet er dog blevet forsinket, fordi der er kommet nye regler for, hvornår man må oprette en uddannelse, fortæller Niels Lehmann, prodekan på fakultetet Arts, som Cognitive Science hører under.

Det er nogle meget dygtige studerende, der kommer ind på uddannelsen, og det er klart, at de i et vist omfang vil orientere sig mod udlandet, hvor man så kan forestille sig, at de bider sig fast.
NIELS LEHMANN, PRODEKAN, AARHUS UNIVERSITET
Tidligere skulle Danmarks Akkrediteringsinstitution se alle nye uddannelser efter i sømmene for at sikre, at kvaliteten var i orden. Nu skal uddannelsesinstitutionerne selv stå for det kvalitetstjek.

Men det tjek har Aarhus Universitet endnu ikke fået grønt lys til selv at udføre, fortæller prodekanen.

- Vi ville meget gerne have kunnet nå at få et udbud på kandidaten i gang i 2018, men så længe man er under institutionsakkreditering, så kan man ikke ansøge om nye uddannelser, siger han.

Det er endnu usikkert, hvornår Aarhus Universitet kan oprette kandidaten i Cognitive Science. Hvis de får alle de nødvendige godkendelser, kan den tidligst være klar i 2019.

Prodekan Niels Lehmann frygter, at Danmark kommer til at miste nogle af landets skarpeste studerende, hvis de er nødt til at rejse til udlandet for at gøre deres uddannelse færdig.

- Det er nogle meget, meget dygtige studerende, der kommer ind på denne uddannelse, og det er klart, at de i et vist omfang vil orientere sig mod udlandet, hvor man så kan forestille sig, at de bider sig fast, siger han.

Hos Danmarks Akkrediteringsinstitution forstår man godt, at universitets ansatte og studenrede ærgrer sig.

- Jeg kan godt forstå, at Aarhus Universitet ærgrer sig over, at det trækker ud, og at der går noget tid, før man får mulighed for at oprette nye uddannelser, og at man ikke har fået den genvej til at oprette nye uddannelser, som ville være fuldt med, hvis man havde opnået en positiv institutionsakkreditering, siger kommunikationsansvarlig Daniel Sebastian Larsen.

I år var Cognitive Science i Aarhus den uddannelse i Danmark, der havde det fjerde højeste karakterkrav - det højeste var 'AP Graduate in Marketing Management' på Erhvervsakademi Sjælland med et krav på 12,3."
  example_title: "Example 3"

---
# mT5-base fine-tuned for News article Summarisation ✏️🧾

[Google's mT5](https://aclanthology.org/2021.naacl-main.41/) for **summarisation** downstream task.

# Model summary
This repository contains a model for Danish abstractive summarisation of news articles. The summariser is based on a language-specific mT5-base, where the vocabulary is condensed to include tokens used in Danish and English. The model is fine-tuned using an abstractive subset of the DaNewsroom dataset (Varab & Schluter, 2020), according to the binned density categories employed in Newsroom (Grusky et al., 2019).

# References
Grusky, M., Naaman, M., & Artzi, Y. (2018). Newsroom: A Dataset of 1.3 Million Summaries with Diverse Extractive Strategies. ArXiv:1804.11283 [Cs]. http://arxiv.org/abs/1804.11283

Varab, D., & Schluter, N. (2020). DaNewsroom: A Large-scale Danish Summarisation Dataset. Proceedings of the 12th Language Resources and Evaluation Conference, 6731–6739. https://aclanthology.org/2020.lrec-1.831

