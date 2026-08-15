# Cycle 0046 — persistance temporelle d'une capture faible-\(L^3\)

Date d'audit : 2026-08-15.

## Verdict

Non : sur un cylindre fini, une suite ne peut pas converger fortement vers zéro dans \(L^3\) espace–temps tout en conservant une capture faible-\(L^3\) de taille fixe sur un intervalle temporel de longueur uniforme.

Plus précisément, avec

\[
K_3(f(t);B_1)
:=\sup_{\lambda>0}
\lambda\,
|\{x\in B_1:|f(t,x)|>\lambda\}|^{1/3},
\]

si

\[
K_3(f_j(t);B_1)\geq\gamma_j
\]

pour presque tout \(t\) dans un ensemble mesurable \(E_j\), alors

\[
\boxed{
\|f_j\|_{L^3(E_j\times B_1)}^3
\geq |E_j|\gamma_j^3.}
\]

La constante est exactement un et elle est optimale. Par conséquent,

\[
f_j\to0\quad\text{fortement dans }L^3(I\times B_1)
\]

impose

\[
|E_j|\gamma_j^3\longrightarrow0.
\]

Pour \(\gamma_j\geq\gamma>0\), la mesure des temps capturés doit tendre vers zéro. Ni un centre mobile, ni une échelle spatiale mobile, ni l'emploi de la quasi-norme faible ne permettent de contourner cette obstruction.

Ce résultat est purement fonctionnel. Il ne construit pas de solution de Navier–Stokes et ne prouve pas que les hypothèses de capture et de compacité forte sont simultanément héritées par une suite issue d'un blow-up.

## Preuve ponctuelle en temps

Pour tout \(\lambda>0\), sur l'ensemble

\[
A_\lambda(t)=\{x\in B_1:|f(t,x)|>\lambda\},
\]

on a

\[
\int_{B_1}|f(t,x)|^3\,dx
\geq
\int_{A_\lambda(t)}|f(t,x)|^3\,dx
\geq
\lambda^3|A_\lambda(t)|.
\]

Prendre le supremum en \(\lambda\) donne

\[
\boxed{
K_3(f(t);B_1)^3
\leq
\int_{B_1}|f(t,x)|^3\,dx.}
\]

Cette formule ne requiert ni régularité, ni divergence nulle, ni équation PDE. Elle vaut pour toute fonction mesurable scalaire ou vectorielle.

En intégrant sur \(E_j\),

\[
\int_{E_j}\int_{B_1}|f_j|^3\,dx\,dt
\geq
\int_{E_j}K_3(f_j(t);B_1)^3\,dt
\geq
|E_j|\gamma_j^3.
\]

En particulier, si \(J_j\subset I\) est un intervalle avec

\[
|J_j|\geq\delta>0,
\qquad
K_3(f_j(t);B_1)\geq\gamma>0
\quad\text{pour p.p. }t\in J_j,
\]

alors

\[
\|f_j\|_{L^3(I\times B_1)}^3
\geq\delta\gamma^3>0.
\]

La convergence forte vers zéro est impossible, même si les intervalles \(J_j\) se déplacent dans le temps.

## Forme quantitative en mesure

Pour un seuil fixe \(\gamma>0\), posons

\[
E_j(\gamma)
=\{t\in I:K_3(f_j(t);B_1)\geq\gamma\}.
\]

La même preuve donne

\[
\boxed{
|E_j(\gamma)|
\leq
\frac{\|f_j\|_{L^3(I\times B_1)}^3}{\gamma^3}.}
\]

Ainsi la convergence forte \(L^3\) écrase quantitativement la mesure des temps de capture. Elle n'interdit cependant pas une capture sur un ensemble de mesure nulle, notamment à un temps terminal isolé.

## Optimalité de la constante

Soit \(E\subset B_1\) de mesure \(s^3\), avec \(s>0\), et posons

\[
g(x)=\frac{\gamma}{s}\,\mathbf1_E(x)e,
\]

où \(e\) est un vecteur unitaire fixe. Alors

\[
\|g\|_{L^3(B_1)}^3
=\frac{\gamma^3}{s^3}|E|
=\gamma^3.
\]

Pour \(0<\lambda<\gamma/s\),

\[
\lambda^3|\{|g|>\lambda\}|
=\lambda^3s^3.
\]

En faisant tendre \(\lambda\) vers \(\gamma/s\) par valeurs inférieures,

\[
K_3(g;B_1)^3=\gamma^3.
\]

La convention stricte \(>\lambda\) à l'atome terminal ne change pas le supremum. On a donc égalité dans l'inégalité ponctuelle. Aucun coefficient supérieur à un ne peut être gagné.

Le profil étagé est mesurable mais discontinu. Des profils lisses peuvent l'approcher, avec une erreur arbitrairement petite ; le certificat exact porte sur le profil mesurable.

## Frontière 1 : capture à un seul temps

Fixons un temps \(t_0\) et

\[
b_{\delta}(t)
=\max\left\{1-\frac{|t-t_0|}{\delta},0\right\}.
\]

Avec le profil spatial optimal \(g\), posons

\[
f_\delta(t,x)=b_\delta(t)g(x).
\]

Au sommet,

\[
K_3(f_\delta(t_0);B_1)=\gamma.
\]

Mais

\[
\int b_\delta(t)^3\,dt
=2\delta\int_0^1(1-s)^3\,ds
=\frac{\delta}{2}.
\]

Par conséquent,

\[
\boxed{
\|f_\delta\|_{L^3_{t,x}}^3
=\frac{\delta\gamma^3}{2}
\longrightarrow0.}
\]

Une capture à un temps isolé est invisible à la norme espace–temps. Même avec une dépendance temporelle continue, elle ne fournit aucune persistance uniforme.

Pour un seuil relatif \(0<\theta<1\),

\[
\{t:K_3(f_\delta(t);B_1)\geq\theta\gamma\}
\]

a une longueur \(2\delta(1-\theta)\), qui tend également vers zéro.

## Frontière 2 : intervalle capturé qui se contracte

Prenons un intervalle \(J_j\) de longueur \(\delta_j\) et

\[
f_j(t,x)=\mathbf1_{J_j}(t)g_j(x),
\qquad
K_3(g_j;B_1)=\gamma_j,
\qquad
\|g_j\|_3^3=\gamma_j^3.
\]

Alors l'égalité est exacte :

\[
\boxed{
\|f_j\|_{L^3_{t,x}}^3
=\delta_j\gamma_j^3.}
\]

Le seuil \(\delta_j\gamma_j^3\to0\) est donc à la fois nécessaire et suffisant dans la classe fonctionnelle mesurable.

Exemples exacts :

- \(\delta_j=j^{-1}\), \(\gamma_j=3/2\) : coût \(27/(8j)\to0\) ;
- \(\delta_j=j^{-3}\), \(\gamma_j=j\) : coût critique égal à \(1\) ;
- \(\delta_j=j^{-4}\), \(\gamma_j=j\) : coût \(j^{-1}\to0\) ;
- \(\delta_j=j^{-2}\), \(\gamma_j=j\) : coût \(j\to\infty\).

Une grande amplitude peut donc être compatible avec la convergence forte uniquement si la fenêtre se contracte plus vite que son cube inverse.

## Frontière 3 : centre et échelle spatiale mobiles

Soit \(B(c_j(t),\rho_j(t))\subset B_1\), et choisissons sa mesure sous la forme \(s_j(t)^3\). Le profil

\[
g_j(t,x)
=\frac{\gamma_j}{s_j(t)}
\mathbf1_{B(c_j(t),\rho_j(t))}(x)e
\]

vérifie pour chaque temps capturé

\[
K_3(g_j(t);B_1)=\gamma_j,
\qquad
\|g_j(t)\|_{L^3(B_1)}^3=\gamma_j^3.
\]

Lorsque \(\rho_j(t)\to0\), l'amplitude croît avec la puissance critique inverse ; le coût \(L^3\) par tranche ne change pas. Le mouvement de \(c_j(t)\) ne change pas non plus la mesure ni l'intégrale.

Si le coeur sort partiellement de \(B_1\), deux possibilités seulement subsistent :

1. la capture locale \(K_3(\,\cdot\,;B_1)\) diminue ;
2. l'amplitude est augmentée pour conserver \(K_3\geq\gamma_j\), et la minoration \(\gamma_j^3\) reste applicable dans \(B_1\).

La mobilité ne répare donc pas l'implication sur un ensemble temporel uniforme.

## Quasi-norme faible et norme forte

Le résultat utilise uniquement

\[
K_3(f;B_1)\leq\|f\|_{L^3(B_1)}.
\]

Il ne suppose pas une inclusion inverse. Une borne supérieure faible-\(L^3\) ne contrôle pas la norme forte \(L^3\) : des empilements multi-échelles peuvent avoir une norme forte arbitrairement grande. Ici seule une **minoration** de la quasi-norme faible est utilisée, ce qui force la même minoration de la norme forte.

Ainsi :

- \(K_3\geq\gamma\) est suffisant pour payer au moins \(\gamma^3\) par tranche ;
- \(K_3\leq M\) ne fournit aucune majoration forte-\(L^3\) générale ;
- le fait que \(B_1\) ait une mesure finie ne renverse pas cette dernière implication à l'endpoint égal.

## Portée pour Navier–Stokes et le problème Clay

Considérons une suite de vitesses localisées \(Z_j\) issue d'une construction Type I. Si deux propriétés étaient démontrées sur le même cylindre :

\[
Z_j\to0
\quad\text{fortement dans }L^3(J\times B_1),
\]

et

\[
K_3(Z_j(t);B_1)\geq\gamma
\quad\text{pour p.p. }t\in J,
\qquad |J|\geq\delta>0,
\]

elles seraient contradictoires par l'inégalité précédente.

Mais le certificat ne démontre aucune des deux propriétés pour une solution de Navier–Stokes :

- la capture Barker–Prange auditée précédemment est attachée à des temps et rayons précis ; le présent certificat ne les synchronise pas. Le rapport principal du cycle ferme séparément ce raccord par l'horloge mobile exacte et le quantificateur « tout temps » ;
- une compacité forte locale espace–temps ne fournit pas automatiquement une trace au temps terminal ;
- des intervalles \(J_j\) peuvent se contracter ou se déplacer ;
- un centre et une échelle doivent être synchronisés avec le même cylindre limite ;
- le passage du produit et de la pression reste une étape PDE distincte.

Les profils frontières de ce rapport sont des fonctions mesurables arbitraires, pas des solutions faibles, fortes, mild ou adaptées. Ils ne satisfont ni l'équation, ni une inégalité d'énergie, ni une condition de pression.

## Reproduction

~~~powershell
python -B experiments/navier-stokes/trace-persistence/trace_persistence_audit.py
~~~

Le script utilise uniquement la bibliothèque standard et fractions.Fraction. Il vérifie l'inégalité sur des profils atomiques multi-niveaux, l'optimalité des profils à un niveau, les coûts temporels exacts, les seuils \(\delta_j\gamma_j^3\), l'invariance sous les échelles mobiles rationnelles, ainsi que l'horloge Type I et le scaling critique ajoutés lors de la synthèse. Il comporte 417 assertions exactes.

Statut : **CONTINUER**. Le rapport principal établit la persistance dynamique Type I au centre fixe sur chaque fenêtre renormalisée bornée. Le prochain verrou est la dérenormalisation exacte de la limite non triviale; la trace correspondant à l'ancien endpoint et la persistance d'une singularité restent des conclusions plus fortes non obtenues.
