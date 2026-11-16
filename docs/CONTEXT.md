# Contexte du projet

## Origine

Projet personnel réalisé dans le cadre d'une recherche d'alternance. Il sert à la fois d'outil réel et de **pièce de portfolio** démontrant l'orchestration d'agents LLM.

## Objectifs

1. Réduire le temps de préparation d'une candidature (analyse d'offre, lettre, entretien).
2. Garantir la **fidélité au CV** : aucune compétence ou expérience inventée.
3. Démontrer des pratiques d'ingénierie sérieuses : tests, évaluation, observabilité, CI, conteneurisation.

## Public visé

- Étudiants en recherche d'alternance.
- Recruteurs et enseignants qui consultent le dépôt (démo en 30 secondes).

## Hors périmètre (pour l'instant)

- Envoi automatique de candidatures.
- Scraping d'offres sur des sites tiers.
- Stockage de données personnelles côté serveur.

## Contraintes

| Contrainte | Conséquence |
|------------|-------------|
| Dépôt public | Uniquement de faux CV dans `data/samples/` |
| Coût des appels LLM | Tests avec faux LLM, évaluations sur échantillon réduit |
| Bibliothèques qui évoluent vite | Versions à figer et à vérifier dans la documentation officielle |
| Langue | Français d'abord, option FR/EN ensuite |

## Décisions de conception

| Décision | Raison |
|----------|--------|
| LangGraph pour l'orchestration | Boucles conditionnelles et branches parallèles explicites |
| Sorties structurées (Pydantic) | Données vérifiables entre agents, moins d'ambiguïté |
| Agent Reviewer dédié | Séparer la rédaction de la vérification de fidélité |
| Température 0 pour l'analyse | Résultats plus reproductibles |
| Maximum 2 tentatives Writer ↔ Reviewer | Éviter les boucles infinies et maîtriser le coût |

## Glossaire

- **Alternance** : formation en entreprise alternant périodes de cours et de travail.
- **Agent** : fonction du graphe qui appelle un LLM avec une tâche précise.
- **État partagé** : dictionnaire typé qui circule entre les agents.
- **Garde-fou** : vérification automatique empêchant une sortie incorrecte.
- **Éval** : mesure de qualité sur un jeu d'exemples avec résultats attendus.
