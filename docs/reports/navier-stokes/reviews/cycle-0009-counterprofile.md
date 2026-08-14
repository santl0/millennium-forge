# Cycle 0009 — contre-profils pour la permutation limite/trace

> **Correction de synthèse.** Les contre-profils testent la permutation au
> bord abstrait `s=0`. Pour un vrai zoom par temps records KNSS, ce bord est le
> temps `t_k`, pas le temps physique `T`, lequel correspond à l'extrémité
> mobile `B_k=M_k²(T-t_k)>0`. Le résidu exact reste valide, mais sa portée est
> limitée à la porte de commutation au temps-record.

Date : 2026-08-14.

## Question falsifiable

Pour une suite maximum-normalisée `v_k`, peut-on déduire une trace terminale
nulle du profil limite en permutant

```text
k -> infini puis s -> 0-
```

avec

```text
s -> 0- puis k -> infini ?
```

Le test cherche prioritairement des solutions exactes de Navier–Stokes
incompressible non forcé. Les deux familles ci-dessous sont exactes ; aucun
champ arbitraire non-trajectory n'est nécessaire. Elles isolent cependant
deux portes différentes : la jauge de pression/mildness et la stabilité
rétrograde des hautes fréquences.

Sauf mention contraire,

\[
 \partial_s v+(v\cdot\nabla)v+\nabla q-\Delta v=0,
 \qquad \nabla\cdot v=0,
\]

avec viscosité `nu=1`.

## Échelle de l'extraction maximum-normalisée

Si `M_k=|u(x_k,t_k)|` et

\[
 v_k(y,s)=M_k^{-1}u(x_k+M_k^{-1}y,t_k+M_k^{-2}s),
 \qquad
 q_k(y,s)=M_k^{-2}p(x_k+M_k^{-1}y,t_k+M_k^{-2}s),
\]

alors

\[
 \operatorname{div}_y v_k=M_k^{-2}\operatorname{div}_xu,
 \qquad
 \mathcal R_{NS}(v_k,q_k)=M_k^{-3}\mathcal R_{NS}(u,p).
\]

La remise à l'échelle conserve donc exactement l'équation et donne
`|v_k(0,0)|=1`. Elle conserve également la norme critique :

\[
 \|v_k(\cdot,s)\|_{L^3(\mathbb R^3)}
 =\|u(\cdot,t_k+M_k^{-2}s)\|_{L^3(\mathbb R^3)}.
\]

Ainsi, demander une borne uniforme `L^infinity_s L^3_x` aux zooms revient
exactement à la demander aux tranches originales correspondantes. Ce n'est
pas une conséquence de la normalisation par le maximum.

## Test A — non-commutation exacte par pression affine

Pour `k>=1`, sur `R^3 x (-infini,0]`, posons

\[
 a_k(s)=e^{k^2s},\qquad
 v_k(x,s)=a_k(s)e_1,\qquad
 q_k(x,s)=-k^2a_k(s)x_1.
\]

### Vérifications exactes

On a

\[
 \nabla\cdot v_k=0,\quad
 (v_k\cdot\nabla)v_k=0,\quad
 \Delta v_k=0,\quad
 \partial_sv_k=k^2a_k e_1,\quad
 \nabla q_k=-k^2a_k e_1.
\]

Par conséquent

\[
 \mathcal R_{NS}(v_k,q_k)=0
\]

identiquement, sans discrétisation ni arrondi. La famille est classique,
ancienne, localement adaptée et uniformément bornée :

\[
 \sup_{k\ge1}\sup_{s\le0,x\in\mathbb R^3}|v_k(x,s)|=1,
 \qquad |v_k(0,0)|=1.
\]

L'égalité locale d'énergie tient aussi exactement :

\[
 \partial_s\frac{|v_k|^2}{2}
 +\nabla\cdot\left[\left(\frac{|v_k|^2}{2}+q_k\right)v_k\right]
 -\Delta\frac{|v_k|^2}{2}+|\nabla v_k|^2
 =a_ka_k'-a_ka_k'=0.
\]

### Pairings distributionnels et deux ordres de limites

Pour tout champ test `phi in C_c^infinity(R^3;R^3)`, notons

\[
 I_\phi=\int_{\mathbb R^3}\phi_1(x)\,dx.
\]

Alors

\[
 \langle v_k(s),\phi\rangle=e^{k^2s}I_\phi.
\]

Si `I_phi != 0`, les deux limites itérées sont différentes :

\[
 \lim_{s\uparrow0}\lim_{k\to\infty}
 \langle v_k(s),\phi\rangle=0,
 \qquad
 \lim_{k\to\infty}\lim_{s\uparrow0}
 \langle v_k(s),\phi\rangle=I_\phi.
\]

Le défaut est donc déjà visible dans `D'(R^3)`, avec un résidu PDE exactement
nul.

Le module terminal n'est pas uniforme :

\[
 \sup_k|\langle v_k(0)-v_k(s),\phi\rangle|
 =|I_\phi|\qquad(s<0).
\]

Il ne tend pas vers zéro lorsque `s->0-`. Équivalemment,
`||partial_s v_k(0)||_infinity=k^2`.

### Porte violée

Cette famille n'est pas mild au sens KNSS. La formule mild annule le terme de
Duhamel pour une vitesse spatialement constante et imposerait
`v_k(t)=v_k(s)`. Ici, toute la variation temporelle est portée par la partie
affine harmonique de la pression. En outre,

\[
 \|v_k(s)\|_{L^3(\mathbb R^3)}
 =\|v_k(s)\|_{L^{3,\infty}(\mathbb R^3)}=+\infty
\]

pour `s` fini, et `q_k(.,s)` n'appartient pas à `BMO(R^3)` modulo les
constantes. Sur une boule,

\[
 \|v_k(s)\|_{L^3(B_R)}
 =e^{k^2s}(4\pi R^3/3)^{1/3},
\]

ce qui montre que tous les contrôles locaux restent pourtant uniformes.

**Conclusion du test A.** La commutation est fausse pour des solutions NS
classiques, bornées et localement adaptées. La propriété mild, ou une jauge
globale équivalente de pression, est une hypothèse indispensable ; elle ne peut
être remplacée par le seul résidu PDE et l'inégalité locale d'énergie.

## Test B — cisaillement calorique exact et coût de la mildness

Sur le tore normalisé `T^3=(R/2pi Z)^3`, posons

\[
 w_k(x,s)=e^{-k^2s}\cos(kx_2)e_1,\qquad r_k=0,
 \qquad s\le0.
\]

Il s'agit d'un cisaillement mild exact :

\[
 \nabla\cdot w_k=0,\qquad
 (w_k\cdot\nabla)w_k=w_{k,1}\partial_1w_k=0,
\]

et

\[
 \partial_sw_k-\Delta w_k
 =-k^2w_k-(-k^2w_k)=0.
\]

Le résidu et la divergence sont donc exactement nuls, et
`|w_k(0,0)|=1`.

À la tranche terminale, `w_k(.,0)=cos(kx_2)e_1 -> 0` dans `D'(T^3)` malgré
la normalisation ponctuelle. La raison est l'absence de compacité spatiale :

\[
 \|\nabla w_k(\cdot,0)\|_\infty=k.
\]

En revanche, pour chaque `s<0`,

\[
 \|w_k(\cdot,s)\|_\infty=e^{k^2|s|}\to\infty.
\]

La limite `k->infini` à temps négatif fixé n'existe même pas dans `D'`. Par
exemple, pour le test analytique fixe

\[
 \phi(x)=e_1\sum_{n\ge1}e^{-n}\cos(nx_2),
\]

avec mesure de Haar normalisée,

\[
 \langle w_k(s),\phi\rangle
 =\tfrac12e^{k^2|s|-k}\to+\infty.
\]

La norme critique exacte vaut

\[
 \|w_k(\cdot,s)\|_{L^3(\mathbb T^3)}
 =\left(\frac{4}{3\pi}\right)^{1/3}e^{k^2|s|}.
\]

Donc, pour tout `tau>0`,

\[
 \|w_k\|_{L^\infty([-\tau,0];L^3)}
 =\left(\frac{4}{3\pi}\right)^{1/3}e^{k^2\tau}\to\infty.
\]

Sur l'intervalle mobile `[-k^-2,0]`, cette norme reste au plus
`e(4/(3pi))^(1/3)`, mais aucun temps négatif fixe n'appartient à tous ces
intervalles. On perd alors précisément le premier ordre de limite.

**Conclusion du test B.** Pour une trajectoire mild dissipative, imposer une
oscillation de fréquence `k` et une amplitude terminale unité exige une
amplification rétrograde `e^{k^2|s|}`. Le mécanisme qui ferait disparaître la
normalisation dans `D'` détruit soit la borne uniforme sur un intervalle passé
commun, soit la borne critique `L^infinity_sL^3_x`.

Le tore n'est pas le domaine Clay `R^3`; ce test ne prétend pas être une
extraction de singularité. Il falsifie seulement une étape fonctionnelle de
commutation qui ignorerait la stabilité rétrograde et la compacité spatiale.

## Lemme abstrait testé sur une vraie extraction maximum-normalisée

Supposons maintenant que, sur un intervalle commun `[-delta,0]`, une famille
`v_k` vérifie :

1. `|v_k(0,0)|=1` ;
2. `sup_k ||nabla v_k(.,0)||_infinity <= L` ;
3. pour chaque `s<0`, `v_k(s)->0` dans `D'` ;
4. pour tout test `phi`, il existe `omega_phi(h)->0` tel que
   \[
   \sup_k|\langle v_k(0)-v_k(-h),\phi\rangle|
   \leq\omega_\phi(h).
   \]

Après extraction, `v_k(0,0)->q` avec `|q|=1`. Pour `k` assez grand,
`q dot v_k(x,0)>=1/2` sur une boule de rayon dépendant seulement de `L`.
Choisissons `rho>=0`, d'intégrale un, supportée dans cette boule, et
`phi=q rho`. Alors

\[
 \langle v_k(0),\phi\rangle\ge\tfrac12.
\]

Mais (3)–(4) donnent, pour chaque `h>0`,

\[
 \limsup_{k\to\infty}|\langle v_k(0),\phi\rangle|
 \leq\omega_\phi(h),
\]

puis zéro lorsque `h->0`. Contradiction.

Un module terminal uniforme ne contredit donc pas **à lui seul** la
normalisation — la solution constante `v=e_1` a un module nul. Il la contredit
exactement lorsqu'on lui ajoute la disparition distributionnelle des tranches
négatives et l'équi-continuité spatiale qui rend l'évaluation ponctuelle stable.

Dans une famille ancienne mild maximum-normalisée, une borne uniforme de
vitesse sur un intervalle passé commun fournit justement les bornes uniformes
de dérivées intérieures. Par conséquent, si l'extraction converge localement
uniformément jusqu'à `s=0`, la normalisation se transmet et interdit que le
même profil possède une trace terminale nulle. Ce n'est pas un défaut
technique de permutation : les deux conclusions sont mathématiquement
incompatibles.

## Le module réintroduit-il `L^infinity_t L^3_x` ?

- **Non, en général.** Un module `D'` local, combiné aux estimations de lissage
  issues d'une borne `L^infinity_{x,s}` mild, ne fournit aucune intégrabilité
  globale en espace. La solution constante le montre.
- **Oui, si la preuve proposée du module utilise une tension globale `L^3`.**
  La norme `L^3` est exactement invariante sous la normalisation par le
  maximum. Une borne uniforme sur les zooms est donc l'hypothèse endpoint
  `L^infinity_tL^3_x` sur les tranches originales, déjà soumise au critère
  ESS ; l'utiliser pour exclure un blow-up Clay général serait circulaire.
- **Le vrai verrou n'est pas le module seul.** Sous les bornes KNSS, le lissage
  donne déjà la compacité locale et conserve `|v(0,0)|=1`. Ce qui ne peut être
  ajouté est la convergence vers zéro des mêmes tranches négatives/terminales.
  ESS obtient une trace nulle pour une autre extraction, sous une borne
  critique globale différente.

## Reproduction symbolique minimale

Le contrôle suivant ne fait intervenir ni grille ni flottant :

```python
from fractions import Fraction

for k in range(1, 65):
    # Test A, après factorisation de exp(k^2 s)e_1 :
    # partial_s v donne k^2 et partial_1 q donne -k^2.
    assert k * k + (-k * k) == 0

    # Test B, après factorisation de exp(-k^2 s)cos(kx_2)e_1 :
    # partial_s donne -k^2 et Delta donne -k^2.
    assert (-k * k) - (-k * k) == 0

# 4 integral_0^(pi/2) cos(theta)^3 dtheta = 4*(2/3)=8/3.
integral_abs_cos3 = 4 * Fraction(2, 3)
assert integral_abs_cos3 == Fraction(8, 3)
print("residuals=0; integral_abs_cos3=8/3")
```

Les identités générales sont démontrées par factorisation juste au-dessus ; le
script en contrôle les coefficients exactement pour `1<=k<=64`, sans paquet
externe. Résidu analytique des deux équations : `0`. Graine, pas spatial, pas
temporel et erreur d'arrondi : sans objet.

## Verdict

Le contre-profil A réfute exactement la permutation dans la classe classique
bornée/localement adaptée ; sa non-mildness identifie la porte manquante. Le
test B montre qu'une tentative mild par hautes fréquences paie une croissance
rétrograde exponentielle et perd toute borne uniforme sur un intervalle passé
commun, notamment `L^infinity_tL^3_x`.

Pour une véritable extraction maximum-normalisée KNSS, un module terminal
uniforme compatible avec les estimations intérieures ne fabrique donc pas une
trace nulle : avec la convergence négative vers zéro, il contredirait la
normalisation. Le prochain lemme ne doit pas chercher à forcer cette
permutation ; il doit expliquer pourquoi une extraction différente portant
une trace nulle représenterait le **même objet**, ou abandonner ce raccord.
