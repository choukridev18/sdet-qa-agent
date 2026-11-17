# Notions à retravailler

Ajouter une ligne quand un quiz ou un blocage montre que ce n'est pas solide. Barrer quand c'est repris et tenu.

- Clé API (secret / Auth Postman) ≠ token LLM (unité de texte facturée). À revoir quand le script affichera `input_tokens` / `output_tokens`.
- Le venv isole **ce** projet (binaire + paquets dans `.venv`). Il ne garantit pas la même version de Python chez un collègue ; ça viendra d’un fichier de dépendances.
- `.env.example` = noms (GitHub) ; `cp` vers `.env` = même liste en local, secrets seulement là. À revoir plus tard.
