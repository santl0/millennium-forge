# Cycle 0040 — Coût critique d'un cutoff annulaire

Date : 2026-08-15
Statut : certificat exact de distributions finies ; aucun correcteur PDE construit
Expérience : experiments/navier-stokes/solenoidal-annular-cutoff/cutoff_cost_audit.py

## Verdict

Le coût élémentaire du col de cutoff est critique, mais **pas petit**.
Si \(U\) est supporté dans une couronne \(E_R\) de volume

\[
|E_R|\le CR^3
\tag{40.1}
\]

et si \(|\nabla\chi_R|\le C_\chi/R\), alors

\[
\boxed{
\|\,|\nabla\chi_R|\,|U|\,\|_{L^{3/2,\infty}}
\le C_\chi C^{1/3}\|U\|_{L^{3,\infty}(E_R)}.}
\tag{40.2}
\]

Le facteur \(R^{-1}\) est exactement compensé par
\(|E_R|^{1/3}\sim R\). Il n'existe aucun facteur \(o(1)\) lorsque
\(R\downarrow0\).

Une famille plateau sature (40.2). Sur la couronne cubique

\[
E_R=(-R,R)^3\setminus[-R/2,R/2]^3,\qquad |E_R|=7R^3,
\tag{40.3}
\]

prenons \(|U_R|=R^{-1}\). Alors

\[
\|U_R\|_{L^{3,\infty}}^3=7,
\qquad
\|R^{-1}U_R\|_{L^{3/2,\infty}}^3=49.
\tag{40.4}
\]

Le rapport des cubes vaut exactement \(7\), pour tout rayon dyadique testé
de \(2^{-40}\) à \(2^{80}\).

Ce ledger ne construit ni le champ correcteur de Bogovskii, ni une
projection de Leray, ni un résidu Navier–Stokes. Il certifie seulement le
coût de multiplication qui précède ces opérations.

## 1. Inégalité de distribution

Pour une fonction \(f\) supportée dans un ensemble \(E\) de mesure \(V\),
notons

\[
\mu_f(t)=|\{|f|>t\}|,
\qquad
K_3(f)=\sup_{t>0}t\mu_f(t)^{1/3}.
\tag{40.5}
\]

Comme \(\mu_f(t)\le V\),

\[
t\mu_f(t)^{2/3}
=\bigl[t\mu_f(t)^{1/3}\bigr]\mu_f(t)^{1/3}
\le K_3(f)V^{1/3}.
\tag{40.6}
\]

Il s'ensuit l'embedding fini-mesure exact

\[
\|f\|_{L^{3/2,\infty}(E)}
\le V^{1/3}\|f\|_{L^{3,\infty}(E)}.
\tag{40.7}
\]

Appliqué à \(f=U/R\),

\[
\|U/R\|_{L^{3/2,\infty}}^3
\le {|E|\over R^3}\|U\|_{L^{3,\infty}}^3.
\tag{40.8}
\]

Sous (40.1), le coefficient cubique est \(C\), indépendamment de \(R\).
Un facteur \(C_\chi\) devient \(C_\chi^3C\) après cubage.

Cette dérivation n'utilise ni Hölder fort, ni interpolation, ni
quasi-triangle. Elle se fait seuil par seuil sur la même distribution.

## 2. Fonctions de distribution du plateau

Sur (40.3), définissons

\[
|U_R|={1\over R}\mathbf1_{E_R},
\qquad
|G_R|={1\over R}|U_R|
={1\over R^2}\mathbf1_{E_R}.
\tag{40.9}
\]

Les distributions strictes complètes sont

\[
\mu_{U_R}(t)=
\begin{cases}
7R^3,&0<t<R^{-1},\\
0,&t\ge R^{-1},
\end{cases}
\tag{40.10}
\]

\[
\mu_{G_R}(s)=
\begin{cases}
7R^3,&0<s<R^{-2},\\
0,&s\ge R^{-2}.
\end{cases}
\tag{40.11}
\]

Les limites à gauche donnent

\[
\begin{aligned}
K_3(U_R)^3&=R^{-3}(7R^3)=7,\\
K_{3/2}(G_R)^3&=R^{-6}(7R^3)^2=49.
\end{aligned}
\tag{40.12}
\]

L'égalité

\[
K_{3/2}(G_R)^3
={|E_R|\over R^3}K_3(U_R)^3
\tag{40.13}
\]

montre l'optimalité de la constante pour les plateaux. Un lissage approche
cette égalité, mais le certificat n'en quantifie pas l'erreur.

## 3. Invariance d'échelle Clay

Sous

\[
U_\lambda(x)=\lambda U(\lambda x),
\qquad
G_\lambda(x)=\lambda^2G(\lambda x),
\tag{40.14}
\]

les amplitudes ont degrés \(1\) et \(2\), et le volume degré \(-3\).
Ainsi

\[
(\lambda A)^3(\lambda^{-3}V)=A^3V
\tag{40.15}
\]

pour faible-\(L^3\), et

\[
(\lambda^2B)^3(\lambda^{-3}V)^2=B^3V^2
\tag{40.16}
\]

pour faible-\(L^{3/2}\). Les deux côtés de (40.2) sont critiques.
Dans le plateau, \(\lambda=R^{-1}\) conserve exactement (40.12).

## 4. Profils étagés non constants

Le certificat construit aussi seize profils rationnels de longueurs
\(1,\ldots,16\), avec amplitudes signées et volumes totalisant
\(7R^3\). Pour chaque profil et chaque \(R=2^{-m}\), \(0\le m\le64\),
il calcule

\[
K_U^3=\max_j |a_j|^3
\sum_{i:\,|a_i|\ge|a_j|}v_i,
\tag{40.17}
\]

\[
K_{\rm col}^3
=\max_j {|a_j|^3\over R^3}
\left(\sum_{i:\,|a_i|\ge|a_j|}v_i\right)^2,
\tag{40.18}
\]

et vérifie exactement

\[
K_{\rm col}^3R^3
\le\left(\sum_iv_i\right)K_U^3
=7R^3K_U^3.
\tag{40.19}
\]

Les signes n'affectent pas ces distributions scalaires. Une cancellation
vectorielle particulière peut réduire le coût, mais aucune borne
universelle ne peut compter dessus ; le plateau colinéaire sature la
constante.

## 5. Ce que le certificat ne dit pas

### Multiplication par cutoff

Pour un champ divergence-free,

\[
\nabla\cdot(\chi_RU)=\nabla\chi_R\cdot U.
\tag{40.20}
\]

Le ledger borne la taille critique des termes contenant
\(\nabla\chi_R\,U\). Il ne résout pas (40.20).

Dans le cas pure-swirl spécial, si \(U\) est azimutal et \(\chi_R\)
axisymétrique, \(\nabla\chi_R\cdot U=0\). Cette simplification disparaît
pour une localisation multi-axe ou un champ général.

### Correcteur de Bogovskii

Un correcteur spatial chercherait \(v_R\) tel que

\[
\nabla\cdot v_R=-\nabla\chi_R\cdot U.
\tag{40.21}
\]

Passer de (40.2) à \(v_R\) exige séparément :

- la compatibilité de moyenne du membre droit ;
- un domaine de col uniforme après remise à l'échelle ;
- les constantes de l'opérateur de Bogovskii ;
- sa bornitude dans les espaces Lorentz pertinents ;
- le contrôle de \(\nabla v_R\), du curl et des traces ;
- l'interaction avec d'autres paquets chevauchants.

Aucune de ces propriétés n'est certifiée ici.

### Projection de Leray et PDE

La projection de Leray est non locale. Elle peut créer des queues hors de
la couronne et interagit avec la pression. Le certificat ne traite ni cette
projection, ni le terme non linéaire, ni la diffusion, ni un pas de temps,
ni une solution faible ou forte. Son résidu exact zéro est arithmétique,
pas un résidu d'équation.

## 6. Reproduction

Commande :

~~~text
python -B experiments/navier-stokes/solenoidal-annular-cutoff/cutoff_cost_audit.py
~~~

Sortie observée :

~~~text
exact checks = 9167
crown volume constant = 7
plateau Ku^3 = 7
plateau cutoff K_(3/2)^3 = 49
sharp cube ratio = 7
exact residual = 0
~~~

Le script utilise exclusivement la bibliothèque standard et
fractions.Fraction. Il n'emploie aucune graine et ne crée aucun fichier.

## 7. Passe contradictoire

1. **Gain fictif \(R\).** Garder le petit volume en oubliant
   \(R^{-1}\) produirait à tort un coût \(O(R)\). (40.8) conserve les deux.
2. **Mauvais embedding.** Sur mesure finie, le sens valide est
   \(L^{3,\infty}\to L^{3/2,\infty}\), avec facteur \(V^{1/3}\).
3. **Seuil du plateau.** La distribution stricte vaut zéro au seuil exact ;
   la quasi-norme emploie la limite à gauche.
4. **Constante cachée.** La couronne cubique donne exactement \(C=7\),
   suivi dans toutes les assertions.
5. **Échelle.** Les degrés d'amplitude \(1,2\) et de volume \(-3\) sont
   vérifiés séparément.
6. **Cancellation.** (40.2) est un majorant. Une configuration peut coûter
   moins, mais le plateau exclut toute petitesse uniforme.
7. **Confusion avec Bogovskii.** Une borne du défaut de divergence n'est
   pas une construction de correcteur.
8. **Continuum.** La couronne et le plateau atomiques sont un falsificateur
   de loi d'échelle, non une donnée lisse certifiée.

## 8. Décision scientifique

**ABANDONNER** toute localisation dont la fermeture repose sur l'idée que
le col devient gratuitement petit lorsque son rayon tend vers zéro.

**CONSERVER** (40.2) comme budget critique : le cutoff coûte
\(O(K_U)\), avec constante déterminée par la géométrie remise à l'échelle.

La prochaine étape doit estimer le correcteur solénoïdal lui-même sur une
couronne uniforme, puis suivre sa projection, son curl et les annulations
entre paquets. Aucun gain ne peut provenir du seul volume \(R^3\).
