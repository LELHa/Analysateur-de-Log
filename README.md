# Analyseur-de-Log

Un outil Python pour l'analyse de fichiers de logs.

## Description

Il s'agit d'un outil développé en Python permettant d'analyser automatiquement des fichiers de logs.

Le programme lit les événements enregistrés, extrait les informations importantes, détecte les erreurs et génère un rapport d'analyse au format texte.

Ce projet permet de travailler la manipulation de fichiers, le parsing de données, l'analyse automatique et la création d'un outil en ligne de commande.

---

## Fonctionnalités

- Lecture de fichiers de logs
- Parsing automatique des événements
- Détection des niveaux de logs :
  - INFO
  - WARNING
  - ERROR
  - CRITICAL
- Comptage des événements
- Détection des lignes invalides
- Génération d'un rapport texte
- Utilisation via une interface en ligne de commande (CLI)

---

## Installation

### Prérequis

- Python 3.x


## Utilisation

Accéder au dossier du projet :

```bash
cd Analysateur-de-Log
```

Lancer l'analyse d'un fichier de logs :

```bash
python main.py logs/example.log
```

Vous pouvez remplacer `logs/example.log` par le chemin du fichier que vous souhaitez analyser.

Exemple :

```bash
python main.py logs/server.log
```

Le programme génère ensuite un rapport d'analyse dans :

```text
reports/report.txt
```

---

## Architecture du projet

```
Analyseur-de-Log/
│
├── main.py
│
├── src/
│   ├── reader.py
│   ├── parser.py
│   ├── analyzer.py
│   └── rapport.py
│
├── logs/
│   └── example.log
│
└── reports/
    └── report.txt
```

---

## Exemple de rapport

```text
RAPPORT DE LOG

Total events: 5

Invalid lines: 1

Stats:
INFO: 2
WARNING: 1
ERROR: 2
CRITICAL: 0

Errors detected:
- Database connection failed
- Server unavailable
```

---

## Technologies utilisées

- Python 3
- Expressions régulières (Regex)
- Manipulation de fichiers
- Interface en ligne de commande (CLI)

---

## Améliorations futures

- Export des rapports en CSV
- Interface graphique
- Analyse des logs en temps réel
- Stockage des historiques dans une base de données
- Visualisation des statistiques
