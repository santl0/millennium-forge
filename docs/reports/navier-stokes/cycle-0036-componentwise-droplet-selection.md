# Cycle 0036 — sélection composante par composante des gouttelettes actives

Date de gel : 2026-08-14.

Statut : dérivation analytique interne, ledger algébrique exact et trois
passes contradictoires IA. Aucun résultat nouveau n'est classé
`PAPER_PROOF`. Aucune trajectoire de Navier–Stokes n'est construite.

## Décision adaptative

| Action candidate | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| convertir le volume total en une boule par Vitali | 2 | 4 | 5 | 4 | 15 |
| tronquer séparément les composantes de niveau signées | 5 | 5 | 5 | 5 | **20** |
| réaliser un contre-profil exact de gouttelettes dispersées | 4 | 4 | 5 | 5 | 18 |

La deuxième action est retenue et la troisième sert de test décisif. Un
argument de covering fondé sur le seul volume ne contrôle pas le diamètre.
En revanche, une troncature qui s'annule sur le bord de chaque composante
conserve exactement le curl intérieur et ne crée aucune mesure de bord.

## Équation, domaine et type d'objet

Le problème Clay de référence reste

```text
partial_t u+(u·nabla)u=-nabla p+nu Delta u,
div u=0, nu>0, f=0,
```

sur `R3` ou `T3`. Le cycle travaille uniquement sur `R3`, à temps fixé, avec
une famille finie de données lisses compactes divergence-free

```text
F_j in C_c^infinity((0,infinity)×R),
supp F_j subset {R_j/2<r<3R_j/2},
U_j=(R_j/r)F_j e_theta,
W_j=curl U_j=(R_j/r)(-partial_z F_j e_r+partial_r F_j e_z).
```

Les supports tridimensionnels complets sont deux à deux disjoints. On pose
`U=sum U_j`, `W=sum W_j`, `K_u=||U||_(L^(3,infinity))>0` et
`K_w=||W||_(L^(3/2,infinity))`. Pression, viscosité et évolution ne sont pas
utilisées.

## Lemme actif

Soit `C_I` une constante admissible de
`Per(E)>=C_I|E|^(2/3)` dans `R3`. Pour `0<eta<1`, choisissons `lambda>0`
tel que

```text
lambda |{|U|>lambda}|^(1/3)>=(1-eta)K_u.         (1)
```

Pour chaque signe `sigma` et chaque composante connexe `C_alpha` de
`{sigma F_j>lambda/4}` rencontrant `{sigma F_j>lambda/2}`, définissons

```text
G_alpha=(sigma F_j-lambda/4)_+ 1_(C_alpha),
U_alpha=(R_j/r)G_alpha e_theta,
V_alpha=|C_alpha intersection {sigma F_j>lambda/2}|.
```

Il n'y a qu'un nombre fini de composantes actives : le compact
`{sigma F_j>=lambda/2}` est contenu dans l'ouvert
`{sigma F_j>lambda/4}` avec une marge de niveau stricte, donc une couverture
finie par des boules intérieures rencontre seulement un nombre fini de
composantes.

### Théorème 1 — sélection d'une composante tronquée

Il existe une composante active `alpha_*` telle que

```text
K_(u,alpha_*)>=(C_I/648)K_u^2/K_w,
K_(u,alpha_*)/K_(w,alpha_*)
  >=(C_I/648)(K_u/K_w)^2,                        (2)
```

où `K_(u,alpha)=||U_alpha||_(L^(3,infinity))` et
`K_(w,alpha)=||curl U_alpha||_(L^(3/2,infinity))`. Le cas `K_w=0` est
incompatible avec `K_u>0`.

Si tous les supports des troncatures actives sont contenus dans une boîte

```text
{R_j/2<r<3R_j/2, |z-z_alpha|<Lambda R_j},        (3)
```

le gate directionnel du cycle 0033 s'applique à `G_alpha`, qui est
lipschitzienne compacte. Pour la composante sélectionnée et toute extension
de la direction du curl global,

```text
MO_(B_alpha)(zeta)
 >=c_Lambda [K_(u,alpha_*)/K_(w,alpha_*)]^6
 >=c_Lambda'(K_u/K_w)^12.                        (4)
```

Le changement de signe `sigma` ne modifie pas l'oscillation moyenne. Le gate
0033 a déjà été démontré pour la troncature lipschitzienne utilisée dans sa
preuve; aucune régularité `C^infinity` de `G_alpha` n'est ajoutée en silence.

## Preuve à constantes suivies

### Pas 1 — aucune mesure de bord

La fonction positive `g=(sigma F_j-lambda/4)_+` est lipschitzienne. Pour des
points situés de part et d'autre de `partial C_alpha`, le segment les joignant
rencontre un point où `g=0`; la borne Lipschitz de `g` montre que
`g 1_(C_alpha)` est encore lipschitzienne avec la même constante. La règle de
chaîne Sobolev donne presque partout

```text
nabla G_alpha=1_(C_alpha intersection {sigma F_j>lambda/4}) sigma nabla F_j,
curl U_alpha=sigma W_j sur ce même ensemble,        (5)
```

et zéro ailleurs. Il n'apparaît donc aucune dérivée de mesure portée par le
bord de la composante. La disjonction des supports originaux donne
`K_(w,alpha)<=K_w`.

### Pas 2 — registre de coaire par composante

Sur le coeur de volume `V_alpha`, `G_alpha>lambda/4` et le poids annulaire
donne `|U_alpha|>lambda/6`. Si
`epsilon=max_alpha K_(u,alpha)`, alors

```text
V_alpha^(1/3)<=6epsilon/lambda.                  (6)
```

Pour presque tout `s in (lambda/4,lambda/2)`, le superniveau de la composante
contient son coeur. Coaire tridimensionnelle, isopérimétrie et
`R_j/r>=2/3` donnent

```text
integral_(H_alpha)|curl U_alpha|
 >=(C_I lambda/6)V_alpha^(2/3),                  (7)
H_alpha=C_alpha intersection
        {lambda/4<sigma F_j<lambda/2}.
```

Avec `V=sum V_alpha`, (6) implique

```text
sum V_alpha^(2/3)>=lambda V/(6epsilon).          (8)
```

Les coeurs partitionnent l'union signée du cycle 0035, donc
`V>=|{|U|>lambda}|`. Les halos `H_alpha` sont disjoints et leur union `H`
est incluse dans `{|U|>lambda/6}`. Ainsi

```text
integral_H|W|>=C_I lambda^2 V/(36epsilon),       (9)
|H|^(1/3)<=6K_u/lambda.                          (10)
```

### Pas 3 — comparaison faible-Lorentz

La borne exacte pour faible-`L^(3/2)` donne

```text
integral_H|W|<=3K_w|H|^(1/3)
              <=18K_wK_u/lambda.                (11)
```

En comparant (9) et (11), puis en utilisant (1),

```text
epsilon>=(C_I/648)(1-eta)^3 K_u^2/K_w.          (12)
```

La famille active est finie, son maximum est atteint et `eta` tend vers zéro.
La seconde inégalité (2) suit de `K_(w,alpha_*)<=K_w`.

## Loi d'échelle

Sous `U^(rho)(x)=rho U(rho x)` et `W^(rho)(x)=rho^2 W(rho x)`, toutes les
quasi-normes de (2) et leurs rapports sont invariants. Le volume se transforme
comme `rho^-3`; `lambda V^(2/3)` et `integral_H|W|` comme `rho^-1`. La boîte
(3) se transforme avec `R_j`, et les constantes `C_I/648` et `c_Lambda` ne
dépendent ni du nombre ni de la séparation des gouttelettes.

## Expérience décisive

`COMPONENTWISE-DROPLET-SELECTION-1` remplace chaque volume actif par
`V_alpha=q_alpha^3` et place coaire, isopérimétrie et la borne Lorentz à leur
bord algébrique. Pour 1 920 familles hétérogènes, 10 560 composantes et 5 773
assertions, le script vérifie exactement

```text
q_max sum q_alpha^2>=sum q_alpha^3,
epsilon^3 648^3 K_w^3>=K_u^6.
```

Il teste aussi jusqu'à 1 024 gouttelettes identiques. Après normalisation, le
cube du rapport endpoint global vaut exactement `1/m` : multiplier des
gouttes identiques ne conserve donc pas un rapport global non dégénéré. Un
filament d'amplitude `lambda/8` est absent des niveaux `lambda/4` et
`lambda/6`, quelle que soit sa longueur; la troncature le coupe sans coût de
bord.

Arithmétique : `fractions.Fraction`, aucune grille, aucune graine, zéro échec,
résidu algébrique minimal nul. Empreinte SHA-256 :
`f0550313e21e05a7cda46fd8d1264b982d3ab3b809b5c5b05ec1f77c5c56892a`.
Le calcul n'établit pas coaire, isopérimétrie ou la règle de chaîne au
continuum et ne calcule aucun résidu de PDE.

## Veille différentielle

Les briques publiées restent la coaire de Fleming–Rishel `NS-SRC-0132`,
l'isopérimétrie euclidienne de Federer–Fleming `NS-SRC-0148` et les règles de
réarrangement Lorentz `NS-SRC-0067`. La veille ciblée n'a identifié aucun
théorème primaire sélectionnant une composante connexe de superniveau
pure-swirl avec la constante (2). La composition et le découpage sont donc
internes; aucune antériorité n'est attribuée aux auteurs des briques.

## Passes contradictoires séparées

- Audit analytique, quantificateurs et interface lipschitzienne :
  `e73b332414050d2412ffa9a3cb732363f14b49c84e47d08a02ed773440ca2e65`.
- Contre-modèle multi-gouttes avec parois et caps du filament :
  `03e8153aef4fe599f8a118fc97177c6ce5d9e090b7d26ad99175ce398603f28c`.
- Audit primaire BV, isopérimétrie quantitative et centres multiples :
  `43821be24db518da47e0ef427dd87ae335211fa98f1a0ffe43faeef6b3d02dc6`.

Le certificat embarqué de la seconde passe a été réexécuté séparément : 465
contrôles rationnels, facteur 648 et résidu nul. Ces trois passes sont issues
d'agents IA du même environnement; elles sont séparées et reproductibles,
mais ne constituent pas une revue éditoriale indépendante.

## Passe contradictoire principale

1. **Composante non régulière.** La fonction tronquée est globalement
   lipschitzienne parce qu'elle s'annule sur le bord; aucun périmètre régulier
   de `C_alpha` n'est supposé.
2. **Infinité de gouttes.** La marge entre `lambda/4` et `lambda/2` et la
   compacité rendent finie la famille des composantes qui rencontrent le
   coeur.
3. **Mauvais jacobien.** Volumes, périmètres et coaire sont tridimensionnels;
   `2/3<=R_j/r<=2` est suivi avant toute intégration.
4. **Deux signes dans une composante.** Une composante est définie après
   fixation de `sigma`; les ensembles positifs et négatifs ne se mélangent
   pas.
5. **Curl artificiel du cutoff.** L'identité (5) exclut précisément le terme
   `nabla chi cross U` qui apparaîtrait avec un cutoff spatial arbitraire.
6. **Somme de quasi-normes.** Aucune inégalité triangulaire Lorentz n'est
   utilisée; seules les distributions d'unions disjointes interviennent.
7. **Supremum non atteint.** `eta` reste présent jusqu'à (12).
8. **Packing naïf.** Pour `m` gouttes identiques, le rapport global décroît
   comme `m^(-1/3)`; ce n'est pas un contre-exemple à (2).
9. **Filament sous le seuil.** Il est exactement supprimé. Un pont restant
   au-dessus de `lambda/4` appartient toutefois à la même composante et peut
   rendre son diamètre arbitraire.
10. **Chevauchement.** Si deux supports originaux se chevauchent, (5) ne donne
    plus `K_(w,alpha)<=K_w` à cause des annulations; le théorème ne couvre pas
    ce cas.
11. **Direction globale.** Sur le support du curl tronqué, la direction est
    `sigma` fois celle du curl global; le gate vaut pour toute extension et
    l'inversion globale ne change pas `MO`.
12. **Clay.** Le résultat reste cinématique, sans pression, diffusion,
    stretching, temps maximal, profil ancien ou compacité-rigidité.

## Résultat scientifique et pivot

La dispersion par des gouttelettes reliées uniquement sous `lambda/4` est
fermée dans la classe pure-swirl disjointe : l'une des troncatures porte un
rapport endpoint quadratique, et une borne de diamètre composante par
composante permet de composer avec le gate directionnel. L'hypothèse globale
de diamètre sur la cellule entière n'est plus nécessaire.

Le premier échappement restant est un pont mince qui demeure au-dessus de
`lambda/4`. Il préserve une composante de grand diamètre tout en pouvant avoir
un volume et une capacité très petits. Le verrou devient
`GAP-ABOVE-THRESHOLD-THIN-BRIDGE`.

## Prochaine expérience décisive

Construire un potentiel pure-swirl lisse constitué de deux gouttes de rayon
`R`, distantes de `L R`, reliées par un tube d'amplitude juste supérieure à
`lambda/4`, de rayon `delta R`. Suivre exactement le coût de ses deux couches
de transition dans faible-`L^(3/2)`, puis décider si `delta=delta(L)` peut
garder le rapport endpoint global non dégénéré lorsque `L->infinity`, ou si
le curl du pont force une sous-composante de diamètre `O(R)` après une seconde
troncature.
