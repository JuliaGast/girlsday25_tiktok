
# Warum sehe ich was auf TikTok und Co?
A presentation and mini recommender app that [Ricarda Link](https://www.uni-mannheim.de/dws/people/researchers/phd-students/ricarda-link/), [Lea Cohausz](https://lea-cohausz.github.io/), and [Julia Gastinger](https://juliagast.github.io/) created for [girls' day](https://www.girls-day.de/) 2025. 

## slides
* Zielgruppe: Teenager (ca 8.-13. Klasse)
* Inhalt:
  * Hintergrund: Die Empfehlungsmethoden hinter Social Media  - eine kurze uebersicht ueber Collaborative Filtering und Content-based Recommendation, mit einfachen Rechenbeispielen
  * Risiken: Unbeabsichtigte Folgen und Gezielte Manipulation - erklaert, was fuer Probleme und Risiken entstehen koennen, und wie das mit den Empfehlungsmethoden zusammenhaengt.
  * Chancen: Wie kannst du Social Media sicher nutzen, oder deinen Content pushen

## code
Ein kleiner dummy recommender Algorithmus (streamlit), in zwei versionen
### Version 1: Positiv `app.py`
Run with `streamlit app.py`
* Es werden Bilder von verschiedenen Kategorien gezeigt (Hunde, Fashion, Backen, Sport, Party)
* User*innen koennen diese Bilder liken oder weiterdruecken
* Am Ende wird ein Bild empfohlen, aus der meistgelikten Kategorie
* Soll mit einfachen Beispielen oberflaechlich zeigen, wie Empfehlungsalgorithmen funktionieren.
 
### Version 2: Negativ `app_negative.py`
Run with `streamlit app_negative.py`
* z.B. wenn viele HighFashion Bilder geliked werden, wird ein Bild zum Thema "Abnehmen" empfohlen, und wenn viele Bilder von Paerchen die Sport machen geliked werden, wird ein Bild zum Thema "Paerchen" gezeigt.
* Soll mit einfachen Beispielen plakativ zeigen, was schiefgehen kann bei Empfehlungsalgorithmen.
