# SAE 105 - Traitée les données

> _SAE 105 — BUT Réseaux & Télécommunications_  
> **BUT RT - Semestre 1** | IUT Université de pau et des pays de l'adour (UPPA)
---

## 🎯 Objectif du projet
Ce projet vise à concevoir un outil d'analyse des logs d'un serveur web, capable de :
- Collecter et parser les données: Extraire les informations pertinentes du fichier de log Apache 2 fourni.
- Analyser les données: Calculer diverses statistiques sur l'activité du site web, notamment:
- Géolocalisation des adresses IP via un API externe.
- Évolution du nombre de requêtes au fil du temps.
- Répartition des systèmes d'exploitation et navigateurs utilisés par les visiteurs.
- Fréquence des erreurs HTTP (codes 200, 404, 500, etc.).
- Autres statistiques pertinentes identifiées lors de l'analyse du fichier log.
---

## 📂 Arborescence du projet
```bash
SAE105/
├── main.py     # Script Python principal
├── out/        # Dossier de sortie (out/maps.html est volontairement absent de ce dépôt)
├── README.md   # Ce fichier
└── LICENSE     # Licence Creative Commons
```
Le fichier de logs `controltower_access.log` est disponible depuis l’intranet de l’université."
---

## 🛠️ Technologies utilisées

| Outil / Langage | Utilisation principale |
|-----------------|------------------------|
| `Python`        | Traitement des données |
---

## 🧑‍💻 Auteur
- 👤 **Louis Deschamps**  
  📧 [contact@louino.fr](mailto:contact@louino.fr)  
  🎓 Étudiant en BUT Réseaux & Télécoms
---

## 🔒 Licence
> [!WARNING]  
> **Plagiat interdit**  
> Ce projet est distribué sous la licence **MIT**. Vous êtes **autorisé à réutiliser, modifier, distribuer ou intégrer ce code**, y compris à des fins commerciales, à **condition d'en citer l'auteur original et de conserver cette licence** dans toute copie ou version modifiée.  
> Le plagiat, défini comme la reproduction ou paraphrase non créditée d’un contenu, constitue une infraction aux **règles universitaires** et au droit d’auteur. **(Vous pouvez consulter, vous inspirer, mais pas copier.)**  
> Toute utilisation sans attribution peut entraîner des sanctions académiques et juridiques.   
> **MIT License – Libre usage, mais attribution obligatoire.**   