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

Les progrès vérifiés se répartissent en quatre familles : existence faible globale, critères critiques conditionnels, exclusions de scénarios structurés, et résultats de non-unicité dans des classes ou avec des données différentes de celles de Clay. La veille 2025–2026 ajoute des résultats importants sur la non-unicité à donnée critique singulière, un blow-up instantané **par la droite** dans une classe faible non énergétique, une annonce de CAP pour la non-unicité de Leray–Hopf à donnée singulière, une croissance arbitraire de normes critiques entre données distinctes et des blow-ups Leray–Hopf forcés. Aucun ne raccorde les quantificateurs et l'admissibilité exacte de l'une des alternatives Clay (A)–(D).

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
| Solutions anciennes | [Koch–Nadirashvili–Seregin–Šverák 2009](https://arxiv.org/abs/0709.3599) (`0015`) | distingue les anciennes faibles des anciennes mild; exhibe les parasites `u=b(t)`, `p=-b'(t)·x`; Liouville dans plusieurs sous-classes | cible de rigidité après zoom et porte de jauge/mildness | aucun Liouville général pour les anciennes mild bornées 3D; la classe seulement locale/adaptée admet déjà des parasites |
| Self-similarité | [Nečas–Růžička–Šverák 1996](https://doi.org/10.1007/BF02551584) (`0016`), [Tsai 1998](https://doi.org/10.1007/s002050050099) (`0017`), [Chae 2007](https://doi.org/10.1007/s00208-007-0082-6) (`0018`), [Hou–Li 2007](https://doi.org/10.3934/dcds.2007.18.637) (`0019`) | exclusion de profils exacts ou asymptotiques sous intégrabilité/convergence | scénarios structurés éliminés | Type II, modulation, intermittence et multi-échelles restent ouverts |
| Auto-similarité forward | [Tsai 2014](https://arxiv.org/abs/1210.2783) (`0020`) | existence globale pour données discrètement self-similaires singulières | laboratoire de profils critiques | direction forward et donnée non lisse |
| Géométrie de vorticité | [Constantin–Fefferman 1993](https://doi.org/10.1512/iumj.1993.42.42034) (`0021`), [Beirão da Veiga–Berselli 2002](https://doi.org/10.57262/die/1356060864) (`0060`), [Berselli 2023](https://doi.org/10.1088/1361-6544/ace096) (`0063`) | cohérence high–high Lipschitz, seuil demi-Hölder pondéré, puis petits sauts discrets conditionnels | critères géométriques intégrés et conditionnels | ni module uniforme déduit de l'énergie, ni signe ponctuel du stretching |
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
- **solution ancienne admissible → trivialité** : les théorèmes de Liouville actuels couvrent des sous-classes (mildness, bornitude de la vitesse, symétrie, intégrabilité, auto-similarité), pas toutes les limites possibles. Sans mildness ou jauge globale de pression, même une ancienne lisse, localement adaptée, à vitesse bornée et de trace terminale nulle peut être non triviale par le mode spatial zéro.

Il est incorrect de remplacer la seconde arête par « les profils self-similaires sont exclus ». Une solution ancienne Type II, modulée ou multi-échelle n'est pas nécessairement self-similaire.

## Audit différentiel 2025–2026

### Résultats primaires directement sur Navier–Stokes standard

| Source | Statut au gel | Énoncé pertinent | Implication explicite vers Clay |
|---|---|---|---|
| [Coiculescu–Palasek, arXiv:2503.14699](https://arxiv.org/abs/2503.14699), DOI [10.1007/s00222-025-01396-z](https://doi.org/10.1007/s00222-025-01396-z) (`NS-SRC-0031`) | *Invent. Math.* 244 (2026), 165–219; version of record en ligne le 2025-12-12; arXiv v2 du 2025-07-21 | sur `T³`, deux solutions globales distinctes, lisses pour `t>0`, depuis une même grande donnée dans `BMO⁻¹(T³)` hors `L²` | donnée d'énergie infinie et non `C∞` au temps initial; **aucune implication** vers une alternative Clay |
| [Cheskidov–Zeng–Zhang, arXiv:2503.05692v1](https://arxiv.org/abs/2503.05692) (`0055`) | prépublication, 2025-03-07 | sur `T³`, une infinité de solutions faibles pour toute donnée `H^{1/2}`, à norme `L²` continue et décroissante | leur notion « dissipative » n'est pas Leray–Hopf : les auteurs excluent l'inégalité d'énergie faible–forte; **ni blow-up classique ni non-unicité Leray–Hopf** |
| [Palasek, arXiv:2509.18595v1](https://arxiv.org/abs/2509.18595) (`0056`) | prépublication, 2025-09-23 | données lisses distinctes, uniformément bornées dans `B^{-1}_{∞,1}(T³)`, dont les solutions fortes globales atteignent des amplitudes arbitraires | réfute des bornes dépendant seulement de `BMO⁻¹`, mais chaque solution est globale et les données diffèrent; **ni non-unicité ni blow-up** |
| [Cheskidov–Dai–Palasek, arXiv:2511.09556v2](https://arxiv.org/abs/2511.09556) (`0032`) | prépublication, 2026-01-12 | pour toute donnée lisse périodique, construit une solution faible avec singularité Type I en `t→T*+`, lisse à chaque temps et hors de la classe énergétique près de `T*` | le blow-up conventionnel Clay est `t→T*−` sur la continuation classique; ici la branche classique jusqu'à `T*` reste lisse et l'énergie de la branche droite diverge : **pas un blow-up Clay** |
| [Liao–Qin, arXiv:2602.12666v1](https://arxiv.org/abs/2602.12666) (`0057`) | prépublication, 2026-02-13; calcul CNS non certifié | trajectoires très précises mais séparées depuis des données distantes de `10^-10`, `10^-20` ou `10^-40`, pour un écoulement de Kolmogorov 2D forcé périodique | sensibilité chaotique de données **différentes**, en dimension 2 et avec force; aucune non-unicité de Cauchy et aucune implication Clay |
| [Hou–Wang–Yang, arXiv:2509.25116v2](https://arxiv.org/abs/2509.25116) et [code primaire](https://github.com/HouGroup2026/3d-navier-stokes-nonuniqueness) (`0033`) | prépublication, 2026-03-19; CAP revendiquée; code audité au commit `615ee6f` mais non exécuté | annonce une infinité de solutions adaptées de Leray–Hopf non forcées sur `R³`, même donnée compacte `C∞(R³\{0})∩L^q`, `q<3`, lisses pour `t>0`; cutoff extérieur avec gain `R^-1/8`; profil pair et mode certifié impair | la donnée garde `1/r`; la régularisation lisse déclenche l'unicité faible–forte, n'est pas petite en topologie critique forte et, si elle est radiale, projette exactement zéro sur le mode impair : **aucun raccord Clay** |
| [Ionescu–Jia–Palasek, arXiv:2606.07501v1](https://arxiv.org/abs/2606.07501) (`0054`) | prépublication, 2026-06-05; calcul flottant non certifié | profils forward auto-similaires axisymétriques sans swirl, résidu ponctuel annoncé `10^-10`; théorème 1.2 conditionnel à un profil et un mode exacts vers non-unicité dans `H^alpha∩L^{3,infinity}`, `alpha<1/2` | la donnée reste homogène `-1` et singulière; ni CAP des objets exacts ni stabilité sous lissage : **même porte Clay manquante** |
| [Galdi–Gazzola, arXiv:2606.15189v3](https://arxiv.org/abs/2606.15189) (`0058`) | prépublication, v3 du 2026-07-21 | sur `R³`, force spécialement construite et donnée lisse; unique solution globale de Leray–Hopf, égalité d'énergie et blow-up en un ensemble dénombrable d'instants/points | ne réfute pas (A)–(B), où `f=0`; la force n'est pas `C∞` rapidement décroissante comme l'exige (C), mais seulement dans des classes d'intégrabilité portant la singularité : **pas une alternative Clay négative** |
| [Feng–He–Wang 2026](https://doi.org/10.3934/dcdsb.2026048) (`0035`) | publié en ligne le 2026-03-06 | estimations quantitatives et taux nécessaires dans des espaces de Lorentz critiques `L^{3,q}`, `q<∞` | critère/taux conditionnels; **aucune borne globale** de la norme critique |
| [Chen–Galdi–Poggi–Schikorra, arXiv:2606.24733v1](https://arxiv.org/abs/2606.24733) (`0036`) | prépublication, 2026-06-23 | régularité intérieure de solutions distributionnelles sur la ligne Serrin, avec hypothèses relâchées | améliore l'étape « contrôle critique → régularité », mais pas « énergie → contrôle critique » |
| [Seregin, arXiv:2606.29468v1](https://arxiv.org/abs/2606.29468) (`0034`) | prépublication, 2026-06-28 | scénarios Type II locaux, zoom d'échelle Euler et théorèmes de Liouville conditionnels | réduction utile, mais **ni existence ni exclusion générale** d'un blow-up Type II |
| [Cheskidov–Hou, arXiv:2603.03666v2](https://arxiv.org/abs/2603.03666) (`0044`) | prépublication, révisée le 2026-06-11 | non-unicité de solutions mild singulières sur le tore dans tout Besov d'indice négatif; produit quadratique défini par paraproduit, sans `L²_loc` général | notion mild distributionnelle et données non lisses; **ni blow-up classique ni ancienne mild bornée KNSS** |
| [Seregin, arXiv:2402.13229v3](https://arxiv.org/abs/2402.13229) (`0045`) | prépublication, révisée le 2026-08-08 | scénario Type II axisymétrique réduit par échelle Euler à une ancienne non triviale sans swirl, puis exclusions conditionnelles | la limite est Euler et les bornes supplémentaires ne sont pas universelles; **pas d'exclusion Type II générale** |
| [Wang–Yang, arXiv:2608.06040v1](https://arxiv.org/abs/2608.06040) (`0046`) | prépublication, 2026-08-06 | Liouville pour des `D`-solutions stationnaires sous enveloppes cylindriques critiques avec gain logarithmique | stationnarité, Dirichlet fini et décroissance ne sont pas hérités par une limite ancienne générale |
| [Lei–Ren–Tian, arXiv:2501.08976v1](https://arxiv.org/abs/2501.08976) (`0061`) | prépublication, 2025-01-15 | critère local pour solution faible adaptée : confinement de la forte vorticité dans un double cône fixe implique la régularité intérieure | hypothèse conditionnelle uniforme dans un cylindre; aucune loi générale ne produit le cône et aucun signe ponctuel n'est obtenu |
| [Yu, arXiv:2606.27560v1](https://arxiv.org/abs/2606.27560) (`0062`) | prépublication, 2026-06-25 | absorption du stretching filtré proche avec perte explicite `(r/ell)^5`, plus budgets de queue, packing, commutateur et localisation | uniforme seulement à rapport `ell/r` fixé; aucun passage uniforme filtre→continuum ni contrôle de la queue lointaine |
| [Grujić, arXiv:2607.08866v2](https://arxiv.org/abs/2607.08866) (`0059`) | prépublication, révisée le 2026-07-13 | revendique l'exclusion d'une singularité ponctuelle critique sous `omega∈L∞L^{3/2,infinity}` et `xi∈L∞bmo_{1/|log r|}` | hypothèses critiques supplémentaires; cycles 0014–0017 ferment conditionnellement les raccords aval `(22)->(55)` avec plusieurs corrections, mais le commutateur `(8)->(22)` et l'endgame complet restent non reproduits |
| [Binz–Coiculescu, arXiv:2607.12159v1](https://arxiv.org/abs/2607.12159) (`0047`) | prépublication, 2026-07-13 | exclusion de profils homothétiques forward dans certaines classes de Morrey/régularité angulaire | profil forward à donnée homogène singulière; **pas un profil backward de blow-up Clay** |
| [Seregin, arXiv:2507.08733v2](https://arxiv.org/abs/2507.08733) (`0048`) | prépublication, révisée le 2026-01-03 | autres scénarios Type II conditionnels donnant des anciennes Euler dissipatives non triviales et exclusions de sous-classes | aucune réduction de tout blow-up Clay ni Liouville Euler ancien général |
| [Escauriaza–Seregin–Šverák 2003](https://doi.org/10.1007/s00205-003-0263-8) (`0049`) | article publié, *Arch. Rational Mech. Anal.* 169(2), 147–157 | unicité rétrograde pour une inégalité parabolique avec termes d'ordre inférieur bornés et croissance gaussienne | outil de vorticité conditionnel; ne crée ni trace nulle ni bornes de coefficients |
| [Lei–Yang–Yuan 2024](https://academic.oup.com/imrn/article/2024/20/13417/7769704) (`0050`) | article publié le 2024-09-24, DOI `10.1093/imrn/rnae208`; arXiv resté `2311.02429v1` | unicité à donnée finale pour deux solutions mild bornées 3D de vorticités bornées | ferme le Liouville conditionnel après construction d'une vraie trace finale sur le même objet; ne fournit pas cette construction |
| [Pineau–Vicol, arXiv:2607.09619v2](https://arxiv.org/abs/2607.09619) (`0051`) | prépublication, révisée le 2026-08-06 | exclusions quantitatives RSS/DSS/RDSS backward sous borne Type I et critère local de quasi-auto-similarité | sous-classes Type I structurées; rotation intermédiaire et scénarios Type II non couverts |
| [Constantin 2023](https://doi.org/10.1007/s00021-023-00779-7) (`0052`) | article publié, *J. Math. Fluid Mech.* 25, article 36; arXiv `2301.04489v1` | la condition (23), petite masse `L³` sur tout ensemble de volume `<=delta` uniformément en temps, donne au théorème 2 une borne explicite de `Hdot1` et le prolongement | le seuil critique n'est pas déduit de l'énergie; l'équi-intégrabilité complète envisagée au cycle 0009 est plus forte et ne constitue pas un critère nouveau |
| [Barker–Seregin 2017](https://doi.org/10.1007/s00208-016-1488-9) (`0053`) | article publié, *Math. Ann.* 369, 1327–1352; arXiv correct `1508.05313v1` | au demi-espace, un blow-up force la divergence des normes `L^{3,q}`, `3<=q<infinity`, via une limite ancienne locale-énergie | frontière sans glissement, endpoint faible `L³` exclu; aucune borne critique a priori pour les cas Clay sans frontière |

Deux confusions doivent être activement empêchées :

1. « non-unicité de solutions faibles » n'implique pas « singularité de la solution classique maximale » ;
2. « donnée critique donnant des solutions lisses pour `t>0` » n'implique pas « donnée initiale lisse au sens Clay » ;
3. « mild » dans une classe de distributions à produit renormalisé n'implique ni
   la mildness bornée de KNSS, ni l'admissibilité énergétique, ni la lissité.
4. « énergie continue et décroissante » n'implique pas l'inégalité d'énergie
   de Leray–Hopf entre deux temps.
5. sensibilité à deux données arbitrairement proches n'implique pas deux
   solutions d'une même donnée.
6. cohérence locale de direction n'implique ni signe ponctuel du stretching,
   ni petite contribution de la partie lointaine du strain.

Le cycle 0008 corrige aussi un statut bibliographique : Lei–Yang–Yuan n'est
pas une simple prépublication. L'article est publié dans l'IMRN 2024. La date
2026 affichée par certains rendus HTML expérimentaux d'arXiv ne correspond pas
à une nouvelle version; l'historique primaire demeure `v1`, soumis en 2023.

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

Une critique non publiée de 2015, [Lam, arXiv:1509.04940](https://arxiv.org/abs/1509.04940),
allègue des erreurs techniques dans l'unicité rétrograde ESS. Elle est
consignée dans la watchlist (`NS-WATCH-0006`) sans adjudication : ce cycle n'a
identifié ni correction publiée ni évaluation experte qui autoriserait à
renverser les résultats publiés. La route principale du lemme 0008 passe par
le lissage KNSS puis le théorème parabolique ESS appliqué à la vorticité.
Lei–Yang–Yuan sert de contrôle analytique séparé : son arXiv v1 contient trois
anomalies de rédaction ou d'algèbre consignées dans `FAIL-NS-0011`, qui
n'autorisent ni à réfuter l'article publié, ni à en faire l'unique support sans
comparaison avec la version éditeur.

## Calcul numérique et preuve assistée

Quatre niveaux sont distingués :

1. **indice numérique non certifié** : trajectoire flottante ou profil tronqué sans borne globale d'erreur ;
2. **calcul haute précision** : convergence empirique et résidus petits, mais sans inclusion mathématique ;
3. **preuve assistée par ordinateur** : réduction analytique à un problème borné, arithmétique rigoureuse, queues et erreurs de troncature incluses ;
4. **preuve analytique** : argument symbolique publié, éventuellement avec constantes explicites.

[Guillod–Šverák](https://arxiv.org/abs/1704.00560) (`NS-SRC-0037`) est un calcul non certifié de profils/bifurcations forward self-similaires à donnée singulière. [Hou 2023](https://doi.org/10.1007/s10208-022-09578-4) (`0038`) est une simulation adaptative haute résolution d'un scénario axisymétrique avec swirl dans un cylindre; la croissance observée et le régime presque self-similaire ne certifient pas un blow-up. Il manque notamment un résidu PDE intervalle, une borne de discrétisation uniforme, le contrôle certifié du bord et un passage à la limite.

À l'inverse, [van den Berg–Breden–Lessard–van Veen 2021](https://doi.org/10.1007/s00332-021-09695-4) (`0040`) valide des orbites périodiques particulières du Navier–Stokes forcé sur `T³` par Newton–Kantorovich et contrôle de queues. [Liu–Nakao–Oishi 2022](https://arxiv.org/abs/2101.03727) (`0041`) certifie localement des solutions stationnaires sur domaines bornés. Ces travaux établissent la faisabilité d'une CAP PDE, mais leur quantificateur reste « il existe une solution proche de ce candidat », non « toute donnée Clay reste régulière ».

La prépublication Hou–Wang–Yang (`0033`) est la seule source récente identifiée revendiquant une CAP d'un résultat de non-unicité Leray–Hopf non forcé. Son dépôt n'a pas été exécuté dans ce cycle. L'audit au commit `615ee6f` confirme Julia `>=1.11`, au moins 800 Go de RAM, six notebooks par intervalles et des candidats `.mat` pré-calculés. Il n'existe ni tag/release, ni `Manifest.toml`, ni section `[compat]`; le README annonce un manifeste dans son arbre puis reconnaît son absence. Le manifeste de blobs du cycle 0011 compte 70 fichiers et 84 137 370 octets : `data/up_eig.mat` expose un mode droit et `data/eig.mat` des bases de coercivité, mais aucun adjoint dynamique normalisé, certificat de simplicité ou borne de résolvante utilisable pour conditionner le projecteur n'a été identifié. Avant promotion bibliographique, il faut au minimum : environnement épinglé, empreinte des entrées, chaîne de génération des candidats, reproduction des bornes intervalle, vérification indépendante des résidus, des queues, de la divergence, de l'adjoint et des constantes de l'inverse fini-dimensionnel.

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
| direction locale → stretching | strain de Biot–Savart lointain et ordre des quantificateurs | paire périodique exacte à signe opposé; exiger une queue non locale explicite |
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

L'extraction théorème-par-théorème ESS/GKP/KNSS/Seregin a été réalisée. Elle
ferme conditionnellement la rigidité d'une ancienne mild bornée à trace nulle,
mais prouve aussi que cette classe n'est produite par aucune chaîne auditée.
Le cycle 0009 corrige l'horloge de cette priorité : dans le zoom KNSS,
`s=0` représente le temps-record `t_k`, et non le temps physique `T`, lequel
devient l'extrémité mobile `B_k=M_k²(T-t_k)`. La commutation au temps-record est
contrôlée et donne une valeur non nulle. L'équi-intégrabilité complète de
`|u|³` exclurait la concentration, mais Constantin 2023 fournit déjà un critère
plus faible à seuil fixe; aucune nouveauté n'est revendiquée.

Après trois stratégies sur le paquet hybride ESS–KNSS, la priorité
bibliographique pivote vers la stabilité sous désingularisation des données
homogènes de degré `-1` de Hou–Wang–Yang : dépendance exacte en cutoff des
constantes spectrales, de l'instabilité et du calcul validé, puis confrontation
à l'unicité faible–forte pour les données Clay lisses.

## Audit ciblé du cycle 0014 — provenance de la sparseness

La réduction « densité volumique `delta` vers tranche centrale
`delta^(1/3)` » est vraie et sharp, mais sa provenance devait être corrigée :

| Source primaire | Ce qu'elle porte exactement | Ce qu'elle ne porte pas |
|---|---|---|
| Grujić 2013, DOI `10.1088/0951-7715/26/1/289` (`0064`) | définition 1D faible, rayon analytique, mesure harmonique de Solynin et critère de prolongement | aucune définition de sparseness 3D ni réduction même-rayon |
| Farhat–Grujić–Leitmeyer 2017, DOI `10.1007/s00021-016-0288-z` (`0065`) | sparseness volumique et seuil `delta^(1/3)` à une échelle `rho≤r` | ne fixe pas nécessairement `rho=r`; l'erratum Besov est conservé |
| Grujić–Xu 2019–2024, DOI `10.1007/s00021-024-00888-x` (`0066`) | formulation même-centre/même-rayon, puis dimension `d` avec `delta^(1/d)` | ne produit pas l'hypothèse géométrique depuis toute donnée Clay |
| Grujić `arXiv:2607.08866v2` (`0059`) | réutilise le maillon avec `delta=3/4` dans une chaîne logarithmique | estimations (47)–(55) et théorème 7.4 non reproduits |

La v2 datée du 13 juillet 2026 reste la version courante contrôlée le
2026-08-14; aucune v3 ni publication évaluée n'a été identifiée. La priorité
bibliographique et analytique passe à l'inversion quantitative (47)–(49), puis
à la queue dyadique du commutateur si cette arête échoue.

## Audit ciblé du cycle 0015 — inversion des réarrangées

| Source primaire | Passage contrôlé | Verdict exact |
|---|---|---|
| Grujić `arXiv:2607.08866v2` (`0059`) | équations (40)–(49), en particulier (47)–(49) | l'enveloppe de réarrangée (47) implique bien une queue `lambda^-3 log^-3` après normalisation et seuil explicites; l'égalité informelle de (48) est fausse sur les plateaux |
| O'Neil 1963, DOI `10.1215/S0012-7094-63-03015-1` (`0067`) | inégalité de convolution utilisée en (41) | la structure coeur–queue est classique; l'application exige une représentation Biot–Savart sans composante harmonique incontrôlée et ne borne pas à elle seule le reste positif de (46) |

Le lemme réparé est purement mesurable. Si
`f*(v)≤A v^(-1/3)/log(eV_*/v)` uniformément pour `0<v≤v_0`, alors, au-dessus
d'un seuil explicite dépendant de `A,V_*,v_0`,

```text
mu_f(lambda) ≤ A^3 /
  [lambda^3 (1+3 log(lambda/Lambda_*))^3],
Lambda_*=A V_*^(-1/3).
```

La preuve utilise `f*(v)>lambda` pour tout `v<mu_f(lambda)`, puis fait tendre
`v` vers la mesure du superniveau; elle n'utilise jamais l'identité fausse
`lambda=f*(mu_f(lambda))`. Un profil à deux plateaux la réfute exactement.
Une famille dont le cutoff `v_0(t)` tend vers zéro montre en outre que la
constante temporelle n'est uniforme que si le domaine de validité de (47)
l'est. Le statut reste `COMPUTATION_ONLY`: le transfert vorticité–vitesse
`(40) -> (41) -> (47)` n'est pas encore reproduit.

## Audit ciblé du cycle 0016 — transfert O'Neil et jauge de Biot–Savart

| Source primaire | Passage contrôlé | Verdict exact |
|---|---|---|
| Grujić `arXiv:2607.08866v2` (`0059`) | équations (40)–(47) | les exposants se transfèrent après quantification; le reste positif de (46) n'est pas `O(1)` et la vitesse entière n'est pas reconstruite depuis la vorticité sous la seule hypothèse `L∞` |
| O'Neil 1963, DOI `10.1215/S0012-7094-63-03015-1` (`0067`) | inégalité de convolution | la forme `(f*g)**` donne exactement les poids `v^-2/3` et `s^-2/3`; le facteur trois du coeur vient de `K**` |
| Majda–Bertozzi 2002, DOI `10.1017/CBO9780511613203` (`0068`) | Biot–Savart et décomposition de Hodge sur `R³` | la reconstruction exige décroissance, intégrabilité ou fixation explicite de la composante harmonique |

Une version dimensionnée et uniforme de (40), complétée par le contrôle global
`omega∈L^{3/2,infinity}` et une décomposition
`u=B[omega]+h`, `||h||_infinity≤H`, implique quantitativement (47). Le cycle
0016 fournit un seuil de sécurité `0<v≤Vexp(-6)` et une constante explicite.

Deux énoncés littéraux sont toutefois réfutés :

1. le reste
   `3 integral_v^1 s^(-4/3)/log²(e/s) ds` diverge comme
   `9v^(-1/3)/log²(e/v)`; il est inférieur au terme principal, mais pas
   `O(1)`;
2. un champ constant non nul a vorticité nulle et contredit (41) si la
   composante harmonique n'est ni retranchée ni contrôlée.

Ces défauts sont localement réparables et ne changent pas l'exposant de (47).
Ils empêchent néanmoins de classer la rédaction actuelle comme une preuve à
constantes et quantificateurs suivis. La priorité remonte à la production
dynamique de (40), notamment les seuils de troncature et le coefficient de
Grönwall de l'étape De Giorgi.

## Audit ciblé du cycle 0017 — énergie tronquée et sources fonctionnelles

| Source primaire | Passage contrôlé | Verdict exact |
|---|---|---|
| Grujić `arXiv:2607.08866v2` (`0059`) | équations (20)–(40) | `(23)->(40)` est réparable à seuils et constantes suivis sous (22); `2` avant (21), le seuil « absolu » et l'extension à `(0,T*)` sont faux littéralement |
| Hunt 1966 (`0069`) et Peetre 1966, DOI `10.5802/aif.232` (`0070`) | Hölder/interpolation de Lorentz et Sobolev–Lorentz | les exposants `theta=2/3`, `L^(6,2)` et `L^(3,1)` sont cohérents; les constantes dépendent des conventions de norme |
| Talenti 1976, DOI `10.1007/BF02418013` (`0071`) | Sobolev homogène dans (33) | combiné à Hölder sur le support, donne (34) sans hypothèse de régularité du bord du superniveau |
| Vasseur 2007, DOI `10.1007/s00030-007-6001-4` (`0072`) | comparaison avec une vraie méthode De Giorgi pour NS | confirme que la v2 n'exécute pas une itération de niveaux : elle fait une troncation fixe, un ODE et Chebyshev |

Le lemme réparé emploie un logarithme `log(lambda/Lambda_*)`, un seuil au
moins exponentiel en `C_H A S_L²/nu`, l'amortissement
`nu lambda/(2S_6²M)` et une ancre où le tronqué est nul. Il produit

```text
U_(2lambda)(t)
 <=C lambda^(-3/2)log(lambda/Lambda_*)^(-3/2)
```

uniformément sur l'intervalle terminal, pas sur tout `(0,T*)`. Faible-
`L^(3/2)` fournit la mesure du support, mais pas l'appartenance du tronqué à
`H¹`; le profil `|x|^-2` réfute cette dernière implication. Pour la solution
classique de la v2, la régularité pré-singulière est donc une prémisse
essentielle et distincte.

L'audit de (20)–(21) fournit déjà un test adverse du prochain verrou : avec
`R=2^-8` et le dernier indice, le ratio de poids vaut `8/3`, non `2`. Le
facteur `3` répare cet échelon à petite échelle, mais les extensions BMO et
toutes les queues de (8)–(22) restent non reproduites.

## Audit ciblé du cycle 0018 — extension BMO et commutateur localisé

| Source primaire | Passage contrôlé | Verdict exact |
|---|---|---|
| Grujić `arXiv:2607.08866v2` (`0059`) | théorème 4.1, équations (8)–(22) | le gain logarithmique survit après correction de la semi-norme, de la réarrangée et du dernier anneau; statut conditionnel seulement |
| Coifman–Rochberg–Weiss 1976 (`0073`) et Hunt 1966 (`0069`) | commutateur BMO sur `L^p`, puis cible faible-`L^(3/2)` | la cible est obtenue par interpolation réelle de deux exposants forts; `L^(3/2,infinity)` n'est pas réflexif |
| Jones 1980 (`0074`) | extension de `B_(2R)` vers `R³` | constante uniforme par dilatation pour la semi-norme BMO; aucune préservation de `L∞` ou de `|xi|=1` |
| John–Nirenberg 1961 (`0075`) | moments locaux d'ordre deux et quatre | fournit les facteurs `R²phi(R)` et `(2^kR)phi(2^(k+1)R)` à constantes dimensionnelles |

Pour `h_a(y)=|y|^-3 1_(|y|>a)`, la réarrangée exacte est
`1/(a³+s/|B_1|)`, non une fonction `min` exacte; sa norme `L^(3,1)` reste
proportionnelle à `a^-2`. Pour la somme intermédiaire, les moyennes peuvent
dériver d'ordre un jusqu'à `sqrt(RR_*)`, mais le poids de noyau `4^-k`
fournit `sum_(k>=1)(k+1)4^-k=7/9`. Le facteur trois remplace uniformément le
facteur deux fautif lorsque `log_2(R_*/R)>=6`.

Le lemme dimensionné résultant est enregistré comme
`NS-LOCALIZED-LOG-COMMUTATOR`, statut `COMPUTATION_ONLY`. Il ferme
conditionnellement l'arête fonctionnelle `(8)->(22)`; il ne produit pas la
borne globale `bmo_phi` de la direction, ne règle pas sa définition aux zéros
de vorticité et n'implique aucune alternative Clay. La prochaine priorité
bibliographique et analytique est la synchronisation de l'endgame
`(49)->(58)` au même temps d'échappement.

## Audit ciblé du cycle 0019 — temps analytique et fermeture harmonique

| Source primaire | Passage contrôlé | Verdict exact |
|---|---|---|
| Grujić `arXiv:2607.08866v2` (`0059`) | équations (49)–(58), théorème 7.4 | le raccord spatial est réparable, mais `s=t+T_t` n'est pas intérieur si `T_t` est maximal; temps garanti et dichotomie requis |
| Grujić 2013 (`0064`) et Grujić–Xu 2024 (`0066`) | critère 1D, fenêtre temporelle et facteur analytique `M` | la version publiée sépare prolongement direct et temps analytique intérieur; le même `M` doit fermer les deux branches |
| Guberović 2010 (`0076`) | analyticité spatiale mild | fournit durée et rayon garantis, non un « maximal local analyticity time » |
| Solynin 1997/1999 (`0077`) et Ransford 1995 (`0078`) | mesure harmonique et principe additif des deux constantes | la combinaison `h/2+(1-h)M=1` et son sens monotone sont corrects après projection scalaire |

La formulation réparée part d'une queue uniforme

```text
|{|u(t)|>a}|<=C_mu/[a³log³(e+a/U_*)],   a>=a_0,
```

choisit `tau_t=nu/[c_1(M)||u(t)||_infinity²]`, puis sépare
`t+tau_t>=T*` et `t+tau_t<T*`. Dans la seconde branche, le rayon témoin

```text
r_s=C_4/[||u(s)||_infinity log(e+theta||u(s)||_infinity/U_*)]
```

est inférieur au sous-rayon analytique `nu/[c_A||u(s)||_infinity]` au-dessus
d'un seuil fini, exponentiel en `C_mu^(1/3)/nu`. Le rayon doit être construit
par égalité depuis le majorant de volume : les rayons plus petits ne sont pas
automatiquement sparse.

Le claim `NS-CONDITIONAL-ENDGAME-SYNCHRONIZATION` est `COMPUTATION_ONLY`.
Le choix maximal littéral est enregistré `REFUTED`. Ce cycle ne valide pas la
production de la queue uniforme depuis une donnée Clay générale; il ferme
seulement le maillon aval sous ses prémisses.
