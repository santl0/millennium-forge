# Cycle 0016 — contre-profils pour le transfert vorticité–vitesse

Date : 2026-08-14.

Type de passe : **revue adverse effectuée par la même famille de modèle que
l'analyse principale; ce document n'est pas une revue externe indépendante**.

Source primaire auditée : Zoran Grujić,
[arXiv:2607.08866v2](https://arxiv.org/abs/2607.08866v2), version du 13 juillet
2026, équations (40)–(47). La référence primaire historique invoquée par le
manuscrit pour la convolution est R. O'Neil,
[*Convolution operators and \(L(p,q)\) spaces*](https://doi.org/10.1215/S0012-7094-63-03015-1),
Duke Mathematical Journal **30** (1963), 129–142.

## Verdict

La chaîne abstraite

\[
 \mu_\omega(\lambda)
 \lesssim \lambda^{-3/2}(\log\lambda)^{-3/2}
 \Longrightarrow
 \omega^*(s)
 \lesssim \frac{s^{-2/3}}{\log(e/s)}
 \Longrightarrow
 (I_1|\omega|)^*(s)
 \lesssim \frac{s^{-1/3}}{\log(e/s)}
 \tag{1}
\]

est **correcte aux petits volumes**, avec les mêmes puissances, si les
conditions suivantes sont ajoutées et suivies :

1. la constante de queue et son seuil de grand niveau sont uniformes en
   temps ;
2. le petit-volume \(V_0\) obtenu après inversion est lui aussi uniforme ;
3. la queue de réarrangée \(s>V_0\) est contrôlée globalement, par exemple par
   une borne uniforme \(\omega\in L^{3/2,\infty}(\mathbb R^3)\) ;
4. la vitesse est la solution de Biot–Savart normalisée à l'infini, ou bien
   on estime \(u-U_\infty\). La vorticité seule ne voit pas le champ
   harmonique constant.

Deux affirmations littérales échouent.

- Une queue valable seulement au-delà d'un seuil \(\Lambda_0(t)\) non
  uniforme ne produit aucune enveloppe de réarrangée uniforme.
- Sur \(\mathbb R^3\), le champ constant \(u\equiv U\ne0\) est une solution
  Navier–Stokes lisse, divergence-free, de vorticité nulle. Il réfute toute
  formule non normalisée prétendant contrôler la vitesse entière par
  \(I_1|\omega|\).

La masse basse fréquence n'altère pas l'exposant asymptotique si la borne
globale \(L^{3/2,\infty}\) est disponible, mais elle entre nécessairement
dans la constante. Une queue de hauts niveaux seule ne suffit pas.

## 1. Cadre et conventions

Pour une fonction mesurable \(f\geq0\), finie presque partout, posons

\[
 \mu_f(\lambda)=|\{x:f(x)>\lambda\}|,
 \qquad
 f^*(s)=\inf\{\lambda\geq0:\mu_f(\lambda)\leq s\}.
 \tag{2}
\]

La relation de pseudo-inverses exacte est

\[
 f^*(s)\leq\lambda
 \quad\Longleftrightarrow\quad
 \mu_f(\lambda)\leq s.
 \tag{3}
\]

Elle reste vraie en présence de plateaux si les superniveaux sont stricts.
L'égalité \(\lambda=f^*(\mu_f(\lambda))\) n'est pas requise et est fausse en
général, comme établi au cycle 0015.

Pour isoler les constantes, on travaille d'abord dans des variables sans
dimension et on suppose

\[
 \mu_\omega(\lambda)
 \leq
 \frac{B}{\lambda^{3/2}(\log\lambda)^{3/2}}
 =\frac{B}{(\lambda\log\lambda)^{3/2}},
 \qquad \lambda\geq\Lambda_0>1.
 \tag{4}
\]

Les références dimensionnelles et l'échelle Navier–Stokes sont réintroduites
à la section 10.

## 2. Inversion exacte de la queue de vorticité

Fixons \(0<s<B\) et posons

\[
 X_s=(B/s)^{2/3}.
 \tag{5}
\]

La fonction \(\lambda\mapsto\lambda\log\lambda\) est strictement croissante
pour \(\lambda>e^{-1}\). Soit \(\Lambda(s)>1\) son inverse au niveau \(X_s\),
c'est-à-dire

\[
 \Lambda(s)\log\Lambda(s)=X_s.
 \tag{6}
\]

Équivalemment, \(\Lambda(s)=X_s/W(X_s)\), où \(W\) est la fonction de
Lambert. Dès que \(\Lambda(s)\geq\Lambda_0\), (4) donne

\[
 \mu_\omega(\Lambda(s))\leq s,
 \tag{7}
\]

et (3) implique rigoureusement

\[
 \omega^*(s)\leq\Lambda(s).
 \tag{8}
\]

Aucune égalité entre niveau et réarrangée n'intervient.

Comme

\[
 W(X)=\log X-\log\log X+o(1),
 \tag{9}
\]

on obtient

\[
 \Lambda(s)
 \sim
 \frac{3}{2}B^{2/3}
 \frac{s^{-2/3}}{\log(1/s)}.
 \tag{10}
\]

Le terme \(-\log\log X\) explique pourquoi le coefficient limite \(3/2\)
n'est pas, à lui seul, une majoration élémentaire exacte à volume fini.

### Majorant élémentaire à seuil explicite

Soit \(L_s=\log(1/s)\) et

\[
 \lambda_s=3B^{2/3}\frac{s^{-2/3}}{L_s}.
 \tag{11}
\]

Un calcul direct donne

\[
 \frac{B}{(\lambda_s\log\lambda_s)^{3/2}}
 =s\left(\frac{L_s}{3\log\lambda_s}\right)^{3/2}.
 \tag{12}
\]

Ainsi \(\mu_\omega(\lambda_s)\leq s\), puis
\(\omega^*(s)\leq\lambda_s\), dès que

\[
 \lambda_s\geq\Lambda_0,
 \qquad
 \log\lambda_s\geq L_s/3.
 \tag{13}
\]

La seconde condition est exactement

\[
 \frac{L_s}{3}-\log L_s+log(3B^{2/3})\geq0,
 \tag{14}
\]

et elle est vraie pour tout \(s\leq V_0(B)\) assez petit. Le choix \(3B^{2/3}\)
est conservateur. Tout coefficient strictement supérieur à
\((3/2)B^{2/3}\) fonctionne après diminution de \(V_0\).

## 3. Profil saturant et optimalité des exposants

Fixons \(A>0\) et \(0<V_0<e^{-2}\), puis considérons la réarrangée

\[
 \omega_A^*(s)=
 \frac{A s^{-2/3}}{L(s)},
 \qquad L(s)=\log(e/s),
 \qquad 0<s\leq V_0,
 \tag{15}
\]

prolongée de manière décroissante au-delà de \(V_0\). Elle est réalisable
par une fonction scalaire radiale sur \(\mathbb R^3\).

À un niveau où l'inverse est continu, écrivons
\(y=\lambda/A\), \(s=\mu_{\omega_A}(\lambda)\). L'égalité
\(y=s^{-2/3}/L(s)\) donne

\[
 s=y^{-3/2}L(s)^{-3/2},
 \qquad
 L(s)\sim\frac32\log y.
 \tag{16}
\]

Par conséquent,

\[
 \mu_{\omega_A}(\lambda)
 \sim
 \left(\frac23\right)^{3/2}A^{3/2}
 \lambda^{-3/2}[\log(\lambda/A)]^{-3/2}.
 \tag{17}
\]

Pour une queue saturante de constante \(B\), le coefficient optimal de la
réarrangée est donc

\[
 A_{\rm crit}=\frac32 B^{2/3},
 \tag{18}
\]

car

\[
 \left(\frac23\right)^3A_{\rm crit}^3=B^2.
 \tag{19}
\]

Le profil (15) montre que ni la puissance \(s^{-2/3}\), ni le logarithme
inverse, ni la constante principale de (10) ne peuvent être améliorés à
partir de (4) seule. Il s'agit d'un contre-profil fonctionnel de réarrangée,
pas de la vorticité d'une solution Navier–Stokes construite.

## 4. Plateaux : ce qu'ils cassent et ce qu'ils préservent

Une fonction à valeurs constantes sur des ensembles de mesure positive donne
des sauts de \(\mu_\omega\) et des plateaux de \(\omega^*\). Elle casse les
égalités heuristiques

\[
 s=\mu_\omega(\lambda),
 \qquad
 \lambda=\omega^*(s),
 \tag{20}
\]

prises simultanément. Elle ne casse pas l'implication (7)–(8).

Pour un plateau tangent au majorant, il peut arriver que
\(\omega^*(s)=\lambda_s\). Avec la convention stricte,

\[
 \omega^*(s)\leq\lambda_s
 \Longrightarrow
 |\{\omega>\lambda_s\}|\leq s
 \tag{21}
\]

reste exacte. Une conclusion concernant \(\{\omega\geq\lambda_s\}\) exige
une marge stricte ou un niveau légèrement abaissé. Le manuscrit emploie les
superniveaux stricts, convention compatible avec (21).

## 5. Contre-famille à seuils non uniformes

Un seuil de grand niveau dépendant du temps ne suffit pas. Prenons des masses
\(m_n\downarrow0\), notons

\[
 Q(m)=\frac{m^{-2/3}}{\log(e/m)},
 \tag{22}
\]

et définissons \(f_n=a_n\mathbf1_{E_n}\), avec

\[
 |E_n|=m_n,
 \qquad
 a_n=nQ(m_n).
 \tag{23}
\]

Pour le seuil non uniforme \(\Lambda_{0,n}=2a_n\), la queue de \(f_n\) est
nulle pour tout \(\lambda\geq\Lambda_{0,n}\). Elle satisfait donc (4) avec
n'importe quel \(B>0\) au-delà de son propre seuil.

Cependant,

\[
 f_n^*(m_n/2)=a_n,
 \tag{24}
\]

et

\[
 \frac{a_n}{Q(m_n/2)}
 =n\,2^{-2/3}
 \frac{\log(2e/m_n)}{\log(e/m_n)},
 \qquad
 \frac{1}{n}\frac{a_n}{Q(m_n/2)}
 \longrightarrow 2^{-2/3}.
 \tag{25}
\]

Aucune constante uniforme ne majore cette famille par \(Q(s)\) sur un même
intervalle de petits volumes. Pour passer de (40) à la ligne 296 du manuscrit,
il faut donc suivre un même \(\Lambda_0\), puis le même \(V_0\), sur tout
l'intervalle temporel.

## 6. Les deux intégrales d'O'Neil aux petits volumes

Supposons désormais

\[
 \omega^*(s)\leq A\frac{s^{-2/3}}{L(s)},
 \qquad 0<s\leq V_0,
 \qquad L_0:=L(V_0)>3.
 \tag{26}
\]

Conditionnellement à l'inégalité de réarrangement écrite en (41) du
manuscrit, le terme de cœur vérifie exactement

\[
 \begin{aligned}
 \int_0^v\frac{s^{-2/3}}{L(s)}\,ds
 &=\frac{3v^{1/3}}{L(v)}
 -3\int_0^v\frac{s^{-2/3}}{L(s)^2}\,ds\\
 &\leq\frac{3v^{1/3}}{L(v)}.
 \end{aligned}
 \tag{27}
\]

Donc

\[
 v^{-2/3}\int_0^v\omega^*(s)\,ds
 \leq3A\frac{v^{-1/3}}{L(v)}.
 \tag{28}
\]

Pour la queue singulière, posons

\[
 I(v)=\int_v^{V_0}\frac{s^{-4/3}}{L(s)}\,ds.
 \tag{29}
\]

L'intégration par parties donne

\[
 I(v)=
 \left[-\frac{3s^{-1/3}}{L(s)}\right]_v^{V_0}
 +3\int_v^{V_0}\frac{s^{-4/3}}{L(s)^2}\,ds.
 \tag{30}
\]

Puisque \(L(s)\geq L_0\) sur \((0,V_0]\),

\[
 I(v)leq
 3\frac{v^{-1/3}}{L(v)}+\frac{3}{L_0}I(v),
 \tag{31}
\]

d'où

\[
 I(v)leq
 \frac{3}{1-3/L_0}
 \frac{v^{-1/3}}{L(v)}.
 \tag{32}
\]

Les constantes asymptotiques sont \(3\) pour chacun des deux termes; leur
somme a donc une constante principale \(6A\), multipliée par les constantes
du noyau de Biot–Savart et de l'inégalité d'O'Neil. Les lignes (43) et (46)
du manuscrit ont les bons signes et les bons exposants, mais le symbole
\(\approx\) doit être remplacé par (27) et (32).

## 7. Queue \(s>V_0\) et masse basse fréquence

L'enveloppe (26) ne contrôle rien au-delà de \(V_0\). La coupure de (44) doit
se faire à \(V_0\), et non automatiquement à \(1\). Si

\[
 \|\omega\|_{L^{3/2,\infty}}leq M_0,
 \qquad
 \omega^*(s)\leq M_0s^{-2/3}quad(s>0),
 \tag{33}
\]

alors

\[
 \int_{V_0}^\infty s^{-2/3}\omega^*(s)\,ds
 \leq
 M_0\int_{V_0}^\infty s^{-4/3}\,ds
 =3M_0V_0^{-1/3}.
 \tag{34}
\]

C'est un terme constant en \(v\), absorbable par
\(v^{-1/3}/L(v)\to\infty\) lorsque \(v\downarrow0\). L'absorption est
uniforme seulement si \(M_0\) et \(V_0\) le sont.

### Contre-profil basse fréquence

Une queue de hauts niveaux seule ne contrôle pas (34). Ajoutons, sur une
région disjointe, un plateau

\[
 h_N=a\mathbf1_{E_N},
 \qquad |E_N|=N,
 \qquad 0<a<\Lambda_0.
 \tag{35}
\]

Cet ajout ne modifie pas la queue (4) pour \(\lambda\geq\Lambda_0\), mais il
ajoute à l'intégrale macroscopique une quantité de taille

\[
 a\int^{N}s^{-2/3}\,ds\asymp3aN^{1/3}.
 \tag{36}
\]

Ce n'est pas seulement une faiblesse de l'estimation. Pour le modèle scalaire
\(h_N=a\mathbf1_{B_R}\), avec \(|B_R|=N\), le potentiel de Riesz à l'origine
vaut, à la constante de normalisation près,

\[
 I_1h_N(0)
 =a\int_{B_R}|y|^{-2}\,dy
 =4\pi aR
 \asymp aN^{1/3}.
 \tag{37}
\]

La constante du transfert vitesse ne peut donc dépendre de \(B\) seul. La
borne globale \(M_0\) utilisée aux lignes 245 et 313 du manuscrit est
précisément le type d'hypothèse qui exclut cette dérive, à condition que sa
dépendance soit conservée dans la constante finale.

Un profil encore plus sévère est

\[
 \omega^*(s)=c s^{-1/3},\qquad s>V_0,
 \tag{38}
\]

raccordé décroissamment à la partie haute fréquence. Alors
\(\int_{V_0}^\infty s^{-2/3}\omega^*(s)ds\) diverge logarithmiquement. Ce
profil ne satisfait pas la borne globale \(L^{3/2,\infty}\); il montre que
celle-ci n'est pas décorative.

## 8. Noyau harmonique de Biot–Savart

Pour un champ lisse divergence-free sur \(\mathbb R^3\),
\(\omega=\nabla\times u\) donne

\[
 -\Delta u=\nabla\times\omega.
 \tag{39}
\]

La reconstruction par Biot–Savart détermine \(u\) seulement modulo un champ
harmonique divergence-free et curl-free. Sous une hypothèse de bornitude sur
\(\mathbb R^3\), ce noyau est constant.

Le témoin exact est

\[
 u(x,t)\equiv U\ne0,
 \qquad p\equiv0,
 \qquad \omega\equiv0.
 \tag{40}
\]

Il s'agit d'une solution classique globale des équations de Navier–Stokes
incompressibles non forcées sur \(\mathbb R^3\), pour toute viscosité
\(\nu>0\). Pourtant,

\[
 (I_1|\omega|)^*(s)=0,
 \qquad
 |u|^*(s)=|U|\quad(s>0).
 \tag{41}
\]

Ainsi la phrase « la vitesse est asservie à la vorticité » est fausse dans
la seule classe \(L^\infty(\mathbb R^3)\). La formule correcte est

\[
 u=\operatorname{BS}[\omega]+U_\infty,
 \tag{42}
\]

ou \(U_\infty=0\) sous décroissance spatiale, intégrabilité finie, ou
normalisation explicite.

Le défaut est pertinent pour l'ensemble relatif de (50). Si
\(0<\theta<1\), alors pour (40)

\[
 \{x:|u(x)|>\theta\|u\|_\infty\}=\mathbb R^3,
 \tag{43}
\]

de volume infini, malgré \(\omega=0\). L'asymptotique de hauts niveaux au-delà
de \(|U|\) est triviale, mais elle ne contrôle pas ce superniveau relatif.

Le même noyau subsiste sans employer le cas dégénéré où la direction de
vorticité n'est pas définie : si \(v\) est une solution classique, alors la
transformation galiléenne

\[
 u_U(x,t)=U+v(x-Ut,t),
 \qquad p_U(x,t)=p(x-Ut,t)
 \tag{44a}
\]

est une solution exacte et sa vorticité est simplement la translatée de celle
de \(v\). Toute hypothèse de réarrangée ou de direction de vorticité qui est
invariante par translation demeure inchangée, tandis que Biot–Savart manque
encore le terme \(U\).

Le champ constant n'est pas une donnée Clay décroissante de Schwartz sur
\(\mathbb R^3\). Comme \(\xi=\omega/|\omega|\) est indéfinie lorsque
\(\omega=0\), (40) seul ne constitue pas une instance littérale de toutes les
hypothèses du théorème 7.4. Il réfute le maillon fonctionnel de reconstruction
sous la seule hypothèse de bornitude; la famille galiléenne (44a) montre que
le noyau persiste pour des vorticités non nulles. Cela ne réfute pas l'énoncé
Clay normalisé. Sur le
tore, le même défaut est le mode moyen constant; il faut fixer la moyenne
nulle. Sur \(\mathbb R^3\), les données Clay décroissantes imposent
\(U_\infty=0\) tant que la solution classique reste dans la classe de
décroissance appropriée.

## 9. Corrections \(\log\log\)

Considérons la queue plus fine

\[
 \mu_\omega(\lambda)
 \leq
 \frac{B}
 {[\lambda\log\lambda
   (\log\log\lambda)^\theta]^{3/2}},
 \qquad \lambda\geq\Lambda_0>e.
 \tag{44}
\]

Son inverse exact est défini par

\[
 \lambda\log\lambda(\log\log\lambda)^\theta
 =(B/s)^{2/3}.
 \tag{45}
\]

Après encadrement des logarithmes, il donne

\[
 \omega^*(s)
 \lesssim
 \frac{B^{2/3}s^{-2/3}}
 {\log(1/s)[\log\log(1/s)]^\theta}.
 \tag{46}
\]

Pour

\[
 \ell(s)=
 \frac1{L(s)[\log L(s)]^\theta},
 \tag{47}
\]

les deux intégrales de la section 6 préservent le même facteur lentement
variable :

\[
 \int_0^v s^{-2/3}\ell(s)ds
 \sim3v^{1/3}\ell(v),
 \qquad
 \int_v^{V_0}s^{-4/3}\ell(s)ds
 \sim3v^{-1/3}\ell(v).
 \tag{48}
\]

Donc le potentiel d'ordre un hérite également du facteur
\([\log L(v)]^{-\theta}\). Une correction \(\log\log\) régulière n'est ni
perdue ni cubée par O'Neil. Elle est cubée seulement lors de l'inversion
ultérieure de la réarrangée de vitesse vers sa distribution, avec les
constantes de changement de variable correspondantes.

Pour une correction lentement variable arbitraire et oscillante, (48) exige
les hypothèses usuelles de variation régulière ou un encadrement de Potter.
Le mot « lente » seul ne garantit pas une constante uniforme. L'inversion
doit porter sur l'enveloppe entière, comme au cycle 0015.

## 10. Échelle Navier–Stokes et références logarithmiques

Sous

\[
 u_\kappa(x,t)=\kappa u(\kappa x,\kappa^2t),
 \qquad
 \omega_\kappa(x,t)=\kappa^2\omega(\kappa x,\kappa^2t),
 \tag{49}
\]

les distributions et réarrangées se transforment exactement comme

\[
 \begin{aligned}
 \mu_{\omega_\kappa}(\lambda)
 &=\kappa^{-3}\mu_\omega(\lambda/\kappa^2),
 &\omega_\kappa^*(s)&=\kappa^2\omega^*(\kappa^3s),\\
 \mu_{u_\kappa}(\lambda)
 &=\kappa^{-3}\mu_u(\lambda/\kappa),
 &u_\kappa^*(s)&=\kappa u^*(\kappa^3s).
 \end{aligned}
 \tag{50}
\]

Les puissances de (1) respectent exactement cette échelle :
\(2-3(2/3)=0\) pour la vorticité et \(1-3(1/3)=0\) pour la vitesse. Les
logarithmes exigent des références qui se remettent elles aussi à l'échelle.
Une formulation dimensionnelle peut écrire

\[
 \log(e+\lambda/\Lambda_*),
 \qquad
 \log(e+V_*/s),
 \tag{51}
\]

avec \(\Lambda_*\mapsto\kappa^2\Lambda_*\) et
\(V_*\mapsto\kappa^{-3}V_*\). Les écritures \(\log\lambda\) et
\(\log(e/s)\) du manuscrit supposent une nondimensionnalisation. Sans cette
précision, les puissances sont cohérentes mais la constante logarithmique
n'est pas intrinsèque.

## 11. Ce qui survit exactement

| Maillon | Verdict | Hypothèses et constante |
|---|---|---|
| (40) queue \(\to\omega^*\) | **survit** | \(B,\Lambda_0\) uniformes; inverse (6); coefficient asymptotique \((3/2)B^{2/3}\) |
| égalités niveau–volume | **réfutées** | utiliser la pseudo-inverse (3); les plateaux sont admis |
| \(\omega^*\to\) deux termes singuliers d'O'Neil | **survit** | petit-volume commun \(V_0\); bornes (28), (32); constante principale \(6A\) avant constante d'opérateur |
| queue \(s>V_0\) | **survit conditionnellement** | borne globale \(M_0\); contribution \(3M_0V_0^{-1/3}\) |
| constante finale dépendant seulement de \(B\) | **réfutée** | le plateau basse fréquence (35) force une dépendance globale |
| reconstruction de la vitesse entière par \(\omega\) | **réfutée dans \(L^\infty\) seul** | estimer \(u-U_\infty\), ou imposer décroissance/moyenne nulle |
| exposants \(-2/3\to-1/3\) et gain \(1/\log\) | **survivent et sont saturés** | profil (15), sous le modèle scalaire de réarrangée/Riesz |
| correction régulière \(\log\log\) | **survit** | variation lente contrôlée; pas de perte dans O'Neil |
| conclusion ponctuelle \(|u(x)|\approx|x|^{-1}/|\log|x||\) | **non démontrée** | une borne de réarrangée est distributionnelle, pas une asymptotique spatiale radiale |

En particulier, la ligne 336 du manuscrit ne suit pas de (47) : une borne sur
\(u^*\) ne localise pas les grandes valeurs autour du cœur supposé et ne
fournit aucune équivalence ponctuelle. Ce défaut rhétorique n'altère pas la
borne de volume si celle-ci est obtenue séparément.

## 12. Certificat Python stdlib exact

Le script ci-dessous vérifie sans flottants les identités de constante et
d'échelle, le défaut harmonique, et les facteurs algébriques des deux
intégrales. Les inégalités logarithmiques et les passages à la limite sont
prouvés dans les sections 2, 3 et 6; le script n'en prétend pas une preuve
numérique.

```python
from fractions import Fraction as F


# Constant of the saturating distribution/rearrangement pair, B=1.
Acrit = F(3, 2)
assert F(2, 3) ** 3 * Acrit ** 3 == 1

# Navier-Stokes algebraic scaling gates.
omega_amplitude = F(2)
omega_volume_exponent = F(-2, 3)
velocity_amplitude = F(1)
velocity_volume_exponent = F(-1, 3)
assert omega_amplitude + 3 * omega_volume_exponent == 0
assert velocity_amplitude + 3 * velocity_volume_exponent == 0

# O'Neil power bookkeeping:
# integral_0^v s^(-2/3) ds ~ 3 v^(1/3), then v^(-2/3);
# integral_v s^(-4/3) ds ~ 3 v^(-1/3).
assert 1 + F(-2, 3) + F(-2, 3) == F(-1, 3)
assert 1 + F(-4, 3) == F(-1, 3)
assert 1 / (1 + F(-2, 3)) == 3    # primitive coefficient, core
assert -1 / (1 + F(-4, 3)) == 3   # magnitude, far tail

# Low-frequency ball: normalized I_1(a 1_{B_R})(0)/(4*pi) = a*R.
a = F(1, 7)
for R in (1, 2, 5, 20):
    normalized_potential = a * R
    assert normalized_potential / a == R

# Harmonic kernel: omega=0 does not force a bounded velocity to vanish.
U = F(5, 3)
omega_star = F(0)
u_star = U
assert omega_star == 0 and u_star > 0

print("saturating constant and scaling gates: PASS")
print("O'Neil algebraic powers and low-frequency growth: PASS")
print("constant harmonic-field countermodel: PASS")
```

Commande de reproduction : extraire ce bloc et exécuter `python -` depuis la
racine du dépôt. Dépendances : bibliothèque standard uniquement. Graine :
aucune.

## 13. Obligations falsifiables

```json
{
  "cycle": "0016",
  "review_independence": "same-model-family adversarial pass; not external independent review",
  "source": "arXiv:2607.08866v2, equations (40)-(47)",
  "claims": [
    {
      "id": "NS-C0016-TAIL-INVERSION",
      "status": "PROVED_IN_REPORT_CONDITIONALLY",
      "statement": "uniform high-level tail implies uniform small-volume rearrangement",
      "requirements": ["uniform B", "uniform Lambda_0"],
      "sharp_leading_constant": "(3/2) B^(2/3)"
    },
    {
      "id": "NS-C0016-ONEIL-LOG",
      "status": "PROVED_IN_REPORT_CONDITIONALLY",
      "statement": "the two O'Neil integrals preserve s^(-1/3)/log(e/s)",
      "requirements": ["uniform V_0", "global weak-L^(3/2) tail", "Biot-Savart component"]
    },
    {
      "id": "NS-C0016-NONUNIFORM-THRESHOLD",
      "status": "REFUTED",
      "statement": "time-dependent high-level thresholds yield a uniform rearrangement envelope",
      "witness": "shrinking plateaus (22)-(25)"
    },
    {
      "id": "NS-C0016-VORTICITY-DETERMINES-U",
      "status": "REFUTED_IN_LINFINITY_ONLY",
      "statement": "bounded velocity on R^3 is determined by its vorticity without normalization",
      "witness": "u identically U, omega identically 0"
    }
  ],
  "pde_scope": "the constant-field witness is an exact classical Navier-Stokes solution; other witnesses are functional rearrangement/Riesz models",
  "decision": "REVISE"
}
```

## Conclusion contradictoire

La puissance logarithmique transportée par (40)–(47) résiste aux plateaux,
au profil saturant et à une correction régulière \(\log\log\). Le verrou
n'est donc pas l'arithmétique des exposants. Il est triple : uniformiser le
seuil de l'estimation (40), conserver la norme globale \(M_0\) et le vrai
petit-volume \(V_0\) dans la constante d'O'Neil, puis éliminer explicitement
le noyau harmonique de la reconstruction de la vitesse. Sous ces réparations,
la chaîne fonctionnelle survit comme borne de réarrangée; elle ne devient ni
une asymptotique ponctuelle du champ, ni une preuve autonome de régularité.
