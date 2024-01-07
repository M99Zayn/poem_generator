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
