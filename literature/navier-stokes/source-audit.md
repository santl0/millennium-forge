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
| Géométrie de vorticité | [Constantin–Fefferman 1993](https://doi.org/10.1512/iumj.1993.42.42034) (`0021`), [Beirão da Veiga–Berselli 2002](https://doi.org/10.57262/die/1356060864) (`0060`), [Berselli 2023](https://doi.org/10.1088/1361-6544/ace096) (`0063`), [Miller 2021](https://doi.org/10.1090/bproc/74) (`0089`) | cohérence high–high Lipschitz, seuil demi-Hölder pondéré, petits sauts discrets et plan variable conditionnel | critères géométriques intégrés et conditionnels | ni module uniforme déduit de l'énergie, ni signe ponctuel du stretching; Miller suppose gradient spatial borné et contrôle transverse critique |
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

## Audit ciblé du cycle 0020 — direction active et espaces log-BMO

| Source primaire | Passage contrôlé | Verdict exact |
|---|---|---|
| Grujić `arXiv:2607.08866v2` (`0059`) | équation (2), théorème 4.1 | norme globale ancrée par `L∞`, petites boules mais tous centres; aucune convention de `xi` sur `{omega=0}` |
| Bradshaw–Grujić 2015 (`0083`) | définition de `tilde-bmo_phi`, théorème 1 | espace ancré par `L¹` appliqué à `psi xi`; il n'est pas la norme globale non coupée de 2026 |
| Spanne 1965 (`0079`) et Janson 1976 (`0080`) | BMO pondéré par l'oscillation | provenance des semi-normes `BMO_phi` modulo les constantes; aucune ancre identique à la v2 |
| Goldberg 1979 (`0081`) | Hardy local et dual `bmo` | le `bmo` inhomogène sépare petites et grandes échelles; il ne définit pas le quotient de la v2 |
| Nakai–Yabuta 1985 (`0082`) | multiplicateurs sur `R^n` | distingue semi-norme, ancre et poids position–échelle; interdit une identification silencieuse des espaces |

La solution nulle fournit un test intrinsèque exact. Avec
`u=p=omega=0`, les extensions unitaires `xi=e_1` et
`xi=sign(x_1)e_1` satisfont toutes deux `omega=|omega|xi`. La première a
une semi-norme nulle; la seconde a une oscillation moyenne un sur chaque
petite boule centrée sur le plan de saut, donc une norme log-pondérée infinie.
Les résidus PDE, divergence et vorticité sont nuls dans les deux cas.

La propriété n'est donc pas définie par la seule vorticité tant qu'une
convention ou un quantificateur d'existence sur les zéros n'est pas fixé. En
outre, le lemme optimal du cycle donne, pour deux phases antipodales de
fractions `a,b` dans un domaine test,

```text
MO_D(xi) >= 4ab/(a+b).
```

Deux cœurs de fractions fixes à des échelles tendant vers zéro réfutent toute
extension globale uniforme déduite de la seule cohérence sur chaque
composante. Cela ne réfute pas le théorème conditionnel de la v2, qui suppose
la norme globale; cela ferme négativement le raccord vers des données Clay
générales sans hypothèse inter-composantes.

## Audit ciblé du cycle 0021 — profil critique ponctuel

| Source primaire | Passage contrôlé | Verdict exact |
|---|---|---|
| Grujić `arXiv:2607.08866v1-v2` (`0059`) | Definition 2.1, théorèmes 4.1 et 7.4 | la magnitude scalaire, la récurrence de `Phi`, le gradient, le faible-Lorentz et la contenance des sur-niveaux ne forment pas une classe quantifiée cohérente sans rayon de cœur ou limite remise à l'échelle |
| Barker `arXiv:2510.20757v3` (`0084`) | notions de solution/singularité, théorèmes 1–3 | fournit un contraste primaire précis et des classifications quantitatives sous approximation axisymétrique; ne valide ni ne réfute seul la v2 |
| Leray 1934, Nečas–Růžička–Šverák 1996 et Tsai 1998 (`0002`, `0016`, `0017`) | profils auto-similaires et énergie locale | exclusions publiées de sous-classes distinctes; aucune réduction de tout blow-up Clay vers Definition 2.1 |

La veille différentielle confirme que `2607.08866` reste à la v2 du 13
juillet 2026, sans référence de revue ou erratum. La v3 de Barker, révisée le
11 août 2026, est ajoutée comme prépublication récente, sans promotion de ses
preuves au-delà de l'audit de texte primaire.

Le profil scalaire doit être séparé du champ vectoriel. Pour
`W=r^-2 Omega(theta)`, les contraintes absentes de la définition sont

```text
div_(S²) Omega_T=0,
integral_(S²) Omega_r dS=0.
```

Le cycle construit un `W` exact, divergence-free, de magnitude `r^-2` et
faible-`L^(3/2)`, dont la direction conserve une oscillation au moins `2/3`
sur toutes les boules centrées. La magnitude critique n'implique donc pas
l'hypothèse directionnelle. Plus généralement, une direction exactement
récurrente par dilatation et dans `bmo_phi`, avec `phi(r)->0`, devient
constante; divergence nulle plus faible-`L^p` global force alors `W=0`.

Cette exclusion ne porte que sur la récurrence spatiale vectorielle exacte.
La v2 ne suppose explicitement la récurrence que du facteur scalaire `Phi`;
les directions non récurrentes ou seulement asymptotiques restent hors du
lemme.

## Audit ciblé du cycle 0022 — rectification fixe et dérive non récurrente

| Source primaire | Passage contrôlé | Verdict exact |
|---|---|---|
| Lei–Ren–Tian `arXiv:2501.08976v1` (`0061`) | théorème 1.1, double cône | une rectification uniforme espace-temps de toute forte vorticité vers `+/-e` implique le cône fixe et donc, conditionnellement à la prépublication, la régularité intérieure; la preuve n'est pas reproduite |
| Chae 2015 (`0085`) | profil périodique en temps similaire | exclusion publiée d'un blow-up localement asymptotiquement DSS sous profil `C¹_t(L³ intersect C²_x)`; pas de dérive apériodique |
| Chae–Wolf 2017 (`0086`) | DSS et facteur proche de un | exclusion publiée d'une sous-classe DSS structurée; ni facteur général, ni Type II |
| Giga–Miura 2011 (`0087`) | critère directionnel avec énergie infinie | sous borne Type I, la continuité uniforme de la direction sur la région active exclut le blow-up; aucune production du module depuis l'énergie |
| Ożański–Palasek 2023 (`0088`) | faible-`L³` axisymétrique | bornes quantitatives et corollaire de Liouville ancien dans la classe axisymétrique; aucun transfert à une géométrie seulement proche d'un axe |
| Grujić `arXiv:2607.08866v2` (`0059`) | magnitude récurrente et direction log-BMO | ne construit pas une direction rectifiée, ne fixe pas un axe et ne transforme pas la norme moyenne en cône uniforme |

Pour `s=log(R_*/r)` et `W=r^-2 Omega(s,theta)`, le signe exact est

```text
div W=r^-3[div_(S²)Omega_T-partial_s Omega_r].
```

Le cycle 0022 teste cette contrainte contre le premier harmonique
`mu=e dot theta`. Si `Phi=|Omega|` est uniformément bornée, si chaque bloc
logarithmique garde une masse critique moyenne `Phi^(3/2)` strictement
positive et si `xi` converge vers un axe fixe en moyenne pondérée par `Phi`,
le moment borné `<mu Omega_r>` doit décroître d'une quantité fixe par bloc.
La contradiction exclut ce profil avant même Biot–Savart ou la pression.

Une construction adverse exacte montre la frontière :

```text
W=(s²-s)e+s(e dot theta)theta,
u=(s²/2)e cross x.
```

Elle est solénoïdale et sa direction se rectifie comme `1/s`, mais son facteur
critique `Phi` vaut seulement `e^-2s s²` à constante près. La singularité
`r^-2` et la masse critique par coquille disparaissent. La prochaine classe
non couverte doit donc faire errer son axe, multiplier les cœurs ou concentrer
les amplitudes de manière à échapper à tout double cône fixe; faible-
`L^(3/2)` seul ne contrôle pas ces traces angulaires.

## Audit ciblé du cycle 0023 — axes mobiles et log-BMO non-Dini

| Source primaire | Passage contrôlé | Verdict exact |
|---|---|---|
| Miller 2021 (`0089`) | théorème 1.6, plan variable | critère publié avec `v×omega∈L⁴_tL²_x` et gradient spatial borné de `v`; aucune dérivée temporelle requise, mais un axe radial logarithmique a un gradient singulier |
| Lei–Ren–Tian `arXiv:2501.08976v1` (`0061`) | théorème 1.1 et corollaires 1.5–1.6 | axe fixe pour le cône de forte vorticité; le critère pairwise tolère un axe par tranche mais porte sur toute vorticité non nulle; preuve non reproduite |
| Grujić `arXiv:2607.08866v2` (`0059`) | définition log-BMO et équation (16) | les moyennes dyadiques ont des incréments `O(1/k)` mais peuvent s'annuler; aucun axe unitaire normalisable ni confinement de grands niveaux n'en découle |
| Giga–Miura 2011 (`0087`) | direction spatialement uniformément continue | tolère une rotation temporelle commune mais exclut conditionnellement une dérive spatiale de taille macroscopique sous borne Type I |
| Pineau–Vicol `arXiv:2607.09619v2` (`0051`) | RSS/RDSS backward | rotation structurée en temps similaire et Type I; aucun transfert vers une phase radiale apériodique ou Type II |

Le poids `1/|log r|` n'est pas Dini. Un champ directionnel radial explicite,
de phase `log log(e/r)`, reste dans la classe log-BMO tout en parcourant un
grand cercle et en échappant à tout cône fixe. Cette construction est un
falsificateur fonctionnel, pas une vorticité : elle ne satisfait pas à elle
seule `div omega=0`, Biot–Savart ou Navier–Stokes.

La conclusion négative de veille est précise : aucune source primaire
inspectée ne donne

```text
direction log-BMO
  -> moyenne active non nulle
  -> axe unitaire global à variation contrôlée
  -> confinement des grands niveaux.
```

Le budget mobile du cycle 0023 exclut néanmoins toute sélection déjà obtenue
dont la variation et l'erreur pondérée sont sublinéaires, sous amplitude
bornée et masse critique par bloc. Le prochain maillon doit donc traiter les
moyennes actives dégénérées, les phases multiples ou l'intermittence.

## Audit ciblé du cycle 0024 — extension unitaire et axes actifs

| Source primaire | Passage contrôlé | Verdict exact |
|---|---|---|
| Grujić `arXiv:2607.08866v2` (`0059`) | section 2.3, direction globale et norme de base | la lecture littérale utilise un champ unitaire global; sa petite oscillation force des moyennes non dégénérées, mais la convention sur `{omega=0}` et l'existence de cette extension ne sont pas produites par la vorticité |
| Bradshaw–Grujić 2015 (`0083`) | direction de vorticité et `tilde-bmo_phi` | ne formule pas un théorème de prolongement `S²`-valué depuis un ensemble actif arbitraire |
| Jones 1980 (`0074`) | extension BMO depuis un domaine uniforme | préserve une norme BMO à valeurs vectorielles, mais ni un ensemble actif arbitraire, ni la contrainte de sphère, ni automatiquement le poids logarithmique |
| Lei–Ren–Tian `arXiv:2501.08976v1` (`0061`) | cône fixe et critère pairwise | les quantificateurs portent intrinsèquement sur la vorticité non nulle; une exclusion de petit ensemble en mesure ne donne pas le cône ponctuel requis |
| Miller 2021 (`0089`) | champ de plan auxiliaire | évite la convention aux zéros en supposant un champ auxiliaire régulier et une norme critique transverse; log-BMO seul ne fournit ni son gradient ni cette norme |

Correction du cycle 0023 : pour un champ global `S²`-valué `Xi`,
`average_B|Xi-(Xi)_B|²=1-|(Xi)_B|²`. Une petite oscillation quadratique fournit
donc bien un axe local. Les incréments dyadiques restent `O(1/k)` et leur série
diverge; aucun axe limite ni cône fixe n'en résulte. Aucune source primaire
inspectée ne ferme le raccord depuis la direction définie seulement sur
`{omega!=0}` vers une même extension globale unitaire log-BMO uniforme en
temps. Aucun nouvel identifiant de source n'est ajouté au cycle 0024.

## Audit ciblé du cycle 0025 — idempotents VMO, analyticité et blobs

| Source primaire | Passage contrôlé | Verdict exact |
|---|---|---|
| Brezis–Nirenberg 1995 (`0090`) | §I.5 et lemme A.7 | l'image essentielle VMO sur un connexe est connexe; la composition uniformément continue préserve VMO |
| Bourgain–Brezis–Mironescu 2015 (`0091`) | introduction, formules (0.2)–(0.4) | une fonction entière VMO est constante; les indicatrices ont une oscillation pairwise explicite |
| Grujić–Kukavica 1998 (`0092`) | analyticité spatiale à temps positif | pendant l'intervalle classique, une vorticité non triviale est analytique; son lieu nodal commun est nul en mesure par le fait analytique standard |
| Herbst–Skibsted 2009 (`0093`) | estimations d'analyticité | corroboration en classes fortes de Sobolev; prépublication v1, aucune portée au temps singulier |
| Feng–Šverák 2015 (`0094`) | problème de Cauchy des vortex rings | donnée mesure circulaire et solution axisymétrique sans swirl; ce n'est pas un blob isotrope critique |
| Gallay–Šverák 2019 et 2024 (`0095`–`0096`) | unicité filamentaire et limite de viscosité | anneaux visqueux rigoureux, mais un cœur mince à rayon majeur fixe n'a pas de borne uniforme faible-`L^(3/2)` |

Pour `zeta=xi 1_A`, `|xi|=1` sur `A`, et
`theta_B=|A intersection B|/|B|`, la dérivation élémentaire donne

```text
theta_B(1-theta_B)<=average_B|zeta-zeta_B|.
```

Elle interdit des densités intermédiaires uniformes sous un module VMO, mais
ne crée pas ce module. Correction des cycles 0020–0024 : pour une solution
forte non triviale à temps positif sur `R³`, les choix qui diffèrent seulement
sur `{omega=0}` sont égaux presque partout; l'obstacle pertinent devient le
comportement de phase **près** des zéros. Cette correction ne s'applique pas
automatiquement à une solution faible au temps terminal ni à une donnée
initiale compacte.

Le train du cycle 0025 montre séparément que divergence, énergie finie,
faible-`L^(3/2)`, masse critique et petite oscillation centrée ne produisent
pas le BMO global. Une forme directionnelle interne récurrente conserve une
oscillation positive sur des boules décentrées. Aucune source primaire trouvée
ne transforme un tel train en scénario dynamique de blow-up.

## Audit ciblé du cycle 0026 — compensation conique et return-flow

| Source primaire | Passage contrôlé | Verdict exact |
|---|---|---|
| Lorentz 1950 (`0097`) et O'Neil 1963 (`0067`) | réarrangement et faible-`L^p` | pour la quasi-norme de distribution fixée, `integral_E f<=p'K|E|^(1/p')`; la constante vaut exactement trois à `p=3/2` |
| Grujić–Guberović 2010 (`0098`) | cohérence directionnelle localisée | critère projectif pairwise, insensible au signe `+e/-e`; aucune masse conique orientée ni compensation globale |
| Smirnov 1993/1994 (`0099`) | décomposition de charges solénoïdales | formalise le retour par solénoïdes élémentaires, sans contrôle faible-Lorentz, BMO, Biot–Savart ou lissage compact |
| Daneri–Székelyhidi 2017 (`0100`) | Mikado flows | contre-courants tubulaires périodiques de vitesse Euler; pas une vorticité compacte NS et aucun raccord Clay |
| Enciso–Peralta-Salas 2015 (`0101`) | tubes de vorticité fermés | retour géométrique dans des champs de Beltrami Euler non compacts et d'énergie infinie; hors classe visqueuse énergétique |

La veille ne trouve aucune source primaire qui assemble la borne faible-
Lorentz pondérée, la compensation conique et l'identité des parties positive
et négative. Le lemme renforcé

```text
MO_D(zeta)>=2alpha³m³/(27K³|D|)
```

reste donc une `AI_DERIVATION` interne composée de briques classiques, jamais
un `PAPER_PROOF`. Sa constante globale n'est pas annoncée optimale. L'identité
`integral curl U=0` est globale; sur une boule, le terme de bord
`integral_(partial B)n cross U` interdit une localisation silencieuse.

Les critères de Constantin–Fefferman, Beirão da Veiga–Berselli, Miller et
Lei–Ren–Tian ne ferment pas ce trou : les trois premiers mécanismes sont
projectifs ou exigent un champ auxiliaire régulier, et le dernier autorise un
double cône contenant simultanément `+e` et `-e`. Les antécédents constructifs
ferment les lignes de flux, mais dans Euler, sur le tore ou hors énergie. Le
premier test transférable reste donc un curl compact explicite avec contrôle
de toutes les boules.

## Audit ciblé du cycle 0027 — potentiel axisymétrique et retour compact

| Source primaire | Statut et passage contrôlé | Verdict transférable |
|---|---|---|
| Liu–Wang 2009 (`0102`) | publié; représentation par swirl et fonction de courant, conditions au pôle | justifie `U=psi e_theta`, `W=curl U` et l'admissibilité lisse loin de l'axe; aucune borne Lorentz/BMO ni dynamique |
| Costabel–McIntosh 2010 (`0103`) et Guzmán–Salgado 2021 (`0111`) | publiés; homotopies de de Rham, support et dépendance géométrique des constantes | un correcteur div–curl compact existe dans les classes indiquées, mais son coût n'est pas uniforme sous aspect dégénérant et sa direction n'est pas préservée |
| Norbury 1972 (`0104`), Cao–Zhan 2026 (`0105`) et Guo–Jeong–Zhao 2026 (`0106`) | deux articles publiés et un arXiv v1; anneaux Euler axisymétriques | géométrie torique utile, mais vorticité toroïdale sans swirl ou système Euler avec swirl; aucun `W` poloïdal NS transféré |
| Gavrilov 2019 (`0107`) et Constantin–La–Vicol 2019 (`0108`) | publiés; champs Euler stationnaires lisses compacts | la compacité simultanée vitesse–vorticité est possible, mais `-nu Delta u` interdit le raccord stationnaire à NS non forcé |
| Peralta-Salas–Slobodeanu 2026 (`0109`) | arXiv v1; symétrie des écoulements Euler analytiques localisables | renforce la pertinence de l'axisymétrie sous hypothèses fortes; prépublication Euler, aucun transfert Clay |
| Chen–Fang–Zhang 2017 (`0110`) | publié; critères sur le swirl et petite donnée `L3` | contrôle publié du cas axisymétrique avec swirl, conditionnel; ne valide aucune revendication 2026 de grandes données |

La veille différentielle ajoute dix sources et porte le corpus à 111 entrées.
Elle confirme que l'ansatz du cycle est classique. Le seul contenu nouveau du
laboratoire reste quantitatif et porte sur les constantes Lorentz, oscillation
et résidu. Le profil lisse compact de la passe analytique réalise le scaling
cubique de l'oscillation **sur le domaine parent**, mais sa vitesse vérifie
`||U_epsilon||_3 -> 0`; il ne s'agit ni d'un profil ancien, ni d'un blow-up.

Les quatre prépublications 2026 de Shahmurov restent en quarantaine : leurs
fiches arXiv ne donnent pas de référence de revue à la date de coupure, et
aucune de leurs premières interpolations critiques, constantes ou compacités
n'a été auditée ligne à ligne. Aucun claim du laboratoire ne les utilise.

## Audit ciblé du cycle 0028 — fermeture toroïdale et propagation

- Les résultats sur les anneaux axisymétriques sans swirl (`NS-SRC-0022`,
  `0094`–`0096`, `0106`) confirment la géométrie et la régularité de la
  sous-classe; ils ne fournissent pas le lemme log-BMO du laboratoire.
- Les conventions de log-BMO de Bradshaw–Grujić et Grujić (`0059`, `0080`,
  `0082`, `0083`) ne sont pas identiques : cubes avec ancre `L1` et boules
  avec ancre `L-infinity` ne partagent pas leurs constantes sans raccord.
- Aucune source primaire ciblée n'assemble tore mince, rotation
  `e_theta -> e_z`, contrôle all-ball et normalisation critique. Le résultat
  reste `AI_DERIVATION`, antériorité non trouvée, jamais nouveauté
  bibliométrique affirmée.
- Le corridor protège l'axe seulement à l'instant statique. Pour un anneau
  unisigné exactement axisymétrique sans swirl sur `R^3`, le principe du
  maximum réactive `e_theta` pour `r>0` à `t>0`; le calcul axial donne une
  oscillation exactement un. Pas de transfert automatique à la périodisation
  cubique ni aux vorticités signées.
- La veille 2025–2026 ne révèle aucune singularité NS incompressible 3D
  admissible ni validation publiée du mécanisme log-BMO récent. Les préprints
  cités restent classés `PREPRINT_CLAIM`. `NS-SRC-0112` indexe en particulier
  la v3 de Grujić sur le scénario Moffatt–Kimura, sans importer sa conclusion.

## Audit ciblé du cycle 0029 — paires signées et moments

- L'identité d'impulsion et l'expansion multipolaire utilisées par le cycle
  sont recalculées dans les rapports; `NS-SRC-0068` fixe le cadre Biot–Savart,
  sans promouvoir la dérivation interne en `PAPER_PROOF`.
- Cinq sources récentes sont ajoutées : Choi–Jeong (`0113`), Lim–Jeong
  (`0114`) et Gustafson–Miller–Tsai (`0115`) sont publiées; Egamberganov–Yao
  (`0116`) et Cao–Fan–Qin v4 (`0117`) restent des prépublications. Toutes
  concernent Euler axisymétrique sans swirl et la croissance à temps infini.
- Aucun de ces résultats ne fournit un blow-up Navier–Stokes à viscosité
  positive. L'ordre des limites dans la comparaison visqueuse de Choi–Jeong
  est `sup_t` avant `nu->0`, pas une explosion à viscosité fixée.
- Pour une paire NS coaxiale, impaire et signée, le principe du maximum donne
  à temps positif deux demi-boules de directions opposées; l'oscillation sur
  une boule coupant le plan nodal vaut exactement un. La paire transversale du
  claim n'est pas couverte par cette symétrie.
- Kato (`0010`) porte sur `R3`. Le seuil de petite donnée `L3(T3)` est standard
  par semi-groupe, mais son énoncé primaire exact et ses constantes restent
  une dette; Giga–Miyakawa n'est pas ajouté sans audit du domaine.

## Audit ciblé du cycle 0030 — cardinal croissant et potentiel poreux

- Yamazaki (`0118`) est ajouté comme source publiée pour l'existence globale
  et l'unicité de petites solutions dans faible-`L^n`. Il justifie seulement
  le rejet perturbatif du stacking normalisé; le seuil dépend du domaine, de
  la viscosité et de la norme et n'est pas évalué dans ce cycle.
- Buttà–Cavallaro–Marchioro (`0119`) traite `N` anneaux Euler axisymétriques
  sans swirl dans une limite d'épaisseur, avec `N` fixé. Le résultat ne fournit
  aucune constante uniforme lorsque `N->infinity`.
- Gancedo–Hidalgo-Torné (`0120`) donne une dynamique Navier–Stokes globale
  pour un filament hélicoïdal mesure, sous symétrie forte. Guerra–Musso
  (`0121`) et Averkiou–Musso (`0122`) sont publiés pour Euler hélicoïdal;
  Averkiou–Musso–Yu (`0123`) reste une v1. « Support transverse compact » ne
  signifie jamais support compact dans `R^3`.
- Fontelos–Ispizua–Vega (`0124`) est une v1 visqueuse récente : `nu t<<1`,
  petite circulation relative et contrôle Morrey. Elle construit un régime
  régulier de filament/soliton, pas un blow-up.
- Hedberg (`0125`) et Lieb (`0126`) sourcent les deux outils de potentiel.
  La constante 9 du découpage dyadique tronqué et la combinaison donnant
  `(h/q)^(4/3)` restent des dérivations internes. Adams–Hedberg (`0127`) est
  une monographie de contexte, non une source primaire pour ce nouveau lemme.

La veille ajoute dix entrées et porte le corpus à 127 sources. Aucun article
primaire 2025–2026 inspecté ne propage un packing de variation totale uniforme
pour un cardinal croissant de tubes Navier–Stokes. La mesure filamentaire a
une croissance locale de dimension un; l'hypothèse cubique n'est utilisable
qu'après troncature au rayon du coeur et contrôle séparé de la partie proche.

Le résultat `NS-POROUS-MANY-TORUS-L3-COLLAPSE` est donc une dérivation interne
fondée sur des outils sourcés, pas un théorème cité. Le contre-profil compact
sépare exactement `L^3` fort et les endpoints faibles, mais il reproduit
l'oscillation directionnelle du bloc de base. Aucun transfert vers le problème
Clay ne suit sans propagation temporelle et contrôle de la pression.

## Audit ciblé du cycle 0031 — swirl compact et rapport d'aspect

- `NS-SRC-0059` est toujours la v2 de Grujić, soumise le 9 juillet et révisée
  le 13 juillet 2026. Son énoncé est conditionnel à une concentration critique
  et à une hypothèse directionnelle; il ne produit pas cette géométrie depuis
  les données Clay.
- `NS-SRC-0061` est toujours la v1 de Lei–Ren–Tian. Le domaine est un cylindre
  parabolique local, la notion une solution faible adaptée, et la conclusion
  un critère de régularité sous double cône. Ce n'est pas une construction de
  curl compact ni un théorème sur des profils séparables.
- Les articles de direction de vorticité et de log-BMO déjà indexés
  (`0080`, `0082`, `0098`) fournissent des critères conditionnels ou des outils
  de localisation. Ils ne donnent aucune constante uniforme pour une famille
  dont les rapports `a/R` et `b/R` dégénèrent.
- Liu–Wang (`0102`) justifie la régularité cylindrique de l'ansatz loin de
  l'axe; Guzmán–Salgado (`0111`) rappelle que les opérateurs div–curl portent
  des constantes géométriques. Aucun des deux n'énonce le budget Lorentz du
  cycle.
- Chemin–Gallagher–Paicu (`0128`) montre que des grandes données lentement
  variables sur `T^2×R` peuvent être globalement régulières. Cette anisotropie
  structurée est un comparateur adverse, pas un raccord au profil compact.
- Lei–Zhang (`0129`) contrôle la magnitude de `ru^theta` par une condition
  critique, et Liu (`0130`) suppose une petite composante swirl dans des
  espaces critiques. Aucun ne contrôle le log-BMO de la direction de `curl U`.
- Peralta-Salas–Wan (`0131`) construit une section hélicoïdale anisotrope pour
  Euler stationnaire piècewise lisse. La viscosité nulle et le support non
  compact dans `R^3` empêchent tout transfert Clay.
- Le résultat `NS-COMPACT-SWIRL-ASPECT-ENDPOINT-GATE` est donc une dérivation
  interne auditée, jamais `PAPER_PROOF`. Il exclut seulement un profil produit
  séparable et ne se transfère pas à une solution de Navier–Stokes en temps.

La veille ajoute `NS-SRC-0128`–`0131` et porte le corpus à 131 sources. Les
pages primaires arXiv et éditeur ont été vérifiées le 2026-08-14; aucune
publication ou version nouvelle n'était indiquée pour `0059` et `0061`.

## Audit ciblé du cycle 0032 — superposition et support méridien

- Fleming–Rishel (`0132`) fournit la formule de coaire. Pour
  `U=(q/r)e_theta`, le jacobien cylindrique donne exactement
  `||curl U||_1=2pi TV(q)`. La variation pertinente est celle de la somme
  réelle; elle ne se décompose pas coercivement en variations de couches.
- Bourgain–Brezis (`0133`) et Van Schaftingen (`0134`) sourcent les gains
  limites des systèmes div–curl/Hodge et des opérateurs canceling. Leur sens
  contrôle un potentiel par la donnée différentielle totale; il n'interdit
  pas l'annulation algébrique de couches opposées.
- Spector–Van Schaftingen (`0135`) atteint `L^(n/(n-1),1)` pour certaines
  classes du premier ordre. Le quantificateur « certaines » interdit toute
  promotion en ledger universel de curls superposés.
- Le lemme `NS-THIN-PURE-SWIRL-LORENTZ-COLLAPSE` utilise plutôt le potentiel
  bidimensionnel du gradient total, le weak HLS et l'inclusion de support
  fini. Une passe indépendante valide aussi le weak HLS par interpolation de
  deux estimations HLS fortes.
- Le résultat couvre tout swirl pur compact séparé de l'axe dont l'aire
  méridienne est `o(R^2)`. Il ne couvre ni une section épaisse, ni une vitesse
  poloïdale, ni une évolution ou une pression Navier–Stokes.
- Grujić `2511.00725v3`, Lei–Ren–Tian `2501.08976v1`, Grujić
  `2607.08866v2` et les annonces Shahmurov restent aux versions et quarantaines
  consignées; aucun statut publié nouveau n'a été trouvé.

La veille ajoute `NS-SRC-0132`–`0135` et porte le corpus à 135 sources. Ces
quatre entrées sont des outils publiés d'analyse géométrique ou harmonique,
pas des résultats nouveaux sur l'équation de Navier–Stokes.

## Audit ciblé du cycle 0033 — degré, VMO et gate directionnel

- Hopf (`0136`) et Whitney (`0139`) sourcent la rotation de la tangente et le
  nombre de rotation des courbes planes régulières. Ces invariants ne
  minorent ni le reach, ni l'arc où tourne la tangente, ni la magnitude du
  gradient.
- Amann (`0137`) donne l'indice local `+1` du gradient à un minimum isolé. En
  dimension deux, le même indice vaut pour un maximum après changement de
  signe. L'isolement du zéro critique reste une hypothèse indispensable.
- Brezis–Nirenberg Part II (`0138`) fournit degré, trace et image essentielle
  pour les applications VMO sur un domaine à bord. Le cycle en déduit, comme
  dérivation interne, qu'une direction de gradient de degré non nul n'est pas
  VMO et échoue donc au log-BMO aux petites échelles.
- Ce résultat topologique reste qualitatif : il ne fournit ni rayon relié au
  coeur, ni masse locale de vorticité, ni constante dépendant seulement de
  `K_u/K_w`. Il ne source donc pas le claim quantitatif du cycle.
- La borne
  `MO_B>=c_Lambda(K_u/K_w)^6` vient indépendamment de la troncature signée,
  du weak HLS, de la coaire et de la compensation conique. Elle reste une
  dérivation IA `COMPUTATION_ONLY`, même après les passes contradictoires.
- Lei–Ren–Tian `2501.08976v1`, Grujić `2607.08866v2` et Grujić
  `2511.00725v3` sont inchangés à la date de gel; aucune source récente
  inspectée ne couple degré et masse faible-`L^(3/2)` localisée.

La veille ajoute `NS-SRC-0136`–`0139` et porte le corpus à 139 sources. Les
textes sont des outils topologiques publiés, sans implication directe vers
une solution globale ou un blow-up admissible de Navier–Stokes.

## Audit ciblé du cycle 0034 — profils et sélection de cellule

- Lions (`0140`) organise compacité, évanescence et dichotomie pour des
  mesures et suites minimisantes. La dichotomie n'est pas exclue sans
  structure variationnelle; aucune paire `U/curl U` n'est synchronisée.
- Solimini (`0141`), Gérard (`0142`), Jaffard (`0143`), Koch (`0144`) et
  Bahouri–Cohen–Koch (`0145`) décomposent des suites bornées dans un espace
  source plus fort. Ils ne transforment pas les seules bornes cibles
  `L^(3,infinity)` et `L^(3/2,infinity)` en une cellule commune.
- Le même indice secondaire faible est une frontière réelle : la source
  Bahouri–Cohen–Koch montre l'échec de son hypothèse d'approximation sur un
  empilement multi-échelle, mais conjecture seulement l'échec de toute
  décomposition générale. Ce statut n'est pas renforcé dans le catalogue.
- Barker–Prange (`0146`, `0147`) fournissent le raccord dynamique publié le
  plus proche. Sous Type I et singularité supposée, ils localisent vitesse
  critique et enstrophie près d'un même centre. Ils ne prouvent pas la
  sélection statique aux deux endpoints faibles et ne couvrent pas Type II.
- La localisation de Biot–Savart conserve un champ lointain critique; un
  cutoff crée `nabla chi cross U` et un défaut de divergence. Les profils de
  `U` et de `W` ne sont donc pas synchronisés par une coupure formelle.
- Le cycle réfute exactement la sélection fondée sur les seules quasi-normes,
  puis la rétablit sous le registre BV
  `integral_(Q_j)|W_j|>=cA_jv_j^(2/3)`. Cette implication est une dérivation
  interne, pas un théorème attribué aux sources de profils.

La veille ajoute `NS-SRC-0140`–`0147` et porte le corpus à 147 sources. Les
prépublications récentes surveillées restent aux versions consignées; aucune
ne ferme le gap de cellule faible-Lorentz statique.

## Audit ciblé du cycle 0035 — coaire 3D et bandes dynamiques

- Fleming–Rishel (`0132`) fournit la formule de coaire; Federer–Fleming
  (`0148`) fournit l'isopérimétrie globale tridimensionnelle. Ensemble, ces
  briques donnent sur la bande
  `lambda/4<sigma F_j<lambda/2` une masse
  `integral|curl U_j|>=c lambda V_(j,sigma)^(2/3)`.
- La bande n'est pas un halo contenant le superniveau. Son volume est contrôlé
  parce qu'elle est incluse dans `{|U|>lambda/6}`. Les sources ne sélectionnent
  ni le niveau global `lambda`, ni une cellule : cette composition reste une
  dérivation interne.
- Korte–Lahti (`0149`), Lions limite II (`0150`), Calderón–Zygmund (`0151`)
  et Coifman–Fefferman (`0152`) sont des analogues de localisation,
  concentration ou good-lambda. Aucun n'est nécessaire à la preuve et aucun
  ne couple automatiquement `U` et `curl U`.
- Li–Ozawa–Wang (`0153`), Barker (`0154`) et
  Barker–Fernández-Dalgo–Prange (`0155`) localisent des quantités critiques
  pour de vraies solutions Navier–Stokes sous hypothèse de blow-up, Type I ou
  géométrie parabolique. Ils ne fournissent pas la sélection statique des deux
  endpoints faibles.
- La constante du lemme interne est
  `(36pi)^(1/3)/324` sous les conventions du registre; aucun résultat source
  n'est promu ni réinterprété comme cette nouvelle inégalité.

La veille ajoute `NS-SRC-0148`–`0155` et porte le corpus à 155 sources. Aucun
théorème littéral identique n'a été trouvé dans le périmètre primaire ciblé;
ce résultat négatif de recherche n'est pas une preuve d'absence absolue.

## Audit ciblé du cycle 0036 — composantes BV, boule locale et centres multiples

- Ambrosio–Caselles–Masnou–Morel (`0156`) fournit la décomposition en
  composantes M-indécomposables et l'additivité du périmètre. Avec
  isopérimétrie, une dérivation interne sélectionne une composante de volume
  `>=c(V/P)^3`; aucun diamètre n'en découle.
- Besicovitch (`0157`) contrôle une multiplicité de recouvrement, sans créer
  de masse locale. Fusco–Maggi–Pratelli (`0158`) donne presque une boule
  seulement sous petit déficit isopérimétrique, hypothèse absente du ledger
  endpoint.
- L'équation (2.2) de Frank–Lieb (`0159`) implique exactement une boule de
  rayon `V/P` captant `>=c(V/P)^3`. La fraction `cV^2/P^3` est optimale en
  échelle pour `N` gouttes égales et peut tendre vers zéro.
- Seregin (`0160`, `0161`) et Barker (`0162`) traitent plusieurs points
  singuliers de vraies solutions adaptées ou Leray–Hopf. Barker obtient
  `O(M^20)` sous borne faible-`L3` le long d'une suite de temps; pression,
  epsilon-régularité et budget espace-temps sont indispensables.
- Aucun de ces textes ne donne le lemme pure-swirl du cycle : la troncature
  signée de chaque composante à `lambda/4`, la constante `C_I/648` et le
  raccord au gate directionnel lipschitzien restent des dérivations internes.
- Translation, fragmentation et tube mince réfutent respectivement le
  confinement global, la capture d'une fraction universelle depuis `V,P`,
  et le diamètre borné d'une composante indécomposable.

La veille ajoute `NS-SRC-0156`–`0162` et porte le corpus à 162 sources. Les
pages primaires EMS, Annals, arXiv, MathNet, AMS et les DOI ont été contrôlés
le 2026-08-14. Aucun résultat récent vérifié ne supprime l'hypothèse critique
additionnelle des théorèmes multi-centres ou ne ferme le cas Type II général.

## Audit ciblé du cycle 0037 — diamètre planaire et persistance des ponts

- Dayrens–Masnou–Novaga–Pozzetta (`0163`) prouvent au lemme 2.13
  `2 diam(E^1)<=P(E)` pour tout ensemble planaire M-indécomposable de mesure
  positive finie. Le représentant de densité un est indispensable; un
  filament nul ajouté à un représentant arbitraire réfuterait la version
  topologique naïve.
- Leur théorème 4.1 représente aussi le périmètre connecté relaxé par
  `P(E)+2 St(E)` sous ses hypothèses. Une connexion planaire de largeur nulle
  conserve donc un coût de longueur de Steiner; cela ne donne aucune durée de
  persistance en amplitude.
- Fleming–Rishel (`0132`) et Ambrosio–Caselles–Masnou–Morel (`0156`), combinés
  à `0163`, donnent par dérivation interne la somme des diamètres essentiels
  intégrée sur les niveaux. La constante axisymétrique `9/(8pi)` du claim
  n'est énoncée dans aucune de ces sources.
- Carr–Snoeyink–Axen (`0164`) suivent les fusions de superniveaux PL par
  join/contour trees; Edelsbrunner–Letscher–Zomorodian (`0165`) mesurent la
  durée de vie des classes d'une filtration. Aucun des deux ne certifie
  diamètre, périmètre, erreur continuum ou PDE.
- Bonicatto–Lahti–Pasqualetto (`0166`, arXiv v1) caractérisent récemment
  l'indécomposabilité via un représentant connexe en topologie 1-fine. Cette
  clarification BV n'est pas nécessaire pour les superniveaux lisses du
  cycle et ne fournit pas de nouvelle constante.
- Chan (`0167`, arXiv v1) annonce une régularité globale axisymétrique sous
  petitesse critique dans un cylindre fini avec conditions
  Navier–Hodge–Lions. Domaine, frontière, symétrie et petitesse empêchent tout
  transfert aux cas Clay `R3` ou `T3`; seule la page primaire arXiv a été
  auditée, pas la preuve ligne à ligne.
- Aucun analogue Navier–Stokes primaire inspecté ne combine merge tree
  métrique, coaire méridienne, pression et évolution. Les filaments réguliers
  et théorèmes multi-centres existants restent des comparateurs conditionnels.

La veille ajoute `NS-SRC-0163`–`0167` et porte le corpus à 167 sources. Les
textes primaires, pages éditeurs, DOI et métadonnées arXiv ont été contrôlés le
2026-08-15. Le résultat du cycle reste une dérivation IA statique
`COMPUTATION_ONLY`, jamais un résultat Clay.

## Audit ciblé du cycle 0038 — stabilité topologique et sélection adaptative

- Cohen-Steiner–Edelsbrunner–Harer (`0168`) donnent la stabilité bottleneck
  des diagrammes de persistance sous erreur uniforme. Une longue barre H0
  contrôle `maximum-col`, pas la marge `col-cutoff` requise par le pont.
- Cardona–Curry–Lam–Lesnick (`0169`) donnent une métrique stable et universelle
  sur les merge trees finis. L'entrelacement ne fournit ni labels spatiaux,
  ni diamètre, ni coaire.
- Bauer–Landi–Mémoli (`0170`) traitent les graphes de Reeb PL. Ce ne sont pas
  les join trees de superniveaux, et leur stabilité ne règle pas le passage
  BV modulo presque-partout.
- Kimura et al. (`0171`) appliquent une structure Reeb/COT à des simulations
  Navier–Stokes incompressibles 2D périodiques. Dimension, stretching,
  pression et certification continuum empêchent tout transfert vers Clay.
- Le certificat continuum minimal d'un calcul PL est un niveau maximin de
  deux coeurs spatiaux, accompagné de `||F-F_h||_infinity<=epsilon`; le barcode
  seul est insuffisant.
- Le lemme positif du cycle n'utilise finalement aucun arbre discret : coaire,
  diamètre planaire, isopérimétrie 3D et Lorentz sélectionnent directement un
  niveau régulier et une composante au même niveau.

La veille ajoute `NS-SRC-0168`–`0171` et porte le corpus à 171 sources. Les
textes primaires LIPIcs/arXiv, page éditeur et DOI ont été contrôlés le
2026-08-15. Aucun théorème source ne contient la composition axisymétrique du
cycle; elle reste `COMPUTATION_ONLY`.

## Audit ciblé du cycle 0039 — endpoint ondelettes, annulation et veille forcée

- Le plein `L^(p,infinity)` est non séparable : une famille non dénombrable
  de fonctions à supports disjoints reste uniformément séparée dans la boule.
  Il ne peut donc posséder de base de Schauder dénombrable norm-convergente.
- Karlovich (`0172`) suppose explicitement un espace de fonctions de Banach
  séparable; son application Lorentz impose `q<infinity`. Elle ne couvre pas
  les endpoints actifs `L^(3,infinity)` et `L^(3/2,infinity)`.
- Stein (`0173`) et l'interpolation de Hunt (`0069`) contrôlent un
  carré-fonction faible-Lorentz du **champ total**. Une paire `+Z_n,-Z_n`
  s'annule avant la projection fréquentielle : cet outil ne sélectionne pas
  une composante spatiale étiquetée.
- Deriaz–Perrier (`0174`) fournit des ondelettes divergence-free/curl-free et
  un algorithme de Hodge 2D/3D. Le texte ne démontre ni base inconditionnelle
  du plein endpoint, ni minoration de Gram, ni erreur continuum certifiée.
- Sous cutoff, l'identité exacte
  `curl P(chi U)=chi curl U+nabla chi cross U` conserve un terme de col
  critique, tandis que la correction de Leray reste non locale. La projection
  ne crée pas de positivité entre cellules.
- Beirão da Veiga–Yang (`0175`, arXiv v1) annonce une perte de bornitude pour
  Navier–Stokes incompressible **forcé** dans un cylindre avec conditions
  mixtes. La force `L1_tL2_x` devient singulière au temps terminal et la
  convection est absorbée par la pression : aucun blow-up non forcé sur
  `R3`/`T3`, donc aucun transfert Clay.
- Une prépublication compressible Navier–Stokes–Korteweg du 2026-08-11 a été
  filtrée sans promotion : densité, capillarité et viscosités variables la
  placent hors du système Clay.

La veille ajoute `NS-SRC-0172`–`0175` et porte le corpus à 175 sources. Les
pages et textes primaires ont été contrôlés le 2026-08-15. Le résultat du
cycle reste un contre-théorème cinématique interne; aucune base, simulation ou
prépublication récente ne ferme la pression, le temps ou le passage au
continuum.

## Audit ciblé du cycle 0040 — localisation solénoïdale sur couronne fixe

- Costabel–McIntosh (`0103`) construit un même opérateur régularisé de type
  Bogovskiĭ sur les domaines Lipschitz avec support et gain d'une dérivée.
  Une couronne n'est pas étoilée : le raccord licite passe par leur résultat
  Lipschitz/recouvrement, puis par homothétie du domaine fixé.
- Guzmán–Salgado (`0111`) suit des **majorations constructives** dépendant de
  la géométrie en `L2->H1`. Leur croissance ne prouve pas l'impossibilité
  d'un meilleur opérateur; cette ancienne ambiguïté du catalogue est corrigée.
- Acosta–Durán–Muschietti (`0176`) fournit la droite inverse sur les domaines
  de John et confirme que la géométrie gouverne les constantes.
- Albritton–Barker–Prange (`0177`) emploie effectivement Bogovskiĭ sur la
  couronne fixe `B_(15/16)\Bbar_(7/8)` dans une preuve d'epsilon-régularité
  Navier–Stokes. Cette source valide le maillon de localisation, pas la borne
  faible-L3 interne ni une conclusion globale.
- Chan–Chen–Su (`0178`, v1 2026) construit un correcteur analytique sur une
  couronne, mais sans estimation `L^p`/Lorentz quantitative identifiée.
- Isett–Mao–Oh–Tao (`0179`, v1 2025) développe des inverses à support prescrit
  dans une théorie générale; aucune spécialisation critique Navier–Stokes ne
  ferme le verrou actif.
- L'interpolation entre les exposants forts `4/3` et `2`, le transport par
  homothétie, la constante de quasi-triangle trois et la minoration
  `c_pR/h` sur une couronne mince sont des dérivations internes, jamais
  attribuées aux sources.
- Le calcul discret arXiv:2603.29018v2 reste en watchlist : il ne certifie
  aucune limite continue faible-Lorentz.

La veille ajoute `NS-SRC-0176`–`0179` et porte le corpus à 179 sources. Les
textes primaires, DOI, versions et usages ciblés ont été contrôlés le
2026-08-15. Aucun développement 2025–2026 audité ne fournit la capture
intrinsèque d'une fraction de la norme faible-`L3` à une échelle de
concentration.

## Audit ciblé du cycle 0041 — concentration Type I faible-`L3`

- Barker–Prange 2020 (`NS-SRC-0146`) est réaudité sur arXiv v2, version
  auteur acceptée et publication. Le théorème 2 est formulé en `L3`; la
  phrase suivant la concentration et l'appendice B transportent le mécanisme
  à `L^(3,infinity)`. Les constantes faibles sont donc notées séparément
  `gamma_w,S_w^*`.
- L'hypothèse exacte est une borne uniforme
  `sup_x sup_(r<r0) sup_(T_*-r^2<t<T_*) r^-1/2||u||_2<=A`. Une borne globale
  pointwise faible-`L3` l'implique avec
  `A=sqrt(3)(4pi/3)^(1/6)M`. Pour `r0=infinity`, le temps inférieur est zéro.
- Barker–Prange 2021 (`NS-SRC-0147`) minore `integral |u|^3` par un logarithme,
  pas la norme `L3` par ce logarithme. La norme ne reçoit qu'une racine
  cubique. Les constantes se détériorent fortement avec `M`, notamment
  `S^sharp(M)=O(M^-100)`.
- Le profil tronqué `a/|x|` conserve une borne faible-`L3` mais accumule une
  intégrale cubique logarithmique. C'est un contre-profil fonctionnel interne,
  non une solution Navier–Stokes.
- La veille différentielle 2025–2026 n'a trouvé aucun transfert uniforme au
  Type II ni aucune implication depuis l'énergie Clay. Les sources récentes
  pertinentes étaient déjà cataloguées sous `0032`, `0034`, `0035`, `0045`,
  `0048`, `0051` et `0059`; aucun identifiant nouveau n'est créé.

Le corpus reste à 179 sources. Le résultat positif du cycle est une fermeture
conditionnelle de la capture du numérateur Type I; le calcul de l'évolution
du cutoff et le cas Type II restent hors des articles audités.

## Audit ciblé du cycle 0042 — cutoff solénoïdal mobile

- Saari–Schwarzacher (`0180`, Annals of PDE 2023) construit et différentie
  un inverse de divergence sur des tranches dépendant du temps, avec poids de
  distance au bord. Le résultat valide le besoin d'un commutateur temporel,
  mais n'annonce aucune constante uniforme lorsqu'une tranche s'effondre.
- Wolf (`0181`, Advances in Differential Equations 2017) sépare pression
  harmonique locale et pression de force sur domaine fixe. Il interdit de
  supprimer la composante non locale lors d'une localisation, sans fournir
  de borne pour un cutoff mobile.
- Kwon (`0182`, Journal of Differential Equations 2023) utilise une
  projection de Leray localisée et une décomposition `u=v+h` pour des
  solutions dissipatives. Le cutoff est fixe et la force perturbative reste
  liée à la solution : aucun endpoint contractant n'est couvert.
- Breit (`0183`, Journal of Differential Equations 2025) traite
  Navier–Stokes sur un domaine physique mobile non dégénéré. Son hypothèse de
  vitesse de bord en `L3_t` exclut exactement
  `R'(t)~(T_*-t)^(-1/2)`.
- Zhang (`0184`, arXiv:2411.13896v3) revendique un blow-up pour une équation
  **forcée**. Sa convention critique `3/p+2/q=2` est celle du potentiel de
  chaleur, non l'invariance de la force `2/q+3/p=3`; aucun transfert à Clay
  non forcé n'est admis.
- La conjugaison interne sur la couronne homothétique donne des constantes
  spatiales uniformes, mais la force localisée complète garde l'ordre
  `R^-3`. Toute norme forte sur la droite critique avec temps fini accumule
  un logarithme si un profil persiste.
- Aucun texte primaire 2025–2026 audité ne démontre une annulation universelle
  de la force projetée complète, ni un lissage au collapse dans l'endpoint
  faible en temps correspondant.

La veille ajoute `NS-SRC-0180`–`0184` et porte le corpus à 184 sources. Les
textes primaires, DOI, versions et limites de transfert ont été contrôlés le
2026-08-15. Le résultat du cycle est une identité conditionnelle et un test
d'échelle interne, pas un théorème de régularité publié.

## Audit ciblé du cycle 0043 — force critique en espace négatif

- Costabel–McIntosh (`0103`) construit sur un domaine lipschitzien un
  opérateur préservant le support et pseudodifférentiel d'ordre `-1`; son
  théorème 4.6 donne l'action dans les espaces de Sobolev de tout ordre. Le
  calcul des ordres `[Delta,B]` et `[B,y·nabla]` relève ensuite du calcul
  symbolique standard : cette inférence est interne et non un énoncé cité
  mot pour mot.
- Geißert–Heck–Hieber (`0185`) énonce exactement
  `B:W_0^{s,p}->W_0^{s+1,p}` pour `s>-2+1/p`. Le choix
  `s=-1,p=4/3` ferme le pont négatif requis par le défaut de pression.
- La notation des auteurs est essentielle : leur `W_0^{-1,p}` est le dual de
  `W^{1,p'}`, donc plus petit que le dual usuel de `W_0^{1,p'}`. Ici le défaut
  est de support strictement intérieur et de moyenne nulle; ces deux
  compatibilités sont vérifiées avant d'appliquer le théorème.
- Saari–Schwarzacher (`0180`) confirme indépendamment la formule intégrale
  de Bogovskii et le gain d'une dérivée pour tout ordre sur la géométrie
  qu'ils considèrent, mais leur cadre mobile n'apporte pas la compacité de la
  force quand la couronne s'éloigne.
- La veille différentielle n'a identifié aucun article primaire 2025–2026
  qui transforme une borne dans
  `L1+div L^(3/2,infinity)` en disparition locale de la force, ni en théorème
  de rigidité ancienne non forcée.

La veille ajoute `NS-SRC-0185` et porte le corpus à 185 sources. La borne
critique uniforme du cycle est une dérivation interne conditionnée au choix
fixe de l'opérateur; elle ne fournit ni petitesse, ni compacité, ni limite
ancienne non forcée.
