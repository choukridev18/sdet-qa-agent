# Décisions

Journal des choix techniques. Une entrée par décision. Ne pas modifier le brief.

## Format

```
### YYYY-MM-DD — Titre
- Décision :
- Pourquoi :
- Alternatives écartées :
- Note entretien :
```

## Entrées

### 2026-11-16 — Nom du venv et secrets

- Décision : dossier `.venv` ; secrets dans `.env` ; modèle commité `.env.example` avec `ANTHROPIC_API_KEY=` vide.
- Pourquoi : convention (dossier caché, déjà dans `.gitignore`) ; la clé ne doit jamais aller sur GitHub.
- Alternatives écartées : `venv` / `env` (valides, moins conventionnels ici).
- Note entretien : les secrets hors Git dès le premier commit ; plafond de dépenses dans la console, pas seulement dans le code.

### 2026-11-17 — Brief mentor hors GitHub recruteur

- Décision : `docs/projet-sdet-brief.md` et `docs/suivi/mon-build.md` restent sur le Mac, pas sur le dépôt public.
- Pourquoi : le recruteur voit le produit, pas le mode d’emploi du mentor ni les notes perso.
- Alternatives écartées : laisser le brief public (transparent mais trop « fiche d’apprentissage »).
- Note entretien : un portfolio montre README, code, chiffres ; le brief pédagogique n’est pas la vitrine.
- À faire avant le premier push : nettoyer l’historique, le brief est encore dans le premier commit local.

