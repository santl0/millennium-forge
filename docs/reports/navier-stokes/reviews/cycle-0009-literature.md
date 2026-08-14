# Revue bibliographique du cycle 0009 — trace terminale et zoom KNSS

Date de veille : **2026-08-14**. Périmètre : Navier–Stokes incompressible, non forcé, viscosité \(1\), principalement sur \(\mathbb R^3\). Cette note sépare les théorèmes publiés des dérivations du laboratoire.

## Verdict

Le raccord recherché n'est pas présent dans les sources primaires examinées. Le zoom au maximum de Koch–Nadirashvili–Seregin–Šverák (KNSS) donne une solution ancienne mild, bornée et non nulle, mais son temps rescalé \(s=0\) correspond au temps physique \(t_k<T\), pas au temps singulier \(T\). Les preuves endpoint de type Escauriaza–Seregin–Šverák/Seregin centrent au contraire le zoom sur \(T\), obtiennent une trace terminale nulle grâce à une borne critique \(L^3\) ou \(L^{3,q}\), \(q<\infty\), puis utilisent la backward uniqueness. Elles ne produisent pas simultanément la borne globale \(L^\infty\) du profil KNSS.

Ce n'est donc pas une simple commutation \(k\to\infty\), puis \(s\uparrow0\), sur l'horloge KNSS : cette opération conserve \(|v(0,0)|=1\). Le défaut est l'extrémité mobile \(s=B_k=M_k^2(T-t_k)>0\). Une équi-intégrabilité critique uniforme des tranches physiques \(|u(t_k)|^3\) ne répare pas ce défaut : la normalisation au maximum force précisément sa violation.

## Sources primaires, versions et statut

| Source | Version et statut vérifiés | Résultat utilisé |
|---|---|---|
| G. Koch, N. Nadirashvili, G. Seregin, V. Šverák, *Liouville theorems for the Navier–Stokes equations and applications* | [arXiv:0709.3599v1](https://arxiv.org/abs/0709.3599), 22 septembre 2007 ; publié dans *Acta Math.* 203 (2009), 83–105, [DOI 10.1007/s11511-009-0039-6](https://doi.org/10.1007/s11511-009-0039-6) | Solutions anciennes mild, compacité bornée (lemme 6.1), extraction maximum-normalisée (proposition 6.1). |
| G. Seregin, *A certain necessary condition of potential blow up for Navier–Stokes equations* | [arXiv:1104.3615v1](https://arxiv.org/abs/1104.3615), 19 avril 2011 ; publié dans *Commun. Math. Phys.* 312 (2012), 833–845, [DOI 10.1007/s00220-011-1391-x](https://doi.org/10.1007/s00220-011-1391-x) | Si \(T\) est singulier, alors \(\|u(t)\|_3\to\infty\). Zoom centré en \(T\), trace nulle et non-trivialité. |
| L. Escauriaza, G. Seregin, V. Šverák, *\(L_{3,\infty}\)-solutions of Navier–Stokes equations and backward uniqueness* | Publié dans *Russian Math. Surveys* 58:2 (2003), 211–250, [DOI 10.1070/RM2003v058n02ABEH000609](https://doi.org/10.1070/RM2003v058n02ABEH000609) | Critère \(L^\infty_tL^3_x\), limite convenable à trace terminale nulle, rigidité par backward uniqueness. Le titre emploie \(L_{3,\infty}\) pour la norme mixte, non le Lorentz spatial \(L^{3,\infty}\). |
| L. Escauriaza, G. Seregin, V. Šverák, *Backward Uniqueness for Parabolic Equations* | Publié dans *Arch. Rational Mech. Anal.* 169 (2003), 147–157, [DOI 10.1007/s00205-003-0263-8](https://doi.org/10.1007/s00205-003-0263-8) | Backward uniqueness dans un domaine extérieur pour une inégalité parabolique, avec contrôle des coefficients et de la croissance. |
| I. Gallagher, G. Koch, F. Planchon, *A profile decomposition approach to the \(L^\infty_t(L^3_x)\) Navier–Stokes regularity criterion* | [arXiv:1012.0145v3](https://arxiv.org/abs/1012.0145), 16 juillet 2012 ; publié dans *Math. Ann.* 355 (2013), 1527–1559, [DOI 10.1007/s00208-012-0830-0](https://doi.org/10.1007/s00208-012-0830-0) | Élément critique \(L^3\), trace nulle dans \(\mathcal S'\) au temps maximal, puis rigidité. |
| P. Constantin, *Pressure, Intermittency, Singularity* | [arXiv:2301.04489v1](https://arxiv.org/abs/2301.04489), 11 janvier 2023 ; publié dans *J. Math. Fluid Mech.* 25 (2023), article 36, [DOI 10.1007/s00021-023-00779-7](https://doi.org/10.1007/s00021-023-00779-7) | Une intégrabilité uniforme finie de \(|u|^3\) donne une borne \(\dot H^1\) et le prolongement fort. |
| T. Barker, G. Seregin, *A necessary condition of potential blowup for the Navier–Stokes system in half-space* | Publié dans *Math. Ann.* 369 (2017), 1327–1352, [DOI 10.1007/s00208-016-1488-9](https://doi.org/10.1007/s00208-016-1488-9) ; prépublication [arXiv:1508.05313v1](https://arxiv.org/abs/1508.05313), 21 août 2015 | Dans \(\mathbb R^3_+\), une singularité force \(\|u(t)\|_{L^{3,q}}\to\infty\) pour \(3\le q<\infty\). |
| A. Cheskidov, M. Dai, S. Palasek, *Instantaneous Type I blow-up and non-uniqueness of smooth solutions of the Navier–Stokes equations* | [arXiv:2511.09556v2](https://arxiv.org/abs/2511.09556), 12 janvier 2026 ; **prépublication**, aucune publication arbitrée vérifiée au 2026-08-14 | Blow-up périodique instantané depuis la droite, faible-* continu dans \(BMO^{-1}\), hors de \(L^\infty_tL^2_x\) et \(L^2_tH^1_x\) près du temps concerné. |

La veille différentielle 2025–2026 sur les solutions anciennes, les traces terminales, la backward uniqueness et les zooms de singularité n'a localisé aucune source primaire fermant le raccord « ancienne mild globalement bornée, non nulle et de trace terminale nulle » à partir d'un blow-up Clay. C'est un résultat de veille daté, non une affirmation d'exhaustivité absolue.

## Équation et échelle

Les deux constructions principales traitent

\[
\partial_tu-\Delta u+(u\cdot\nabla)u+\nabla p=0,
\qquad \nabla\cdot u=0
\quad\text{sur }\mathbb R^3.
\]

Sous

\[
u^{(\lambda)}(y,s)=\lambda u(x_0+\lambda y,t_0+\lambda^2s),
\qquad
p^{(\lambda)}(y,s)=\lambda^2p(x_0+\lambda y,t_0+\lambda^2s),
\]

\(L^3_x\) est invariant, tandis que la norme \(L^2_x\) acquiert le facteur \(\lambda^{-1/2}\). Une convergence d'énergie pure ne transmet donc pas automatiquement une trace rescalée nulle.

## 1. Zoom au maximum KNSS : théorème exact et horloges

Pour une solution mild sur \(\mathbb R^3\times[0,T)\), KNSS posent

\[
h(t)=\sup_x|u(x,t)|,\qquad H(t)=\sup_{0\le r\le t}h(r),
\]

choisissent \(t_k\uparrow T\), \(\gamma_k\downarrow1\), \(N_k=H(t_k)\), et \(x_k\) tels que

\[
M_k:=|u(x_k,t_k)|>N_k/\gamma_k.
\]

Le zoom

\[
v_k(y,s)=M_k^{-1}u\left(x_k+\frac y{M_k},t_k+\frac s{M_k^2}\right)
\]

est défini sur \((A_k,B_k)\), où

\[
A_k=-M_k^2t_k\to-\infty,
\qquad B_k=M_k^2(T-t_k)\ge c>0.
\]

Il vérifie

\[
|v_k(y,s)|\le\gamma_k\quad(s\le0),
\qquad |v_k(0,0)|=1.
\]

Le lemme 6.1 extrait une sous-suite localement uniforme sur les compacts de \(\mathbb R^3\times(-\infty,0)\). Les estimations mild sur une bande passée fixe transmettent la valeur au bord, et KNSS concluent explicitement que la limite ancienne mild satisfait

\[
|v|\le1,\qquad |v(0,0)|=1.
\]

Le temps physique singulier \(T\) correspond cependant à \(s=B_k\). En recentrant le temps en \(T\),

\[
w_k(y,\tau)
=M_k^{-1}u\left(x_k+\frac y{M_k},T+\frac{\tau}{M_k^2}\right)
=v_k(y,\tau+B_k),
\]

on obtient

\[
|w_k(0,-B_k)|=1,
\qquad |w_k(y,\tau)|\le\gamma_k
\quad\text{seulement si }\tau\le-B_k.
\]

Deux branches épuisent les sous-suites :

1. Si \(B_k\to\infty\), le témoin non nul \((0,-B_k)\) s'échappe vers le passé ; une limite sur les cylindres terminaux compacts peut être triviale.
2. Si \(B_k\to\beta<\infty\), le témoin reste à \(\tau=-\beta\), mais la borne maximum-normalisée ne contrôle que \(\tau\le-\beta\), pas la bande \((-\beta,0)\).

Ainsi, \(k\to\infty\) à \(s<0\), puis \(s\uparrow0\), mène bien à \(v(0,0)=1\). L'opération injustifiée serait d'identifier l'extrémité mobile \(s=B_k\) à \(s=0\), ou de permuter la limite avec une évaluation à \(s=B_k\).

## 2. Zoom terminal \(L^3\) : topologies et trace

Seregin suppose par contradiction qu'il existe \(t_k\uparrow T\) avec

\[
\sup_k\|u(t_k)\|_{L^3}\le M
\]

pour une solution d'énergie issue de \(a\in C^\infty_{0,\sigma}(\mathbb R^3)\). Avec \(S>0\) fixé, il choisit

\[
\lambda_k=\sqrt{\frac{T-t_k}{S}},
\qquad
u_k(y,s)=\lambda_k u(\lambda_k y,T+\lambda_k^2s).
\]

Ici \(t_k\) est toujours \(s=-S\), et \(T\) est toujours \(s=0\). Après extraction et soustraction de constantes spatiales dépendant du temps dans la pression, sur toute boule \(B(a)\) :

- \(u_k\rightharpoonup^\ast u\) dans \(L^\infty(-S,0;L^2(B(a)))\) ;
- \(u_k\to u\) fortement dans \(L^3(B(a)\times(-S,0))\) ;
- \(u_k\to u\) fortement dans \(C([\tau,0];L^{9/8}(B(a)))\) pour tout \(-S<\tau<0\) ;
- la pression normalisée converge faiblement dans \(L^{3/2}(-S,0;L^{3/2}(B(a)))\).

La tranche fixe \(U=u(T)\) appartient à \(L^3\) sous l'hypothèse de contradiction. Pour \(p<3\), toute boule fixe \(B_R\), et même des centres mobiles \(x_k\), l'absolue continuité donne

\[
\|\lambda_kU(x_k+\lambda_k\,\cdot)\|_{L^p(B_R)}
\le C_R\|U\|_{L^3(B_{\lambda_kR}(x_k))}
\longrightarrow0.
\]

La convergence \(C_tL^{9/8}_{\mathrm{loc}}\) transmet donc \(u(\cdot,0)=0\). La non-trivialité vient séparément d'un seuil d'epsilon-régularité, de la convergence forte espace-temps et du contrôle de pression. La backward uniqueness est appliquée seulement après ces étapes.

Une trace uniquement énergétique \(U\in L^2\) ne suffit pas. Pour \(\varphi\in C_c^\infty(B_R)\),

\[
|\langle\lambda U(x_k+\lambda\cdot),\varphi\rangle|
\le
\lambda^{-1/2}\|U\|_{L^2(B_{\lambda R}(x_k))}\|\varphi\|_{L^2}.
\]

L'absolue continuité \(L^2\) ne fournit pas le taux \(o(\lambda^{1/2})\). Le profil scalaire \(U(x)=\chi(x)|x|^{-\alpha}\), \(1<\alpha<3/2\), appartient à \(L^2\), mais \(\lambda U(\lambda y)=\lambda^{1-\alpha}|y|^{-\alpha}\) ne tend pas vers zéro dans les distributions positives locales. Ce n'est pas une donnée Navier–Stokes divergence-free : c'est exactement un contre-profil fonctionnel à l'implication « topologie d'énergie \(\Rightarrow\) trace zoomée nulle ».

Le théorème Barker–Seregin en demi-espace exploite de même l'ordre-continu de \(L^{3,q}\), \(q<\infty\), sur les ensembles de mesure décroissante. Cette propriété échoue à l'endpoint spatial \(L^{3,\infty}\), exclu de leur conclusion.

## 3. Équi-intégrabilité critique : critère connu et obstruction KNSS

Constantin suppose, pour une solution forte lisse sur \([0,T)\), qu'il existe \(\delta>0\) tel que, pour tout temps et tout ensemble mesurable \(|A|\le\delta\),

\[
\int_A|u(x,t)|^3\,dx
\le\left(\frac{\nu}{2C}\right)^3,
\]

\(C\) étant la constante de Sobolev utilisée. Son théorème 2 donne une borne explicite de \(\|u(t)\|_{\dot H^1}\) et le prolongement. Cette condition à seuil fixe est plus faible que l'équi-intégrabilité complète, où le membre de gauche doit tendre uniformément vers zéro avec \(|A|\). Postuler cette dernière uniformément près de \(T\) est donc déjà une hypothèse de régularité connue.

### Dérivation du laboratoire : concentration aux tranches de normalisation

**Statut : dérivation AI/laboratoire, non attribuée aux articles et non PAPER_PROOF.**

Les estimations de régularisation mild de KNSS, redémarrées sur \(s\in[-1,0]\), donnent pour \(k\) assez grand une constante \(C_0<\infty\), indépendante de \(k\), telle que

\[
\|\nabla v_k(\cdot,0)\|_\infty\le C_0.
\]

Avec \(r_0=\min\{1,(2C_0)^{-1}\}\), la condition \(|v_k(0,0)|=1\) implique

\[
|v_k(y,0)|\ge\frac12\quad(|y|\le r_0),
\qquad
\int_{B_{r_0}}|v_k(y,0)|^3dy
\ge c_0:=\frac{|B_{r_0}|}{8}>0.
\]

Par invariance critique,

\[
\int_{B_{r_0/M_k}(x_k)}|u(x,t_k)|^3dx\ge c_0.
\]

Or \(M_k\to\infty\), donc le volume de ces boules tend vers zéro. La famille \(\{|u(t_k)|^3\}_k\) n'est pas équi-absolument continue : pour \(\varepsilon=c_0/2\), aucun \(\delta\) uniforme ne convient. L'entrée analytique falsifiable est la borne \(C_0\) issue des estimations mild sur la bande redémarrée.

En revanche, les \(v_k(0)\), uniformément bornés localement, sont équi-intégrables sur les compacts, mais convergent vers une tranche non nulle. L'équi-intégrabilité après zoom ne produit donc pas de trace terminale nulle. Enfin, sans constante explicite \(C_0\), la borne \(c_0\) ne permet pas d'affirmer que le seuil fixe de Constantin est violé ; elle réfute exactement l'équi-intégrabilité complète.

**Portée bibliographique corrigée.** Ce corollaire quantitatif est une reformulation directe de la normalisation KNSS et du lissage parabolique, donc un phénomène classique de concentration de blow-up, pas un nouveau critère de régularité revendiqué. Une équi-intégrabilité complète uniforme en temps implique immédiatement la condition (23) de Constantin en choisissant son seuil fixe ; le théorème 2 fournit alors déjà le prolongement. Une équi-intégrabilité limitée à la seule suite \(t_k\) ne transmet toujours pas la tranche terminale \(u(T)\) et ne ferme donc pas, par elle-même, le problème Clay.

## 4. Backward uniqueness, élément critique et nouveauté 2026

Gallagher–Koch–Planchon démontrent qu'un élément critique hypothétique, forward et borné dans \(L^\infty_tL^3_x\), tend vers zéro dans \(\mathcal S'\) au temps maximal (théorème 6), puis qu'une telle solution ne peut avoir un temps maximal fini (théorème 7). Cet objet n'est pas la solution ancienne \(L^\infty_{x,t}\) de KNSS. Importer sa trace dans le profil KNSS supposerait le raccord à démontrer.

La backward uniqueness est une rigidité, non une production de trace. Sa forme pertinente contrôle une solution de

\[
|\partial_tw+\Delta w|
\le c_1(|\nabla w|+|w|)
\]

avec donnée terminale nulle, dérivées locales \(L^2\), coefficients appropriés et croissance contrôlée. Pour Navier–Stokes, elle s'applique à la vorticité après obtention de la décroissance spatiale. Elle ne justifie ni \(u(\cdot,0)=0\), ni la convergence de la pression, ni l'alignement de \(B_k\).

La prépublication Cheskidov–Dai–Palasek v2 traite un phénomène différent sur \(\mathbb T^d\) : le champ est spatialement lisse à \(T_*\), mais \(\|u(t)\|_\infty\) explose quand \(t\downarrow T_*\) **depuis la droite**. Le théorème donne une continuité faible-* \(BMO^{-1}\), tandis que la remarque 1.4 exclut \(L^\infty_tL^2_x\) et \(L^2_tH^1_x\) près de \(T_*\). Ce n'est ni un blow-up forward de la solution classique Clay, ni une solution Leray–Hopf admissible. Il confirme toutefois qu'une trace faible critique ne contrôle pas une injection instantanée depuis les hautes fréquences hors de la classe d'énergie.

## Implications et non-implications Clay

| Maillon | Statut | Conclusion exacte |
|---|---|---|
| Blow-up classique fini \(\Rightarrow\) ancienne mild bornée non nulle | Classique, KNSS | Oui sur \(\mathbb R^3\), sur l'horloge centrée en \(t_k\). |
| Borne \(L^3\) le long de \(t_k\uparrow T\) \(\Rightarrow\) limite terminale non triviale à trace nulle | Classique, Seregin/ESS | Oui, puis contradiction ; donc le \(L^3\) diverge à une singularité. |
| Trace \(L^2\) \(\Rightarrow\) trace zoomée nulle dans \(\mathcal D'\) | Faux fonctionnellement | Il manque un taux local \(o(\lambda^{1/2})\). |
| Équi-intégrabilité de \(|u(t_k)|^3\) \(\Rightarrow\) raccord KNSS | Inapplicable aux maxima | La concentration \(c_0\) sur des boules de rayon \(M_k^{-1}\) la réfute. |
| \(v_k\to v\) pour \(s<0\) \(\Rightarrow\) valeur au temps physique \(T\) | Maillon manquant | \(T\) correspond à \(s=B_k\), hors des compacts contrôlés. |
| Trace nulle et hypothèses de coefficient/décroissance \(\Rightarrow\) vorticité nulle | Classique, ESS | Oui par backward uniqueness ; aucune prémisse n'est créée par ce théorème. |
| Blow-up instantané 2026 \(\Rightarrow\) résolution négative Clay | Non | Mauvais sens temporel et absence d'admissibilité Leray–Hopf. |

## Recommandation falsifiable

**Abandonner comme axe principal l'équi-intégrabilité \(L^3\) complète des tranches maximum-normalisées.** Elle est réfutée par la concentration quantitative ci-dessus et, postulée uniformément près de \(T\), recouvre un critère de prolongement connu.

Le test suivant à meilleure valeur informationnelle est une **porte de compacité terminale alignée sur l'horloge**. Pour une suite KNSS, séparer les deux branches de \(B_k\) et chercher une hypothèse strictement plus faible qu'une borne critique \(L^3\) donnant simultanément :

1. \(B_k\to\beta\in(0,\infty)\), afin de conserver \(w_k(0,-B_k)=1\) à temps fini ;
2. une compacité locale-énergie et une pression normalisée sur chaque cylindre terminal \([-S,0]\) ;
3. \(w_k(\cdot,0)\to0\) dans \(\mathcal D'\), idéalement dans \(L^{9/8}_{\mathrm{loc}}\) ;
4. un contrôle suffisant sur \((-\beta,0)\) pour la rigidité, sans réintroduire \(L^\infty_tL^3_x\), \(L^{3,q}\) ou la condition de Constantin.

**Critère de réfutation.** Abandonner cet axe si toute hypothèse assurant 2–4 implique déjà un critère critique connu, ou si un contre-profil compatible avec les seules bornes d'énergie impose \(B_k\to\infty\) ou conserve un défaut terminal. Un résultat positif doit suivre les constantes de pression locale et la stabilité de la notion de solution ; une convergence de vitesse seule ne suffit pas.

**État bibliographique du verrou : ouvert dans ce programme.** Les sources auditées donnent les deux moitiés du mécanisme sur des objets et des horloges différents ; aucune ne justifie leur identification.
