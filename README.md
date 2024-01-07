# poem_generator
```
  import random
  import nltk
  from nltk.corpus import cmudict
  from nltk.corpus import words
  
  nltk.download('cmudict')
  nltk.download('words')
  
  def find_rhyme(word):
      pronouncing = cmudict.dict()
      if word.lower() in pronouncing:
          word_pronunciation = pronouncing[word.lower()][0]
          rhyming_words = [w for w, pron in pronouncing.items() if pron[-2:] == word_pronunciation[-2:]]
          return rhyming_words
      else:
          return [word]
  
  def generate_line_with_rhyme(words_database):
      line_length = random.randint(3, 8)
      line = ""
      for _ in range(line_length):
          word_category = random.choice(list(words_database.keys()))
          word = random.choice(words_database[word_category])
          line += word + " "
      last_word = line.split()[-1].lower()
      rhyming_words = find_rhyme(last_word)
      rhyming_word = random.choice(rhyming_words)
      return line.strip().capitalize() + " " + rhyming_word.capitalize()
  
  def generate_free_verse_with_features(words_database, lines=10):
      poem = ""
      for _ in range(lines):
          line = generate_line_with_rhyme(words_database)
          poem += line + "\n"
      return poem
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