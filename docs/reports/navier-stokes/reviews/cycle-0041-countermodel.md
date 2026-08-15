# Cycle 0041 — certificat exact faible-L3 vers L2 local

Date d'audit : 2026-08-15.

## Verdict

La constante 3 dans l'inclusion de Lorentz sur un ensemble de mesure finie est certifiée et optimale : si

\[
K_3(f):=\sup_{\lambda>0}\lambda\,|\{|f|>\lambda\}|^{1/3}<\infty,
\qquad |E|=V<\infty,
\]

et si l'on restreint `f` à `E`, alors

\[
\|f\|_{L^2(E)}^2\leq 3K_3(f)^2V^{1/3}.
\]

La constante est un supremum : les profils étagés rationnels ci-dessous l'approchent, sans l'atteindre à paramètres finis. Le certificat ne fournit aucune énergie minimale dans un coeur spatial et ne constitue donc pas, seul, un lemme de capture Type I.

## Dérivation avec constantes suivies

Posons (K=K_3(f)). La fonction de distribution vérifie

\[
\mu_f(t):=|\{|f|>t\}|\leq \min\{V,K^3t^{-3}\}.
\]

Avec (t_0=KV^{-1/3}), la formule des couches donne exactement

\[
\begin{aligned}
\|f\|_2^2
 &=2\int_0^\infty t\mu_f(t)\,dt\\
 &\leq 2V\int_0^{t_0}t\,dt
   +2K^3\int_{t_0}^{\infty}t^{-2}\,dt\\
 &=Vt_0^2+2K^3t_0^{-1}
 =3K^2V^{1/3}.
\end{aligned}
\]

Cette preuve utilise seulement la mesure finie du support. Sur tout ℝ³, une borne faible-L3 ne contrôle pas la norme L2 sans information supplémentaire sur les queues.

## Suite rationnelle adverse et optimalité

Pour (m,N\geq1), posons (q=(m+1)/m), (r=q^{-1}), les amplitudes (a_k=q^k), et les masses

\[
w_k=q^{-3k}-q^{-3(k+1)}\quad(0\leq k<N),
\qquad w_N=q^{-3N}.
\]

Alors (sum_{k=0}^Nw_k=1). À chaque niveau (a_k), la masse cumulée à gauche vaut

\[
\mu(a_k^-)=\sum_{j=k}^Nw_j=q^{-3k},
\]

d'où (a_k^3\mu(a_k^-)=1) et (K_3=1) exactement. La nuance de convention est suivie : pour (mu(t)=|\{|f|>t\}|), la valeur au seuil est (q^{-3(k+1)}) lorsque (k<N), mais le supremum est la limite à gauche (q^{-3k}).

Le calcul exact de la norme est

\[
\begin{aligned}
L_{m,N}:=\|f\|_2^2
 &=\sum_{k=0}^{N-1}q^{2k}(q^{-3k}-q^{-3(k+1)})
   +q^{2N}q^{-3N}\\
 &=(1+r+r^2)(1-r^N)+r^N.
\end{aligned}
\]

Son erreur exacte par rapport à 3 vaut

\[
3-L_{m,N}=(2-r-r^2)+(r+r^2)r^N>0.
\]

En faisant d'abord croître (N), puis (m), cette erreur tend vers zéro. Ainsi aucune constante universelle strictement inférieure à 3 ne peut remplacer 3.

## Remise à l'échelle exacte

Afin de rester dans l'arithmétique rationnelle, on écrit `beta=s^3`, avec
`s>0` rationnel, et

\[
V=\beta R^3=(sR)^3.
\]

On multiplie les masses par (V) et les amplitudes par (K/(sR)). Le profil remis à l'échelle vérifie exactement

\[
K_3(f)=K,
\qquad
\|f\|_2^2=K^2sR\,L_{m,N}
\leq3K^2\beta^{1/3}R.
\]

L'écart exact au majorant est

\[
K^2sR\,(3-L_{m,N}).
\]

La dépendance linéaire en (R) est celle de l'énergie locale sous l'échelle Navier–Stokes (u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t)).

## Test adverse : concentration absolue contre fraction capturée

Au niveau exact du raccord Type I, supposons uniquement

\[
K_3(f;B_R)\geq\gamma.
\]

Une fraction uniforme de la quasi-norme globale n'en découle pas. Prenons
deux ensembles disjoints, l'un dans le coeur et l'autre arbitrairement loin,
de volumes respectifs `gamma^3` et `T^3`, et un champ scalaire de module un
sur leur union. Les quasi-normes faible-`L3` du coeur et de la queue valent
exactement `gamma` et `T`, tandis que la quasi-norme globale vaut
`(gamma^3+T^3)^(1/3)`. Par conséquent

\[
\left(\frac{K_3(f;B_R)}{K_3(f)}\right)^3
=\frac{\gamma^3}{\gamma^3+T^3}\longrightarrow0.
\]

En revanche, l'hypothèse globale additionnelle

\[
K_3(f)\leq M
\]

implique immédiatement

\[
\frac{K_3(f;B_R)}{K_3(f)}\geq\frac{\gamma}{M}.
\]

Le test sépare donc deux énoncés : une concentration absolue à l'échelle (R),
et la capture d'une fraction uniforme. Le second exige une borne globale (M),
ou une hypothèse de queue équivalente. L'ajout de queue est un contre-modèle
exact de quasi-normes scalaires, pas la construction d'un champ
divergence-free ni d'une solution de Navier–Stokes.

Le script vérifie aussi la même algèbre pour le coefficient de Morrey
`R^-1||f||_2^2`, qui intervient entre faible-`L3` et l'hypothèse Type I de la
source. Aucun de ces deux ledgers ne prétend réaliser simultanément les
paquets par une solution Navier–Stokes.

## Reproduction

Commande :

~~~powershell
python -B experiments/navier-stokes/type-i-core-capture/type_i_capture_audit.py
~~~

Le programme n'emploie que la bibliothèque standard et `fractions.Fraction`. Il vérifie :

- la masse unité et toutes les fonctions de distribution aux seuils ;
- (K_3=1) exactement pour une grille de profils ;
- l'identité de (L_{m,N}) et l'erreur exacte ;
- la remise à l'échelle pour plusieurs (K,s,R) rationnels ;
- l'implication (gamma/M) sous borne globale ;
- l'effondrement de la fraction lorsque la queue croît sans borne.

## Limites et statut

- Objet certifié : inégalité scalaire de mesure finie et optimalité de sa constante.
- Type de preuve : dérivation analytique élémentaire plus audit arithmétique exact reproductible.
- Objet non certifié : existence d'un coeur, borne inférieure (gamma R), localisation de la pression, compacité forte, ou rigidité d'une solution ancienne.
- Transfert Clay : aucun transfert direct vers la régularité globale ; ce résultat contrôle seulement le coût L2 local d'une borne faible-L3.
- Statut du verrou : **RÉVISER**. Une future capture Type I doit apporter séparément une borne inférieure de concentration et une maîtrise uniforme de la queue ou de l'énergie totale à l'échelle (R).
