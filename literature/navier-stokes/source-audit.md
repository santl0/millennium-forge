# Audit des sources — Navier–Stokes incompressible 3D

Date de gel : **2026-08-14**. Registre machine : [`sources.json`](sources.json).
Les deltas postérieurs sont consignés sans réécrire ce gel dans
[`watch-log.md`](watch-log.md).

## Verdict exécutif

Le problème officiel demeure ouvert dans le corpus primaire contrôlé. Aucun résultat publié ou prépublié identifié ne fournit à la fois :

1. l'équation de Navier–Stokes incompressible standard en dimension trois ;
2. sur `R³` ou `T³`, sans bord ;
3. avec `ν>0` et la force correspondant à une alternative Clay ;
4. une donnée initiale `C∞`, solénoïdale et admissible par Clay ;
5. soit une solution classique globale avec les bornes demandées, soit une rupture à temps fini de sa continuation classique ;
6. un argument analytique publié ou un calcul assisté entièrement reproductible avec passage certifié au continuum.

Les progrès vérifiés se répartissent en quatre familles : existence faible globale, critères critiques conditionnels, exclusions de scénarios structurés, et résultats de non-unicité dans des classes ou avec des données différentes de celles de Clay. La veille 2025–2026 ajoute des résultats importants sur la non-unicité à donnée critique singulière, un blow-up instantané **par la droite** dans une classe faible non énergétique, une annonce de CAP pour la non-unicité de Leray–Hopf à donnée singulière et de nouvelles réductions Type II. Aucun n'est un raccord au problème Clay.

`SOURCE_VERIFIED` est employé ici au sens bibliographique : la source primaire et son énoncé ont été contrôlés. Cela ne signifie pas que sa preuve a été reproduite. Les prépublications récentes restent des prépublications même lorsque leur démonstration se présente comme rigoureuse.

## Cadre invariant utilisé pendant l'audit

L'équation de référence est

```text
∂t u + (u·∇)u = -∇p + νΔu + f,
div u = 0,
u(0) = u₀,
```

avec `ν>0`. Sur `R³`, la remise à l'échelle parabolique est

```text
uλ(x,t) = λ u(λx, λ²t),
pλ(x,t) = λ² p(λx, λ²t),
fλ(x,t) = λ³ f(λx, λ²t).
```

Elle donne

```text
||uλ||Lq_t Lp_x = λ^(1-3/p-2/q) ||u||Lq_t Lp_x.
```

La ligne `2/q+3/p=1`, `L∞_tL³_x`, `Ḣ^{1/2}` et `BMO⁻¹` sont critiques. La norme `L²_x` se transforme comme `λ^{-1/2}` et son carré comme `λ^{-1}` : l'énergie est supercritique pour le contrôle des petites échelles. Toute affirmation de fermeture obtenue seulement depuis

```text
u ∈ L∞_tL²_x ∩ L²_tḢ¹_x
```

doit donc exhiber un gain structurel supplémentaire.

La pression n'est jamais traitée comme une variable locale indépendante. Sans bord et à une fonction du temps près,

```text
p = Σi,j Ri Rj(ui uj),
```

et la projection de Leray est `P = I - ∇Δ⁻¹ div`. Les arguments localisés doivent conserver le terme harmonique ou de pression lointaine correspondant.

## Notions de solution : séparations obligatoires

- **Faible distributionnelle** : satisfait l'équation testée; cette classe peut ne satisfaire ni inégalité d'énergie ni contrôle `L²_tH¹_x`.
- **Leray–Hopf** : typiquement `u∈L∞_loc L² ∩ L²_loc H¹`, continuité faible en temps, équation distributionnelle et inégalité d'énergie globale.
- **Faible adaptée / suitable** : ajoute l'inégalité locale d'énergie avec une pression suffisamment intégrable; c'est la classe de Caffarelli–Kohn–Nirenberg.
- **Forte** : régularité suffisante pour rendre l'équation forte et obtenir l'unicité faible–forte sur son intervalle d'existence.
- **Mild** : satisfait la formule de Duhamel du semi-groupe de Stokes; son sens dépend de l'espace fonctionnel choisi.
- **Classique / lisse** : dérivées classiques requises par l'énoncé; c'est la cible positive de Clay.
- **Dissipative** : terme non univoque dans la littérature; il faut donner la définition (inégalité d'énergie globale, locale, ou notion de Lions) avant tout transfert.

Une solution peut être lisse pour chaque `t>0` tout en ayant une trace initiale singulière. Cela ne la transforme pas en solution Clay issue d'une donnée `C∞`.

La continuité forte à `t=0` d'une solution Leray–Hopf fixée ne fournit pas un
module fort uniforme pour une famille de données seulement bornée. Le cadre
trajectoriel de [Foias–Rosa–Temam 2013](https://doi.org/10.5802/aif.2836)
(`NS-SRC-0043`) donne `partial_t u in L^(4/3)_tV'` et la compacité dans une
topologie temporelle faible. Une famille initiale fortement précompacte permet
de récupérer une trace forte uniforme par projection finie et inégalité
d'énergie; les zooms de blow-up ne possèdent pas cette précompacité a priori.

## Matrice des résultats établis

| Bloc | Source primaire | Formulation et conclusion contrôlées | Maillon obtenu | Trou exact vers Clay |
|---|---|---|---|---|
| Énoncé | [Fefferman/CMI](https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf) (`NS-SRC-0001`) | `R³` et `T³`, `ν>0`, alternatives forcées/non forcées | cible normative | aucun résultat intermédiaire |
| Existence faible | [Leray 1934](https://doi.org/10.1007/BF02547354) (`0002`), [Hopf 1951](https://doi.org/10.1002/mana.3210040121) (`0003`) | solutions faibles globales d'énergie | existence pour tout temps | énergie supercritique; unicité et lissité absentes |
| Topologie temporelle Leray–Hopf | [Foias–Rosa–Temam 2013](https://doi.org/10.5802/aif.2836) (`0043`) | continuité faible `L²`, continuité forte initiale individuelle, dérivée dans `L^(4/3)V'` | compacité de trajectoire faible | aucun module critique fort uniforme pour des données seulement bornées |
| Régularité partielle | [Scheffer 1976](https://doi.org/10.2140/pjm.1976.66.535) (`0004`), [CKN 1982](https://doi.org/10.1002/cpa.3160350604) (`0005`), [Lin 1998](https://doi.org/10.1002/(SICI)1097-0312(199803)51:3%3C241::AID-CPA2%3E3.0.CO;2-A) (`0006`) | solutions adaptées; ensemble singulier parabolique très petit | critères epsilon-locaux et compacité | un point singulier reste possible; pression localisée non locale |
| Prodi–Serrin | [Prodi 1959](https://doi.org/10.1007/BF02410664) (`0007`), [Serrin 1962](https://doi.org/10.1007/BF00253344) (`0008`), [Ladyzhenskaya 1967](https://www.mathnet.ru/eng/znsl2228) (`0009`) | intégrabilité espace-temps supplémentaire implique unicité/régularité | critère de prolongement | aucune borne a priori de la norme conditionnelle depuis l'énergie |
| Endpoint `L³` | [Escauriaza–Seregin–Šverák 2003](https://doi.org/10.1070/RM2003v058n02ABEH000609) (`0012`), [Seregin 2012](https://doi.org/10.1007/s00220-011-1391-x) (`0013`) | la borne `L∞_tL³_x` exclut le blow-up; au blow-up `||u(t)||₃→∞` | quantité critique nécessaire | ne contrôle ni la croissance ni la concentration de `L³` |
| Petites données critiques | [Kato 1984](https://doi.org/10.1007/BF01174182) (`0010`), [Koch–Tataru 2001](https://math.berkeley.edu/~tataru/papers/nas.pdf) (`0011`) | globalité pour petite donnée dans `L³` ou `BMO⁻¹` | théorie critique robuste | le seuil de petitesse ne couvre pas une donnée lisse arbitrairement grande |
| Profils critiques | [Gallagher–Koch–Planchon 2013](https://arxiv.org/abs/1012.0145) (`0014`) | décomposition en profils pour le critère `L∞L³` | compacité modulo échelle/translation | il faut d'abord borner la quantité critique ou construire l'élément minimal |
| Solutions anciennes | [Koch–Nadirashvili–Seregin–Šverák 2009](https://arxiv.org/abs/0709.3599) (`0015`) | théorèmes de Liouville dans plusieurs sous-classes | cible de rigidité après zoom | aucun Liouville général pour les anciennes 3D admissibles |
| Self-similarité | [Nečas–Růžička–Šverák 1996](https://doi.org/10.1007/BF02551584) (`0016`), [Tsai 1998](https://doi.org/10.1007/s002050050099) (`0017`), [Chae 2007](https://doi.org/10.1007/s00208-007-0082-6) (`0018`), [Hou–Li 2007](https://doi.org/10.3934/dcds.2007.18.637) (`0019`) | exclusion de profils exacts ou asymptotiques sous intégrabilité/convergence | scénarios structurés éliminés | Type II, modulation, intermittence et multi-échelles restent ouverts |
| Auto-similarité forward | [Tsai 2014](https://arxiv.org/abs/1210.2783) (`0020`) | existence globale pour données discrètement self-similaires singulières | laboratoire de profils critiques | direction forward et donnée non lisse |
| Géométrie de vorticité | [Constantin–Fefferman 1993](https://doi.org/10.1512/iumj.1993.42.42034) (`0021`) | cohérence de direction déplète l'étirement | critère géométrique conditionnel | le module d'alignement n'est pas contrôlé par l'énergie |
| Axisymétrie | [Ukhovskii–Yudovich 1968](https://doi.org/10.1016/0021-8928(68)90147-0) (`0022`), [Chen–Strain–Tsai–Yau 2008](https://doi.org/10.1093/imrn/rnn016) (`0023`) | régularité sans swirl; taux/critères avec swirl | sous-cas invariants et contraintes près de l'axe | le swirl et les perturbations 3D réintroduisent le mécanisme critique |
| Cascade | [Dascaliuc–Grujić 2011](https://arxiv.org/abs/1101.2193) (`0024`) | flux positif comparable sur une plage d'échelles sous condition suffisante | transfert physique rigoureux | pas d'uniformité jusqu'à l'échelle zéro |
| Intermittence | [Cheskidov–Shvydkoy 2014](https://doi.org/10.1137/120876447) (`0026`) | dimension active Littlewood–Paley pour Euler/turbulence | dictionnaire multi-échelle | pas de borne NS a priori de la dimension active |
| Modèles voisins | [Tao 2016](https://arxiv.org/abs/1402.0290) (`0025`), [Tao 2009](https://arxiv.org/abs/0906.3070) (`0027`), [Biferale–Titi 2013](https://arxiv.org/abs/1303.1215) (`0028`) | blow-up d'une non-linéarité moyennée; globalité hyperdissipative ou hélicoïdale décimée | tests négatifs des méthodes génériques | projection/dissipation/triades différentes de NS standard |
| Intégration convexe | [Buckmaster–Vicol 2019](https://doi.org/10.4007/annals.2019.189.1.3) (`0029`) | non-unicité faible non forcée sur `T³` | flexibilité distributionnelle | classe non Leray–Hopf; ni blow-up classique ni défaut Clay |
| Non-unicité forcée | [Albritton–Brué–Colombo 2022](https://doi.org/10.4007/annals.2022.196.1.3) (`0030`) | deux solutions de Leray, même donnée nulle, force construite | non-unicité énergétique forcée | pas de limite uniforme supprimant la force |

### Lecture correcte de la chaîne connue

La cartographie bibliographique autorise la chaîne conditionnelle suivante :

```text
donnée lisse solénoïdale
  → solution classique locale unique
  → temps maximal T*
  → si T*<∞, perte de tout critère critique de prolongement applicable
  → en particulier ||u(t)||L³ → ∞ dans R³
  → sous normalisation et compacité suffisantes, extraction d'un objet limite ancien
  → il faudrait un théorème de Liouville adapté à cette classe limite
  → contradiction, donc régularité globale.
```

Les deux arêtes non disponibles sans hypothèse supplémentaire sont :

- **concentration → compacité non triviale** : l'énergie n'est pas critique, les translations/dilatations échappent, et la pression impose un contrôle lointain ;
- **solution ancienne admissible → trivialité** : les théorèmes de Liouville actuels couvrent des sous-classes (bornitude, symétrie, intégrabilité, auto-similarité), pas toutes les limites possibles.

Il est incorrect de remplacer la seconde arête par « les profils self-similaires sont exclus ». Une solution ancienne Type II, modulée ou multi-échelle n'est pas nécessairement self-similaire.

## Audit différentiel 2025–2026

### Résultats primaires directement sur Navier–Stokes standard

| Source | Statut au gel | Énoncé pertinent | Implication explicite vers Clay |
|---|---|---|---|
| [Coiculescu–Palasek, arXiv:2503.14699](https://arxiv.org/abs/2503.14699), DOI [10.1007/s00222-025-01396-z](https://doi.org/10.1007/s00222-025-01396-z) (`NS-SRC-0031`) | publié, version arXiv v2 du 2025-07-21 | deux solutions globales distinctes, lisses pour `t>0`, depuis une même grande donnée dans `BMO⁻¹` | la donnée initiale est au seuil critique et n'est pas `C∞`; **aucune implication** vers une alternative Clay |
| [Cheskidov–Dai–Palasek, arXiv:2511.09556v2](https://arxiv.org/abs/2511.09556) (`0032`) | prépublication, 2026-01-12 | pour toute donnée lisse périodique, construit une solution faible avec singularité Type I en `t→T*+`, lisse à chaque temps et hors de la classe énergétique près de `T*` | le blow-up conventionnel Clay est `t→T*−` sur la continuation classique; ici la branche classique jusqu'à `T*` reste lisse et l'énergie de la branche droite diverge : **pas un blow-up Clay** |
| [Hou–Wang–Yang, arXiv:2509.25116v2](https://arxiv.org/abs/2509.25116) et [code primaire](https://github.com/HouGroup2026/3d-navier-stokes-nonuniqueness) (`0033`) | prépublication, 2026-03-19; CAP revendiquée; code repéré mais non exécuté | annonce une infinité de solutions adaptées de Leray–Hopf non forcées sur `R³`, même donnée compacte `C∞(R³\{0})∩L^q`, `q<3`, lisses pour `t>0` | même si la CAP est reproduite, la donnée est singulière en zéro : **pas de contradiction** avec l'unicité/régularité pour donnée Clay lisse |
| [Feng–He–Wang 2026](https://doi.org/10.3934/dcdsb.2026048) (`0035`) | publié en ligne le 2026-03-06 | estimations quantitatives et taux nécessaires dans des espaces de Lorentz critiques `L^{3,q}`, `q<∞` | critère/taux conditionnels; **aucune borne globale** de la norme critique |
| [Chen–Galdi–Poggi–Schikorra, arXiv:2606.24733v1](https://arxiv.org/abs/2606.24733) (`0036`) | prépublication, 2026-06-23 | régularité intérieure de solutions distributionnelles sur la ligne Serrin, avec hypothèses relâchées | améliore l'étape « contrôle critique → régularité », mais pas « énergie → contrôle critique » |
| [Seregin, arXiv:2606.29468v1](https://arxiv.org/abs/2606.29468) (`0034`) | prépublication, 2026-06-28 | scénarios Type II locaux, zoom d'échelle Euler et théorèmes de Liouville conditionnels | réduction utile, mais **ni existence ni exclusion générale** d'un blow-up Type II |

Deux confusions doivent être activement empêchées :

1. « non-unicité de solutions faibles » n'implique pas « singularité de la solution classique maximale » ;
2. « donnée critique donnant des solutions lisses pour `t>0` » n'implique pas « donnée initiale lisse au sens Clay ».

### Programme 2025 de découverte de singularités instables assistée par IA

La source primaire contrôlée est [Wang et al., *Discovery of unstable singularities*, arXiv:2509.14185v1](https://arxiv.org/abs/2509.14185) (`NS-SRC-0039`). Elle traite plusieurs équations : modèle CCF 1D, IPM 2D, Euler 3D avec frontière et systèmes reliés. La chaîne de transfert vers Clay s'arrête au premier maillon :

```text
profil instable certifié/observé pour un modèle M
  ⇏ profil pour Navier–Stokes incompressible standard,
```

car `M` diffère au moins par la viscosité, la frontière, la dimension ou l'opérateur non local. Aucun lemme de conjugaison, perturbation uniforme ou continuation transformant ces profils en solution de Navier–Stokes 3D standard n'est fourni. Le résultat transférable est donc **méthodologique seulement** : recherche en variables renormalisées, haute précision, extraction d'un profil puis validation séparée. Cette méthode est un générateur de candidats, pas une preuve de blow-up Clay.

Test adverse reproductible minimal pour toute future tentative de transfert : écrire les deux opérateurs renormalisés sur le même espace, calculer leur différence sur le profil candidat, puis certifier une borne d'inverse pour le linéarisé de Navier–Stokes standard. Si le résidu n'est pas dans l'espace où cet inverse est borné, ou si la constante d'inverse diverge avec la troncature/le bord/la viscosité, le transfert échoue. Aucune telle donnée certifiée n'est présente dans la source auditée.

### Annonces de « résolution » mises en quarantaine

Des dépôts Zenodo/SSRN/Preprints.org de 2025–2026 revendiquant une résolution ont été découverts. Ils figurent seulement dans `watchlist` du JSON. Ils ne fondent aucune affirmation : ni publication évaluée, ni audit de quantificateurs, ni reproduction de constantes, ni validation du passage au continuum n'ont été établis. Leur présence dans la veille ne modifie pas le statut ouvert du problème.

Deux revendications arXiv de Rishad Shahmurov sont également isolées dans cette watchlist : [arXiv:2606.07869v1](https://arxiv.org/abs/2606.07869), soumis le 2026-06-05, revendique la régularité globale axisymétrique avec swirl; [arXiv:2605.09797v2](https://arxiv.org/abs/2605.09797), révisé le 2026-05-15, revendique une réduction du système 3D complet et la régularité globale. Seuls leurs métadonnées et résumés primaires ont été contrôlés. Les preuves, constantes, arguments de compacité et réductions n'ont pas été audités; leur statut est **unreviewed claim, aucune implication admise**.

## Calcul numérique et preuve assistée

Quatre niveaux sont distingués :

1. **indice numérique non certifié** : trajectoire flottante ou profil tronqué sans borne globale d'erreur ;
2. **calcul haute précision** : convergence empirique et résidus petits, mais sans inclusion mathématique ;
3. **preuve assistée par ordinateur** : réduction analytique à un problème borné, arithmétique rigoureuse, queues et erreurs de troncature incluses ;
4. **preuve analytique** : argument symbolique publié, éventuellement avec constantes explicites.

[Guillod–Šverák](https://arxiv.org/abs/1704.00560) (`NS-SRC-0037`) est un calcul non certifié de profils/bifurcations forward self-similaires à donnée singulière. [Hou 2023](https://doi.org/10.1007/s10208-022-09578-4) (`0038`) est une simulation adaptative haute résolution d'un scénario axisymétrique avec swirl dans un cylindre; la croissance observée et le régime presque self-similaire ne certifient pas un blow-up. Il manque notamment un résidu PDE intervalle, une borne de discrétisation uniforme, le contrôle certifié du bord et un passage à la limite.

À l'inverse, [van den Berg–Breden–Lessard–van Veen 2021](https://doi.org/10.1007/s00332-021-09695-4) (`0040`) valide des orbites périodiques particulières du Navier–Stokes forcé sur `T³` par Newton–Kantorovich et contrôle de queues. [Liu–Nakao–Oishi 2022](https://arxiv.org/abs/2101.03727) (`0041`) certifie localement des solutions stationnaires sur domaines bornés. Ces travaux établissent la faisabilité d'une CAP PDE, mais leur quantificateur reste « il existe une solution proche de ce candidat », non « toute donnée Clay reste régulière ».

La prépublication Hou–Wang–Yang (`0033`) est la seule source récente identifiée revendiquant une CAP d'un résultat de non-unicité Leray–Hopf non forcé. Son dépôt n'a pas été exécuté dans ce cycle. Avant promotion bibliographique, il faut au minimum : environnement épinglé, empreinte des entrées, reproduction bit-à-bit ou bornes intervalle équivalentes, vérification indépendante des résidus, des queues, de la divergence et des constantes de l'inverse fini-dimensionnel.

## Formalisation

Le dépôt primaire [iDNS-Lean4-Mathlib4](https://github.com/jcamlin/iDNS-Lean4-Mathlib4) (`NS-SRC-0042`) a été repéré. Son propre README décrit un socle Fourier incomplet, avec Sobolev, Galerkin, énergie, vorticité et le théorème principal encore planifiés; il mentionne au moins un axiome et un `sorry`. Il ne constitue pas une formalisation de Leray–Hopf ni du problème Clay.

L'audit formel séparé, détaillé dans
[`formal/navier-stokes/README.md`](../../formal/navier-stokes/README.md), a aussi
identifié : (i) deux encodages Lean de l'énoncé Clay dont les conclusions sont
laissées par `sorry`; (ii) `uda-lab/leray-hopf` v0.2.1, dont la CI épinglée
atteste une construction formelle de solutions faibles non forcées sur `T³` et
`R³`, avec des différences publiques par rapport à la formulation espace-temps
standard; et (iii) un squelette Coq conditionnel supposant les verrous
décisifs. Aucun de ces builds externes n'a été rejoué localement et aucun ne
prouve unicité, régularité globale ou breakdown Clay. Il est donc exact de
conserver zéro claim local `FORMALIZED` sur la résolution, mais inexact de dire
qu'aucune existence faible formelle n'a été repérée.

Aucune preuve complète et sans prémisse décisive d'un résultat Clay n'a été
vérifiée en Lean, Isabelle ou Coq pendant cette recherche. C'est un constat de
recherche finie, **pas une preuve d'absence**. La prochaine veille formelle doit
enregistrer l'URL, le commit, la version du prouveur, les axiomes imprimés et la
commande de compilation.

## Pertes structurelles observées

| Passage | Perte ou dépendance | Test adverse prioritaire |
|---|---|---|
| énergie → norme critique | une puissance d'échelle | familles concentrées `uλ`; vérifier toute constante prétendument uniforme en `λ` |
| estimation en vorticité | une dérivée dans `ω·∇u` | paquet de hautes fréquences divergence-free avec triades signées |
| localisation | pression lointaine et commutateurs de cutoff | déplacer une composante distante sans changer les données locales |
| Galerkin → continuum | compacité seulement faible du terme quadratique | profiler oscillations/concentrations; exiger convergence forte locale suffisante |
| domaine tronqué → `R³` | constante de Poincaré/Poisson et condition artificielle au bord | faire croître le rayon et suivre chaque constante |
| profil numérique → solution exacte | inverse du linéarisé, queues, résidu et noyaux de symétrie | validation intervalle avec phase fixée et borne d'inverse uniforme |
| exclusion self-similaire → absence de blow-up | hypothèse de convergence vers un profil | scénario modulé ou à deux échelles sans profil unique |
| non-unicité faible → échec Clay | notion de solution et régularité de la donnée | tester faible–forte unicité et inégalité d'énergie au temps de bifurcation |

## Zones non vérifiées et dette bibliographique

- Réextraire des textes originaux les domaines et exposants exacts de Prodi et Ladyzhenskaya avant de créer des claims détaillés; la gamme moderne ne doit pas leur être attribuée rétroactivement sans preuve.
- Extraire et recalculer les constantes quantitatives de Feng–He–Wang 2026; aucune uniformité vers `L^{3,∞}` n'est actuellement documentée.
- Reproduire la CAP Hou–Wang–Yang sur une machine propre, puis vérifier indépendamment la matrice finie, les quadratures, les fonctions de Bessel, les queues et les résidus.
- Extraire la condition exacte au bord radial et les jeux de données complets de Hou 2023 avant toute expérience comparative.
- Refaire la veille de statut éditorial des arXiv `2511.09556`, `2509.25116`, `2606.24733` et `2606.29468` à chaque cycle.
- Étendre le corpus primaire sur les critères de pression, les régions de régularité conditionnelle au bord et les formulations dissipatives; ils ne sont couverts ici qu'au niveau nécessaire à la première carte.

## Priorité bibliographique résultante

Le meilleur verrou informationnel n'est pas un nouvel ansatz self-similaire. C'est la classe exacte des limites anciennes produites par une concentration critique non auto-similaire : quelles bornes locales survivent à la remise à l'échelle, comment la pression lointaine est normalisée, et quelle hypothèse minimale de rigidité reste compatible avec les contre-profils multi-échelles. Le triplet de sources de départ est `NS-SRC-0012` + `NS-SRC-0014` + `NS-SRC-0015`, avec `NS-SRC-0034` pour le régime Type II.

L'action bibliographique décisive suivante est une extraction théorème-par-théorème de ces quatre textes : hypothèses exactes, normalisations, topologies de convergence, non-trivialité du profil, contrôle de pression et point précis où la rigidité échoue. Cette extraction doit précéder toute nouvelle revendication de lemme.
