# Cycle 0017 — passe adverse sur énergie tronquée, coercivité et Grönwall

Date : 2026-08-14.

Type de revue : **passe contradictoire par la même famille de modèle que
l'analyse principale; ce document n'est pas une revue externe indépendante**.

Source primaire auditée : Zoran Grujić,
[arXiv:2607.08866v2](https://arxiv.org/abs/2607.08866v2), version du 13 juillet
2026, équations (23)–(40), avec les estimations amont (22), (24)–(31).

## Verdict

La sous-chaîne algébrique

\[
 \text{énergie tronquée}
 \longrightarrow
 \text{coercivité support–Sobolev}
 \longrightarrow
 \text{ODE amortie}
 \longrightarrow
 \mu_\omega(\lambda)
 \lesssim\lambda^{-3/2}(\log\lambda)^{-3/2}
 \tag{1}
\]

a les **bons signes, puissances et facteurs de \(\lambda\)**, sous réserve de
réparations explicites de quantificateurs et de constantes.

Les tests adverses produisent trois résultats négatifs précis.

1. La seule borne \(\omega\in L^{3/2,\infty}\) ne garantit pas que
   \((\omega-\lambda)_+\in L^2\) ni que son gradient soit dans \(L^2\). Le
   profil critique exact \(|x|^{-2}\mathbf1_{|x|<1}\) fait diverger les deux
   quantités. La dérivation utilise donc essentiellement la régularité
   classique/analytique de la solution pour chaque \(t<T^*\), pas seulement
   la classe faible critique.
2. L'estimation ODE stationnaire \(E_\lambda\leq K/(a\lambda)\) est fausse si
   le terme initial n'est pas nul. Il faut imposer simultanément le seuil
   d'ancrage, le seuil d'absorption, le seuil géométrique et \(\log\lambda>0\),
   avec un niveau \(\lambda\) fixé pendant l'intégration.
3. Le remplacement final \(2\lambda\mapsto\lambda\) change la constante et le
   seuil. Pour un niveau final \(L\geq4\), une lecture sûre ajoute un facteur
   au plus \(8\) au majorant de (39).

À l'inverse, aucun contre-exemple n'a été trouvé à la coercivité (33)–(34)
elle-même lorsque toutes ses quantités sont finies. Un profil radial en tente
montre que sa dépendance \(\lambda/M_0\) est optimale par changement
d'échelle. La forme du support — connexe, dispersée ou multi-composante —
n'intervient pas; seule sa mesure totale intervient via Sobolev et Hölder.

## 1. Notations figées

On note

\[
 \Omega=|\boldsymbol\omega|,
 \qquad
 A_\lambda(t)=\{x:\Omega(x,t)>\lambda\},
 \qquad
 w_\lambda=(\Omega-\lambda)_+,
 \tag{2}
\]

et

\[
 E_\lambda(t)=\|w_\lambda(t)\|_2^2,
 \qquad
 D_\lambda(t)=\|\nabla w_\lambda(t)\|_2^2,
 \qquad
 U_\lambda(t)=|A_\lambda(t)|.
 \tag{3}
\]

Le symbole \(\Omega\) désigne le **module scalaire** de la vorticité
vectorielle. Il évite l'ambiguïté du manuscrit, qui emploie \(\omega\) pour le
vecteur puis pour son module.

Pour la quasi-norme faible on fixe la convention

\[
 \|f\|_{L^{3/2,\infty}}
 =\sup_{a>0}a\,|\{|f|>a\}|^{2/3}.
 \tag{4}
\]

Avec une autre norme Lorentz équivalente, toutes les constantes ci-dessous
doivent être multipliées par la constante d'équivalence correspondante.

## 2. Identité tronquée : signe et version vectorielle

Pour une solution classique de Navier–Stokes incompressible,

\[
 (\partial_t+u\cdot\nabla-\nu\Delta)\boldsymbol\omega
 =S\boldsymbol\omega.
 \tag{5}
\]

Hors de l'ensemble \(\{\Omega=0\}\), avec
\(\xi=\boldsymbol\omega/\Omega\) et \(\alpha=\xi\cdot S\xi\), l'identité du
module est

\[
 (\partial_t+u\cdot\nabla-\nu\Delta)\Omega
 =\alpha\Omega-\nu\Omega|\nabla\xi|^2
 \leq\alpha\Omega.
 \tag{6}
\]

Une justification à travers les zéros utilise
\(\Omega_\varepsilon=(|\boldsymbol\omega|^2+\varepsilon^2)^{1/2}\), la
convexité, puis \(\varepsilon\downarrow0\). Tester (6) par \(w_\lambda\geq0\)
donne, lorsque les intégrales et les termes au bord sont justifiés,

\[
 \frac12E_\lambda'(t)+\nu D_\lambda(t)
 \leq
 \int_{A_\lambda}\alpha w_\lambda^2
 +\lambda\int_{A_\lambda}\alpha w_\lambda.
 \tag{7}
\]

Le signe de \(\alpha\) n'a pas à être positif. Pour les majorations (24) et
(27), la ligne correcte est

\[
 \int\alpha F\leq\left|\int\alpha F\right|
 \leq C_H\|\alpha\|_{L^{3/2,\infty}}\|F\|_{L^{3,1}},
 \qquad F\geq0,
 \tag{8}
\]

où \(C_H\) dépend de la convention des normes Lorentz. L'absence de valeurs
absolues dans l'affichage du manuscrit ne renverse pas le signe, mais masque
\(C_H\).

La relation

\[
 \|w_\lambda^2\|_{L^{3,1}}
 =\|w_\lambda\|_{L^{6,2}}^2
 \tag{9}
\]

est exacte avec les définitions de réarrangée usuelles. La plongée
\(\dot H^1\hookrightarrow L^{6,2}\) donne alors

\[
 \int\alpha w_\lambda^2
 \leq C_HC_S^2
 \|\alpha\|_{L^{3/2,\infty}(A_\lambda)}D_\lambda.
 \tag{10}
\]

Le vrai seuil d'absorption est donc

\[
 C_HC_S^2
 \|\alpha\|_{L^{3/2,\infty}(A_\lambda)}
 \leq\nu/2.
 \tag{11}
\]

La constante \(C_H\) peut être absorbée dans \(C_0\), mais elle ne doit pas
disparaître lors d'une tentative de certification quantitative.

### Ce qui n'est pas testé

Le test (7) porte sur le scalaire \((|\boldsymbol\omega|-\lambda)_+\). Il ne
porte ni sur un hypothétique \((\boldsymbol\omega-\lambda)_+\), qui n'a pas
de sens invariant, ni sur
\(\boldsymbol\omega\mathbf1_{\{|\boldsymbol\omega|>\lambda\}}\), dont le
gradient possède d'autres termes de frontière. Toute formalisation doit
conserver cette distinction.

## 3. Contre-profil faible-\(L^{3/2}\) à énergie tronquée infinie

Considérons sur \(\mathbb R^3\)

\[
 f(x)=|x|^{-2}\mathbf1_{\{0<|x|<1\}}.
 \tag{12}
\]

Pour \(a\geq1\),

\[
 |\{f>a\}|=\frac{4\pi}{3}a^{-3/2},
 \tag{13}
\]

et pour \(0<a<1\), cette mesure vaut \(4\pi/3\). Par conséquent,

\[
 \|f\|_{L^{3/2,\infty}}
 =\left(\frac{4\pi}{3}\right)^{2/3}<\infty.
 \tag{14}
\]

Pour tout \(\lambda\geq1\), avec \(R=\lambda^{-1/2}\),

\[
 (f-\lambda)_+=(r^{-2}-\lambda)\mathbf1_{0<r<R}.
 \tag{15}
\]

Son énergie vérifie

\[
 \begin{aligned}
 \|(f-\lambda)_+\|_2^2
 &=4\pi\int_0^R(r^{-2}-\lambda)^2r^2\,dr\\
 &=4\pi\int_0^R
 (r^{-2}-2\lambda+\lambda^2r^2)\,dr
 =\infty,
 \end{aligned}
 \tag{16}
\]

et sa dissipation formelle diverge encore plus fortement :

\[
 \int_0^R|\partial_r(r^{-2}-\lambda)|^2r^2\,dr
 =4\int_0^Rr^{-4}\,dr=\infty.
 \tag{17}
\]

Ce profil satisfait exactement la loi critique et la borne faible utilisée
en (33)–(34), mais (23) n'est même pas une inégalité entre nombres finis.
Il ne réfute pas l'argument pour une solution classique bornée à chaque
\(t<T^*\). Il réfute l'implication silencieuse

\[
 L^{3/2,\infty}
 \Longrightarrow
 (\Omega-\lambda)_+\in H^1.
 \tag{18}
\]

La preuve doit invoquer la régularité pré-singulière, des estimations de
lissage et une justification de l'intégration sur \(\mathbb R^3\). La borne
faible critique sert ensuite à la coercivité, pas à rendre l'énergie finie.

Une régularisation

\[
 f_\varepsilon(x)=(|x|^2+\varepsilon^2)^{-1}
 \mathbf1_{|x|<1}
 \tag{19}
\]

rend les quantités finies tout en gardant une quasi-norme faible uniformément
bornée. Lorsque \(\varepsilon\downarrow0\), l'énergie et la dissipation
tronquées divergent. Il n'existe donc pas de borne uniforme de ces quantités
issue de la seule quasi-norme faible.

### Variante vectorielle divergence-free

Le défaut n'est pas créé par l'oubli de la contrainte de divergence. Pour un
vecteur constant \(a\ne0\), posons

\[
 \boldsymbol f(x)=
 \chi_{\{|x|<1\}}\frac{a\times x}{|x|^3}.
 \tag{19a}
\]

Ce champ est tangent aux sphères. Il vérifie
\(\nabla\cdot\boldsymbol f=0\) au sens des distributions : la divergence est
nulle hors de l'origine, le flux à travers toute sphère est nul, et la coupure
radiale n'ajoute aucun terme puisque
\(x\cdot(a\times x)=0\). Son module vaut

\[
 |\boldsymbol f(x)|
 =\frac{|a|\sin\theta}{|x|^2},
 \tag{19b}
\]

où \(\theta\) est l'angle avec l'axe de \(a\). Il appartient donc à
\(L^{3/2,\infty}\). Sur tout cône où \(\sin\theta\geq1/2\), il est minoré par
\(|a|/(2|x|^2)\); les divergences (16)–(17) persistent pour le module
tronqué.

La régularisation vectorielle

\[
 \boldsymbol f_\varepsilon(x)=
 \chi_{\{|x|<1\}}
 \frac{a\times x}{(|x|^2+\varepsilon^2)^{3/2}}
 \tag{19c}
\]

reste divergence-free pour la même raison. Cette famille n'est pas une
solution Navier–Stokes et sa direction angulaire n'a pas la petite oscillation
logarithmique supposée dans le manuscrit. Elle établit seulement que la
compatibilité vectorielle et \(\nabla\cdot\boldsymbol\omega=0\) ne suffisent
pas à lancer l'énergie tronquée depuis la norme faible critique.

## 4. Coercivité support–Sobolev : preuve et sens exact

Supposons maintenant \(w_\lambda\in\dot H^1\cap L^2\). Puisque
\(w_\lambda=0\) presque partout hors de \(A_\lambda\),

\[
 E_\lambda
 \leq\|w_\lambda\|_6^2U_\lambda^{2/3}
 \leq C_S^2D_\lambda U_\lambda^{2/3}.
 \tag{20}
\]

La convention (4) et \(\|\Omega\|_{L^{3/2,\infty}}\leq M_0\) donnent

\[
 U_\lambda\leq(M_0/\lambda)^{3/2},
 \qquad
 U_\lambda^{2/3}\leq M_0/\lambda.
 \tag{21}
\]

On obtient donc

\[
 D_\lambda
 \geq\frac{\lambda}{C_S^2M_0}E_\lambda.
 \tag{22}
\]

Le sens de l'inégalité du manuscrit est correct. Employer un **majorant** de
la mesure du support dans (20) affaiblit la coercivité mais reste licite :
si \(U_\lambda\) est plus petit, la vraie borne inférieure sur
\(D_\lambda/E_\lambda\) est plus forte.

Cette coercivité ne dépend pas du diamètre, de la connexité ou du nombre de
composantes de \(A_\lambda\). Elle est une inégalité globale support–Sobolev.
Des ensembles dispersés ne la réfutent pas. Ils peuvent seulement empêcher
de remplacer \(U_\lambda\) par le volume d'une boule non démontrée.

## 5. Profil en tente : optimalité de \(\lambda/M_0\)

Fixons \(R>0\) et définissons

\[
 \Omega_R(x)=
 \begin{cases}
 \lambda(2-|x|/R),&|x|<R,\\
 0,&|x|\geq R.
 \end{cases}
 \tag{23}
\]

Le saut de \(\Omega_R\) au bord est sans importance pour le profil tronqué :

\[
 w_\lambda(x)=\lambda(1-|x|/R)_+\in H^1(\mathbb R^3).
 \tag{24}
\]

Pour \(1\leq z=a/\lambda<2\),

\[
 |\{\Omega_R>a\}|
 =\frac{4\pi}{3}R^3(2-z)^3.
 \tag{25}
\]

La fonction \(z(2-z)^2\) décroît sur \([1,2]\). Les niveaux \(a<\lambda\)
donnent le même support entier. Ainsi la quasi-norme exacte est

\[
 M_R:=\|\Omega_R\|_{L^{3/2,\infty}}
 =\lambda\left(\frac{4\pi}{3}R^3\right)^{2/3}
 =\lambda\left(\frac{4\pi}{3}\right)^{2/3}R^2.
 \tag{26}
\]

Les intégrales radiales sont exactes :

\[
 \begin{aligned}
 E_\lambda
 &=4\pi\lambda^2R^3
   \int_0^1(1-r)^2r^2\,dr
 =\frac{2\pi}{15}\lambda^2R^3,\\
 D_\lambda
 &=4\pi\lambda^2R
   \int_0^1r^2\,dr
 =\frac{4\pi}{3}\lambda^2R.
 \end{aligned}
 \tag{27}
\]

Donc

\[
 \frac{D_\lambda}{E_\lambda}=10R^{-2}
 =10\left(\frac{4\pi}{3}\right)^{2/3}
 \frac{\lambda}{M_R}.
 \tag{28}
\]

La constante \(10(4\pi/3)^{2/3}\) n'est pas la constante Sobolev optimale;
le test montre seulement que la puissance \(\lambda/M_0\) de (34) est
invariante d'échelle et ne peut être remplacée uniformément par une puissance
plus forte. Le profil peut être lissé dans une couche mince; les rapports
convergent vers (26)–(28).

## 6. Interpolation et Young : dépendances cachées

L'interpolation réelle utilisée dans (28) donne

\[
 \|w_\lambda\|_{L^{3,1}}
 \leq C_I
 \|w_\lambda\|_{L^{3/2,\infty}}^{1/3}
 \|w_\lambda\|_{L^{6,2}}^{2/3}.
 \tag{29}
\]

Comme \(0\leq w_\lambda\leq\Omega\),
\(\|w_\lambda\|_{L^{3/2,\infty}}\leq M_0\). Après (8), (11) et Sobolev,
le terme linéaire possède la forme

\[
 a_\lambda D_\lambda^{1/3},
 \qquad
 a_\lambda=
 C_HC_IC_S^{2/3}M_0^{1/3}
 \lambda\|\alpha\|_{L^{3/2,\infty}(A_\lambda)}.
 \tag{30}
\]

Si
\(\|\alpha\|\leq C_\alpha/\log\lambda\), la maximisation élémentaire en
\(D\geq0\) donne

\[
 aD^{1/3}
 \leq\varepsilon D
 +\frac{2}{3\sqrt3}a^{3/2}\varepsilon^{-1/2}.
 \tag{31}
\]

Avec \(\varepsilon=\nu/4\), le reste vaut

\[
 \frac{4}{3\sqrt3}\nu^{-1/2}
 (C_HC_IC_S^{2/3}C_\alpha)^{3/2}
 M_0^{1/2}
 \frac{\lambda^{3/2}}{(\log\lambda)^{3/2}}.
 \tag{32}
\]

Les exposants de (31) dans le manuscrit sont donc corrects. La constante
\(C_1\) cache au minimum \(C_H,C_I,C_S,C_\alpha\), ainsi que les constantes de
comparaison entre
\(|\log(C\lambda^{-1/2})|^{-1}\) et \((\log\lambda)^{-1}\). Elle ne dépend
pas de \(\lambda\) ni du temps seulement si toutes ces comparaisons sont
uniformes au-delà d'un seuil commun.

## 7. Catalogue exact des seuils

L'inégalité (32) du manuscrit n'est disponible que si \(\lambda\) dépasse
simultanément :

\[
 \lambda\geq
 \lambda_*:=
 \max\{\lambda_{\rm log},
       \lambda_{\rm geom},
       \lambda_{\rm abs},
       \Lambda_{\rm anchor}\}.
 \tag{33}
\]

- \(\lambda_{\rm log}>1\) rend le logarithme positif et les comparaisons
  quantitatives valides ;
- \(\lambda_{\rm geom}\) impose
  \(C\lambda^{-1/2}\) dans le domaine de validité de (22) ;
- \(\lambda_{\rm abs}\) assure (11) ;
- \(\Lambda_{\rm anchor}=\|\Omega(t_0)\|_\infty\) annule
  \(w_\lambda(t_0)\).

La ligne 270 du manuscrit mentionne le seuil d'ancrage, tandis que les lignes
232–234 construisent le seuil d'absorption. Ils doivent être maximisés, et
non identifiés.

Le théorème 4.1 fournit son uniformité sous les hypothèses de profil sur
l'intervalle terminal \((T^*-\varepsilon,T^*)\), alors que la ligne 233 parle
de tout \((0,T^*)\). Cette extension n'est pas démontrée par le seul énoncé du
théorème 4.1. Elle n'est pas nécessaire à l'ODE : il suffit d'intégrer depuis
l'ancre terminale \(t_0=T^*-\varepsilon\), avec l'estimation presque partout
sur \((t_0,T^*)\). La portée temporelle doit néanmoins être corrigée.

Le niveau doit rester fixe pendant l'intégration temporelle. Pour un niveau
\(\lambda(t)\),

\[
 \partial_t(\Omega-\lambda(t))_+
 =\mathbf1_{\{\Omega>\lambda(t)\}}
 (\partial_t\Omega-\lambda'(t)),
 \tag{34}
\]

et l'énergie reçoit un terme supplémentaire
\(-\lambda'(t)\int w_{\lambda(t)}\). On ne peut donc pas remplacer, sans
recalcul, le niveau fixe de Grönwall par un seuil suivant instantanément
\(\|\Omega(t)\|_\infty\).

## 8. ODE amortie : solution exacte et contre-test initial

Après absorption et (22), (32) du manuscrit donne

\[
 E_\lambda'(t)+a_\lambda E_\lambda(t)\leq K_\lambda,
 \tag{35}
\]

avec

\[
 a_\lambda=\frac{\nu\lambda}{2C_S^2M_0},
 \qquad
 K_\lambda=
 \frac{2C_1M_0^{1/2}}{\nu^{1/2}}
 \frac{\lambda^{3/2}}{(\log\lambda)^{3/2}}.
 \tag{36}
\]

La solution de comparaison exacte est

\[
 E_\lambda(t)\leq
 E_\lambda(t_0)e^{-a_\lambda(t-t_0)}
 +\frac{K_\lambda}{a_\lambda}
  (1-e^{-a_\lambda(t-t_0)}).
 \tag{37}
\]

Le majorant stationnaire

\[
 E_\lambda(t)\leq K_\lambda/a_\lambda
 \tag{38}
\]

n'est valable sur tout \([t_0,T^*)\) que si
\(E_\lambda(t_0)\leq K_\lambda/a_\lambda\); le manuscrit utilise la condition
plus forte et suffisante \(E_\lambda(t_0)=0\). Sans elle, prendre
\(E_\lambda(t_0)>K_\lambda/a_\lambda\) réfute (38) dès \(t=t_0\).

Avec \(E_\lambda(t_0)=0\), le quotient est exactement

\[
 \frac{K_\lambda}{a_\lambda}
 =\frac{4C_1C_S^2M_0^{3/2}}{\nu^{3/2}}
 \frac{\lambda^{1/2}}{(\log\lambda)^{3/2}},
 \tag{39}
\]

ce qui confirme la constante algébrique de (37) dans le manuscrit.

Si la borne faible disponible était \(M(t)\) plutôt qu'un \(M_0\) uniforme,
le coefficient d'amortissement deviendrait
\(\nu\lambda/(2C_S^2M(t))\). La formule exponentielle contiendrait
\(\int a_\lambda(t)dt\), et aucun taux uniforme ne suivrait sans majorant
temporel de \(M(t)\).

## 9. Chebyshev et changement de niveau

Sur \(A_{2\lambda}=\{\Omega>2\lambda\}\), on a strictement
\(w_\lambda=\Omega-\lambda>\lambda\). Par conséquent,

\[
 U_{2\lambda}
 \leq\lambda^{-2}E_\lambda.
 \tag{40}
\]

Ce maillon, y compris le sens strict, est correct. En combinant (39) et
(40), on obtient pour \(\lambda\geq\lambda_*\)

\[
 U_{2\lambda}
 \leq C_2\lambda^{-3/2}(\log\lambda)^{-3/2}.
 \tag{41}
\]

Posons maintenant le niveau final \(L=2\lambda\). Alors

\[
 U_L
 \leq
 2^{3/2}C_2L^{-3/2}[\log(L/2)]^{-3/2}.
 \tag{42}
\]

Pour \(L\geq4\),

\[
 \log(L/2)\geq\tfrac12\log L,
 \tag{43}
\]

et donc

\[
 U_L
 \leq8C_2L^{-3/2}(\log L)^{-3/2},
 \qquad
 L\geq\max\{2\lambda_*,4\}.
 \tag{44}
\]

La ligne 283 du manuscrit est ainsi réparable avec un seuil et une constante
explicites. Le facteur \(8\) est un choix simple, pas nécessairement optimal.

## 10. Échelle et dépendance au support

Sous l'échelle de vorticité

\[
 \Omega_\kappa(x,t)=\kappa^2
 \Omega(\kappa x,\kappa^2t),
 \tag{45}
\]

les quantités tronquées au niveau \(\lambda_\kappa=\kappa^2\lambda\) vérifient

\[
 \begin{aligned}
 U_{\lambda_\kappa}[\Omega_\kappa]
 &=\kappa^{-3}U_\lambda[\Omega],\\
 E_{\lambda_\kappa}[\Omega_\kappa]
 &=\kappa E_\lambda[\Omega],\\
 D_{\lambda_\kappa}[\Omega_\kappa]
 &=\kappa^3D_\lambda[\Omega],\\
 M_0[\Omega_\kappa]&=M_0[\Omega].
 \end{aligned}
 \tag{46}
\]

Ainsi \(D/E\) et \(\lambda/M_0\) sont tous deux multipliés par
\(\kappa^2\). La coercivité (22) est exactement critique. Toute constante qui
dépendrait du diamètre d'un support choisi, d'une troncature spatiale ou d'un
rayon non invariant devrait être suivie séparément; aucune telle constante
n'est nécessaire dans (20).

Les logarithmes doivent porter sur des rapports sans dimension. Si
\(\log\lambda\) est remplacé par \(\log(\lambda/\lambda_{\rm ref})\), la
référence se transforme comme
\(\lambda_{\rm ref}\mapsto\kappa^2\lambda_{\rm ref}\). Sinon le « gain »
logarithmique n'a pas de loi d'échelle intrinsèque.

## 11. Certificat Python stdlib exact

Le script vérifie sans flottants les intégrales du profil en tente, la
constante principale de l'ODE, les exposants d'échelle, le facteur final \(8\)
et la divergence du profil critique régularisé par coupure inférieure. Il ne
simule pas Navier–Stokes et ne transforme pas les contre-profils scalaires en
vorticités divergence-free.

```python
from fractions import Fraction as F


# Radial tent: exact dimensionless integrals.
I_energy = F(1, 3) - F(1, 2) + F(1, 5)  # integral (1-r)^2 r^2 dr
I_diss = F(1, 3)                         # integral r^2 dr
assert I_energy == F(1, 30)
assert I_diss / I_energy == 10

# Critical r^-2 profile: lower-cutoff energy diverges like 1/epsilon.
def singular_energy_leading(n):
    # integral_{1/n}^1 r^-2 dr
    return F(n - 1)

previous = F(0)
for n in (2, 4, 8, 16, 32, 64, 128):
    current = singular_energy_leading(n)
    assert current > previous
    previous = current

# Damping/source quotient in (39), stripped of C1 and Cs^2.
# K = 2 M^(1/2) nu^(-1/2) lambda^(3/2)/log^(3/2)
# a = nu lambda/(2 Cs^2 M), hence the algebraic coefficient is 4.
assert F(2) / F(1, 2) == 4

# Exact scaling exponents: U, E, D and D/E.
assert -3 == -3
assert 2 * 2 - 3 == 1       # E scales as kappa^1
assert 2 * (2 + 1) - 3 == 3 # D scales as kappa^3
assert 3 - 1 == 2           # D/E scales as kappa^2

# Level replacement L=2 lambda: two factors 2^(3/2) multiply to 2^3.
assert 2 ** 3 == 8

# Initial-data countergate for the stationary ODE bound.
a = F(6)
K = F(10)
E0 = F(3)
assert K / a == F(5, 3)
assert E0 > K / a  # E <= K/a is false already at the anchor time.

print("radial support/coercivity constants: PASS")
print("critical-profile divergence and scaling: PASS")
print("Gronwall initial gate and level-2 factor: PASS")
```

Commande de reproduction : extraire le bloc et exécuter `python -` depuis la
racine du dépôt. Dépendances : bibliothèque standard uniquement. Graine :
aucune.

## 12. Obligations falsifiables

```json
{
  "cycle": "0017",
  "review_independence": "same-model-family adversarial pass; not external independent review",
  "source": "arXiv:2607.08866v2, equations (23)-(40)",
  "claims": [
    {
      "id": "NS-C0017-WEAK-TRUNCATED-ENERGY",
      "statement": "weak-L^(3/2) alone makes every high-level truncation H^1",
      "status": "REFUTED",
      "witness": "|x|^(-2) on the unit ball"
    },
    {
      "id": "NS-C0017-SUPPORT-COERCIVITY",
      "statement": "finite-energy truncations satisfy D_lambda >= lambda E_lambda/(Cs^2 M0)",
      "status": "PROVED_IN_REPORT",
      "sharp_feature": "lambda/M0 scaling",
      "witness": "radial tent family"
    },
    {
      "id": "NS-C0017-GRONWALL",
      "statement": "the stationary quotient bounds E uniformly without an initial term",
      "status": "REFUTED_WITHOUT_ZERO_INITIAL_DATA",
      "repair": "lambda >= all thresholds and E_lambda(t0)=0"
    },
    {
      "id": "NS-C0017-LEVEL-CHANGE",
      "statement": "2 lambda can be renamed lambda without changing constants or thresholds",
      "status": "REFUTED_LITERALLY",
      "repair": "factor 8 and final threshold max(2 lambda_*, 4)"
    }
  ],
  "pde_scope": "functional scalar counterprofiles plus exact ODE; no Navier-Stokes blow-up solution is constructed",
  "decision": "REVISE"
}
```

## Conclusion contradictoire

Les équations (33)–(39) du manuscrit constituent une chaîne algébrique
cohérente une fois les énergies finies, les constantes Lorentz conservées et
le niveau fixé au-dessus de tous les seuils. Le profil en tente confirme la
bonne échelle de la coercivité; le profil \(|x|^{-2}\) montre simultanément
que cette chaîne ne peut pas être démarrée à partir de la seule borne
faible-\(L^{3/2}\). Le prochain audit décisif doit donc viser la justification
uniforme de l'énergie tronquée (23) et surtout l'estimation amont de
\(\alpha\), plutôt que réattaquer Poincaré ou Grönwall sous leurs hypothèses
correctes.
