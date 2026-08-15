# Cycle 0061 — dépendance métrique entre les isotypes SO(2) \(k=1,2\)

Date d'exécution : 2026-08-15

## Verdict

La phase hilbertienne canonique

\[
\beta_w
=
\frac{\langle d,g\rangle_w}{\langle g,g\rangle_w}
\tag{1}
\]

n'est pas intrinsèque à la seule trajectoire modale. Elle dépend du produit scalaire utilisé pour projeter \(d\) sur la tangente \(g=RZ\).

Pour les isotypes SO(2) distincts \(k=1\) et \(k=2\), avec amplitudes choisies pour égaliser les Gram tangentiels et vitesses \(+N\) et \(-N\), deux métriques fixes, positives et uniformément équivalentes donnent :

\[
\beta_{(1,1)}=0,
\qquad
\beta_{(2,1)}=\frac N3.
\tag{2}
\]

La différence est d'ordre \(N\), malgré un rapport d'équivalence métrique constant égal à \(2\).

Un second modèle montre que la visibilité asymptotique d'un mode lent dépend également du choix entre métrique fixe et poids dépendant de \(N\). La métrique doit donc être figée dans tout énoncé de modulation, et toute famille de métriques doit avoir des constantes d'équivalence uniformes.

Le certificat est une expérience exacte en dimension quatre. Il ne réalise aucun champ ni aucune solution de Navier–Stokes.

## 1. Représentation et jauge pondérée

Posons

\[
H=\mathbb R^2\oplus\mathbb R^2
\]

et

\[
J(x,y)=(-y,x),
\qquad
R=J\oplus2J.
\]

Le premier bloc est l'isotype azimutal \(k=1\), le second l'isotype \(k=2\) : sous un angle \(\theta\), ils tournent respectivement de \(\theta\) et \(2\theta\). Ils ne sont donc pas deux copies équivalentes. Pour deux poids strictement positifs \(w_1,w_2\), définissons

\[
\langle u,v\rangle_w
=
w_1u_1\cdot v_1+w_2u_2\cdot v_2.
\tag{3}
\]

Cette métrique est SO(2)-invariante. Si

\[
g=RZ
\]

et \(g\ne0\), la projection canonique est (1), avec résidu transverse

\[
r_w=d-\beta_wg.
\tag{4}
\]

Le certificat vérifie pour chaque cas :

\[
d=\beta_wg+r_w,
\tag{5}
\]

\[
\langle r_w,g\rangle_w=0,
\tag{6}
\]

\[
\|d\|_w^2
=
\|\beta_wg\|_w^2+\|r_w\|_w^2.
\tag{7}
\]

Attention au vocabulaire : le résidu canonique \(r_w\) de (4) est généralement non nul. Les « résidus zéro » du calcul sont l'erreur de reconstruction

\[
d-\beta_wg-r_w=0
\]

et le résidu d'orthogonalité (6), tous deux exactement nuls en arithmétique rationnelle.

## 2. Vitesses opposées et métriques fixes

Prenons deux vecteurs unitaires \(z_1,z_2\) dans les plans \(k=1\) et \(k=2\), et choisissons l'état

\[
Z=(z_1,\tfrac12z_2).
\]

Le facteur \(1/2\) compense le facteur \(2\) du second générateur. Ainsi,

\[
g=RZ=(Jz_1,Jz_2).
\]

Les deux tangentes modales ont exactement une norme égale à \(1\), bien que les isotypes soient distincts. Considérons la dérivée modale

\[
d=(N Jz_1,-N Jz_2).
\tag{8}
\]

Les contributions de Gram sont

\[
G_1=w_1,
\qquad
G_2=w_2,
\qquad
\langle g,g\rangle_w=w_1+w_2.
\]

Le numérateur de (1) vaut

\[
\langle d,g\rangle_w=Nw_1-Nw_2.
\]

Par conséquent,

\[
\boxed{
\beta_w=N\frac{w_1-w_2}{w_1+w_2}.}
\tag{9}
\]

### Poids égaux

Pour \(w=(1,1)\),

\[
\langle g,g\rangle_w=2,
\qquad
\langle d,g\rangle_w=0,
\qquad
\beta_w=0.
\]

Ici,

\[
r_w=d,
\qquad
\|d\|_w^2=\|r_w\|_w^2=2N^2.
\]

Les deux vitesses opposées s'annulent exactement dans la projection scalaire.

### Poids \(2:1\)

Pour \(w=(2,1)\),

\[
\langle g,g\rangle_w=3,
\qquad
\langle d,g\rangle_w=N,
\qquad
\boxed{\beta_w=\frac N3.}
\]

Les vitesses résiduelles des deux modes sont

\[
N-\beta_w=\frac{2N}{3},
\qquad
-N-\beta_w=-\frac{4N}{3}.
\]

Les trois termes de Pythagore valent

\[
\|d\|_w^2=3N^2,
\qquad
\|\beta_wg\|_w^2=\frac{N^2}{3},
\qquad
\|r_w\|_w^2=\frac{8N^2}{3}.
\]

Les deux métriques sont fixes et uniformément équivalentes, mais leurs phases canoniques ont des asymptotiques différentes. La compensation de modes opposés rend donc la jauge sensible même à une modification bornée du produit scalaire.

Le script vérifie ces identités aux quatre orientations de quart de tour et sur dix échelles \(N=2,\ldots,1024\).

## 3. Mode lent asymptotiquement invisible

Considérons maintenant un état rapide \(k=1\) d'amplitude \(1\) et de vitesse \(N\), ainsi qu'un état lent \(k=2\) d'amplitude

\[
\frac1{2N}
\]

et de vitesse \(1\). Le générateur \(2J\) transforme cette amplitude d'état en amplitude tangentielle \(1/N\). Posons \(\varepsilon_N=1/N\) pour cette amplitude tangentielle. Ainsi,

\[
g_N=(Jz_1,\varepsilon_NJz_2),
\]

\[
d_N=(NJz_1,\varepsilon_NJz_2).
\tag{10}
\]

### Métrique fixe

Avec \(w=(1,1)\), les contributions de Gram sont

\[
G_{\rm rapide}=1,
\qquad
G_{\rm lent}=\frac1{N^2}.
\]

La part lente du Gram vaut donc

\[
\frac{G_{\rm lent}}{G_{\rm rapide}+G_{\rm lent}}
=
\frac1{N^2+1}
\longrightarrow0.
\tag{11}
\]

Le mode lent devient asymptotiquement invisible pour la projection. La phase exacte est

\[
\boxed{
\beta_N^{\rm fixe}
=
\frac{N+N^{-2}}{1+N^{-2}}
=
\frac{N^3+1}{N^2+1}.}
\tag{12}
\]

Elle vérifie

\[
1-\frac{\beta_N^{\rm fixe}}N
=
\frac{N-1}{N(N^2+1)}
\longrightarrow0.
\]

### Poids dépendant de \(N\)

Prenons maintenant

\[
w_N=(1,N^2).
\tag{13}
\]

Le poids du mode lent compense exactement son amplitude :

\[
G_{\rm rapide}=1,
\qquad
G_{\rm lent}=N^2\varepsilon_N^2=1.
\]

Sa part de Gram redevient

\[
\frac12,
\]

et la phase vaut

\[
\boxed{
\beta_N^{\rm dépendante}
=\frac{N+1}{2}.}
\tag{14}
\]

La même trajectoire modale produit donc \(\beta_N\sim N\) sous la métrique fixe et \(\beta_N\sim N/2\) sous la métrique dépendante. Les constantes d'équivalence de (13) divergent comme \(N^2\) : ce changement n'est pas une perturbation métrique uniforme.

### Poids \(N^4\) : coefficient artificiellement borné

Pour exposer le danger maximal, prenons la métrique

\[
\widetilde w_N=(1,N^4).
\tag{15}
\]

Le Gram effectif du mode lent vaut maintenant

\[
\widetilde G_{\rm lent}
=N^4\varepsilon_N^2
=N^2,
\]

sa part du Gram total vaut

\[
\frac{N^2}{N^2+1}\longrightarrow1,
\]

et la phase canonique devient

\[
\boxed{
\widetilde\beta_N
=
\frac{N+N^2}{1+N^2}
\longrightarrow1.}
\tag{16}
\]

Le script vérifie même la borne exacte

\[
1<\widetilde\beta_N<2
\qquad(N\ge2).
\]

Une vitesse modale rapide égale à \(N\) produit donc un coefficient canonique borné après modification \(N\)-dépendante de la métrique. Ce cas est volontairement interdit dans une formulation à métrique fixe : le rapport des poids croît comme \(N^4\).

Ce test distingue deux mécanismes :

1. sous une métrique fixe, un mode dont la tangente physique décroît peut devenir réellement invisible ;
2. des poids dépendant de \(N\) peuvent restaurer ou surpondérer artificiellement sa contribution, jusqu'à rendre \(\beta_N\) borné.

## 4. Passe contradictoire

Le certificat réfute les formulations trop faibles suivantes :

| formulation | contre-exemple exact |
|---|---|
| la phase canonique est indépendante d'une métrique fixe équivalente | \(0\) contre \(N/3\) pour les poids \(1:1\) et \(2:1\) |
| l'équivalence ponctuelle des normes suffit à préserver l'asymptotique | la compensation opposée amplifie un changement métrique borné |
| un mode lent est intrinsèquement invisible | le poids \(N^2\) restaure une part de Gram égale à \(1/2\) |
| des poids positifs dépendant de \(N\) sont inoffensifs | le poids \(N^4\) force \(\beta_N\to1\) malgré une vitesse \(N\) |

Une utilisation robuste de (1) doit donc :

- fixer le produit scalaire avant le passage \(N\to\infty\) ;
- suivre les Gram modaux ;
- exclure ou quantifier les compensations signées ;
- imposer des constantes d'équivalence uniformes pour toute métrique variable ;
- distinguer la stabilité de \(\beta\) de celle de la projection \(\beta g\).

## 5. Séparation stricte avec Navier–Stokes

Les « modes » sont les isotypes abstraits distincts \(k=1\) et \(k=2\) de SO(2). Le certificat ne construit :

- aucun champ vectoriel sur \(\mathbb R^3\) ou \(\mathbb T^3\) ;
- aucune condition de divergence ;
- aucune pression ni projection de Leray ;
- aucune interaction convective ;
- aucune solution faible, forte, suitable ou ancienne.

Les vitesses \(+N\), \(-N\), \(N\) et \(1\) sont prescrites. Aucun lemme de raccord à Navier–Stokes n'est fourni. Le résultat porte uniquement sur la robustesse métrique d'une projection hilbertienne finie.

## 6. Reproduction

Commandes :

~~~powershell
python -B experiments/navier-stokes/modal-metric-robustness/modal_metric_robustness.py
git diff --check
~~~

Sortie validée :

~~~text
modal_metric_robustness: PASS
exact_assertions=1809
opposed_equal_weights=beta_N=0
opposed_weights_2_to_1=beta_N=N/3
fixed_metric_slow_share=1/(N^2+1)_to_zero
N_dependent_metric_slow_share=1/2_and_beta_N=(N+1)/2
N4_metric=slow_share=N^2/(N^2+1)_and_beta_N=(N^2+N)/(N^2+1)_to_1
identity_residual=0; orthogonality_residual=0; arithmetic=Fraction
case_sha256=9d36b7f8992dc961a4882ed2475303e4aa004bcc40f5c87e7f998f4a73fa286c
seed=n/a; scope=SO(2) isotypes k=1 and k=2; no PDE realization
sha256_self=e38b2c7ff22c0821b28c71b2067543a2c5cd186362db88bb7b5039df44cafbe3
~~~

Validation :

~~~text
git_diff_check=PASS
~~~

Les 1809 assertions utilisent exclusivement **Fraction**. Elles certifient les Gram, coefficients canoniques, reconstructions, orthogonalités et identités de Pythagore. Graine : non applicable.

Empreinte SHA-256 du script :

~~~text
e38b2c7ff22c0821b28c71b2067543a2c5cd186362db88bb7b5039df44cafbe3
~~~

Empreinte SHA-256 des cas rationnels :

~~~text
9d36b7f8992dc961a4882ed2475303e4aa004bcc40f5c87e7f998f4a73fa286c
~~~

## Décision

**CONSERVER** ce certificat comme test adverse de robustesse métrique. **ABANDONNER** toute phase dite canonique sans métrique explicitement figée. **RÉVISER** toute métrique dépendant de \(N\) en suivant ses constantes d'équivalence et les Gram modaux. Aucune revendication PDE.
