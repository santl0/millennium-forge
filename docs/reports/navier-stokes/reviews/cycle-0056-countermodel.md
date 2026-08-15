# Cycle 0056 — modulation bornée, convergence forte et produit limite

Date d'exécution : 2026-08-15

## Verdict

Le passage de produit suivant est valide et quantitativement stable :

\[
\beta_n\overset{*}{\rightharpoonup}\beta
\quad\text{dans }L^\infty,
\qquad
\sup_n\|\beta_n\|_\infty\le M,
\qquad
h_n\to h\quad\text{dans }L^1,
\]

impliquent

\[
\int\beta_nh_n\to\int\beta h.
\]

La preuve sépare exactement

\[
\int\beta_nh_n-\int\beta h
=\int\beta_n(h_n-h)
+\int(\beta_n-\beta)h.
\tag{1}
\]

Le premier terme est borné par \(M\|h_n-h\|_1\) ; le second tend vers zéro parce que \(h\) est un test **fixé**.

Les contre-modèles dyadiques exacts montrent que chaque mot compte. Le passage échoue si \(h_n\) n'est que faible, si \(\beta_n\) n'est pas uniformément bornée, si un générateur dégénère tandis que la modulation diverge, si les sous-suites ne sont pas communes, ou si la convergence faible-étoile est testée contre une fonction dépendant de \(n\).

## 1. Grilles dyadiques rationnelles

Sur \([0,1)\), considérons les fonctions de Rademacher

\[
r_n(x)=(-1)^{\lfloor2^nx\rfloor}.
\]

Elles sont constantes sur les \(2^n\) cellules dyadiques de niveau \(n\), prennent les valeurs \(\pm1\) et satisfont

\[
\|r_n\|_\infty=1.
\]

Si \(\varphi\) est constante sur les cellules d'un niveau fixé \(m<n\), alors chaque cellule de \(\varphi\) contient un nombre pair de sous-cellules de signes opposés. Par conséquent,

\[
\int_0^1r_n\varphi\,dx=0
\qquad(n>m).
\tag{2}
\]

Le script représente toutes ces fonctions par des tuples de `Fraction` et calcule les intégrales comme moyennes rationnelles exactes. L'identité (2), jointe à \(\|r_n\|_\infty=1\) et à la densité des fonctions dyadiques en \(L^1\), est le modèle standard de

\[
r_n\overset{*}{\rightharpoonup}0
\quad\text{dans }L^\infty(0,1).
\]

## 2. Cas positif certifié

Fixons une fonction dyadique rationnelle \(h\), constante sur quatre cellules, et posons

\[
\beta_n=r_n,
\qquad
h_n=h+\frac1n r_n.
\]

Pour \(n>2\),

\[
\int\beta_nh=0,
\]

et

\[
\|h_n-h\|_1=\frac1n.
\]

Comme \(r_n^2=1\),

\[
\int\beta_n(h_n-h)=\frac1n,
\]

d'où

\[
\boxed{
\int\beta_nh_n=\frac1n\to0
=\int0\cdot h.}
\]

L'exemple sature exactement le majorant du premier terme de (1) :

\[
\left|\int\beta_n(h_n-h)\right|
=\|\beta_n\|_\infty\|h_n-h\|_1.
\]

Le certificat vérifie également l'inégalité discrète

\[
\left|\int fg\right|
\le\|f\|_\infty\|g\|_1
\]

sur plusieurs familles rationnelles indépendantes.

## 3. Échec faible–faible par oscillations corrélées

Prenons

\[
\beta_n=r_n,
\qquad
h_n=r_n.
\]

Les deux suites tendent faiblement-étoile vers zéro dans \(L^\infty\), donc également faiblement dans tout cadre réflexif compatible sur cet intervalle fini. Pourtant,

\[
\beta_nh_n=r_n^2=1
\]

et

\[
\boxed{\int_0^1\beta_nh_n\,dx=1.}
\]

La corrélation des oscillations survit intégralement. Il n'existe pas de règle générale « faible fois faible donne le produit des limites ». Une compensation PDE éventuelle doit être formulée et démontrée séparément — par exemple via structure div–curl, fréquences séparées ou compacité forte.

## 4. Modulation non bornée

Sur une grille quelconque, posons

\[
\beta_n=n,
\qquad
h_n=\frac1n.
\]

Alors

\[
\|h_n\|_1=\frac1n\to0,
\]

mais

\[
\beta_nh_n=1.
\]

La convergence forte du second facteur ne suffit donc plus lorsque

\[
\|\beta_n\|_\infty=n\to\infty.
\]

Dans (1), le majorant réel est \(\|\beta_n\|_\infty\|h_n-h\|_1\), ici exactement égal à un.

## 5. Générateur dégénéré et vitesse modulée

Dans le plan, soit

\[
R=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
U_n=\frac1n e_1,
\qquad
\beta_n=n.
\]

Alors

\[
RU_n=\frac1n e_2\to0
\]

fortement, tandis que

\[
\boxed{\beta_nRU_n=e_2.}
\]

Ainsi, connaître séparément \(RU_n\to0\) et l'existence de chaque \(\beta_n\) ne contrôle pas la vitesse de modulation. Il faut soit une borne uniforme de \(\beta_n\), soit un taux quantitatif garantissant

\[
\|\beta_nRU_n\|\to0.
\]

Ce modèle est celui du cycle 0055 placé exactement dans le cadre produit du présent test.

## 6. Absence de sous-suite commune

Considérons dans \(\mathbb R^2\)

\[
x_n=
\begin{cases}
e_1,&n\text{ pair},\\
e_2,&n\text{ impair}.
\end{cases}
\]

Le test \(e_1\) s'annule sur la sous-suite impaire, et le test \(e_2\) sur la sous-suite paire. Mais

\[
\langle x_n,e_1\rangle+
\langle x_n,e_2\rangle=1
\]

pour tout \(n\). Aucun indice, et donc aucune sous-suite, n'annule simultanément les deux défauts.

La famille bornée possède évidemment des sous-suites convergeant vers \(e_1\) ou \(e_2\). Ce que le contre-modèle réfute est l'inversion

\[
\forall\varphi\ \exists\text{ une sous-suite adaptée à }\varphi
\quad\Longrightarrow\quad
\exists\text{ une sous-suite commune pour tous les }\varphi.
\]

Une preuve de produit doit être menée après fixation d'une extraction commune à la convergence faible-étoile, à la convergence forte et aux autres défauts PDE.

## 7. Test fixé contre test mobile

Pour chaque fonction dyadique fixée \(\varphi_m\), (2) donne

\[
\int r_n\varphi_m=0
\qquad\text{dès que }n>m.
\]

Mais si le test dépend de la suite,

\[
\varphi_n=r_n,
\]

alors

\[
\int r_n\varphi_n=1.
\]

Il n'y a aucune contradiction : la convergence faible-étoile est définie contre chaque test fixé, pas uniformément sur la boule unité de \(L^1\). Dans la preuve positive, la convergence forte de \(h_n\) sert précisément à remplacer le test mobile par le test fixé \(h\), avec une erreur dominée.

## 8. Dictionnaire pour une modulation PDE

Dans une application abstraite à une orbite modulée, le terme à passer à la limite peut avoir la forme

\[
\beta_n(s)\,RU_n(s,x).
\]

Pour le tester contre une fonction PDE fixe \(\Phi\), on obtient un facteur

\[
h_n(s)=\langle RU_n(s,\cdot),\Phi(s,\cdot)\rangle_x.
\]

Le lemme positif s'applique si l'on démontre réellement :

1. \(\beta_n\) bornée uniformément dans \(L^\infty_s\) et convergente faible-étoile sur une sous-suite commune ;
2. \(h_n\to h\) fortement dans \(L^1_s\) pour chaque \(\Phi\) fixé ;
3. une domination permettant d'étendre d'une famille dénombrable de tests à la classe entière ;
4. la stabilité du domaine du générateur \(R\) sous la convergence disponible.

Une convergence seulement faible de \(RU_n\), une modulation non bornée ou un test dépendant implicitement de \(n\) ne suffit pas.

## 9. Séparation stricte avec Navier–Stokes

Les grilles du certificat ne portent aucune vitesse tridimensionnelle, aucune divergence, aucune pression et aucune équation différentielle. Les fonctions de Rademacher sont des oscillations scalaires de test, pas des solutions de Navier–Stokes.

Pour une vraie suite NS, il faudrait en outre vérifier :

- l'action exacte du générateur spatial ou renormalisé \(R\) ;
- la compatibilité avec la projection de Leray et la pression ;
- la convergence du terme quadratique dans la même sous-suite ;
- les bornes de temps et d'espace nécessaires à la convergence forte de \(h_n\) ;
- la suitability ou l'inégalité d'énergie requise ;
- l'absence de concentration et de fuite spatiale.

Le certificat établit un lemme de produit élémentaire et ses frontières. Il ne construit aucune solution ancienne sur \(\mathbb R^3\), aucune relative equilibrium Navier–Stokes et aucun scénario de singularité Clay.

## 10. Reproduction et certificat

Commande :

```powershell
python -B experiments/navier-stokes/bounded-modulation-compactness/bounded_modulation_audit.py
```

Sortie validée :

```text
bounded_modulation_audit: PASS
exact_assertions=1288
positive=beta_n_weak-star_bounded_times_h_n_strong_L1_converges
sharp_example=product_error=||h_n-h||_L1=1/n
weak_weak=rademacher_correlation_has_product_integral_one
unbounded=beta_n=n_and_h_n=1/n_have_product_one
degenerate=beta_n*R*U_n_stays_unit_while_R*U_n_to_zero
subsequence=individual_test_subsequences_need_not_be_common
tests=weak-star_is_fixed-test_not_sequence-dependent-test
scope=exact_dyadic_algebra; no Navier-Stokes PDE claim
```

Le script utilise seulement la bibliothèque standard et `Fraction`. Les 1288 assertions vérifient exactement les annulations dyadiques, les normes, la décomposition (1), les produits corrélés et les défauts de quantificateurs. Résidu rationnel : zéro ; aucune approximation flottante.

Empreinte SHA-256 du script validé :

```text
6ab32500ee3d2ab7d153e67b344b70197705407da4c3a5245c879daa896df06c
```

## Décision contradictoire

**CONSERVER** le passage faible-étoile borné \(\times\) fort \(L^1\). **ABANDONNER** tout passage faible \(\times\) faible ou toute suppression de la borne uniforme. **RÉVISER** l'application Navier–Stokes pour identifier une sous-suite commune et démontrer la convergence forte exacte du facteur contenant le générateur avant toute conclusion sur la modulation limite.
