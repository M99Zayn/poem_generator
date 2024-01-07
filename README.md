# poem_generator
Ce script Python exploite le module NLTK pour rechercher des rimes et élaborer un poème libre. Voici une analyse détaillée de ses composants :

## Importation des modules : 
    Cette étape initiale implique l'intégration des modules nécessaires, notamment NLTK, qui joue un rôle central dans le traitement linguistique.

## Téléchargement des données linguistiques : 
    Un chargement préalable des données linguistiques essentielles à NLTK est effectué. Cela garantit que le module dispose des ressources nécessaires pour fonctionner efficacement.

## Fonction find_rhyme : 
    Cette fonction utilise le dictionnaire de prononciation CMU (Carnegie Mellon University) pour identifier des mots en rime avec un terme spécifique. Cela enrichit la capacité du script à créer des lignes poétiques cohérentes.

## Fonction generate_line_with_rhyme : 
    La création de lignes poétiques se réalise ici en sélectionnant aléatoirement des mots provenant de différentes catégories de la words_database. La particularité de cette fonction réside dans la garantie que le dernier mot de chaque ligne rime avec son prédécesseur.

## Fonction generate_free_verse_with_features : 
    Cette fonction s'appuie sur la précédente pour générer un poème libre. Elle permet de spécifier le nombre désiré de lignes, offrant ainsi une flexibilité dans la création poétique.

## Exemple d'utilisation : 
    L'exemple pratique fourni met en lumière le fonctionnement du script. Une base de données de mots est présentée à titre illustratif, et le résultat concret prend la forme d'un poème généré qui est ensuite affiché. Ce procédé démontre l'efficacité du script dans un contexte d'utilisation réelle.