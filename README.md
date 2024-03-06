# wp3-2024-starter
Template voor WP3 opdracht "Accessibility Hub". Vul dit document aan zoals beschreven in eisen rondom opleveren (zie ook de [opdracht](CASUS.md)) 


# Bron voor ChatGPT

Stichting Accessibility heeft als missie een inclusieve samenleving te bevorderen, waarin alle mensen, met of zonder beperking, gelijkwaardig kunnen participeren. Dat is een mooi streven en gaat hand in hand met het besef van bedrijven en organisaties dat het belangrijk is om hun producten en diensten toegankelijk te maken voor iedereen. 

Met het oog op het doen van onderzoek naar de huidige toegankelijkheid en het indienen van verbetervoorstellen, wil Stichting Accessibility een webapplicatie laten ontwikkelen. Deze applicatie is bedoeld om een panel van ongeveer 125 mensen met een beperking samen te brengen met organisaties en bedrijven. Hierin wil Stichting Accessibility een rol nemen als poortwachter, om onderzoek uitvragen en ervaringsdeskundigen zorgvuldig geselecteerd bij elkaar te krijgen. Omdat het om een kwetsbare doelgroep gaat zal de Stichting Accessibility de gegevens van de ervaringsdeskundigen beheren en alle acties in het proces goedkeuren. Daarbij spelen twee aspecten een grote rol: toegankelijkheid van de applicatie en informatiebeveiliging.

Hoe zet ik dit om in m'n eigen woorden?


Antwoord van ChatGPT:

Stichting Accessibility heeft als voornaamste doel een inclusieve samenleving te bevorderen, waarin iedereen, ongeacht eventuele beperkingen, gelijkwaardig kan deelnemen. Dit streven sluit nauw aan bij de groeiende bewustwording onder bedrijven en organisaties dat het cruciaal is om hun producten en diensten toegankelijk te maken voor alle gebruikers.

Om de huidige toegankelijkheid te onderzoeken en verbeteringen voor te stellen, is Stichting Accessibility van plan een webapplicatie te laten ontwikkelen. Deze applicatie heeft als doel een panel van ongeveer 125 mensen met diverse beperkingen samen te brengen met bedrijven en organisaties. Hierbij fungeert Stichting Accessibility als tussenpersoon, waarbij ze zorgvuldig ervaringsdeskundigen selecteren en het proces beheren. Gezien de kwetsbaarheid van de doelgroep, zal de stichting de gegevens van de ervaringsdeskundigen beheren en alle stappen in het proces nauwkeurig goedkeuren. Hierbij zijn twee belangrijke aspecten van groot belang: de toegankelijkheid van de applicatie zelf en de beveiliging van de informatie.

# Sem

Ik heb de login en registratie gemaakt voor de ervaringsdeskundige en administrators, hier liep ik best lang op vast en was ook niet even makkelijk. Uiteindelijk na veel uitzoek werk en gesprekken met Mark erover heb ik het nu op een andere manier opgelost. Helaas niet op de Django manier, maar wel werkend.

# links en tutorials
Voor de login heb ik heel erg veel videos gekeken voor de vele manieren.

invoer voor als input niet ingevuld is.
https://www.sololearn.com/en/Discuss/2304405/in-python-if-the-user-doesnt-enters-a-input-and-simply-press-submit-button-if-this-is-situation-then-how-to-set-default-value

Deze video heb ik het meest gekeken toen ik begon, deze had mij veel geholpen.
https://www.youtube.com/watch?v=Z3qTXmT0yoI&ab_channel=CloudWithDjango

https://www.youtube.com/watch?v=cu-1EdSMzK0&ab_channel=MyAcademy

https://www.youtube.com/watch?v=meREllvata8&ab_channel=Desphixs

# Videos voor de omweg (bijna al deze video's heb ik zowat volledig bekeken.)
Deze video gebruikte ik om een custom user model aan te maken, hieronder bij het kopje django site zie je waarom dat fout liep
https://www.youtube.com/watch?v=mndLkCEiflg&ab_channel=CodeWithStein

https://www.youtube.com/watch?v=mOS0L5Lb2u0&ab_channel=Desphixs
https://www.youtube.com/watch?v=Rhg-Ua6tM2w&t=449s&ab_channel=THESHOW
https://www.youtube.com/watch?v=ypAAh_Abjxs&t=386s&ab_channel=SelmiTech
https://www.youtube.com/watch?v=sbCd52JiCU4&t=1268s&ab_channel=CodingWithMitch
https://www.youtube.com/watch?v=SFarxlTzVX4&t=1915s&ab_channel=CodingWithMitch
https://www.youtube.com/watch?v=Pc4SF7bSkMs&t=473s&ab_channel=CodingEntrepreneurs

# Django site
Hier wilde ik de omweg maken en required fields aanmaken, helaas kwam daar veel meer bij kijken. Ook elke keer dat ik een video had die dat behandelde, hadden ze het over het aanmaken van een superuser die dan meer velden kreeg. Ik wilde natuurlijk dat de gebruikers gewoon konden inloggen op de applicatie zelf. Ook was het moeilijk om de lege stukken in te vullen.
https://docs.djangoproject.com/en/5.0/topics/auth/default/

https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#:~:text=It%20authenticates%20using%20credentials%20consisting,see%20Customizing%20Users%20and%20authentication).

# Sites voor custom usermodel
https://reintech.io/blog/writing-custom-authentication-backend-django
https://dev.to/amoabakelvin/creating-a-custom-authentication-backend-in-django-17bl
https://reintech.io/blog/building-a-custom-authentication-system-in-django

# Stackoverflow
https://stackoverflow.com/questions/57556793/login-check-the-username-and-password-from-database-in-django-website-using-post

https://stackoverflow.com/questions/70644038/get-data-from-one-column-in-database-django