# Étape 7 — Intégration continue

## Objectif

L'agent tourne automatiquement sur chaque pull request de l'application.

## Livrables

- CI qui lance l'app, exécute la suite, demande le diagnostic des échecs
- Rapport en commentaire de PR, traces en pièces jointes
- Plafond de coût par exécution
- Cas où la clé API n'est pas disponible géré proprement

## Réussi quand

- Une PR qui introduit un bug reçoit un commentaire qui le signale
- Une PR qui change seulement l'interface reçoit une proposition de réparation

## À savoir expliquer

- Comment limiter le coût en CI
- Que faire si le secret n'est pas disponible

## Plan de tâches

À proposer au début de l'étape.

## Notes

_(Choukri)_
