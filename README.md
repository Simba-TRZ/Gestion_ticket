# Gestion de Tickets

## Description
Je m'appelle Aziz, étudiant en 2ème année de BTS SIO (Services Informatiques aux Organisations), option SLAM (Solutions Logicielles et Applications Métiers). J'ai conçu ce projet dans le cadre de mon stage en support informatique. L'objectif était de créer une solution pratique et légère pour aider les équipes techniques à gérer efficacement les incidents signalés par les utilisateurs. 

Ce projet m'a permis d'appliquer mes compétences en développement Python tout en répondant à un besoin concret d'organisation et de suivi des tickets. Il illustre ma capacité à développer des outils utiles pour des environnements professionnels.

## Objectif
L'idée derrière ce programme est de simplifier la gestion des problèmes techniques rencontrés par les utilisateurs ou l'équipe. 
Il permet :
- De centraliser toutes les demandes dans un seul système.
- De suivre facilement l’état d’un ticket (ouvert, en cours, fermé).
- D’attribuer des priorités pour traiter les demandes les plus urgentes en premier.
- D’avoir un historique des tickets grâce à la sauvegarde automatique.

Ce programme est conçu pour les petites équipes de support technique qui souhaitent un outil léger sans avoir à installer de solutions complexes.

## Fonctionnalités
- **Créer un ticket** : Ajouter une demande avec une description et une priorité (Basse, Moyenne, Haute).
- **Afficher tous les tickets** : Lister les tickets existants avec leurs informations complètes.
- **Mettre à jour un ticket** : Modifier le statut d’un ticket pour refléter son état.
- **Supprimer un ticket** : Supprimer un ticket résolu ou non pertinent.
- **Rechercher un ticket** : Trouver rapidement un ticket à l’aide d’un mot-clé.
- **Sauvegarde automatique** : Tous les tickets sont sauvegardés dans un fichier JSON pour éviter toute perte.
- **Exporter les tickets** : Générer un fichier texte contenant la liste des tickets.

## Technologies utilisées
- **Langage** : Python
- **Stockage des données** : JSON pour les tickets, TXT pour l’exportation

## Installation
1. Installez Python 3.x sur votre ordinateur.
2. Téléchargez les fichiers du projet dans un dossier.
3. Lancez le programme avec la commande suivante dans le terminal :
   ```bash
   python gestion_tickets.py
