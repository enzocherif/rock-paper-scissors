# 🤖 Rock Paper Scissors - Bot intelligent (freeCodeCamp)

Ce projet est une solution au défi **Rock Paper Scissors** proposé dans le cadre du cursus *Machine Learning with Python* de [freeCodeCamp.org](https://www.freecodecamp.org/).

🎯 **Objectif** : Concevoir un bot capable de battre quatre adversaires automatisés (quincy, abbey, kris, mrugesh) à Pierre-Feuille-Ciseaux, avec un taux de victoire **supérieur à 60 %** contre chacun d’eux.

---

## 📚 Contexte pédagogique

Ce projet permet de :
- S'initier aux stratégies adaptatives
- Travailler sur la mémoire d'état dans une fonction pure
- Explorer des approches simples d’apprentissage par motif (type Markov)
- Tester des algorithmes contre des adversaires aux comportements variés

---

## 🚀 Fonctionnalités du bot

- 🧠 Stratégie Markov multi-niveaux (analyse des 4, 3, 2 derniers coups)
- 🔄 Adaptation dynamique en cas de baisse de performance
- 📊 Système de prédiction avec fallback sur les fréquences globales
- ⚔️ Capable de s'adapter à des adversaires cycliques, aléatoires ou réactifs

---

## 🧪 Résultats obtenus

| Bot       | Taux de victoire |
|-----------|------------------|
| Quincy    | 99 % ✅           |
| Abbey     | 63 % ✅           |
| Kris      | 65 % ✅           |
| Mrugesh   | 78 % ✅           |

> Tous les bots sont battus avec un taux supérieur à 60 % sur 1000 parties.

---

## ⚙️ Comment exécuter le projet

### 🔧 Prérequis
- Python 3 installé
- Environnement Gitpod ou local avec les fichiers fournis (`main.py`, `RPS_game.py`, `test_module.py`)

### ▶️ Lancer les tests

Dans le terminal, tape :

```bash
python main.py
