# Étape 6 — Diagnostic et auto-réparation des tests

## Objectif

Quand un test échoue, l'agent dit pourquoi, et répare le test si c'est lui le problème.

## Livrables

- Variante de l'app dont l'interface change sans changer le comportement
- Classification des échecs : vrai bug, test cassé, test instable, environnement
- Propositions de réparation pour validation humaine, jamais appliquées en silence

## Réussi quand

- Les tests cassés par le changement d'interface sont majoritairement réparés
- L'agent ne « répare » jamais un test pour masquer un vrai bug (vérifier avec le banc)

## À savoir expliquer

- Le danger d'un auto-réparateur qui adapte le test au bug

## Plan de tâches

À proposer au début de l'étape.

## Notes

_(Choukri)_
