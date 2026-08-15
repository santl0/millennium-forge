# Cycle 0054 — conjugaison générateur--flux et obstruction tangentielle

Date : 2026-08-15.

Statut : `AI_INTERNAL_DERIVATION`; aucune conclusion Clay.

## Décision adaptative

Le verrou relu est
`GAP-TYPE-I-RENORMALIZED-GENERATOR-TO-SIGNED-FLUX`. Les actions candidates
sont fixées avant le calcul :

| action | nouveauté | tractabilité | falsifiabilité | levier | total |
|---|---:|---:|---:|---:|---:|
| conjuguer exactement générateur renormalisé et flux, puis isoler l'angle manquant | 4 | 5 | 5 | 5 | **19** |
| intégrer une triade visqueuse sur une fenêtre similaire complète | 4 | 4 | 5 | 3 | 16 |
| imposer une observabilité locale directe de la pression calorifiée | 5 | 2 | 4 | 4 | 15 |

La première action est sélectionnée. Le lemme actif est unique : écrire la
densité signée du cycle 0052 entièrement dans les variables renormalisées,
avec horloge, filtre, signe et adjoint suivis, puis décider si la minoration
du générateur du cycle 0053 contrôle cette densité.

## Cadre exact et horloge

Soit `kappa>0`. Sur `R3 x (-infinity,0]`, sans frontière, considérons la
solution ancienne renormalisée faible adaptée locale

```text
partial_s Z-Delta Z+N_Z+kappa D Z=0,
N_Z=P div(Z tensor Z),
D Z=(1+y dot nabla)Z,
div Z=0.                                                  (54.1)
```

La pression est dans la jauge globale de Riesz et `Z` est uniformément
bornée dans `L^(3,infinity)`. Introduisons

```text
rho(s)=exp(-kappa s),
tau(s)=[1-rho(s)^2]/(2kappa),
(T_rho f)(x)=rho^(-1)f((x-x_0)/rho).                     (54.2)
```

Alors `tau_s=rho^2`, `rho_s=-kappa rho`, `tau(0)=0`, et la solution physique
ancienne est

```text
v(tau(s))=T_(rho(s))Z(s).                                 (54.3)
```

Elle résout Navier--Stokes incompressible standard, non forcé, de viscosité
un sur `R3 x (-infinity,0]`. Le temps terminal physique est fixé à zéro dans
tout ce cycle.

## Conjugaison du flot calorifique

Notons `S(b)=exp(b Delta)` et fixons un temps calorifique physique `a>0`.
Posons

```text
A_s=-tau(s)/rho(s)^2
   =[1-rho(s)^(-2)]/(2kappa),

B_s=[a-tau(s)]/rho(s)^2
   =1/(2kappa)+[a-1/(2kappa)]rho(s)^(-2).                 (54.4)
```

En particulier,

```text
min(a,1/(2kappa))<=B_s<=max(a,1/(2kappa)),               (54.5)
```

donc le lissage en variables similaires ne dégénère jamais. La covariance
du semi-groupe donne

```text
S(-tau(s))v(tau(s))=T_rho S(A_s)Z(s),
S(a-tau(s))v(tau(s))=T_rho S(B_s)Z(s).                   (54.6)
```

Pour le correcteur du cycle 0052,

```text
g_s=v(0)-S(-tau(s))v(tau(s)),
G_a(s)=S(a)g_s,
E_a(s)=||G_a(s)||_2^2,                                   (54.7)
```

on obtient l'identité exacte

```text
G_a(s)=S(a)v(0)-T_rho S(B_s)Z(s),
G_a(0)=0.                                                 (54.8)
```

Les deux termes de (54.8) ne sont pas affirmés séparément dans `L2`; leur
différence `G_a` l'est par le Duhamel lissé. Les dérivations suivantes se
lisent d'abord dans les distributions puis dans cette représentation `L2`.

## Dérivée exacte et commutateur de dilatation

On a

```text
partial_s[T_rho f]=kappa T_rho(D f),
[D,Delta]=-2Delta,
D S(B)=S(B)D-2B Delta S(B),
B_s'=(2kappa a-1)rho^(-2),
B_s'-2kappa B_s=-1.                                      (54.9)
```

Par conséquent,

```text
partial_s[T_rho S(B_s)Z]
 =T_rho S(B_s)[partial_sZ-Delta Z+kappa D Z].            (54.10)
```

Définissons le résidu renormalisé sans pression

```text
L_kappa Z:=partial_sZ-Delta Z+kappa D Z=-N_Z.             (54.11)
```

Alors

```text
partial_sG_a(s)=-T_rho S(B_s)L_kappa Z(s)
               = T_rho S(B_s)N_Z(s).                    (54.12)
```

Le coefficient `-1` de `Delta Z` dans (54.10) résulte de la somme de trois
termes : variation de l'horloge, dérivée du filtre `a/rho^2` et commutateur
de la dilatation. Omettre l'un d'eux change l'équation observée.

## Identité de projection radiale du flux

Soit `I_a(t;0)` la densité signée physique du cycle 0052. Puisque

```text
partial_t E_a(t;0)=-I_a(t;0),
tau_s=rho^2,                                             (54.13)
```

la densité en temps similaire est

```text
J_a(s):=rho(s)^2 I_a(tau(s);0)=-partial_sE_a(s).         (54.14)
```

Les formules (54.12)--(54.14) donnent

```text
boxed:
J_a(s)=2 <G_a(s),T_rho S(B_s)L_kappa Z(s)>_(L2_x),       (54.15)

E_a(s)=integral_s^0 J_a(sigma)dsigma.                   (54.16)
```

L'adjoint de `T_rho` est

```text
(T_rho^*G)(y)=rho^2G(x_0+rho y).                         (54.17)
```

En posant

```text
Theta_a(s)=S(B_s)T_rho^*G_a(s),                          (54.18)
```

on obtient la forme entièrement renormalisée

```text
boxed: J_a(s)=2 <L_kappa Z(s),Theta_a(s)>.                (54.19)
```

Le champ `Theta_a` est solénoïdal. Comme `B_s` est uniformément strictement
positif, le lissage place `nabla Theta_a` dans `L^(3,1)`; le pairing avec
`Z tensor Z in L^(3/2,infinity)` est donc celui de Hölder--Lorentz. En
utilisant (54.11),

```text
J_a(s)=2 integral_R3 (Z tensor Z):nabla Theta_a dy.       (54.20)
```

La pression disparaît seulement parce que `Theta_a` est solénoïdal et que la
projection globale est conservée; aucune pression locale n'est effacée.

## Pourquoi `D_R` ne contrôle pas `J_a`

Le défaut `D_R` du cycle 0053 est une variation sur une fenêtre unitaire,
locale dans `B_R`, de `partial_sZ`, prise comme supremum sur tous les tests
`W_0^(1,(3,1))`. L'identité (54.19) porte au contraire sur :

1. une tranche presque partout fixée;
2. le résidu global `L_kappa Z`, pas `partial_sZ` seul;
3. un unique test dépendant de la trajectoire future, `Theta_a(s)`;
4. un appariement signé scalaire.

Ainsi `D_R(s)>=epsilon` signifie qu'un test local détecte une variation, mais
ne donne ni la taille de `L_kappa Z`, ni son angle avec `Theta_a`. Même dans
une géométrie de Hilbert où l'on identifierait favorablement le générateur à
`L_kappa Z`, une composante tangentielle peut être arbitrairement grande et
rester invisible à `J_a`.

## Contre-modèle tangent exact

Soient `e(s),t(s)` deux vecteurs orthonormés vérifiant

```text
e'=t,
t'=-e.                                                    (54.21)
```

Pour `s<=0`, posons `q=exp(s)`, `h=1-q` et

```text
G(s)=h e(s),
L(s)=-G'(s)=q e(s)-h t(s).                               (54.22)
```

Alors

```text
G(0)=0,
E(s)=||G(s)||^2=h^2,
J(s)=2<L(s),G(s)>=2qh=-E'(s),                            (54.23)

||L(s)||^2=q^2+h^2>=1/2.                                (54.24)
```

Cependant

```text
integral_(-infinity)^0 J(s)ds
 =integral_0^1 2(1-q)dq=1,
0<=E(s)<=1,
J(s)->0 quand s->-infinity.                              (54.25)
```

Le générateur reste donc uniformément actif tandis que la primitive signée
est bornée. La composante `-h t` devient purement tangentielle et ne contribue
pas à l'énergie. Deux polarisations solénoïdales orthogonales d'une même
fréquence sur `T3` réalisent exactement cette géométrie; le semi-groupe
isotrope agit par le même scalaire sur les deux modes.

Ce modèle satisfait la condition terminale et l'identité scalaire plus
fidèlement qu'une orbite périodique de rayon constant. Il n'est toutefois ni
une solution de Navier--Stokes, ni une ancienne sur `R3`, ni une paire
suitable. Il réfute uniquement une coercivité universelle tirée de la norme
du générateur et de (54.15).

## Loi d'échelle et constantes

La quantité `J_a ds=I_a dt` a le même poids `lambda^(-1)` que `E_a` sous la
dilatation physique de Navier--Stokes. Le temps similaire `s` est sans
dimension et `rho` porte la dilatation. Le filtre renormalisé `B_s` reste
entre les deux constantes positives de (54.5); aucune constante de
troncature spatiale ou limite `a->0` n'est utilisée.

La norme `L2` de `T_rho f` vaut `rho^(1/2)||f||_2`, et celle de
`T_rho^*G` vaut `rho^(1/2)||G||_2`. Ces facteurs sont inclus dans
`Theta_a`; les omettre produirait un faux appariement invariant.

## Passe contradictoire

1. **Signe.** `G_a'=-T_rho S(B_s)L_kappa Z`; par conséquent
   `J_a=+2<G_a,T_rho S(B_s)L_kappa Z>`.
2. **Filtre.** Le bon temps similaire est
   `B_s=(a-tau)/rho^2`, pas `a+A_s`.
3. **Commutateur.** La dérivée de `T_rho` ne commute pas avec la chaleur;
   `B_s'-2kappa B_s=-1` reconstruit exactement `-Delta Z`.
4. **Terminal.** Le temps physique terminal reste zéro; le laisser dépendre
   de `s` ajouterait un terme de bord.
5. **Endpoint.** Le pairing utilise
   `L^(3/2,infinity)`--`L^(3,1)`, jamais faible-`L3` contre faible-`L^(3/2)`.
6. **Local contre global.** `D_R` sur un rayon ne contrôle pas la queue de
   `Theta_a`, qui est globale après chaleur et Riesz.
7. **Supremum contre direction.** Un supremum sur tous les tests ne minore
   pas l'action contre un test particulier.
8. **Résidu contre dérivée.** `L_kappa Z` contient diffusion et drift; une
   minoration de `partial_sZ` ne les empêche pas de compenser.
9. **Mouvement tangent.** Le contre-modèle est solénoïdal en réalisation
   Fourier, mais ne satisfait pas la non-linéarité Navier--Stokes.
10. **RSS/RDSS.** Une rotation exacte est une sous-classe PDE plus rigide;
    les résultats récents ne doivent pas être étendus aux orbites générales.
11. **Clay.** La conjugaison ne borne pas (54.16), ne donne pas `v(0) in L2`
    et ne traite pas Type II.

## Résultat et pivot

Le résultat positif est l'identité exacte

```text
flux similaire = projection radiale calorifiée de L_kappa Z.             (54.26)
```

Le résultat négatif est

```text
activité persistante du générateur
  -/-> coercivité ou non-bornitude de la primitive signée.                (54.27)
```

Le raccord direct par norme est abandonné et enregistré dans
`FAIL-NS-0090`. Le verrou est raffiné en

```text
GAP-TYPE-I-RENORMALIZED-TANGENTIAL-ACTIVITY-CLASSIFICATION.               (54.28)
```

La prochaine expérience décisive doit tester la compatibilité PDE d'une
activité asymptotiquement tangentielle. Le premier sous-cas falsifiable est
une orbite relative de rotation

```text
Z(s,y)=R(alpha s)U(R(-alpha s)y),                        (54.29)
```

dont le profil satisfait l'équation RSS. Il faut comparer les régimes de
rotation déjà exclus aux paramètres intermédiaires et aux orbites non
exactement périodiques, sans transformer la prépublication correspondante en
théorème général.
