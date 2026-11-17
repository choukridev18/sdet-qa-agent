# Étape 5 — Le banc d'essai

C'est l'étape qui fait la différence. Version minimale présentable à la fin.

## Objectif

Prouver avec des chiffres ce que vaut l'agent.

## Livrables

- Une trentaine de bugs activables, types variés (voir annexe 6.1 du brief)
- Preuve que chaque bug est observable par au moins un test manuel
- Mesure (a) : l'agent explore chaque version buggée
- Mesure (b) : la suite générée et figée contre chaque version buggée
- Runs de contrôle sur l'app saine
- Résultats enregistrés, graphiques, courte analyse des ratés

## Réussi quand

- On peut annoncer taux de détection, fausses alertes, coût et durée
- Plusieurs répétitions pour le hasard
- Chiffres reproductibles

## À savoir expliquer

- Mutation testing
- Rappel vs précision
- Pourquoi des runs de contrôle et des répétitions
- Limites (ex. LLM-as-judge pour relier un bug signalé au bug injecté)

## Attention

Ne pas régler le prompt en regardant tous les bugs du banc. Garder une partie « cachée ».

## Plan de tâches

À proposer au début de l'étape.

## Notes

_(Choukri)_
