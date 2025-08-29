# Kreditausfalls Vorhersage ML-Modellierung App

Dieses Repository enthält die Streamlit-App zur **Kreditrisikovorhersage**.  
Die App ermöglicht es, mit Hilfe von Machine-Learning-Modellen (z. B. XGBoost, Extra Trees) das Risiko eines Kreditausfalls für Kunden vorherzusagen.  
Zusätzlich können Was-wäre-wenn-Analysen durchgeführt werden, um die Auswirkungen einzelner Eingabeparameter auf das Kreditrisiko zu verstehen.  

## Thema des Projekts:
In diesem Projekt steht die Analyse von Kreditdaten (German Credit Data Dataset) im Mittelpunkt, mit dem Ziel, Zahlungsausfallrisiken präzise vorherzusagen.

**Beobachteter Zeitraum:** 202x  

**Geografische Abgrenzung:** Deutschland  

**Kategorien:**  

-    Age – Alter der Antragsteller (in Jahren)
-    Sex – Geschlecht (männlich oder weiblich)
-    Job – Berufskategorie (0 = niedrigste Qualifikation, 3 = höchste Qualifikation)
-    Housing – Wohnsituation (eigene Wohnung, Miete oder kostenloses Wohnen)
-    Saving accounts – Kategorie des Sparguthabens (z.B. "little", "moderate", "rich")
-    Checking account – Kategorie des Girokontos (z.B. "little", "moderate", "rich")
-    Credit amount – Höhe des aufgenommenen Kredits
-    Duration – Laufzeit des Kredits in Monaten
-    Purpose – Zweck des Kredits (z.B. Auto, Radio/TV, Urlaub, Ausbildung, Geschäft)
-    Risk – Zielvariable: Kreditrisiko
     -   good = Kunde gilt als risikoarm
     -   bad = Kunde gilt als risikoreich

### Features der App
- 📑 **Vorhersagen**: Risiko-Berechnung basierend auf individuellen Eingaben  
- ❔ **What-if Analyse**: Simulation, wie sich das Risiko verändert, wenn ein einzelnes Merkmal variiert  
- ✅ **Erklärung**: Erläuterung des Modells und der Ergebnisse  
- ℹ️ **About**: Hintergrundinformationen zur App  

### Built with
[![Python][Python]][Python-url]
[![Streamlit]][Streamlit-url]
[![GitHub]][GitHub-url]



# Erste Schritte

*Windows*

- Python 3 oder höhere Version installieren
- Repository klonen:
  
  `git clone`  `git@github.com:predragt565/streamlit_app_creditrisk.git` <project_name>
  
- Gehe dann in das Projektverzeichnis:
  
  `cd <project_name>`
  
- Virtuele Entwicklungsumgebung erstellen:
  
  `python -m venv .venv`
  
- Virtuele Entwicklungsumgebung aktivieren:
  
  `.venv\Scripts\activate`  
  
- Abhängigkeiten installieren:
  
  `pip install -r requirements.txt`
  

*MacOS*

- Python 3 oder höhere Version installieren
- Repository klonen:
  
  git clone  `git@github.com:predragt565/streamlit_app_creditrisk.git` <project_name>
  
- Gehe dann in das Projektverzeichnis:
  
  `cd <project_name>`
  
- Virtuele Entwicklungsumgebung erstellen:
  
  `python3 -m venv .venv`
  
- Virtuele Entwicklungsumgebung aktivieren:
  
  `source .venv/bin/activate` 
  
- Abhängigkeiten installieren:
  
  `pip install -r requirements.txt`

<p align="right">(<a href="#readme-top">back to top</a>)</p>


# Berichtsablauf

- App starten mit:
  ```bash
  streamlit run main_2.py
  ```

- Eingabeparameter im Sidebar setzen
- Risiko berechnen lassen oder What-if Analyse durchführen


<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- USAGE EXAMPLES -->

## Beispielhafte Nutzung

- Bewertung der Kreditwürdigkeit und Vorhersage des Ausfallrisikos von Kunden  
- Analyse, wie einzelne Faktoren (z. B. Einkommen, Zweck, Spar- oder Girokonto) die Kreditrisikoeinstufung beeinflussen


<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->


<!--Open localhost with the port 5172: http://localhost:5173/<br>
In your case the port could be different.-->


<!-- CONTACT -->

## Contact

[Predrag@LinkedIn](https://www.linkedin.com/in/predrag-trikic-6696a429/)  
[Predrag@GitHub](https://github.com/predragt565)  
[Predrag@Kaggle](https://www.kaggle.com/predragtrikic)  

<!-- ACKNOWLEDGMENTS -->

## Useful information

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [GitHub](https://github.com/)



<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
[Flask]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/
[Chakra]: https://img.shields.io/badge/chakra-%234ED1C5.svg?style=for-the-badge&logo=chakraui&logoColor=white
[Chakra-url]: https://v2.chakra-ui.com/
[JavaScript]: https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E
[JavaScript-url]: https://developer.mozilla.org/en-US/docs/Web/JavaScript
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[Vite]: https://img.shields.io/badge/vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=white
[Vite-url]: https://vitejs.dev/
[Render]: https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white
[Render-url]: https://render.com/
[Power BI]: https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=white  
[Power BI-url]: https://powerbi.microsoft.com/
[Jupyter]: https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white  
[Jupyter-url]: https://jupyter.org/
[Streamlit]: https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white
[Streamlit-url]: https://streamlit.io/
[GitHub]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[GitHub-url]: https://github.com/
