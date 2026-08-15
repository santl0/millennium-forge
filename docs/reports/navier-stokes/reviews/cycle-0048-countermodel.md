# Cycle 0048 — audit contradictoire du raccord faible-\(L^3\) / mild

Date d'exécution : 2026-08-15

## Verdict

L'estimation directe du terme de Duhamel issu d'un tenseur uniformément borné dans \(L^{3/2,\infty}(\mathbb R^3)\) fournit bien un gain temporel dans \(L^{p,\infty}\) pour tout \(3/2<p<3\). Sa constante intégrée diverge toutefois lorsque \(p\uparrow3\), et le calcul terme à terme au point critique \(p=3\) est logarithmique. Cette méthode directe ne démontre donc pas le raccord critique faible-\(L^3\) / mild.

Ce constat ne réfute pas un raccord obtenu par dualité de Lorentz et par une estimation intégrée de type Yamazaki. Cette dernière est un lemme endpoint distinct, à énoncer et sourcer séparément ; elle ne résulte pas de l'intégration de la norme d'opérateur ponctuelle en temps.

Enfin, une borne faible-\(L^3\) seule ne donne ni énergie finie ni décomposition automatique en un cœur d'énergie contrôlée et une queue petite dans la norme critique. Le champ solénoïdal explicite

\[
U(x)=\frac{(-x_2,x_1,0)}{|x|^2}
\]

fournit un test adverse exact : il appartient à \(L^{3,\infty}\), n'appartient pas à \(L^2(\mathbb R^3)\), et sa queue extérieure conserve toute sa taille faible-\(L^3\), quel que soit le rayon de coupure.

## 1. Estimation sous-critique exacte

Pour un tenseur \(S\) et le terme abstrait

\[
B[S](t)=\int_{t_0}^t e^{(t-s)\Delta}\,\mathbb P\nabla\!\cdot S(s)\,ds,
\]

l'estimation de gradient de la chaleur entre espaces de Lorentz a l'exposant d'échelle

\[
\left\|\nabla e^{\tau\Delta}f\right\|_{L^{p,\infty}}
\le C_p\tau^{-\alpha(p)}\|f\|_{L^{3/2,\infty}},
\qquad
\alpha(p)=\frac12+\frac32\left(\frac{2}{3}-\frac1p\right)
=\frac{3(p-1)}{2p}.
\]

Pour \(3/2<p<3\),

\[
\beta(p)=1-\alpha(p)=\frac{3-p}{2p}>0
\]

et, sous l'hypothèse \(\sup_s\|S(s)\|_{L^{3/2,\infty}}\le M\),

\[
\|B[S](t)\|_{L^{p,\infty}}
\le C_pM\,\frac{2p}{3-p}
(t-t_0)^{(3-p)/(2p)}.
\]

La puissance temporelle respecte exactement la loi d'échelle. La constante issue de cette intégration n'est pas uniforme près de l'endpoint : pour \(p_n=3-1/n\), elle vaut exactement \(6n-2\).

## 2. Obstruction logarithmique au point \(p=3\)

À \(p=3\), \(\alpha(3)=1\) et la majoration directe exige

\[
\int_0^T\frac{d\tau}{\tau}.
\]

Avec une coupure \(\varepsilon>0\), cette intégrale vaut \(\log(T/\varepsilon)\). De manière équivalente, chaque coquille dyadique

\[
[2^{-(k+1)},2^{-k}]
\]

contribue exactement \(\log 2\). Le résidu normalisé après \(N\) coquilles est donc \(N\), sans borne uniforme lorsque \(N\to\infty\).

Portée précise : ce calcul invalide uniquement une preuve endpoint obtenue en intégrant terme à terme cette norme d'opérateur positive. Il ne démontre ni que l'intégrale de Duhamel diverge pour un tenseur donné, ni qu'une compensation, une dualité ou une structure de Navier–Stokes ne puisse fermer l'estimation.

## 3. Endpoint dual de type Yamazaki : mécanisme séparé

Pour viser \(B[S](t)\in L^{3,\infty}\), on peut tester contre \(g\in L^{3/2,1}\) et écrire formellement, avec les adjoints appropriés,

\[
|\langle B[S](t),g\rangle|
\le \|S\|_{L_t^\infty L_x^{3/2,\infty}}
\int_0^{t-t_0}
\left\|\nabla e^{\tau\Delta}\mathbb Pg\right\|_{L^{3,1}},d\tau.
\]

La géométrie des exposants est critique :

\[
\frac{1}{3/2}-\frac13=\frac13,
\qquad
\frac12+\frac32\cdot\frac13=1.
\]

Une estimation intégrée distincte de la forme

\[
\int_0^\infty
\left\|\nabla e^{\tau\Delta}\mathbb Pg\right\|_{L^{3,1}},d\tau
\le C\|g\|_{L^{3/2,1}}
\tag{Y}
\]

permettrait alors de conclure par dualité de Lorentz. L'audit présent ne prouve pas (Y). Il vérifie seulement que son choix d'espaces et son homogénéité sont compatibles, et qu'il s'agit d'une affirmation logiquement différente de l'intégration ponctuelle divergente. Toute utilisation ultérieure de (Y) doit préciser le semigroupe, la projection de Leray, la classe de fonctions, la complétion des espaces de Lorentz et la source primaire qui garantit l'estimation.

## 4. Témoins critiques explicites

### 4.1 Témoin scalaire

Pour \(f(x)=|x|^{-1}\),

\[
|\{|f|>\lambda\}|=\frac{4\pi}{3}\lambda^{-3},
\qquad
K_3(f)^3:=\sup_{\lambda>0}\lambda^3|\{|f|>\lambda\}|
=\frac{4\pi}{3}.
\]

En revanche,

\[
\int_{B_R}|f|^2\,dx=4\pi R,
\]

si bien que \(f\notin L^2(\mathbb R^3)\). Ce témoin n'est pas solénoïdal ; il sert seulement à isoler le défaut énergétique de l'espace faible-\(L^3\).

### 4.2 Témoin solénoïdal

Le champ

\[
U(x)=\frac{e_3\times x}{|x|^2}
\]

est homogène de degré \(-1\), tangent aux sphères et divergence-free au sens des distributions. Son module est \(|U|=\sin\theta/r\). Sa fonction de distribution se calcule sans quadrature numérique :

\[
|\{|U|>\lambda\}|
=\frac{1}{3\lambda^3}\int_{S^2}\sin^3\theta\,d\omega
=\frac{\pi^2}{4\lambda^3},
\]

car \(\int_0^\pi\sin^4\theta\,d\theta=3\pi/8\). Par conséquent,

\[
K_3(U)^3=\frac{\pi^2}{4}.
\]

Son énergie tronquée est

\[
\int_{B_R}|U|^2\,dx
=R\int_{S^2}\sin^2\theta\,d\omega
=\frac{8\pi}{3}R.
\]

Ainsi \(U\notin L^2(\mathbb R^3)\). Ce champ n'est pas présenté comme une donnée régulière admissible du problème Clay ni comme une solution de Navier–Stokes ; c'est un contre-profil fonctionnel.

## 5. Échec d'un split énergétique naïf

La coupure radiale conserve la divergence, puisque \(U\cdot\nabla\chi(|x|)=0\). Pour les coupures caractéristiques, le cœur \(1_{|x|<R}U\) et la queue \(1_{|x|>R}U\) satisfont tous deux

\[
K_3^3=\frac{\pi^2}{4}.
\]

Le supremum du cœur est récupéré aux grands seuils ; celui de la queue l'est à la limite des petits seuils. En même temps, l'énergie du cœur vaut \((8\pi/3)R\). Faire croître \(R\) augmente donc linéairement le budget énergétique sans rendre petite la queue dans \(L^{3,\infty}\).

Résultat négatif falsifiable : aucune procédure de coupure spatiale radiale ne peut, sur la seule hypothèse d'une borne faible-\(L^3\), garantir simultanément un cœur \(L^2\) uniformément borné et une queue arbitrairement petite dans la quasi-norme critique.

## 6. Faible-étoile n'est pas trace forte

Deux familles critiques empêchent de remplacer silencieusement une convergence faible-étoile par une convergence forte :

- les translations \(V_n(x)=V(x-ne_1)\) conservent leurs normes \(L^{3,\infty}\) et \(L^2\), tout en convergeant faible-étoile vers zéro contre le prédual approprié pour un profil localisé ;
- les concentrations \(C_n(x)=nV(nx)\) conservent exactement leur quasi-norme faible-\(L^3\), tandis que \(\|C_n\|_2^2=n^{-1}\|V\|_2^2\).

Dans les deux cas, la taille critique ne tend pas vers zéro. Une limite faible-étoile ne fournit donc pas, à elle seule, une trace forte dans \(L^{3,\infty}\), ni une continuité mild dans cette quasi-norme. Tout raccord entre une solution faible bornée dans \(L_t^\infty L_x^{3,\infty}\) et une solution mild doit identifier explicitement la topologie de trace, la formulation intégrale, la classe de test et l'unicité utilisée.

## 7. Portée par rapport à Navier–Stokes et au problème Clay

Le certificat porte uniquement sur :

1. les exposants exacts de l'estimation de chaleur ;
2. le résidu logarithmique de l'intégration directe à l'endpoint ;
3. l'homogénéité du mécanisme dual conditionnel ;
4. les fonctions de distribution et énergies de contre-profils explicites ;
5. les défauts de compacité forte et de split énergétique.

Il ne construit aucune solution de Navier–Stokes, n'établit aucune régularité, n'établit aucun blow-up, ne contrôle pas la pression d'une solution et ne réalise aucun passage calcul-continuum. Il montre que le premier maillon d'un argument faible-\(L^3\) / mild doit être un véritable théorème endpoint, et non la limite formelle de l'estimation sous-critique.

## 8. Reproduction et résidu certifié

Commande :

```powershell
python -B experiments/navier-stokes/weak-l3-mildness/weak_l3_mildness_audit.py
```

Résultat attendu :

```text
weak_l3_mildness_audit: PASS
exact_assertions=144
endpoint_p3=termwise_integral_has_one_unit_per_log_shell
swirl=K3_cube=pi^2/4, L2_energy_B_R=(8*pi/3)*R
energy_split=outer_weak_L3_tail_does_not_become_small
```

Le script utilise uniquement la bibliothèque standard et `Fraction`. Les facteurs transcendants sont conservés symboliquement comme coefficients de \(\pi\) ou \(\pi^2\) ; aucune approximation flottante n'intervient. Empreinte SHA-256 du script validé :

```text
c5fcfef5a5cb3202cbc55bc7656c03651e281679badb4561ae34eabd7414a902
```

Résidu certifié : zéro pour les 144 identités et inégalités rationnelles testées ; croissance non bornée \(N\) pour le résidu endpoint normalisé sur \(N\) coquilles logarithmiques.

## Décision contradictoire

**RÉVISER.** Abandonner toute dérivation du raccord critique par intégration directe de la norme ponctuelle \(t^{-1}\). Conserver comme prochain test décisif l'audit d'un énoncé primaire précis de type (Y), puis vérifier séparément son application à la projection de Leray et au terme de Duhamel de la classe de solutions considérée.
