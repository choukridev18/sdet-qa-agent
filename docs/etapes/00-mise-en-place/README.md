# Étape 0 — Mise en place

## Objectif

Un environnement prêt et un premier appel à l'API qui fonctionne.

## Livrables

- Un dépôt GitHub public
- Les outils installés
- La clé API configurée de façon sûre, avec une limite de dépenses
- Un petit script qui interroge le modèle et affiche les tokens consommés
- Lint, typage et une CI minimale

## Réussi quand

- La CI est verte
- Aucun secret n'est dans l'historique Git

## À savoir expliquer

- Ce qu'est un token
- Comment se calcule le coût d'un appel

## Plan de tâches

À proposer et ajuster avec Choukri au démarrage de l'étape. Pistes :

1. Python + venv + Git local (déjà initialisé) + `.env.example`
2. Compte Anthropic, clé dans `.env`, plafond de dépenses
3. Script minimal d'appel API + affichage des tokens
4. Ruff / mypy + GitHub Actions minimale
5. Dépôt GitHub public, premier push sans secrets

## Notes

_(Choukri)_
