# Cycle 0060 — équation moyenne de Haar et transfert de Reynolds

Date : 2026-08-15.

Statut : `AI_INTERNAL_DERIVATION`, avec certificat exact séparé. Aucun
résultat de régularité Clay.

## Décision adaptative

Le verrou relu est
`GAP-TYPE-I-HAAR-DEFECT-DECAY-OR-RSS-RIGIDITY`. Trois actions réellement
distinctes sont notées avant le calcul.

| action | nouveauté | tractabilité | falsifiabilité | levier | total |
|---|---:|---:|---:|---:|---:|
| dériver le système Haar moyen/fluctuant et auditer le signe du stress | 4 | 5 | 5 | 5 | **19** |
| chercher une asymptotique ancienne imposant une moyenne constante | 4 | 3 | 4 | 5 | 16 |
| convertir la capture critique en observable moyen indépendant du temps | 3 | 2 | 4 | 4 | 13 |

La première action est sélectionnée. C'est le premier des trois mécanismes
PDE annoncés au cycle 0059 : la dissipation. Le lemme actif demande ce que
la forte compacité locale fait réellement au stress des fluctuations. Le
test décisif cherche si le transfert d'énergie associé possède un signe.

## Équation, action et type de solution

Sur `R3 x J`, `J` borné, sans frontière, viscosité un et axe `e_3` passant
par l'origine, les champs classiques approchants vérifient

```text
partial_s Z_n-Delta Z_n+div(Z_n tensor Z_n)+nabla Pi_n
 +kappa(1+y dot nabla)Z_n=F_n,
div Z_n=0,                                      (60.1)
```

avec `kappa>0`. La pression est dans la jauge globale de Riesz lorsque
`F_n` est solénoïdale. Le défaut de cutoff `F_n` tend vers zéro localement;
la limite du pipeline est une solution faible adaptée locale, ancienne et
non forcée. Ce n'est ni une solution forte globale, ni automatiquement une
solution mild.

Pour une rotation `R_theta`, les actions covariantes sont

```text
Q0_theta q(y)=q(R_-theta y),
Q1_theta U(y)=R_theta U(R_-theta y),
Q2_theta T(y)=R_theta T(R_-theta y) R_theta^T.  (60.2)
```

Leurs moyennes de Haar sont notées `A_0,A_1,A_2`. Posons

```text
V_n=A_1 Z_n,       W_n=(I-A_1)Z_n,
Sigma_n=A_2(W_n tensor W_n).                    (60.3)
```

Le centrage est essentiel : une rotation autour d'un centre mobile ne
commute pas avec `y dot nabla` sans terme correctif.

## Échelle

Sous l'échelle physique

```text
u_lambda(x,t)=lambda u(lambda x,lambda^2 t),
p_lambda=lambda^2 p(lambda x,lambda^2 t),
```

`V,W` ont le poids `lambda`, `Sigma` et la pression le poids `lambda^2`,
et `div Sigma` le poids `lambda^3`. La norme `L3` de la vitesse et la norme
`L^(3/2)` du stress sont critiques. La densité
`Sigma:nabla V` a le poids `lambda^4`; son intégrale spatiale a le poids
`lambda`, comme le taux de dissipation. Les espaces `H^-3` du cycle 0059
restent locaux et sous-critiques. À `kappa` fixé, l'équation renormalisée
n'est pas déclarée invariante sous une nouvelle dilatation parabolique.

## Lemme actif : fermeture exacte de la moyenne

Les rotations centrées commutent, au sens des distributions, avec
`partial_s`, `Delta`, `1+y dot nabla`, le gradient scalaire et la divergence
tensorielle. Comme `A_1V_n=V_n` et `A_1W_n=0`, la covariance du produit donne

```text
A_2(Z_n tensor Z_n)=V_n tensor V_n+Sigma_n.     (60.4)
```

Les termes croisés ont moyenne nulle, mais `Sigma_n` n'est généralement
pas nul. L'équation moyenne exacte est

```text
partial_s V_n-Delta V_n
 +div(V_n tensor V_n+Sigma_n)+nabla bar(Pi)_n
 +kappa(1+y dot nabla)V_n=bar(F)_n,
div V_n=0.                                      (60.5)
```

L'équation fluctuante exacte est

```text
partial_s W_n-Delta W_n
 +div(V_n tensor W_n+W_n tensor V_n
      +W_n tensor W_n-Sigma_n)+nabla Pi'_n
 +kappa(1+y dot nabla)W_n=F'_n,
div W_n=0,       A_1W_n=0.                     (60.6)
```

Si `F_n` est solénoïdale, la reconstruction globale est

```text
bar(Pi)_n=R_iR_j(V_(n,i)V_(n,j)+Sigma_(n,ij)),
Pi'_n=R_iR_j(V_(n,i)W_(n,j)+W_(n,i)V_(n,j)
              +W_(n,i)W_(n,j)-Sigma_(n,ij)).   (60.7)
```

La pression moyenne n'est donc pas celle de `V_n` seul. Si `F_n` n'est pas
solénoïdale, (60.7) reçoit aussi le potentiel de `div F_n`; (60.5) reste
exacte avec la pression moyenne complète.

## Fermeture forte locale du stress dans le régime rapide

Le cycle 0045 donne, après extraction commune,

```text
Z_n -> Z fortement dans L3_loc(R3 x J),         (60.8)
sup_n ||Z_n||_(L-infinity(J;L^(3,infinity)(R3)))<infinity.
                                                        (60.9)
```

Le cycle 0059, sous divergence de l'infimum essentiel de la vitesse
canonique, donne `mathcal R Z=0`. Pour une action continue de `SO(2)`, cette
égalité distributionnelle implique `Q1_theta Z=Z` pour tout `theta`, donc

```text
A_1Z=Z.                                         (60.10)
```

Sur toute boule centrée et toute sous-fenêtre compacte, `A_1` est une
contraction de `L3`. Ainsi

```text
V_n -> Z fortement dans L3_loc,
W_n -> 0 fortement dans L3_loc,                 (60.11)
```

et Jensen--Hölder donne la constante explicite

```text
||Sigma_n||_(L^(3/2)(K))
 <=||W_n||_(L3(SO(2)K))^2 ->0.                 (60.12)
```

Pour une boule centrée, `SO(2)K=K`. Il n'existe donc aucun défaut de
Reynolds **intérieur** dans cette sous-suite : `div Sigma_n->0` dans les
distributions locales.

La pression reste non locale. La borne globale (60.9) borne `Sigma_n` dans
`L^(3/2,infinity)`. Pour `phi` test, `R_iR_j phi` appartient à
`L^(3,1)`; sa queue tend vers zéro dans cette norme. La dualité de Lorentz,
(60.12) sur une grande boule, puis la petite queue donnent

```text
R_iR_j Sigma_(n,ij) ->0 dans D'(R3 x J).         (60.13)
```

Cette conclusion utilise la jauge globale de Riesz et la borne globale
faible-`L3`; une pression seulement locale peut conserver une composante
harmonique et doit être traitée séparément.

Les équations (60.5), (60.12) et (60.13) passent donc à

```text
partial_s Z-Delta Z+div(Z tensor Z)+nabla Pi
 +kappa(1+y dot nabla)Z=0,
div Z=0,       A_1Z=Z.                          (60.14)
```

C'est exactement l'équation renormalisée axisymétrique, swirl permis. Elle
n'ajoute aucune identité à l'équation limite déjà obtenue au cycle 0045.
En particulier,

```text
partial_s A_1Z_n=A_1 partial_sZ_n=A_1r_n        (60.15)
```

peut converger vers `partial_sZ` non nul.

## Premier mécanisme testé : budget dissipatif

Pour des champs lisses de Schwartz, définissons

```text
T(s)=integral_R3 Sigma_n:nabla V_n
    =integral_R3 (W_n tensor W_n):nabla V_n.    (60.16)
```

Les intégrations par parties donnent exactement

```text
(1/2)d_s||V_n||_2^2+||nabla V_n||_2^2
 -(kappa/2)||V_n||_2^2=<bar(F)_n,V_n>+T,        (60.17)

(1/2)d_s||W_n||_2^2+||nabla W_n||_2^2
 -(kappa/2)||W_n||_2^2=<F'_n,W_n>-T.           (60.18)
```

Le drift contribue `-kappa||U||_2^2/2` au membre gauche en dimension trois;
déplacé à droite, c'est une source renormalisée. Les deux transferts sont
opposés et s'annulent dans le budget total.

Le tenseur `Sigma_n` est positif semi-défini, mais il contracte la partie
symétrique sans trace de `nabla V_n`. Cette contraction n'a aucun signe.
De plus, la seule borne globale faible-`L3` ne donne pas des énergies `L2`
finies : (60.17)--(60.18) ne sont alors que des identités de modèle lisse,
pas des budgets disponibles pour la limite suitable.

## Test adverse exact du signe

Écrivons `q=x^2+y^2+z^2` et considérons les potentiels de Schwartz

```text
A_V=(-yz,xz,0) exp(-q),
A_W=(0,0,x) exp(-q),
V=curl A_V,       W=curl A_W.                  (60.19)
```

Alors `V,W` sont divergence-free, `V` est axisymétrique, et `A_1W=0` : le
potentiel `A_W` est un mode azimutal `m=1`, tandis que curl commute aux
rotations. Le calcul exact des moments gaussiens donne

```text
integral_R3 (W tensor W):nabla V
 =-(8/27)(pi/3)^(3/2).                         (60.20)
```

Remplacer `V` par `-V` conserve toutes les contraintes et inverse le signe.
Le test ne simule pas Navier--Stokes et ne produit pas un blow-up; il réfute
précisément toute coercivité issue des seules propriétés
`div V=div W=0`, `A_1V=V`, `A_1W=0` et `Sigma>=0`.

## Raccord publié découvert par la passe indépendante

L'échec du signe ne laisse finalement pas ouverte la rigidité de la limite
axisymétrique dans le paquet complet du pipeline. Deux résultats publiés se
composent :

1. Seregin 2020 (`NS-SRC-0222`, théorème 2.1 et section 3) montre qu'une
   paire suitable axisymétrique, swirl permis, localement
   `L-infinity_t L^(3,infinity)_x`, n'a ni singularité Type I ni Type II.
   Une ancienne solution satisfaisant la borne globale uniforme est donc
   classique à tout point intérieur.
2. Ożański--Palasek 2023 (`NS-SRC-0088`, théorème 1.1) donnent, pour une
   solution classique axisymétrique sur `[s,t]`,

   ```text
   ||u(t)||_infinity<=C(A_*)(t-s)^(-1/2).          (60.21)
   ```

   La constante ne dépend pas de `s`. Faire `s->-infinity` donne `u(t)=0`.

La pression de Riesz d'une vitesse axisymétrique est elle-même
axisymétrique, à jauge temporelle près. Ainsi

```text
ancienne suitable + axe fixe + pression de Riesz
 + sup_(t<0)||u(t)||_(L^(3,infinity)(R3))<infinity
  --> u classique                     [Seregin 2020]
  --> u=0.                             [Ożański--Palasek 2023] (60.22)
```

La dérenormalisation du pipeline doit toujours être exécutée : (60.22)
porte sur la NS physique sans drift, pas directement sur (60.14). Sous le
ledger déjà séparé de dérenormalisation, suitability, pression, borne
faible-`L3` et capture, `u=0` contredit la non-trivialité. La condition
`partial_s mathcal AZ_n->0` n'est donc plus nécessaire dans cette branche.

## Passe contradictoire

1. La moyenne tensorielle de (60.2), et non une moyenne composante par
   composante, est requise pour commuter avec la divergence.
2. `A_2(W tensor W)` ne se factorise pas en `A_1W tensor A_1W`.
3. Les termes croisés disparaissent de la moyenne, pas de l'équation de
   fluctuation.
4. La pression moyenne contient le stress; l'ignorer détruit la divergence
   nulle et la non-localité.
5. La disparition locale du stress utilise la forte `L3_loc`; la seule
   convergence distributionnelle ne suffit pas.
6. Le passage de la pression utilise en plus la borne globale faible-`L3`
   et la jauge de Riesz. Une constante ou une partie harmonique locale n'est
   pas contrôlée par un argument purement local.
7. L'axisymétrie obtenue autorise le swirl et la dépendance temporelle.
8. Les budgets globaux ne sont pas disponibles depuis la seule suitability
   locale.
9. La positivité de `Sigma` ne fixe pas le signe de `Sigma:nabla V`.
10. L'annulation de `Sigma_n` à la limite ne donne pas un taux contrôlant
    `partial_sV_n`.
11. Ożański--Palasek seuls supposent une solution classique; les appliquer
    directement à (60.14) serait faux. Seregin 2020 fournit séparément le
    raccord suitable-vers-classique.
12. La constante faible-`L3` doit être unique sur tout le passé. Des bornes
    dépendant de la fenêtre ne permettent pas la limite dans (60.21).
13. L'axisymétrie concerne la paire vitesse--pression autour d'un axe fixe.
    La jauge globale de Riesz ferme ce quantificateur; un axe mobile ou une
    pression locale arbitraire ne se transfère pas.
14. Wang--Yang 2026 traite des D-solutions stationnaires physiques avec
    décroissance supplémentaire. Ce résultat récent n'est pas utilisé dans
    (60.22).

## Résultat et décision

Le lemme ferme le calcul du stress, de la pression et de leur passage à la
limite. La forte compacité montre qu'aucun stress non axisymétrique ne
survit à l'intérieur. Ce résultat est positif mais insuffisant : l'équation
moyenne limite est simplement l'équation axisymétrique complète.

Le mécanisme « dissipation seule » est abandonné. `FAIL-NS-0096` enregistre
le transfert sans signe. La passe bibliographique indépendante ferme
toutefois la branche ancienne axisymétrique par (60.22), sans stationnarité.
Les mécanismes « asymptotique ancienne » et « capture pour stationnariser »
deviennent donc inutiles et ne sont pas comptés comme échecs.

Le verrou suivant est

```text
GAP-TYPE-I-METRIC-ROBUST-FAST-AXISYMMETRIZATION.             (60.23)
```

La prochaine expérience décisive décompose `partial_sZ` et `mathcal RZ` en
modes azimutaux dans le Hilbert du cycle 0059. Elle testera si la vitesse
canonique est une moyenne pondérée des vitesses modales et si la propriété
`ess inf|beta_n|->infinity` est robuste sous changement des poids invariants.
Un contre-exemple métrique éliminerait la production automatique du régime
rapide; une borne uniforme sur tous les poids donnerait au contraire un
critère intrinsèque d'axisymétrisation.
