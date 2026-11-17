# Étape 3 — La boucle agent

## Objectif

L'agent atteint seul un objectif donné en langage naturel.

## Livrables

- Boucle agent avec le SDK Anthropic
- Garde-fous (actions, tokens, durée)
- Trace de chaque exécution
- Prompt système versionné
- CLI pour lancer une exploration

## Réussi quand

- Un objectif simple (se connecter et ajouter un produit au panier) réussit dans la grande majorité des runs
- Aucun run ne dépasse son budget
- Le coût moyen d'un run est connu

## À savoir expliquer

- Le cycle demande d'outil et résultat
- Pourquoi l'API ne garde pas l'historique (effet sur le coût)
- D'où vient le non-déterminisme

## Plan de tâches

À proposer au début de l'étape.

## Notes

_(Choukri)_
