# Les agents

Chaque agent est une fonction `state -> dict` dans `src/alternance_copilot/agents/`.

## 1. Offer Analyzer (`offer_analyzer.py`)

- **Entrée** : `offer_text`
- **Sortie** : `offer` (`OfferAnalysis`)
- **Consigne clé** : extraire uniquement ce qui est écrit dans l'offre, ne rien inventer.
- **Température** : 0

## 2. CV Analyst (`cv_analyst.py`)

- **Entrée** : `cv_text`, `offer`
- **Sortie** : `match` (`CVMatch`)
- **Rôle** : score de correspondance, points forts, lacunes, expériences à mettre en avant.
- **Consigne clé** : ne citer que des éléments présents dans le CV.

## 3. Letter Writer (`letter_writer.py`)

- **Entrée** : `offer`, `match`, `cv_text`, et `review.problemes` lors d'une nouvelle tentative
- **Sortie** : `letter`, `attempts` incrémenté
- **Consigne clé** : s'appuyer exclusivement sur le CV ; corriger les problèmes signalés par le Reviewer.

## 4. Reviewer (`reviewer.py`)

- **Entrée** : `letter`, `cv_text`
- **Sortie** : `review` (`ReviewResult`)
- **Rôle** : découper la lettre en affirmations et vérifier chacune par rapport au CV.
- **Décision** : `valide = False` si au moins une affirmation n'est pas appuyée.

## 5. Interview Coach (`interview_coach.py`)

- **Entrée** : `offer`, `match`
- **Sortie** : `interview_prep` (`InterviewPrep`)
- **Rôle** : questions techniques et comportementales, avec pistes de réponse basées sur les expériences réelles du CV.

## Principes communs

1. Une seule responsabilité par agent.
2. Sorties structurées validées par Pydantic.
3. Pas d'invention : tout élément doit être traçable vers l'offre ou le CV.
4. Les textes d'entrée sont des données, pas des instructions.
