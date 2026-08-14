# Revue d'analyse de réarrangement — cycle 0015

## Verdict

L'implication entre les équations (47) et (49) de
[arXiv:2607.08866v2](https://arxiv.org/html/2607.08866v2) est
**mathématiquement valide aux grandes amplitudes**, mais la justification
du manuscrit par l'égalité

\[
\lambda=u^*(\mu_u(\lambda))
\tag{1}
\]

n'est pas correcte en présence de plateaux, d'atomes de distribution ou
de valeurs de seuil non atteintes. Le symbole « \(\approx\) » employé dans
l'inversion ne suit pas non plus les constantes.

Une version exacte, uniforme et sans hypothèse de continuité de la
distribution est la suivante. Fixons :

\[
V_0>0
\quad\text{(volume de référence)},\qquad
A>0
\quad\text{(vitesse de référence)},\qquad
0<\theta_0\leq1.
\tag{2}
\]

Supposons que, uniformément pour les temps considérés,

\[
\boxed{
f^*(v)
\leq
A\,
\frac{(V_0/v)^{1/3}}
{\log(eV_0/v)}
\qquad
\text{pour }0<v\leq v_0:=\theta_0V_0.}
\tag{3}
\]

Posons

\[
\Lambda_0
=
A\max\left\{
1,\
\frac{\theta_0^{-1/3}}
{\log(e/\theta_0)}
\right\}.
\tag{4}
\]

Alors, pour tout \(\lambda\geq\Lambda_0\),

\[
\boxed{
\mu_f(\lambda)
\leq
V_0
\frac{(A/\lambda)^3}
{\bigl(1+3\log(\lambda/A)\bigr)^3}.}
\tag{5}
\]

La forme plus proche de l'équation (49) est

\[
\boxed{
\mu_f(\lambda)
\leq
\bigl[\log(e+1)\bigr]^3
\frac{V_0A^3}
{\lambda^3
\log^3(e+\lambda/A)}.}
\tag{6}
\]

Toutes les quantités placées dans les logarithmes sont sans dimension.
Les constantes de (5) sont exactes pour la preuve donnée ci-dessous ;
\(\log^3(e+1)\) dans (6) est le coût explicite du remplacement du
logarithme plus précis de (5).

Ainsi, (47) implique bien une queue

\[
\mu_f(\lambda)
\lesssim
\lambda^{-3}\log^{-3}\lambda
\tag{7}
\]

après fixation des unités et d'un seuil de grande amplitude. La puissance
logarithmique \(3\) est la bonne puissance d'inversion.

Ce rapport n'audite ni la démonstration de (47), ni les estimations de
commutateur, De Giorgi, Biot–Savart, analyticity ou maximum harmonique de
la prépublication. Il valide uniquement le maillon de théorie de la
mesure \((47)\Rightarrow(49)\), sous les hypothèses uniformes explicites
de (3).

## 1. Distribution et réarrangée décroissante

Soit \(f:\mathbb R^3\to\mathbb R^m\) mesurable. Sa fonction de
distribution, avec la convention stricte utilisée pour les superniveaux
du manuscrit, est

\[
\boxed{
\mu_f(\lambda)
=
\left|
\{x\in\mathbb R^3:|f(x)|>\lambda\}
\right|,
\qquad \lambda\geq0.}
\tag{8}
\]

Sa réarrangée décroissante est définie, pour \(v>0\), par l'inverse
généralisé

\[
\boxed{
f^*(v)
=
\inf\{
\lambda\geq0:\mu_f(\lambda)\leq v
\},}
\tag{9}
\]

avec \(\inf\varnothing=+\infty\).

La fonction \(\mu_f\) est décroissante et continue à droite. En effet, si
\(\lambda_n\downarrow\lambda\), alors

\[
\{|f|>\lambda_n\}\uparrow\{|f|>\lambda\},
\tag{10}
\]

et la continuité monotone de la mesure donne

\[
\mu_f(\lambda_n)\longrightarrow\mu_f(\lambda).
\tag{11}
\]

La propriété d'inversion robuste est

\[
\boxed{
f^*(v)>\lambda
\quad\Longleftrightarrow\quad
\mu_f(\lambda)>v.}
\tag{12}
\]

Pour l'implication de droite à gauche, la continuité à droite est
essentielle. Si \(\mu_f(\lambda)>v\), il existe
\(\varepsilon>0\) tel que

\[
\mu_f(\lambda+\varepsilon)>v.
\tag{13}
\]

Tous les seuils inférieurs ou égaux à \(\lambda+\varepsilon\) ont donc
une distribution supérieure à \(v\), et
\(f^*(v)\geq\lambda+\varepsilon>\lambda\). La réciproque suit directement
de (9).

Une conséquence équivalente est l'identité d'équirépartition

\[
\boxed{
\mu_f(\lambda)
=
\left|
\{v>0:f^*(v)>\lambda\}
\right|.}
\tag{14}
\]

Cette convention traite exactement les plateaux.

## 2. Plateaux et atomes

Considérons

\[
|f|=a
\quad\text{sur un ensemble de mesure }m,
\qquad
f=0\quad\text{ailleurs},
\tag{15}
\]

avec \(a,m>0\). Alors

\[
\mu_f(\lambda)
=
\begin{cases}
m,&0\leq\lambda<a,\\
0,&\lambda\geq a,
\end{cases}
\tag{16}
\]

tandis que

\[
f^*(v)
=
\begin{cases}
a,&0<v<m,\\
0,&v\geq m,
\end{cases}
\tag{17}
\]

pour la convention (9). D'autres conventions de réarrangement peuvent
modifier seulement cette valeur de bord, sans modifier (12)–(14).

Au seuil \(\lambda=a\),

\[
\mu_f(a)=0,
\tag{18}
\]

alors que \(f^*\) possède un plateau entier de valeur \(a\). L'expression
\(f^*(\mu_f(a))\) fait intervenir \(f^*(0)\), qui n'est même pas définie
par (9). Cet exemple réfute (1) comme identité générale.

La bonne procédure est :

\[
0<v<\mu_f(\lambda)
\stackrel{(12)}{\Longrightarrow}
\lambda<f^*(v),
\tag{19}
\]

puis faire tendre \(v\) vers \(\mu_f(\lambda)\) par valeurs inférieures.
Les atomes et plateaux ne produisent alors aucune erreur.

## 3. Lemme quantitatif uniforme

### Énoncé

Soit \(I\) un intervalle de temps et
\((f_t)_{t\in I}\) une famille mesurable. Supposons que les mêmes
constantes \(V_0,A,\theta_0\) satisfassent (3) pour tout \(t\in I\).
Alors (5) et (6) valent pour tout \(t\in I\) et tout
\(\lambda\geq\Lambda_0\), avec les mêmes constantes.

Ni la continuité de \(f_t\), ni la stricte décroissance de
\(\mu_{f_t}\), ni l'absence d'atomes ne sont requises.

### Étape 1 : entrer dans le régime de petit volume

Au bord \(v_0=\theta_0V_0\), (3) donne

\[
f_t^*(v_0)
\leq
A\frac{\theta_0^{-1/3}}
{\log(e/\theta_0)}
\leq\Lambda_0.
\tag{20}
\]

Pour \(\lambda\geq\Lambda_0\), (12) implique

\[
\mu_{f_t}(\lambda)\leq v_0.
\tag{21}
\]

Cette étape est indispensable. Une estimation de \(f^*(v)\) disponible
seulement pour \(v\leq v_0\) ne peut être inversée avant d'avoir démontré
que le superniveau considéré a lui-même un volume inférieur à \(v_0\).

### Étape 2 : passage sans égalité au volume du superniveau

Fixons \(t\) et \(\lambda\geq\Lambda_0\), et posons

\[
m=\mu_{f_t}(\lambda).
\tag{22}
\]

Si \(m=0\), (5) est immédiate. Supposons \(m>0\). Pour tout
\(0<v<m\), (19) et (3) donnent

\[
\lambda
<
A
\frac{(V_0/v)^{1/3}}
{\log(eV_0/v)}.
\tag{23}
\]

Le membre droit est continu en \(v>0\). En faisant tendre
\(v\uparrow m\), on obtient

\[
\lambda
\leq
A
\frac{(V_0/m)^{1/3}}
{\log(eV_0/m)}.
\tag{24}
\]

Aucune valeur de \(f^*\) au point \(m\) n'est utilisée.

### Étape 3 : inversion algébrique

Introduisons les variables sans dimension

\[
y=\frac{\lambda}{A}\geq1,
\qquad
z=\frac{m}{V_0}\leq\theta_0\leq1,
\qquad
L(z)=\log(e/z)=1+\log(1/z).
\tag{25}
\]

L'inégalité (24) devient

\[
y\leq\frac{z^{-1/3}}{L(z)}.
\tag{26}
\]

Elle implique d'abord

\[
z
\leq
\frac1{y^3L(z)^3}.
\tag{27}
\]

Comme \(L(z)\geq1\), (26) donne également

\[
z^{-1}\geq y^3.
\tag{28}
\]

Par conséquent,

\[
L(z)
=1+\log(1/z)
\geq1+3\log y.
\tag{29}
\]

L'injection de (29) dans (27) donne

\[
z
\leq
\frac1{
y^3(1+3\log y)^3}.
\tag{30}
\]

En revenant à \(m,\lambda,A,V_0\), (30) est exactement (5).

## 4. Passage à la forme Lorentz–Zygmund usuelle

Posons

\[
c_E=\log(e+1).
\tag{31}
\]

Pour \(y\geq1\),

\[
\begin{aligned}
\log(e+y)
&\leq\log((e+1)y)\\
&=c_E+\log y\\
&\leq c_E(1+3\log y).
\end{aligned}
\tag{32}
\]

Donc

\[
1+3\log y
\geq
\frac1{c_E}\log(e+y).
\tag{33}
\]

En remplaçant le dénominateur de (5) par celui de (33), on obtient (6)
avec la constante exacte

\[
c_E^3=[\log(e+1)]^3.
\tag{34}
\]

Pour \(\lambda\geq eA\), une autre forme est

\[
\boxed{
\mu_f(\lambda)
\leq
\frac{V_0A^3}
{27\lambda^3\log^3(\lambda/A)}.}
\tag{35}
\]

La constante \(1/27\) vient de

\[
1+3\log(\lambda/A)
\geq3\log(\lambda/A).
\tag{36}
\]

L'écriture informelle

\[
\lambda^{-3}(\log\lambda)^{-3}
\tag{37}
\]

doit toujours être comprise comme (6) ou (35), après choix d'une unité de
vitesse.

## 5. Relation avec la constante de l'équation (47)

Supposons que l'équation (47) soit écrite sous la forme dimensionnellement
correcte

\[
f^*(v)
\leq
C_R
\frac{v^{-1/3}}
{\log(eV_0/v)},
\qquad 0<v\leq\theta_0V_0,
\tag{38}
\]

où \(C_R\) a la dimension

\[
[C_R]=[\text{vitesse}]\,[\text{volume}]^{1/3}.
\tag{39}
\]

Alors (3) correspond à

\[
A=C_RV_0^{-1/3}.
\tag{40}
\]

La conclusion précise (5) devient

\[
\boxed{
\mu_f(\lambda)
\leq
\frac{C_R^3}
{\lambda^3
\left[
1+3\log\left(
\frac{\lambda V_0^{1/3}}{C_R}
\right)
\right]^3}.}
\tag{41}
\]

La forme régularisée est

\[
\boxed{
\mu_f(\lambda)
\leq
[\log(e+1)]^3
\frac{C_R^3}
{\lambda^3
\log^3\left(
e+\frac{\lambda V_0^{1/3}}{C_R}
\right)}.}
\tag{42}
\]

Les deux quotients à l'intérieur des logarithmes sont sans dimension.

## 6. Seuil de petit volume

Le seuil (4) contient deux contraintes distinctes :

\[
\lambda\geq A
\tag{43}
\]

pour avoir \(y\geq1\), et

\[
\lambda
\geq
A\frac{\theta_0^{-1/3}}
{\log(e/\theta_0)}
\tag{44}
\]

pour forcer \(\mu_f(\lambda)\leq v_0\).

Le seuil ne peut être supprimé si (3) n'est connu que pour les petits
volumes. Une borne uniforme en temps exige donc :

\[
\exists A,V_0,\theta_0>0
\quad
\forall t\in I
\quad
\forall v\in(0,\theta_0V_0]
\quad
\text{l'inégalité (3).}
\tag{45}
\]

L'énoncé plus faible

\[
\forall t\in I\quad
\exists\theta(t)>0
\quad
\text{tel que (3) vaut pour }v\leq\theta(t)V_0
\tag{46}
\]

ne fournit pas un seuil d'amplitude uniforme si
\(\inf_{t\in I}\theta(t)=0\).

De même, une constante \(A(t)\) non bornée ne produit ni
\(\Lambda_0\), ni constante de queue uniformes.

## 7. Optimalité de la puissance logarithmique

La puissance \(3\) n'est pas un artefact du majorant. Pour
\(0<z\leq\theta_0<e^{-2}\), posons formellement

\[
g^*(zV_0)
=
A\frac{z^{-1/3}}{1+\log(1/z)}.
\tag{47}
\]

Sur cet intervalle, cette enveloppe est décroissante en \(v=zV_0\) et
peut être réalisée comme la réarrangée d'une fonction mesurable sur un
espace non atomique.

Posons \(s=z^{-1/3}\). Le niveau \(y=g^*/A\) vérifie

\[
y=\frac{s}{1+3\log s}.
\tag{48}
\]

Lorsque \(y\to\infty\),

\[
s\sim3y\log y,
\tag{49}
\]

et donc

\[
z=s^{-3}
\sim
\frac1{27y^3\log^3y}.
\tag{50}
\]

Une hypothèse de la seule force de (3) ne peut donc produire
uniformément une puissance logarithmique strictement supérieure à \(3\).
Le profil modèle sature l'ordre de (35).

## 8. Loi d'échelle

Pour \(\alpha,\kappa>0\), définissons

\[
f_{\alpha,\kappa}(x)=\alpha f(\kappa x).
\tag{51}
\]

En dimension trois,

\[
\boxed{
\mu_{f_{\alpha,\kappa}}(\lambda)
=
\kappa^{-3}
\mu_f(\lambda/\alpha),}
\tag{52}
\]

et

\[
\boxed{
f_{\alpha,\kappa}^*(v)
=
\alpha f^*(\kappa^3v).}
\tag{53}
\]

Pour préserver la forme dimensionless de (3), les références doivent se
transformer selon

\[
V_0'=\kappa^{-3}V_0,
\qquad
A'=\alpha A,
\qquad
\theta_0'=\theta_0.
\tag{54}
\]

Alors

\[
\frac{v}{V_0'}
=
\frac{\kappa^3v}{V_0},
\qquad
\frac{\lambda}{A'}
=
\frac{\lambda/\alpha}{A},
\tag{55}
\]

et les lemmes (3)–(6) sont exactement covariants.

Sous l'échelle Navier–Stokes

\[
u_\kappa(x,t)
=
\kappa u(\kappa x,\kappa^2t),
\tag{56}
\]

on a \(\alpha=\kappa\). Les volumes sont multipliés par
\(\kappa^{-3}\), les niveaux de vitesse par \(\kappa\), et les références
doivent suivre (54).

Dans la paramétrisation (38), la constante

\[
C_R=AV_0^{1/3}
\tag{56a}
\]

est invariante sous ce scaling :

\[
C_R'
=(\kappa A)(\kappa^{-3}V_0)^{1/3}
=C_R.
\tag{56b}
\]

Le rapport dimensionless
\(\lambda V_0^{1/3}/C_R\) est lui aussi invariant lorsque le niveau
\(\lambda\) est multiplié par \(\kappa\), tandis que le préfacteur
\(C_R^3/\lambda^3\) est multiplié par \(\kappa^{-3}\), exactement comme
la fonction de distribution.

Si \(A\) et \(V_0\) sont maintenus comme références physiques fixes, le
logarithme change sous scaling. C'est précisément une rupture
subcritique de la loi critique \(L^{3,\infty}\), mais elle doit être
énoncée relativement à ces références fixes. On ne peut simultanément
laisser les unités implicites et réclamer une constante universelle
invariante d'échelle.

## 9. Application exacte à l'équation (49)

La source est Z. Grujić,
[*Logarithmic Depletion of Vortex Stretching and Singularity Evasion in
the 3D Navier–Stokes Equations*,
arXiv:2607.08866v2](https://arxiv.org/html/2607.08866v2),
prépublication de 2026.

L'équation (47) affirme, uniformément sur l'intervalle temporel étudié,

\[
u^*(v,t)
\leq
C v^{-1/3}\log^{-1}(e/v)
\tag{57}
\]

pour les petits \(v\). Après introduction de \(V_0\) et identification
de \(A\) par (38)–(40), le lemme donne

\[
\sup_t
\left|
\{x:|u(x,t)|>\beta\}
\right|
\leq
[\log(e+1)]^3
\frac{V_0A^3}
{\beta^3
\log^3(e+\beta/A)}
\tag{58}
\]

pour

\[
\beta\geq\Lambda_0.
\tag{59}
\]

Cette conclusion est une version quantitative, uniforme et
dimensionnellement correcte de l'équation (49).

Le manuscrit utilise ensuite une fraction relative fixe
\(\lambda_{\mathrm{rel}}\in(0,1)\) et le niveau

\[
\beta
=
\lambda_{\mathrm{rel}}
\|u(t)\|_\infty.
\tag{60}
\]

Il faut distinguer ce paramètre sans dimension
\(\lambda_{\mathrm{rel}}\) du niveau dimensionné \(\beta\). Si
\(\beta\geq\Lambda_0\), (58) donne

\[
\boxed{
|V_t|
\leq
[\log(e+1)]^3
\frac{V_0A^3}
{\lambda_{\mathrm{rel}}^3
\|u(t)\|_\infty^3
\log^3\left(
e+
\frac{\lambda_{\mathrm{rel}}\|u(t)\|_\infty}{A}
\right)}.}
\tag{61}
\]

Cette formule justifie la structure du majorant global employé à
l'équation (55), sous réserve que \(V_0,A,\theta_0\) soient uniformes en
temps.

## 10. Quantificateurs et passe contradictoire

1. **Égalité inverse.** L'identité
   \(\beta=u^*(\mu_u(\beta))\) est fausse en général. Seule (12), puis la
   limite \(v\uparrow\mu_u(\beta)\), est robuste.
2. **Plateaux.** Un atome de distribution peut faire chuter
   \(\mu_u\) brutalement. La convention stricte \(>\) doit rester la même
   dans (8), (9), (14) et les superniveaux \(V_t\).
3. **Seuil petit volume.** « Pour \(v\) petit » doit signifier
   \(0<v\leq\theta_0V_0\) avec \(\theta_0\) indépendant du temps.
4. **Entrée dans le régime.** Il faut l'étape (20)–(21) avant de
   substituer le volume d'un superniveau dans (3).
5. **Constante temporelle.** Une borne \(C(t)\) ou un seuil
   \(\theta(t)\) dégénérant près de \(T^*\) détruit l'uniformité de (49).
6. **Logarithme dimensionné.** Ni \(\log(e/v)\) pour un volume physique,
   ni \(\log\beta\) pour une vitesse physique ne sont définis sans
   références \(V_0,A\).
7. **Petites amplitudes.** (49) ne suit pas de (47) pour tous les niveaux.
   Le niveau relatif (60) doit franchir \(\Lambda_0\).
8. **Notation conflictuelle.** La lettre \(\lambda\) désigne tour à tour
   un niveau de réarrangement et une fraction relative. La distinction
   \(\beta\) contre \(\lambda_{\mathrm{rel}}\) est obligatoire dans le
   calcul des constantes.
9. **Asymptotique contre inégalité.** Les phrases « à l'ordre dominant »
   et « logarithme lentement variable » ne donnent pas une borne uniforme.
   Les étapes (26)–(33) les remplacent par des inégalités.
10. **Scaling.** Garder la même expression logarithmique après
    \(u\mapsto u_\kappa\) exige soit de transformer les références, soit
    de suivre la variation de la constante.
11. **Volume total infini.** La définition (9) reste valable sur
    \(\mathbb R^3\), mais l'hypothèse (3) est seulement locale dans la
    variable de volume. La finitude des grands superniveaux est obtenue
    par (20)–(21), pas supposée silencieusement.
12. **Reste de la PDE.** Cet audit part de (47). Il ne démontre pas que
    Navier–Stokes, les hypothèses de la prépublication ou les estimations
    antérieures produisent effectivement (47).

## Conclusion

**Résultat positif borné.** Le lemme (3)–(6) prouve rigoureusement
l'implication

\[
u^*(v)
\lesssim
v^{-1/3}\log^{-1}(1/v)
\quad\Longrightarrow\quad
\mu_u(\lambda)
\lesssim
\lambda^{-3}\log^{-3}\lambda
\tag{62}
\]

aux petits volumes et grandes amplitudes, avec seuil, références,
constantes et uniformité entièrement explicités.

**Correction requise dans le manuscrit.** Remplacer l'égalité informelle
\(\lambda=u^*(v)\) à \(v=\mu_u(\lambda)\) par (19), faire tendre
\(v\uparrow\mu_u(\lambda)\), et annoncer un seuil uniforme
\(\Lambda_0\). Remplacer les logarithmes dimensionnés par

\[
\log(eV_0/v)
\quad\text{et}\quad
\log(e+\lambda/A).
\tag{63}
\]

**Statut de \((47)\Rightarrow(49)\) : PROUVÉ CONDITIONNELLEMENT À (47).**
La puissance \(3\) et la loi d'échelle sont cohérentes. Les autres maillons
de la prépublication, et donc toute conclusion de régularité
Navier–Stokes, restent **NON VALIDÉS** par cette passe.

**État : CONTINUER.** Le prochain verrou est l'uniformité réelle de la
constante \(C\) et du seuil « small \(v\) » dans (47), puis la validité
indépendante de la convolution de réarrangements qui produit (47).
