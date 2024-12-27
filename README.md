# Person_Counting_with_OpenCV

# Object Counting with YOLO and OpenCV

Ce projet utilise un modèle de détection d'objets pré-entraîné YOLO (You Only Look Once) et la bibliothèque OpenCV pour compter les personnes dans une vidéo en fonction d'une zone définie.

## Description

Le but de ce projet est de détecter et compter les personnes qui entrent et sortent d'une zone délimitée dans une vidéo. Le projet utilise le modèle YOLOv5 (version 11n) de la bibliothèque `ultralytics` pour la détection des objets (ici, les personnes). Les résultats du comptage sont affichés en temps réel sur chaque frame de la vidéo.

### Fonctionnalités

- Détection des personnes dans une vidéo.
- Comptage des personnes entrant et sortant d'une région définie.
- Affichage en temps réel du nombre de personnes à l'intérieur de la zone sur chaque frame de la vidéo.
- Exportation de la vidéo traitée avec les annotations.

## Prérequis

Avant de lancer le projet, assurez-vous d'avoir installé les dépendances suivantes :

- Python 3.x
- OpenCV
- NumPy
- `ultralytics` (pour utiliser YOLOv5)

Vous pouvez installer les dépendances nécessaires via `pip` :

```bash
pip install opencv-python numpy ultralytics
