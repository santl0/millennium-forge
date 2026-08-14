# Cycle 0026 — compensation conique au seuil faible-`L^(3/2)`

Date de gel : 2026-08-14.

Statut : dérivation interne falsifiable et certificat rationnel exact. Aucun
résultat n'est promu en preuve publiée ou en résolution Clay.

## Décision du cycle

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| inégalité masse conique–Lorentz–oscillation | 5 | 5 | 5 | 5 | **20** |
| retour compact explicite à deux amplitudes | 5 | 2 | 4 | 5 | 16 |
| évolution validée d'un train tronqué | 4 | 2 | 4 | 3 | 13 |

Le verrou sélectionné est `GAP-DIRECTIONALLY-FLAT-INTERMITTENCY`. Le lemme
actif quantifie la masse directionnelle opposée qu'un curl compact doit payer,
puis teste si la borne critique faible-`L^(3/2)` empêche ce paiement de se
concentrer sur un ensemble arbitrairement petit.

## Équation et type de solution

La cible Clay reste

```text
partial_t u-Delta u+(u dot nabla)u+nabla p=0,
div u=0,                  omega=curl u
```

sur `R³`, sans frontière ni force, viscosité positive. Le cycle ne construit
aucune solution. Il isole une propriété statique de tout blob de vorticité

```text
W=curl U,                 U compactement supporté,
```

à savoir `integral W dx=0`, puis travaille sur un domaine test `D` de mesure
finie contenant son support.

## Lemme actif révisé par la passe contradictoire

Soit `0<|D|<infinity` et

```text
W∈L^(3/2,infinity)(D;R³),
K=sup_(lambda>0) lambda |{|W|>lambda}|^(2/3)<infinity. (1)
```

Sur `A={W!=0}`, posons `xi=W/|W|`. Fixons `e∈S²`, `alpha∈(0,1]`,

```text
G={x∈A: xi dot e>=alpha},
m=integral_G |W| dx,
nu_e=integral_D (-W dot e)_+ dx.                         (2)
```

Pour toute extension `zeta∈L¹(D;R³)` telle que `zeta=xi` sur `A`, et pour
`K>0`, l'oscillation moyenne sur `D` vérifie la forme canonique

```text
average_D |zeta-zeta_D|
 >=2 min(alpha m³,nu_e³)/[27 K³ |D|].                   (3)
```

Si, en plus, `integral_D W dx=0`, alors `nu_e>=alpha m` et

```text
average_D |zeta-zeta_D|
 >=2 alpha³m³/[27 K³ |D|].                              (4)
```

Le premier jet du cycle donnait seulement `alpha^4/27`. La passe analytique
indépendante a conservé le poids de projection négative et renforcé à la fois
la puissance de `alpha` et le facteur deux. Le cas `K=0` implique `W=0`
presque partout et se traite séparément avec membre droit nul; le cas `m=0`
est trivial.

## Étape 1 — intégration critique de Lorentz

La définition (1) donne pour la réarrangée décroissante

```text
W*(s)<=K s^(-2/3).
```

Donc, pour tout ensemble mesurable `E⊂D`,

```text
integral_E |W|
 <=integral_0^|E| W*(s)ds
 <=3K |E|^(1/3).                                         (5)
```

La constante trois est `p/(p-1)` au seuil `p=3/2`.

## Étape 2 — intégration pondérée et compensation

Pour tout poids `0<=q<=1`, la représentation en couches, (5), la concavité
de `s^(1/3)` et Cavalieri donnent

```text
integral_D |W|q
 <=3K integral_0^1 |{q>t}|^(1/3)dt
 <=3K (integral_D q)^(1/3).                              (6)
```

Avec `q=(-xi dot e)_+`, (6) implique

```text
integral_D q >=nu_e³/(27K³).                            (7)
```

De même, (5) appliquée à `G` donne

```text
|G|>=m³/(27K³).                                         (8)
```

Si la moyenne vectorielle de `W` est nulle, sa projection sur `e` annule la
partie positive par la partie négative. La contribution positive de `G`
vaut au moins `alpha m`, donc `nu_e>=alpha m`.

## Étape 3 — équilibre des écarts positifs et négatifs

Posons `h=zeta dot e` et `c=h_D`. Si `c>=0`, la partie négative de `h-c`
porte au moins `integral_Dq`; si `c<0`, sa partie positive porte au moins
`alpha|G|`. Comme `h-c` a moyenne nulle, ses parties positive et négative ont
la même intégrale et

```text
average_D |h-c|
 >=2 min(alpha|G|,integral_Dq)/|D|.                     (9)
```

La projection est contractante :
`|zeta-zeta_D|>=|h-h_D|`. Les bornes (7)–(9) donnent (3), puis (4) sous
annulation. La preuve n'utilise aucune valeur de `zeta` hors des ensembles
actifs, mais son intégrabilité est nécessaire pour définir sa moyenne.

Pour un curl compact régulier, l'hypothèse d'annulation vient de

```text
integral_R³ curl U dx=0                                (10)
```

par intégration des dérivées. Le lemme reste formulé avec (1), afin de ne pas
cacher les hypothèses de régularité nécessaires à (10). Sur un sous-domaine
qui coupe le support, la circulation de bord ne s'annule pas nécessairement.

## Corollaire log-BMO

Définissons la masse conique normalisée

```text
mu= m/[K |D|^(1/3)].                                   (11)
```

Elle est sans dimension et (3) devient

```text
MO_D(zeta)>=2alpha³ mu³/27.                            (12)
```

Si une famille de blobs de diamètre `rho_n->0` satisfait sur leurs domaines
`D_n`

```text
MO_(D_n)(zeta)<=B phi(rho_n),       phi(r)->0,
```

alors nécessairement

```text
mu_n³ <=27B phi(rho_n)/(2alpha³).                       (13)
```

Au taux `phi(r)=1/[1+log(R_*/r)]`, toute masse alignée normalisée doit donc
disparaître au moins comme la racine cubique du logarithme. Une masse conique
uniformément positive exclurait immédiatement le blob directionnellement plat.

## Test adverse sharp à deux amplitudes

Sur un espace de probabilité, pour `n>=2`, posons

```text
epsilon_n=n^-3,
a_n=n²/(n³-1),
W_n= a_n e     sur une fraction 1-epsilon_n,
W_n=-n² e      sur une fraction epsilon_n.              (14)
```

Alors exactement

```text
integral W_n=0,
||W_n||_(L^(3/2,infinity))=1,
m_n=integral_(W_n dot e>0)|W_n|=1/n,                   (15)
MO(xi_n)=4n^-3(1-n^-3),
MO(xi_n)/m_n³=4(1-n^-3).                                (16)
```

La phase négative porte à elle seule une masse forte `L^(3/2)` égale à un;
la masse totale reste entre un et deux. Ainsi :

1. l'exposant cubique de (3) est optimal dans la classe mesurable;
2. une masse critique `L^(3/2)` non dégénérée ne fournit aucune minoration de
   `m_n`;
3. le faible-Lorentz et l'annulation vectorielle permettent une direction
   plate en **moyenne de domaine** en transférant toute la masse critique au
   compensateur rare.

Cette famille n'est pas un champ spatial. Si les deux phases sont séparées
par une interface régulière, une boule qui résout l'interface avec fractions
`1/2,1/2` a une oscillation directionnelle exacte égale à un. Le petit nombre
dans (16) ne certifie donc pas le BMO global.

La passe adverse affine cette dichotomie. Si une région où `W=0` sépare un
cœur négatif de rayon `h` d'une phase positive à distance `R`, une extension
unitaire radiale en `log r` peut étaler la rotation avec BMO
`O(1/log(R/h))`; un télescopage de moyennes donne réciproquement un coût
`>=7/[32 ceil(log_2(2R/h))]` dans ce modèle annulaire. Pour `h/R~1/n` et un
blob physique `ell_n~2^-n/n`, le poids log-BMO croît encore comme `n/log n`.
Le volume seul ne contrôle toutefois ni un rayon intérieur, ni une capacité.

## Échelle des quantités

Sous `W_ell(x)=ell^-2 W(x/ell)`, `K` est invariant,
`m_ell=ell m` et `|D_ell|=ell³|D|`. Par conséquent

```text
m_ell³/[K³|D_ell|]=m³/[K³|D|].                         (17)
```

Le lemme suit exactement l'échelle critique de la vorticité. Il n'introduit
ni perte de dérivée, ni constante de troncature, ni pression.

## Passe contradictoire

1. Sans `integral W=0`, un champ constant orienté dans `D` réfute la forme
   simplifiée (4), mais pas la forme canonique (3), dont `nu_e=0`.
2. Sans la masse conique `m`, une masse `L^(3/2)` peut résider entièrement
   dans le compensateur rare; (14) le réalise.
3. Une petite oscillation sur le domaine entier ne donne pas la petite
   oscillation sur toutes ses sous-boules.
4. Une extension `L¹` arbitraire aux zéros ne modifie pas la preuve, qui
   n'utilise que `G` et le poids négatif actifs; sans intégrabilité, la moyenne
   et `MO_D` ne sont pas définies.
5. L'identité `integral curl U=0` exige une décroissance ou un support compact;
   elle n'est pas vraie pour toute vorticité globale distributionnelle.
6. La constante faible-Lorentz dépend de la convention de quasi-norme. Ici
   `K` est fixé explicitement par (1).
7. Aucune disposition spatiale, divergence, vitesse, pression ou évolution
   n'est associée au modèle atomique (14).
8. Un champ exactement collinéaire `W=f e`, compactement supporté et
   divergence-free sur `R³`, est nul : `partial_e f=0` contredit le support
   compact. Tout lift non trivial doit donc créer des composantes transverses
   ou fermer les lignes de vorticité.
9. La moyenne nulle est globale. Sur une boule qui coupe le support,
   `integral_B curl U=integral_(partial B)n cross U`; appliquer (4) boule par
   boule sans ce terme inverse les quantificateurs.

## Veille différentielle

La veille primaire ciblée est conservée dans
`reviews/cycle-0026-literature.md`. La borne d'intégration faible-Lorentz est
classique; le chaînage quantitatif précis avec annulation vectorielle, masse
conique et oscillation de direction est enregistré comme dérivation du
laboratoire, pas comme théorème publié. Cinq sources primaires sont ajoutées :
Lorentz (`0097`), Grujić–Guberović (`0098`), Smirnov (`0099`),
Daneri–Székelyhidi (`0100`) et Enciso–Peralta-Salas (`0101`). Elles couvrent
respectivement la brique faible-Lorentz, la cohérence locale, les solénoïdes,
les Mikado flows et les tubes fermés; aucune ne ferme le raccord complet.

## Verdict et écart avec Clay

Résultat positif borné : un curl compact à masse conique normalisée non nulle
ne peut devenir directionnellement plat sous une borne critique faible-
`L^(3/2)`. La constante et l'échelle sont explicites.

Résultat négatif : ni la masse forte critique, ni le faible-Lorentz, ni
l'annulation vectorielle ne garantissent cette masse conique. Le compensateur
à deux amplitudes rend `m_n->0` tout en gardant les deux contrôles critiques.

Le verrou devient `GAP-NESTED-RETURN-FLOW-CASCADE` : réaliser spatialement le
compensateur rare avec `div W=0` et `W=curl U`, puis répartir la rotation de
direction sur une cascade interne assez profonde pour satisfaire le log-BMO
sur toutes les sous-boules. Le premier ansatz discriminant est un potentiel
azimutal axisymétrique `U=psi(r,z)e_theta`, pour lequel le curl est exact et
les composantes transverses de cutoff sont visibles. Biot–Savart, pression et
résidu devront ensuite être recalculés.

## Reproduction

```text
python -B experiments/navier-stokes/cone-compensation/cone_compensation_audit.py
```

Le script utilise Python 3.13.14 et `fractions.Fraction`, sans grille,
flottant ni graine. Il exécute 670 contrôles exacts, incluant 180 tests de
l'inégalité d'intégration sur des sous-ensembles atomiques, 12 tests pondérés,
une famille de profils signés et 63 instances sharp. Résidus algébriques :
zéro. Empreinte SHA-256 :
`12eadf58f6bf5fdec9855527f58d9a7e6ba98650c3fd8fca78adbbbcfc1e1727`.

Empreintes des trois passes séparées : analyse
`1bb08a1e4d52a5a9730fdf0378daf3df146871329769ce103348acd30e1d42e8`,
contre-modèle
`04ed8064abb4323759b893e08c289d72c001a7cda6e6a4e2014fdbb1dacaa91d`
et littérature
`4061592c8c14209222ec35b4255e9f07c35dab6f80bd83fa85f0c266c007475e`.
Ces passes utilisent la même famille de modèles et ne constituent pas une
revue externe indépendante.
