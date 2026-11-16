# Contribuer

## Installation

```bash
python -m venv .venv
# Windows : .venv\Scripts\Activate.ps1   |   Linux/Mac : source .venv/bin/activate
pip install -e ".[dev]"
```

## Conventions

- Branches : `feat/...`, `fix/...`, `docs/...`
- Commits : messages courts à l'impératif (`feat: ajoute le reviewer`)
- Code : type hints, un agent par fichier, sorties Pydantic
- Noms du domaine en français (`competences_requises`), code technique en anglais

## Avant d'ouvrir une pull request

```bash
pytest
```

## Règles de confidentialité

- Ne jamais commiter de vrai CV, de clé API ou de fichier `.env`.
- Les exemples dans `data/samples/` doivent être fictifs.
