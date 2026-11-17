# Journal de séances

## 2026-11-16 — Espace de travail

- **Fait :** copie du brief WhatsApp ; création de la doc par étape, du suivi, des règles Cursor, du skill mentor et des commandes de séance. Pas de code applicatif.
- **Appris :** —
- **Difficultés :** —
- **Prochaine étape :** Phase 0 après calibration.

## 2026-11-16 — Phase 0, environnement local

- **Fait :** calibration (macOS, Python 3.14.0, pas Docker, pas d’API IA en Python). Venv `.venv` créé et activé. `.env.example` (`ANTHROPIC_API_KEY=`) + copie vers `.env` vide. Git ignore bien `.env`.
- **Appris :** venv = isoler le projet (Python de `.venv`, pas celui du Mac). `.venv` = nom choisi ; le `.` cache le dossier, ça n’est pas le gitignore. U = Untracked. Clé API (Auth / Postman) ≠ token LLM (facturation). `docs.claude.com` = doc ; `platform.claude.com` = compte API.
- **Difficultés :** pause au moment de créer le compte API et d’ajouter un moyen de paiement. Reprise plus tard.
- **Prochaine étape :** `platform.claude.com` → paiement → workspace (pas Default) → plafond → clé **uniquement** dans `.env` (ne jamais la coller dans le chat).
