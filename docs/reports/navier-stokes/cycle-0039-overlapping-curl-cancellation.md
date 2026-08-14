# Cycle 0039 — Annulation de curls et non-invariance des cellules étiquetées

Date : 2026-08-15
Statut : `AI_INTERNAL_DERIVATION`; le claim universel attaqué est `REFUTED`
Portée : obstruction cinématique statique; aucune évolution Navier–Stokes.

## Décision adaptative

| Action | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| paire lisse `Z_n,-Z_n` annulée dans deux cellules étiquetées | 5 | 5 | 5 | 5 | **20** |
| agréger d'abord toutes les cellules de même axe et même anneau | 3 | 5 | 5 | 4 | 17 |
| décomposition canonique par ondelettes/carré-fonction | 4 | 2 | 4 | 5 | 15 |

La première action est sélectionnée. Elle décide si une borne de multiplicité
peut remplacer la disjonction dans la sélection cellulaire. Le résultat est
négatif, avec multiplicité exactement deux et champs lisses curl-compatibles.

## Cadre exact

Le problème de référence reste Navier–Stokes incompressible non forcé sur
`R3`, viscosité positive. L'objet effectivement traité est une donnée
statique pure-swirl. Pour un champ compact non nul `U`, posons

```text
q(U)=||U||_(L^(3,infinity))/||curl U||_(L^(3/2,infinity)).
```

On attaque l'énoncé universel suivant : pour toute décomposition
`U=sum_j U_j` en champs lisses compacts divergence-free de multiplicité de
supports au plus `m`, il existerait une fonction positive `Phi` telle que

```text
max_j q(U_j) >= Phi(q(U),m).
```

La fonction `Phi` doit être indépendante du nombre de cellules, des
amplitudes cachées et de la décomposition choisie.

## Contre-théorème lisse à multiplicité deux

Fixons des cutoffs

```text
chi in C_c^infinity((1/2,3/2)), chi=1 sur [3/4,5/4], |chi|<=1,
eta in C_c^infinity(R), eta=1 sur [0,2pi], |eta|<=1.
```

Pour chaque entier `n>=1`, définissons

```text
Z_n=(1/r)chi(r)eta(z)sin(nz)e_theta.
```

Soit `B=(1/r)Psi(r,z)e_theta` un champ pure-swirl fixe, lisse, compact et non
nul dans le même anneau. Posons

```text
U_(1,n)=B+Z_n,
U_(2,n)=-Z_n.
```

Ces champs sont lisses, compacts et exactement divergence-free. Leurs
supports se recouvrent avec multiplicité au plus deux et

```text
U_(1,n)+U_(2,n)=B,
curl U_(1,n)+curl U_(2,n)=curl B                         (39.1)
```

point par point.

## Témoin de haute fréquence à volume fixe

Le curl pure-swirl exact est

```text
curl Z_n=(1/r)(-partial_z F_n e_r+partial_r F_n e_z),
F_n=chi eta sin(nz).
```

Sur le plateau des deux cutoffs, son terme radial vaut
`-(n/r)cos(nz)e_r`. Posons

```text
E_n={3/4<=r<=5/4, 0<=theta<2pi, 0<=z<=2pi,
     |cos(nz)|>=1/2}.
```

La mesure axiale du dernier ensemble est exactement `4pi/3` pour tout entier
`n`. Avec le jacobien cylindrique,

```text
|E_n|=2pi integral_(3/4)^(5/4) r dr * 4pi/3
     =4pi^2/3.                                           (39.2)
```

Sur `E_n`, `|curl Z_n|>=2n/5`. Par définition de la quasi-norme,

```text
||curl Z_n||_(L^(3/2,infinity))
  >=(2n/5)(4pi^2/3)^(2/3).                              (39.3)
```

La vitesse `Z_n` a amplitude et support uniformément bornés. Ainsi

```text
q(U_(2,n))=q(-Z_n)=O(n^-1).                              (39.4)
```

Le curl du fond `B` est borné. Sur le même témoin,

```text
|curl(B+Z_n)|>=2n/5-||curl B||_infinity.
```

Pour `n` assez grand, cette quantité est au moins `n/5`, tandis que la
vitesse `B+Z_n` reste uniformément bornée sur un support fixe. Par conséquent,

```text
q(U_(1,n))=O(n^-1).                                      (39.5)
```

En revanche, `B` et `curl B` sont non nuls, lisses et compacts, donc

```text
0<q(B)<infinity,
q(U_(1,n)+U_(2,n))=q(B)                                 (39.6)
```

est indépendant de `n`. Les équations (39.4)–(39.6) réfutent toute fonction
positive `Phi(q(B),2)`.

## Premier quantificateur faux

Le premier quantificateur réfuté est « pour toute décomposition à
multiplicité bornée ». Une borne de multiplicité contrôle combien de termes
sont présents en un point, jamais leur amplitude ni leur anti-alignement.

La monotonie disponible pour une restriction d'un curl unique,

```text
||1_E W||_(L^(3/2,infinity))<=||W||_(L^(3/2,infinity)),
```

ne se transforme pas en

```text
||W_j||_(L^(3/2,infinity))<=||sum_k W_k||_(L^(3/2,infinity))
```

sous recouvrement. La seconde inégalité est explicitement fausse ici : les
deux membres individuels croissent comme `n`, leur somme reste fixe.

## Scaling

À rayon majeur `R`, le mode non normalisé

```text
Z_(n,R)=(R/r)chi(r/R)eta(z/R)sin(nz/R)e_theta
```

possède un témoin de volume `(4pi^2/3)R^3` et un curl d'amplitude
`>=2n/(5R)`. Son rapport reste `O(n^-1)`. La normalisation Clay exacte

```text
U_R(x)=R^-1 U(x/R),
W_R(x)=R^-2 W(x/R)
```

conserve séparément les deux quasi-normes critiques, la multiplicité et tous
les rapports. L'obstruction n'est donc pas un effet d'une échelle fixée.

## Certificat atomique exact

L'expérience indépendante remplace l'espace par quatre atomes de volume
`1/4`, indexés par deux signes `p,z`. Elle pose

```text
V=B=1, P=p, Z=Mz,
(U1,W1)=(V+P,B+Z), (U2,W2)=(-P,-Z).
```

Les sommes valent exactement `(V,B)` sur chaque atome. Pour `M>=8`, les
fonctions de distribution complètes donnent

```text
q_global^3=1,
q_1^3=4/(M-1)^3,
q_2^3=1/M^3.                                             (39.7)
```

Le certificat principal parcourt toutes les fréquences `8..4096`, cinq
rescalings critiques et la famille dyadique jusqu'à `2^40`. Il exécute
344 121 assertions `Fraction`, recalcule chaque supremum après la somme et
obtient un résidu pointwise nul. Le ledger ne certifie pas le continuum; les
équations (39.2)–(39.5) constituent le raccord analytique séparé.

## Réparation par agrégation du champ total

Le contre-exemple est délibérément une mauvaise décomposition du champ fixe
`B`. Il ne réfute pas une sélection directement appliquée au champ total.

Si tous les termes partagent le même axe, le même rayon `R` et le même anneau,

```text
U_j=(R/r)F_j e_theta,
```

alors, même sous recouvrement et cancellation,

```text
sum_j U_j=(R/r)(sum_j F_j)e_theta.
```

Le claim du cycle 0038 s'applique au potentiel total `F=sum_jF_j`. Les
annulations sont calculées avant les valeurs absolues et aucune cellule
étiquetée n'est sélectionnée. Ainsi le recouvrement de même axe et de même
anneau est fermé par **agrégation**, pas par multiplicité.

Cette réparation ne couvre pas des axes différents, des anneaux non
comparables ni une décomposition produite par projection de Leray : le champ
total n'est alors plus un potentiel méridien scalaire unique.

## Passe contradictoire

1. **Volume oscillant.** Il est exactement indépendant de `n`, pas seulement
   asymptotiquement positif.
2. **Cutoffs.** Leurs dérivées s'annulent sur le témoin; elles ne peuvent
   retirer la masse déjà comptée.
3. **Fond oscillant.** `curl B` est borné indépendamment de `n` et ne peut
   annuler le terme `n cos(nz)` sur le témoin entier.
4. **Quasi-triangle.** Aucune quasi-inégalité de Lorentz n'est utilisée : les
   distributions du total et des cellules sont recalculées séparément.
5. **Support.** Dériver un profil lisse compact n'agrandit pas son support;
   les curls se recouvrent réellement.
6. **Divergence et axe.** Les champs azimutaux axisymétriques sont
   divergence-free et s'annulent près de `r=0`.
7. **Décomposition artificielle.** Elle réfute l'universalité sur toutes les
   décompositions, pas l'existence d'une bonne décomposition de `B`.
8. **Superniveaux disjoints.** Les sélections 0035–0038 construites depuis des
   restrictions du champ total ne sont pas réfutées.
9. **Carré-fonction.** Une frame peut donner un registre canonique, mais son
   contrôle endpoint et sa compatibilité avec les cellules géométriques ne
   sont pas fournis par la multiplicité.
10. **Clay.** Aucune pression, projection de Leray, diffusion, évolution,
    solution faible ou singularité n'est construite.

## Résultat et prochain verrou

`GAP-OVERLAPPING-CURL-CANCELLATION` est fermé négativement pour la sélection
par cellules arbitrairement étiquetées : multiplicité bornée seule est
insuffisante. Il est réparé par agrégation dans la sous-classe commune
axe–anneau.

Le prochain verrou est `GAP-MULTIAXIS-TOTAL-FIELD-LOCALIZATION` : formuler une
sélection intrinsèque depuis le champ total lorsque plusieurs axes ou
géométries locales coexistent, ou construire un contre-profil multi-axe qui
échappe à toute boule directionnelle malgré les deux endpoints globaux.
