# Cycle 0008 — veille primaire : unicité finale, solutions anciennes et traces

Date de vérification : 2026-08-14.

## Périmètre et méthode

Cette veille est indépendante de la dérivation analytique du cycle. Elle cible
les sources primaires portant sur :

- l'unicité rétrograde et l'unicité à donnée finale ;
- les solutions Navier–Stokes anciennes mild et globalement bornées ;
- les théorèmes de Liouville pour ces solutions ;
- la topologie nécessaire pour donner un sens à la trace terminale.

Les métadonnées ont été vérifiées sur les pages arXiv et, lorsqu'elle existe,
sur la page primaire de l'éditeur. Des requêtes arXiv ordonnées par dernière
mise à jour ont été lancées sur `backward uniqueness`, `final data`, `ancient`,
`ancient mild`, `bounded ancient`, `Liouville` et `terminal trace`, avec
`Navier-Stokes`. Une absence dans ces requêtes est seulement un résultat de
veille négatif, pas une preuve d'absence dans toute la littérature.

## Résultat différentiel

### 1. Statut corrigé du résultat directement applicable

Zhen Lei, Zhaojie Yang et Cheng Yuan, *Backward Uniqueness for 3D
Navier–Stokes Equations With Non-Trivial Final Data and Applications* :

- [arXiv:2311.02429v1](https://arxiv.org/abs/2311.02429), soumis le
  2023-11-04, sans nouvelle version arXiv ;
- article publié dans *International Mathematics Research Notices*, volume
  2024, no 20, pages 13417–13431, publié en ligne le 2024-09-24,
  [DOI 10.1093/imrn/rnae208](https://doi.org/10.1093/imrn/rnae208).

Le statut « prépublication seulement » serait donc incorrect. La date
« August 11, 2026 » actuellement rendue dans l'HTML expérimental arXiv n'est
pas une révision : l'historique primaire reste uniquement `v1`, datée de 2023.

Le théorème 1.1 porte sur deux solutions mild bornées de Navier–Stokes 3D sur
`R^3 x [0,T]`, avec la même force et la même donnée finale **comme fonction
bornée**. Sous bornitude des deux vorticités, leur vitesse et leur gradient de
pression coïncident sur tout l'intervalle. Pour la force nulle, la remarque 1.1
indique que la régularisation mild fournit la régularité de vorticité requise.
La définition 2.1 impose la formule de Duhamel/Leray sur chaque sous-intervalle.

Ce résultat ne dit pas littéralement qu'une convergence dans `D'` vers zéro
est une donnée terminale nulle. Ce raccord reste à démontrer avant application.

### 2. Pont exact vers le lemme candidat

Lemme candidat du laboratoire :

```text
u ancienne mild sur R^3 x (-infini,0),
sup |u| < infini,
u(t) -> 0 dans D'(R^3) quand t -> 0-
=> u = 0.
```

La combinaison des sources primaires réduit ce lemme à un pont de trace
élémentaire, non énoncé comme tel par leurs auteurs :

1. La définition KNSS d'une ancienne mild exige une suite `T_l -> -infini`
   telle que la formule mild soit valable sur chaque `(T_l,0)` :
   [Koch–Nadirashvili–Seregin–Šverák,
   arXiv:0709.3599v1](https://arxiv.org/abs/0709.3599), publié dans *Acta
   Mathematica* 203 (2009),
   [DOI 10.1007/s11511-009-0039-6](https://doi.org/10.1007/s11511-009-0039-6).
2. La proposition 4.1 de KNSS donne les estimations de lissage mild, notamment
   des bornes sur les dérivées spatiales et temporelles à distance positive du
   temps initial.
3. Pour tout `a<0`, choisir `T_l<a`. La borne globale de `u` et le lissage sur
   `[a,0)` donnent une borne uniforme de `partial_t u` sur cette tranche. Par
   conséquent `u(t)` possède, quand `t->0-`, une limite dans
   `L^infinity(R^3)` — donc aussi dans `D'`.
4. L'unicité de la limite distributionnelle identifie cette trace bornée à
   zéro. La solution se prolonge alors en solution mild bornée sur `[a,0]`
   avec donnée finale nulle ; sa vorticité est bornée grâce au même lissage.
5. Le théorème 1.1 de Lei–Yang–Yuan, appliqué à `u` et à la solution zéro après
   translation du temps, donne `u=0` sur `[a,0]`. Comme `a<0` est arbitraire,
   `u=0` sur tout `R^3 x (-infini,0]`.

Ainsi, **au niveau des sources**, le coeur d'unicité rétrograde n'est plus un
verrou ouvert : il existe un théorème publié exactement dans la classe mild
bornée. La seule partie propre au laboratoire est le passage de la limite
`D'` à une vraie trace bornée via l'estimation uniforme de `partial_t u`. Cette
dérivation doit rester `AI_DERIVATION`/`COMPUTATION_ONLY` tant qu'elle n'a pas
été auditée séparément ; elle ne doit pas être attribuée à Lei–Yang–Yuan.

Le pont échoue immédiatement si « mild » est remplacé par « faible » ou
« localement adaptée » : Lei–Yang–Yuan donnent eux-mêmes le contre-exemple
spatialement constant `u=(h(t),0,0)`, `p=-h'(t)x_1`, nul au temps final mais
non trivial auparavant. Il confirme indépendamment le contre-profil du cycle
0006.

### 3. Nouveau Liouville 2026 manqué au cycle précédent

Ben Pineau et Vlad Vicol, *On rotated backwards self-similar solutions of the
incompressible 3D Navier–Stokes equations*,
[arXiv:2607.09619v2](https://arxiv.org/abs/2607.09619), soumis le 2026-07-10 et
révisé le 2026-08-06. Statut au jour de la veille : prépublication, 37 pages,
« additional results and comments added » ; aucune publication n'est indiquée
par les métadonnées primaires.

Équation : Navier–Stokes incompressible 3D non forcé, viscosité normalisée à
un, sur `R^3 x [-1,0)`. Résultats pertinents :

- théorème 1.4 : une solution globalement backward rotated self-similar,
  satisfaisant `|u(x,t)| <= C/(|x|+sqrt(-t))`, est triviale lorsque la vitesse
  angulaire de rotation est suffisamment petite ou suffisamment grande ; le
  régime intermédiaire reste ouvert ;
- théorèmes 1.6–1.7 : exclusions DSS/RDSS lorsque le facteur discret est assez
  proche de un, avec restrictions supplémentaires sur la rotation ;
- théorème 1.9 : critère local de régularité sous borne Type I, pression bornée
  sur un anneau et quasi-auto-similarité quantitative à une tranche de temps.

Transfert : ce texte exclut des sous-classes substantielles de profils Type I,
mais ne concerne pas toute solution ancienne mild bornée. Il ne donne ni la
trace terminale `D'` du lemme candidat, ni une classification générale des
limites KNSS, ni une exclusion des scénarios Type II. Il ne résout donc pas le
maillon Clay général.

### 4. Sources anciennes pertinentes, statuts inchangés

- Dallas Albritton et Tobias Barker,
  [arXiv:1811.00502v2](https://arxiv.org/abs/1811.00502), dernière révision
  2019-11-18, publié dans *Journal of Mathematical Fluid Mechanics* 21 (2019),
  article 43,
  [DOI 10.1007/s00021-019-0448-z](https://doi.org/10.1007/s00021-019-0448-z).
  Leur théorème 1.2 impose une borne `L^3` le long d'une suite
  `t_k -> -infini`, non une trace terminale. Il ne s'applique pas au lemme
  candidat sous la seule borne `L^infinity_x`.
- Xinghong Pan et Zijin Li,
  [arXiv:1908.11591v2](https://arxiv.org/abs/1908.11591), publié dans *Nonlinear
  Analysis: Real World Applications* 56 (2020),
  [DOI 10.1016/j.nonrwa.2020.103159](https://doi.org/10.1016/j.nonrwa.2020.103159).
  Le résultat est axisymétrique et impose une croissance spatiale sublinéaire.
- Zhen Lei, Qi S. Zhang et Na Zhao,
  [arXiv:1701.00868v1](https://arxiv.org/abs/1701.00868), traduction anglaise
  d'un article de *Science China Mathematics* (2017). Les conclusions portent
  sur les cas 2D ou axisymétriques, avec hypothèses de vorticité ou de swirl.
- Zhen Lei, Xiao Ren et Qi S. Zhang,
  [arXiv:1911.01571v1](https://arxiv.org/abs/1911.01571), prépublication selon
  les métadonnées arXiv consultées. Le domaine est `R^2 x T`, avec
  axisymétrie ; ce n'est pas `R^3`.
- ESS reste l'article publié de 2003,
  [notice primaire MathNet](https://www.mathnet.ru/eng/rm609),
  [DOI 10.1070/RM2003v058n02ABEH000609](https://doi.org/10.1070/RM2003v058n02ABEH000609).
  Sa trace terminale forte `L^2_loc` appartient à une limite adaptée sous borne
  globale `L^infinity_t L^3_x`, pas à une ancienne mild bornée issue de KNSS.

Les nombreux résultats 2025–2026 retournés sous « Liouville Navier–Stokes »
mais consacrés aux équations stationnaires, fractionnaires, compressibles,
inhomogènes ou avec frontière ont été écartés : ils ne donnent pas l'unicité à
donnée finale pour l'équation évolutive standard. Cela inclut notamment
[Coiculescu–Yang, arXiv:2506.14533v2](https://arxiv.org/abs/2506.14533), qui
porte explicitement sur les `D`-solutions stationnaires.

## Passe contradictoire

1. **Topologie terminale.** `u(t)->0` dans `D'` ne permet pas, seule, de poser
   `u(0)=0` dans `L^infinity`. Le pont utilise réellement la borne uniforme de
   `partial_t u` fournie par le lissage mild depuis un temps strictement
   antérieur. Sans cette étape, l'application du théorème publié serait un
   changement silencieux de topologie.
2. **Bornitude de la vorticité.** Elle n'est pas déduite d'une solution faible
   bornée. Elle vient ici de la mildness ancienne et du fait que toute tranche
   finie est à distance positive d'un temps initial `T_l` antérieur.
3. **Mode de pression affine.** La mildness/Leray est indispensable ; la seule
   équation distributionnelle avec pression locale admet les solutions
   parasites spatialement constantes.
4. **Quantificateur temporel.** Le théorème Lei–Yang–Yuan agit sur un intervalle
   fini. Il faut l'appliquer sur chaque `[a,0]`, puis quantifier sur tout
   `a<0`; aucune application directe à un intervalle infini n'est revendiquée.
5. **Objet limite.** Le lemme ainsi fermé ne répare pas la non-composition du
   cycle 0007 : ESS fournit la trace nulle sans la borne ponctuelle/mildness,
   tandis que KNSS fournit mildness et bornitude avec une normalisation
   terminale non nulle.

## Verdict pour le graphe Clay

```text
ancienne NS mild globalement bornée
+ limite terminale nulle dans D'
  --[pont de trace à auditer]-->
ancienne NS mild bornée avec donnée finale L-infinity nulle
  --[Lei–Yang–Yuan, théorème publié]-->
u = 0.
```

Ce verrou de rigidité conditionnelle est très probablement fermable. Le verrou
dominant se déplace vers l'**héritage simultané**, par une même extraction de
blow-up, de la mildness, de la borne globale ponctuelle et de la trace terminale
nulle. Aucune source primaire nouvelle ou révisée trouvée jusqu'au 2026-08-14
ne fournit ce raccord, et la prépublication Pineau–Vicol ne le remplace pas.
