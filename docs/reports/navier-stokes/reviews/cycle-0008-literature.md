# Cycle 0008 — audit source-exact du lemme ancien à trace terminale nulle

Date de coupure : **2026-08-14**.

## Verdict borné

Le lemme candidat suivant est compatible avec les théorèmes publiés et son
chaînage peut être fermé sans hypothèse de pression :

> Soit `u` une solution ancienne mild de Navier–Stokes incompressible, non
> forcé, de viscosité `nu=1`, sur `R^3 x (-infinity,0)`. Si
> `M=sup_(x,t)|u(x,t)|<infinity` et si `u(t)->0` dans `D'(R^3)` lorsque
> `t->0-`, alors `u=0`.

Ce n'est pas un théorème énoncé mot pour mot dans une des sources : c'est une
**dérivation** combinant le lissage mild de KNSS, la rétro-unicité parabolique
d'ESS, le Liouville harmonique et la jauge mild de KNSS. Une seconde route,
plus directe, utilise le théorème publié de Lei–Yang–Yuan. La première route
est préférable pour l'audit, car elle ne dépend pas du traitement non local de
la pression de Lei–Yang–Yuan.

Ce lemme ne ferme pas le problème Clay : aucune extraction auditée ne transmet
simultanément à une même limite la mildness globale, la borne ponctuelle
uniforme, la trace terminale nulle et une normalisation non triviale.

## Sources primaires et statuts

| Source | Version et statut vérifiés | Localisateurs utilisés |
|---|---|---|
| G. Koch, N. Nadirashvili, G. Seregin, V. Sverak, *Liouville theorems for the Navier–Stokes equations and applications* | [arXiv:0709.3599v1](https://arxiv.org/abs/0709.3599), soumis le 2007-09-22 ; publié dans *Acta Math.* **203** (2009), 83–105, [DOI 10.1007/s11511-009-0039-6](https://doi.org/10.1007/s11511-009-0039-6) | version publiée : formule mild (3.5), noyau (3.7), pp. 88–89 ; Proposition 4.1 et (4.6), pp. 91–92 ; définition ancienne, Lemme 6.1 et Remarque 6.1, p. 98 |
| L. Escauriaza, G. Seregin, V. Sverak, *L_{3,infinity}-solutions of the Navier–Stokes equations and backward uniqueness* | article publié, *Russian Math. Surveys* **58:2** (2003), 211–250, [DOI 10.1070/RM2003v058n02ABEH000609](https://doi.org/10.1070/RM2003v058n02ABEH000609), [texte primaire MathNet](https://www.mathnet.ru/eng/rm609) | équations de vorticité (3.31)–(3.35), pp. 226–227 ; Théorème 5.1 et hypothèses (5.1)–(5.4), pp. 233–234 |
| L. Escauriaza, G. Seregin, V. Sverak, *Backward Uniqueness for Parabolic Equations* | article publié, *Arch. Ration. Mech. Anal.* **169** (2003), 147–157, [DOI 10.1007/s00205-003-0263-8](https://doi.org/10.1007/s00205-003-0263-8), [PDF primaire hébergé par l'auteur](https://www.pdmi.ras.ru/~seregin/Recent%20Publications/complementtoball.pdf) | Théorème 1, p. 149 ; domaine extérieur et croissance (1.1)–(1.2), pp. 147–149 |
| Z. Lei, Z. Yang, C. Yuan, *Backward Uniqueness for 3D Navier–Stokes Equations With Non-Trivial Final Data and Applications* | [arXiv:2311.02429v1](https://arxiv.org/abs/2311.02429), soumis le 2023-11-04 ; publié dans *IMRN* **2024:20** (2024), 13417–13431, publication en ligne le 2024-09-24, [DOI 10.1093/imrn/rnae208](https://doi.org/10.1093/imrn/rnae208) | Théorème 1.1, p. 13419 / arXiv p. 3 ; Définition 2.1 et (2.1), p. 13421 / arXiv p. 5 ; Théorème 3.1, p. 13422 / arXiv p. 6 ; Corollaire 3.3, p. 13425 / arXiv p. 9 ; preuve du Théorème 1.1, pp. 13425–13431 / arXiv pp. 9–15 |

Le champ `date` rendu aujourd'hui par l'HTML expérimental arXiv de
`2311.02429` n'est pas une nouvelle version. L'historique primaire ne contient
que `v1`, datée du 2023-11-04. Le statut publié est en revanche confirmé par la
[notice de l'éditeur](https://academic.oup.com/imrn/article/2024/20/13417/7769704),
qui donne aussi les dates de réception, révision et acceptation. Le texte
intégral de la version d'éditeur étant sous contrôle d'accès, les localisateurs
de contenu ci-dessous ont été contrôlés sur `v1`; la comparaison ligne à ligne
avec la version d'éditeur n'a pas été possible.

## 1. KNSS : formulation mild, dérivées et jauge

### Équation et domaine

KNSS considère, sur `R^n x (0,infinity)`,

```text
partial_t u + (u dot nabla)u + nabla p - Delta u = 0,
div u = 0,
u(0)=u_0,
```

avec viscosité normalisée à un et sans force. En dimension trois, c'est
l'équation du lemme après translation du temps.

### Formule mild exacte et pression

La formule (3.5), avec `f_k=-u_k u`, est la formule d'Oseen/Leray. Le noyau
différentié vérifie l'estimation (3.7)

```text
|K_ijk(x,t)| <= C (|x|^2+t)^(-(n+1)/2).
```

Elle rend le terme bilinéaire bien défini pour `u tensor u in L^infinity`.
KNSS précise, p. 89, que la définition mild ne contient pas la pression. La
projection de Helmholtz en `L^infinity` est ambiguë modulo les constantes,
mais la divergence placée devant `u tensor u` annule cette ambiguïté. Une
pression reconstruite n'est déterminée que modulo une fonction du temps.

La définition ancienne de la p. 98 exige une suite `T_j->-infinity` telle que
`u(T_j)` soit définie et que `u` soit mild sur chaque `R^n x (T_j,0)`. La
propriété de semi-groupe permet alors de redémarrer la formule à tout temps
intermédiaire `s<t<0` :

```text
u(t)=exp((t-s)Delta)u(s)
     - integral_s^t exp((t-r)Delta) P div(u tensor u)(r) dr.    (1)
```

### Estimations de dérivées

La Proposition 4.1, équation (4.6), affirme que pour `k,l>=0`

```text
|| t^(k/2+l) nabla^k partial_t^l u ||_infinity
  <= C(k,l) ||u_0||_infinity
```

sur `0<t<T'`, avec
`T'=epsilon(k,l)||u_0||_infinity^(-2)`. Le facteur temporel et la dépendance
en `||u_0||_infinity` sont essentiels.

Pour l'ancienne globalement bornée, redémarrons (1) à `s=t-h`, avec

```text
h = epsilon(k,l)/(2 M^2),   M>0.
```

Comme `||u(s)||_infinity<=M`, la fenêtre autorisée depuis `s` est au moins
`epsilon(k,l)M^(-2)`. On obtient donc, uniformément pour tout `t<0`,

```text
||nabla^k partial_t^l u(t)||_infinity
  <= C'(k,l) M^(k+2l+1).                                     (2)
```

Les constantes ne dépendent ni de `t`, ni de `T_j`, ni de la distance au bord
terminal. Le cas `M=0` est immédiat. Ce redémarrage est le point qui empêche
une dépendance cachée à une troncature temporelle.

### Jauge mild

La Remarque 6.1, p. 98, énonce qu'une ancienne mild bornée de la forme
`u(x,t)=b(t)` est constante en temps. C'est aussi immédiat dans (1) : le
semi-groupe conserve les constantes spatiales et
`div(b(t) tensor b(t))=0`, donc `b(t)=b(s)`.

Cette étape est fausse pour une solution seulement distributionnelle avec
pression. Le couple

```text
u(x,t)=b(t),   p(x,t)=-b'(t) dot x
```

est une solution classique bornée pour toute fonction régulière bornée `b`,
mais n'est mild que si `b` est constante.

## 2. ESS : théorème exact de rétro-unicité

### Théorème 5.1 dans l'article `L_{3,infinity}`

ESS pose `Q_+=R^n_+ x (0,1)`. Le Théorème 5.1, pp. 233–234, s'applique à une
fonction vectorielle suffisamment régulière satisfaisant :

```text
|partial_t w + Delta w| <= c_1 (|nabla w|+|w|)       (5.1)
w(.,0)=0 sur R^n_+                                   (5.2)
|w(x,t)| <= exp(M |x|^2)                             (5.3)
```

et la condition (5.4) : `w`, `partial_t w` et `nabla^2 w`, pris au sens des
dérivées généralisées, sont de carré intégrable sur chaque sous-domaine borné
de `Q_+`. La conclusion est `w=0` sur `Q_+`. Aucune valeur n'est imposée sur
la frontière latérale du demi-espace. La remarque suivant le théorème étend
explicitement l'argument aux fonctions à valeurs dans `R^m`.

Le temps unitaire n'est pas restrictif : une remise à l'échelle parabolique
ramène tout ruban fini au ruban `(0,1)`, au prix de changer les constantes
`c_1` et `M`, qui peuvent être quelconques mais finies.

### Article original distinct

L'article *Backward Uniqueness for Parabolic Equations* est distinct. Son
Théorème 1, p. 149, travaille dans

```text
Q_(R,T)=(R^n \ B_R) x [0,T]
```

et suppose

```text
|partial_t w+Delta w| <= M(|w|+|nabla w|),
|w(x,t)| <= M exp(M|x|^2),
w(x,0)=0 sur R^n \ B_R.
```

Les dérivées intervenant dans la preuve peuvent être distributionnelles si
elles sont localement de carré intégrable. Le texte suivant le Théorème 1
précise que l'énoncé vaut pour un champ vectoriel. Le résultat ne contrôle pas
les valeurs sur la frontière latérale `partial B_R x (0,T)`. Le Théorème 5.1
du papier `L_{3,infinity}` est présenté comme une extension au demi-espace des
résultats extérieurs de cet article et d'une note antérieure.

Pour le lemme candidat, l'une ou l'autre version suffit. Le demi-espace est le
cadre le plus direct ; la version extérieure peut aussi être translatée autour
de centres différents puisque la trace terminale est nulle sur tout `R^3`.

## 3. Promotion exacte de la trace `D'`

L'hypothèse `u(t)->0` dans `D'` n'est pas, isolément, la donnée ponctuelle
requise par ESS ou la donnée `L^infinity` requise par Lei–Yang–Yuan.

L'estimation (2) avec `(k,l)=(0,1)` donne

```text
||partial_t u(t)||_infinity <= C M^3,   t<0.                    (3)
```

Ainsi `u(t)` est de Cauchy dans `L^infinity(R^3)` lorsque `t->0-` et admet une
limite globale `u_*` dans cet espace. La convergence `L^infinity` implique la
convergence dans `D'`; l'unicité de la limite distributionnelle impose
`u_*=0`. On a donc en fait

```text
u(t)->0 dans L^infinity(R^3).                                  (4)
```

Alternativement, (2) avec `k>=1` et Arzela–Ascoli donne la convergence dans
`C^m_loc` pour tout `m`. En particulier,

```text
omega(t)=curl u(t) -> 0 dans C^0_loc(R^3).                     (5)
```

Cette promotion utilise réellement la mildness et la borne uniforme jusqu'à
`t=0`; une borne seulement sur chaque `(-infinity,-delta]` ne suffit pas.

## 4. Application sur chaque ruban fini : route ESS

Fixons `S>0` et posons, pour `0<tau<S`,

```text
W(x,tau)=omega(x,-tau).
```

La vorticité lisse vérifie

```text
partial_t omega-Delta omega
  =(omega dot nabla)u-(u dot nabla)omega.
```

Par (2),

```text
|partial_tau W+Delta W|
  <= ||u||_infinity |nabla W| + ||nabla u||_infinity |W|
  <= C_M (|nabla W|+|W|).                                     (6)
```

Audit des hypothèses du Théorème 5.1 :

- **domaine/temps** : restreindre `W` à un demi-espace, puis remettre
  `(0,S)` à l'échelle `(0,1)` ;
- **coefficient** : `C_M<infinity` par (2), indépendamment de `S` ; la seule
  finitude sur chaque ruban aurait déjà suffi ;
- **régularité** : `W`, `partial_tau W` et `nabla^2 W` sont localement dans
  `L^2` puisque (2) borne toutes les dérivées nécessaires ;
- **croissance** : `W` est bornée ; après division par une constante, elle
  vérifie (5.3), donc a fortiori la croissance gaussienne admise ;
- **trace terminale** : (5) donne `W(x,0)=0` ponctuellement ;
- **frontière latérale** : aucune condition n'est requise par le théorème.

ESS donne `W=0` sur tout demi-espace translaté `x_3>c`. Leur union couvre
`R^3`, donc `omega=0` sur `R^3 x (-S,0)`. Comme `S` est arbitraire,
`omega=0` sur tout `R^3 x (-infinity,0)`.

Pour chaque temps fixé,

```text
Delta u = nabla div u - curl curl u = 0.
```

Chaque composante est harmonique et bornée sur `R^3`; le Liouville harmonique
donne `u(x,t)=b(t)`. La Remarque 6.1 de KNSS donne ensuite `b(t)=b_*`, et la
trace distributionnelle nulle donne `b_*=0`.

### Pression

La pression n'intervient à aucun stade de la rétro-unicité : le passage à la
vorticité élimine `nabla p`. Elle n'est pas reconstruite lors du passage à la
limite terminale. La non-localité restante est contenue en amont dans la
formule mild d'Oseen/Leray, où KNSS traite explicitement l'ambiguïté de la
projection sur `L^infinity`.

## 5. Lei–Yang–Yuan : route directe et hypothèses exactes

### Équation et Théorème 1.1

Lei–Yang–Yuan considère sur `R^3 x [0,T]`

```text
partial_t u-Delta u+(u dot nabla)u+nabla p=f,
div u=0,
u(T)=g,
```

avec `f=div F` dans la formulation introductive. La Définition 2.1 exige
`u in L^infinity_(t,x)`, l'équation distributionnelle et la formule

```text
u(t)=exp((t-s)Delta)u(s)
     + integral_s^t exp((t-r)Delta) P[div(u tensor u)+f](r) dr,
0<=s<=t<=T.                                                    (LYY-2.1)
```

Le Théorème 1.1 affirme que deux solutions mild bornées, de vorticités
également bornées, qui ont la même donnée finale ont les mêmes vitesse et
gradient de pression sur `[0,T]`. Pour `f=0`, la Remarque 1.1 indique que le
lissage mild fournit la borne de vorticité requise.

Dans le lemme candidat, (4) permet de poser `u(0)=0`. Le passage `t->0-` dans
(1) est licite en `L^infinity` : la norme `L^1_x` du noyau d'Oseen différentié
est de taille `C(t-r)^(-1/2)`, intégrable en temps. Ainsi, après translation,
`u` est une solution mild au sens de (LYY-2.1) sur chaque `[a,0]`. La solution
zéro a la même force `f=0` et la même donnée finale. Le Théorème 1.1 donne
`u=0` sur `[a,0]`, puis sur tout l'intervalle ancien puisque `a<0` est
arbitraire.

### Coefficients, pression et itération temporelle

La preuve du Théorème 1.1 utilise :

- le Théorème 3.1, une estimation `L^2` à poids polynomial avec
  `h(t)=t exp(-t)` sur un petit intervalle positif ;
- le Corollaire 3.3, qui étend l'estimation aux fonctions dans
  `H^1_0((T_-,T^+);W^{2,p}(R^3))` ;
- le Lemme 4.1, équation (4.3), qui contrôle le terme non local
  `R div f` pour `0<=k<5/2` ;
- une absorption dont le petit temps dépend des normes
  `||u_i||_infinity` et `||curl u_i||_infinity` ;
- une itération finie, p. 13431 / arXiv p. 15, la longueur du pas étant
  indépendante du temps terminal lorsque ces normes globales sont fixées.

La pression est reconstruite dans la Remarque 2.2 par des opérateurs de Riesz,
et la preuve garde le terme non local via la projection de Leray. Cette route
traite donc directement la pression, contrairement à la route ESS qui
l'élimine par le rotationnel.

### Anomalies textuelles à ne pas masquer

Dans `arXiv:2311.02429v1` :

1. p. 9, la preuve dit appliquer le « Corollaire 1.3 » alors que l'énoncé
   fonctionnel utilisé est le Corollaire 3.3 ; c'est une référence interne
   manifestement erronée ;
2. pp. 9–10, l'identité affichée
   `|nabla u_2|^2=Delta|u_2|^2-u_2 dot Delta u_2` omet les facteurs corrects :
   `|nabla u_2|^2=(1/2)Delta|u_2|^2-u_2 dot Delta u_2`. Dans la suite, les
   deux contributions sont seulement majorées à constante multiplicative
   près ; la correction paraît donc locale, mais elle doit être vérifiée sur
   la version d'éditeur avant toute formalisation ;
3. le Théorème 3.1 est énoncé avec un poids spatial d'exposant `-k`, tandis
   que la conjugaison de sa preuve produit d'abord `-2k`. Un renommage de
   paramètre semble réconcilier les formules, mais ce point mérite lui aussi
   une comparaison avec la version d'éditeur.

Ces anomalies ne réfutent pas le Théorème 1.1, désormais publié et évalué par
les pairs. Elles justifient cependant de ne pas faire de cette preuve le seul
support du lemme candidat. La route ESS ci-dessus n'en dépend pas.

## 6. Passe contradictoire et trous explicites

1. **Topologie inversée.** Une valeur arbitrairement assignée `u(0)=0` ne
   remplace pas la limite `t->0-`. Le pont utilise (3) pour obtenir une vraie
   trace `L^infinity`.
2. **Mauvaise notion de solution.** Sans mildness, les solutions parasites
   `b(t)` réfutent l'énoncé, même avec vitesse classique bornée et trace nulle.
3. **Borne non uniforme.** Une borne `L^infinity` seulement sur
   `(-infinity,-delta]` laisse les constantes de (2) exploser à l'approche de
   zéro ; ESS n'est alors pas applicable.
4. **Force.** La conclusion contre la solution zéro est ici strictement
   non forcée. Lei–Yang–Yuan compare deux solutions soumises à la même force ;
   il ne transforme pas une solution forcée en solution nulle.
5. **Domaine/frontière.** Le chaînage est sur `R^3`, sans frontière. Il ne se
   transfère pas tel quel à un domaine borné ou à un demi-espace Navier–Stokes
   avec conditions au bord.
6. **Viscosité.** Les sources normalisent `nu=1`. Toute `nu>0` constante se
   ramène à ce cas par changement d'échelle ; `nu=0` est Euler et hors portée.
7. **Pression.** La seule équation de Poisson pour `p` ne fixe pas les modes
   affines. La route ESS les évite par le rotationnel et la mildness les élimine
   à la fin ; supprimer l'une de ces deux sécurités réintroduit les parasites.
8. **Application finie, pas infinie.** ESS et Lei–Yang–Yuan agissent sur des
   intervalles finis. L'ancienne est couverte en quantifiant sur tout `S>0` ou
   tout `a<0`; aucune application directe à `(-infinity,0)` n'est faite.
9. **Écart Clay restant.** ESS construit une limite adaptée avec trace forte
   locale dans une chaîne `L^infinity_t L^3_x`, mais pas l'ancienne mild
   globalement bornée du lemme. KNSS construit une ancienne mild bornée avec
   une normalisation non nulle au temps terminal, pas une trace terminale
   nulle. Réunir les propriétés de deux objets différents est invalide.

## Recommandation de statut

- Théorèmes KNSS, ESS et Lei–Yang–Yuan : `SOURCE_VERIFIED`, avec les domaines
  et notions de solution ci-dessus.
- Lemme « ancienne mild bornée + trace `D'` nulle => zéro » :
  `AI_DERIVATION` jusqu'à intégration d'une preuve autonome auditée ; son noyau
  analytique est fermé par la route ESS.
- Arête vers Clay : toujours `MISSING`, car l'héritage simultané des prémisses
  par une extraction de blow-up n'est pas démontré.
