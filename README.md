# poem_generator
```
# Importation des modules nécessaires
import random
import nltk
from nltk.corpus import cmudict
from nltk.corpus import words

# Téléchargement des données linguistiques nécessaires
nltk.download('cmudict')
nltk.download('words')

# Fonction pour trouver des mots qui riment avec un mot donné
def find_rhyme(word):
    pronouncing = cmudict.dict()
    if word.lower() in pronouncing:
        # Obtention de la prononciation du mot
        word_pronunciation = pronouncing[word.lower()][0]
        # Recherche de mots qui riment avec le mot donné
        rhyming_words = [w for w, pron in pronouncing.items() if pron[-2:] == word_pronunciation[-2:]]
        return rhyming_words
    else:
        # Retourne le mot original s'il n'y a pas de prononciation trouvée
        return [word]

# Fonction pour générer une ligne de poème avec rime
def generate_line_with_rhyme(words_database):
    # Détermination de la longueur de la ligne de manière aléatoire
    line_length = random.randint(3, 8)
    line = ""
    for _ in range(line_length):
        # Choix aléatoire d'une catégorie de mots
        word_category = random.choice(list(words_database.keys()))
        # Choix aléatoire d'un mot de la catégorie
        word = random.choice(words_database[word_category])
        line += word + " "
    # Obtention des mots qui riment avec le dernier mot de la ligne
    last_word = line.split()[-1].lower()
    rhyming_words = find_rhyme(last_word)
    rhyming_word = random.choice(rhyming_words)
    # Retourne la ligne de poème avec le dernier mot rime
    return line.strip().capitalize() + " " + rhyming_word.capitalize()

# Fonction pour générer un poème libre avec rimes
def generate_free_verse_with_features(words_database, lines=10):
    poem = ""
    for _ in range(lines):
        # Génération de chaque ligne du poème
        line = generate_line_with_rhyme(words_database)
        poem += line + "\n"
    return poem

# Exemple d'utilisation avec une base de données de mots
words_database = {
    "adjective": ["beautiful", "mysterious", "gentle"],
    "noun": ["moon", "forest", "whisper"],
    "verb": ["dances", "echoes", "reveals"]
}

# Génération d'un poème libre avec rimes
poem_result = generate_free_verse_with_features(words_database, lines=10)
# Affichage du résultat
print(poem_result)

```
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

# Réalisé par :
Saddedin Saleh
EL GUEZDI Mohamed Zinelabidine