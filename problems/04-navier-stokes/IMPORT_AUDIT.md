# Audit d'import des travaux historiques Navier–Stokes

Date de l'audit : 2026-08-14.

## Périmètre et conclusion

Source auditée en lecture seule :
`D:\04_PROJECTS_PROTOTYPE\CODEX_DEV\millennium-open-problems\04-navier-stokes`.

L'inventaire contient 22 fichiers, 4 répertoires et 104 869 octets. Il n'y a
dans ce sous-arbre ni dépôt Git imbriqué, ni PDF, image, archive, environnement
virtuel ou sortie lourde. Les 80 783 octets qui ne sont pas des bytecodes Python
ont été lus. Les trois scripts ont été exécutés avec l'écriture de bytecode
désactivée ; ils terminent sans erreur sous Python 3.13.14, avec NumPy 2.4.6
pour la vérification FFT. Les deux fichiers JSON sont syntaxiquement valides.

La migration ne doit **pas** copier le dossier `AUDIT_AOUT_2026` en bloc. Deux
scripts exacts sont importables sous statut conservateur `COMPUTATION_ONLY` ;
le reste doit être transformé, reproduit, re-sourcé ou exclu.

| Classe primaire | Nombre |
|---|---:|
| Stable et importable | 2 |
| Utile mais à réviser | 12 |
| Expérience à reproduire | 3 |
| Obsolète ou réfuté | 2 |
| Artefact généré à exclure | 2 |
| Résultat insuffisamment sourcé | 1 |
| **Total** | **22** |

## Dépendance au socle local

L'audit a été produit sur la branche
`codex/millennium-forge/navier-stokes-state-of-art`, au commit
`58aa8b316ebe3f5d7675dede6f18d37d0b844a30` (`feat: add autonomous research
lab core`). Ce commit est identique à la branche locale
`codex/millennium-forge/bootstrap-lab`, mais n'est pas ancêtre de la branche
locale `main`, positionnée sur
`05a83bab7a255f602f7dd96a84e1b91b01f442fb`. Aucune référence locale
`origin/main` n'était disponible au moment de l'audit : l'état publié ou fusionné
du socle ne peut donc pas être conclu depuis les références locales.

Les recommandations ci-dessous dépendent du schéma et des scripts du socle
local non fusionné. Elles ne demandent aucune réécriture d'historique. Le dossier
historique lui-même n'a pas de racine Git détectable ; auteur, commit d'origine
et chronologie ne peuvent pas être certifiés par son historique.

## Critères d'import

Un fichier est classé **stable et importable** seulement si son objet est borné,
compréhensible sans mémoire de conversation, exécutable localement, sans sortie
lourde, et si son empreinte a été contrôlée. L'import restera conditionné à :

1. une destination conforme à l'architecture Forge ;
2. une commande de reproduction et un environnement épinglé ;
3. une affirmation JSON conforme au schéma, au plus `COMPUTATION_ONLY` pour
   les dérivations produites par IA ;
4. une passe contradictoire ou réplication indépendante avant toute promotion ;
5. la validation complète du dépôt.

**Utile mais à réviser** signifie que le contenu peut servir de brouillon, pas
de source de vérité. **Expérience à reproduire** exige une nouvelle exécution et
une sortie déterministe adressée par contenu. **Insuffisamment sourcé** interdit
de transformer le texte en affirmations canoniques avant audit des sources.

## Stable et importable

| Fichier historique | Octets | SHA-256 | Recommandation |
|---|---:|---|---|
| `AUDIT_AOUT_2026/EXPERIENCES/test_viscosity_gate.py` | 4 266 | `201cc2e97cb6ec35618019512fc6e9225459034e1bd6c65ac67165e5be08fb0a` | Importer le calcul rationnel, sans le présenter comme une simulation PDE. Ajouter une commande de reproduction, des tests unitaires et une affirmation `COMPUTATION_ONLY`. Re-vérifier séparément les exposants attribués aux sources P1/P2. |
| `AUDIT_AOUT_2026/EXPERIENCES/test_triade_phase.py` | 8 302 | `a02b6959a5c00dbb248864ccd43ba55336769869d83bc73fd21d05ad4419e493` | Importer comme certificat algébrique fini de `TRI-PHASE-1`, avec convention de Fourier explicite. Le contre-exemple reste `COMPUTATION_ONLY` et non `PAPER_PROOF` tant qu'une revue indépendante n'a pas contrôlé le raccord entre code et énoncé. |

Les deux scripts ont été reproduits pendant cet audit. Leur succès établit
seulement les assertions testées par le programme, pas leur nouveauté ni une
implication vers la régularité globale.

## Utile mais à réviser

| Fichier historique | Octets | SHA-256 | Risque et recommandation |
|---|---:|---|---|
| `PROGRAMME_DE_RECHERCHE.md` | 4 629 | `833f9bcf65c04d2835a187371bec298a220f19048ecd1ca35901c4cbd031868f` | Bonne taxonomie de verrous, mais aucun identifiant d'affirmation ni source. Extraire les axes dans `RESEARCH_MAP.md`, avec lemme minimal, test d'abandon, dépendances et score actualisés. |
| `AUDIT_AOUT_2026/CADRE_CLAY.md` | 2 919 | `48f8f983f2c8afd4889f6f0476b218240ef15fa5bca19e6ead3b4d6c0b227fa6` | Cadrage utile de l'assertion (A), de la pression et des échelles, mais pas une reproduction complète des cas officiels. Repartir du PDF CMI et couvrir fidèlement (A)–(D), espaces, force et critères positif/négatif dans `FORMULATION_CLAY.md`. |
| `AUDIT_AOUT_2026/SOURCES_PRIMAIRES.md` | 10 303 | `1aff6ae610786cf57f5f19ec474abddef2bf595732b4fb811d54913b20ecdf9d` | Audit thématique utile, mais les versions, absences de supplément et annonces 2026 doivent être re-vérifiées à la date de migration. Scinder les métadonnées dans `sources.json` et l'analyse dans `source-audit.md`; ajouter pages/théorèmes et identifiants de version. |
| `AUDIT_AOUT_2026/REGISTRE_AFFIRMATIONS.md` | 4 833 | `0ee79794de1c216512b8c09bb8d5bb3a1648eef862f857db2a2fab572cc9f7d9` | Les statuts `ÉTABLI`, `PRÉPUBLICATION`, `HEURISTIQUE` et `CONDITIONNEL` ne sont pas ceux de Forge, et le fichier invoque un `METHODOLOGIE.md` hors sous-arbre. Transformer affirmation par affirmation : sources auditées vers `SOURCE_VERIFIED`, calculs vers `COMPUTATION_ONLY`, conjectures vers `SPECULATION`, contre-exemples vers `REFUTED`. Ne pas convertir automatiquement `ÉTABLI` en `PAPER_PROOF`. |
| `AUDIT_AOUT_2026/GRAPHE_CRITERES.md` | 3 289 | `2b0f7b013d14d52bd0d26910fdf9220881c0f65f7a3514860dc6e64b2e5ea8da` | Bonne amorce logique, mais les nœuds ne sont pas tous des IDs Forge et les arêtes n'ont ni source ni statut canonique. Réécrire dans `proof-graphs/navier-stokes/dependencies.md`, en distinguant classique, conditionnel, heuristique, numérique, contesté et manquant. |
| `AUDIT_AOUT_2026/JOURNAL_SUPERCRITIQUE.md` | 3 539 | `3672270c4c6a035c4edbf658515250f53bc06d3f5e08e46988a0f0a4e57d778b` | Contient des contre-profils et lois d'échelle utiles. Extraire chaque entrée avec sa convention de domaine et sa dépendance au lemme correspondant ; conserver les limites sur intermittence et multi-échelles. |
| `AUDIT_AOUT_2026/QUESTIONS_OUVERTES.md` | 2 801 | `108f8334616cf8b051c295721e28e19797e75571e8eae4cf65e50ab521537f4a` | Scores et pivot utiles, mais le premier classement est déjà dépassé par le cycle 0002. Importer les deux instantanés comme historique, puis reconstruire une file active dans `RESEARCH_MAP.md`. |
| `AUDIT_AOUT_2026/JOURNAL_EXPERIENCES.md` | 3 403 | `8236d2d6c1f48d13289bd660931ba7631a5f6f18fb5f5dfe598ae6db4dfd1b33` | Métadonnées riches et empreintes cohérentes, mais pas de fichier d'environnement épinglé ni de générateur commun des résultats. Conserver comme provenance historique et recréer un README par expérience. |
| `AUDIT_AOUT_2026/LEMME_VISCOSITE_AUTO_SIMILAIRE.md` | 3 336 | `aa05835cd3d8a80d970d3c1fbab73739141eef0a4212601dd9d8a6566aad7036` | Dérivation d'échelle cohérente et testable, mais le statut historique « DÉMONTRÉ » est incompatible avec la gouvernance sans revue indépendante. Importer comme note de dérivation liée au script exact, statut initial `COMPUTATION_ONLY`; faire auditer la convention d'exposant de chaque modèle source. |
| `AUDIT_AOUT_2026/LEMME_PHASE_TRIADIQUE.md` | 3 305 | `16a8a509aa266eb1eb4229867d82425d87390d6813b0060c5ceca3fc08af2cd0` | Contre-énoncé précis, support fini et limites explicites. Importer après revue indépendante des normalisations de Parseval, de la coupure `|k|<=N` et du signe du flux ; ne pas lui attribuer `PAPER_PROOF`. |
| `AUDIT_AOUT_2026/CYCLES/CYCLE_0001.md` | 2 743 | `63037a161313e924d6c3024ad7925211c66e805c589ece03306dea0e1f5f313d` | Bon journal de décision et d'attaque, sans provenance modèle/run ni commit historique. Importer comme checkpoint hérité, explicitement non canonique, et relier VAS-1 aux sources re-vérifiées. |
| `AUDIT_AOUT_2026/CYCLES/CYCLE_0002.md` | 3 261 | `0880d030f3f08fd56ccf60caaa115559883a73f3c9166b83d77d2f75681631a1` | Bon journal négatif sur la déplétion signée, mais même manque de provenance Git/modèle. Importer comme checkpoint hérité après rattachement aux scripts et à une affirmation `REFUTED` revue. |

## Expériences à reproduire

| Fichier historique | Octets | SHA-256 | Risque et protocole requis |
|---|---:|---|---|
| `AUDIT_AOUT_2026/EXPERIENCES/verify_triade_fft.py` | 3 774 | `5d97193862abfe1b1c837778720af2324c51e3984b2e199e673d330df1ca249e` | La passe binary64 réussit, mais NumPy n'est pas épinglé et l'absence d'aliasing n'est pas testée automatiquement. Reproduire dans un environnement verrouillé, ajouter au moins un second schéma/convention et enregistrer la sortie adressée par contenu. |
| `AUDIT_AOUT_2026/EXPERIENCES/resultat_viscosity_gate.json` | 1 455 | `c4f1bbc4da098b81e85069ffa1afda40bd410ef1a4653d8b21b84cbdf5e0cee8` | JSON valide et empreinte du script cohérente, mais ce fichier enrichi n'est pas la sortie byte-for-byte produite par le script actuel. Créer un générateur déterministe ou traiter le fichier comme manifeste saisi manuellement. |
| `AUDIT_AOUT_2026/EXPERIENCES/resultat_triade_phase.json` | 1 765 | `6c6a395ee06ae0fef43e9a66ca45dcf80b09425e0404e1df36a86dfc1a0e7aff` | JSON valide et empreintes internes cohérentes, mais il agrège manuellement deux programmes et n'est régénéré par aucun des deux. Ajouter un orchestrateur déterministe puis reproduire avant import de la sortie. |

## Obsolète ou réfuté

| Fichier historique | Octets | SHA-256 | Motif |
|---|---:|---|---|
| `PROMPT_CONVERSATION.md` | 4 064 | `c77cbda35b2857e2b1edf9483c05e87017b36ee6976fabda46e3912f5c7899ad` | Prompt autonome remplacé par `AGENTS.md`, `agents/PROTOCOL_AUTONOME.md` et `agents/missions/navier-stokes.md`. Ne pas importer ; conserver seulement cette empreinte de provenance. |
| `AUDIT_AOUT_2026/README.md` | 1 325 | `9b56374426197f18c388757a821545922dcef795ef1072f7ad8cf53dc536076f` | Index d'une architecture historique qui ne doit pas devenir la source de vérité. Ses liens et sa politique append-only sont remplacés par l'architecture et la gouvernance Forge. |

La proposition réfutée `|Pi_N| = o(N E^{3/2})` n'est pas un fichier à
supprimer : son contre-exemple doit être conservé dans le registre Forge des
échecs. La présente classe « obsolète ou réfuté » ne vise ici que les deux
conteneurs remplacés, pas les résultats négatifs qu'ils référencent.

## Artefacts générés à exclure

| Fichier historique | Octets | SHA-256 | Motif |
|---|---:|---|---|
| `AUDIT_AOUT_2026/EXPERIENCES/__pycache__/test_triade_phase.cpython-313.pyc` | 17 841 | `178bb0ad41a4307a76a2aea690ed0d69f4c1f19e2e69daef59bc03e912ec5f17` | Bytecode CPython 3.13 dérivé, non portable et reconstructible. Exclure et couvrir `__pycache__/`/`*.pyc` par `.gitignore`. |
| `AUDIT_AOUT_2026/EXPERIENCES/__pycache__/verify_triade_fft.cpython-313.pyc` | 6 245 | `6722d0841a356118cc5fa6a8c27142ceb34a3957efdf9e213e1ff0b4ae9666ac` | Même motif ; ne jamais importer. |

## Résultat insuffisamment sourcé

| Fichier historique | Octets | SHA-256 | Lacune et recommandation |
|---|---:|---|---|
| `ETAT_DE_L_ART.md` | 7 471 | `5188be4b699ca1003f7411f474e0fec435be7652ba2537e22e00984f144cb276` | Synthèse utile pour découvrir des axes, mais plusieurs affirmations générales n'ont ni article exact ni version, et les « manuscrits 2025–2026 » ne sont pas identifiés. Ne pas l'importer comme état de l'art canonique. Refaire la recherche primaire, puis citer chaque résultat avec domaine, notion de solution, hypothèses, constantes et version. |

## Risques transversaux

- **Provenance absente** : aucun historique Git n'est disponible pour le dossier
  source ; les dates de fichiers ne remplacent pas des commits.
- **Statuts incompatibles** : `ÉTABLI` ou `DÉMONTRÉ` ne se convertissent pas en
  `PAPER_PROOF`. Les deux lemmes nouveaux proviennent d'une campagne IA et
  commencent au plus à `COMPUTATION_ONLY`.
- **Veille temporelle** : les affirmations « aucune v2 visible » et « aucun code
  public » datées du 2026-08-14 doivent être revérifiées au moment de l'import.
- **Sorties non déterministes au niveau fichier** : les JSON sont cohérents avec
  les journaux, mais ne sont pas produits tels quels par les scripts.
- **Raccord Clay** : VAS-1 exclut seulement un transfert mono-échelle ;
  TRI-PHASE-1 réfute seulement une borne instantanée dépendant de l'énergie.
  Aucun des deux ne constitue un résultat de régularité ou de blow-up.
- **Domaine** : la triade vit sur le tore ; son raccord à `R^3` n'est pas fourni.
- **Dépendance manquante** : le registre historique invoque un
  `METHODOLOGIE.md` qui n'appartient pas au sous-arbre audité.

## Commandes de contrôle utilisées

Les lectures, empreintes et exécutions ci-dessous n'ont produit aucune écriture
dans la source historique :

```powershell
$source = 'D:\04_PROJECTS_PROTOTYPE\CODEX_DEV\millennium-open-problems\04-navier-stokes'
Get-ChildItem -LiteralPath $source -Recurse -Force -File
Get-ChildItem -LiteralPath $source -Recurse -Force -File |
  ForEach-Object { Get-FileHash -Algorithm SHA256 -LiteralPath $_.FullName }

$env:PYTHONDONTWRITEBYTECODE = '1'
python -B "$source\AUDIT_AOUT_2026\EXPERIENCES\test_viscosity_gate.py"
python -B "$source\AUDIT_AOUT_2026\EXPERIENCES\test_triade_phase.py"
python -B "$source\AUDIT_AOUT_2026\EXPERIENCES\verify_triade_fft.py"
python -m json.tool "$source\AUDIT_AOUT_2026\EXPERIENCES\resultat_viscosity_gate.json"
python -m json.tool "$source\AUDIT_AOUT_2026\EXPERIENCES\resultat_triade_phase.json"
```

Les empreintes de tous les fichiers historiques étaient identiques avant et
après ces contrôles.
