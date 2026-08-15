# Cycle 0047 — dérenormalisation exacte du drift parabolique

Date d'audit : 2026-08-15.

## Verdict

Considérons l'équation renormalisée incompressible

\[
\partial_sZ-\Delta_yZ+(Z\cdot\nabla_y)Z+\nabla_y\Pi
+\kappa(1+y\cdot\nabla_y)Z=\mathcal F,
\qquad
\nabla_y\cdot Z=0,
\]

avec \(\kappa>0\). Le changement de variables

\[
r(s)=e^{-\kappa s},
\qquad
\tau(s)=\frac{1-r(s)^2}{2\kappa},
\qquad
x=r(s)y,
\]

\[
v(\tau,x)=r(s)^{-1}Z(s,y),
\qquad
q(\tau,x)=r(s)^{-2}\Pi(s,y)
\]

donne exactement

\[
\partial_\tau v-\Delta_xv+(v\cdot\nabla_x)v+\nabla_xq
=r^{-3}\mathcal F,
\qquad
\nabla_x\cdot v=0.
\]

En particulier, lorsque \(\mathcal F=0\), on retrouve Navier–Stokes standard non forcé. Le jacobien espace–temps est

\[
dx\,d\tau=r^5\,dy\,ds.
\]

Les puissances \(r^{-1}\) pour la vitesse, \(r^{-2}\) pour la pression, \(r^2\) pour l'horloge et le signe négatif dans \(r_s/r=-\kappa\) sont chacun nécessaires. Le certificat produit un résidu symbolique non nul dès que l'un d'eux est modifié.

Ce rapport vérifie une identité de chaîne pour des champs assez réguliers. Il ne construit pas la limite renormalisée, ne justifie aucun passage distributionnel et ne prouve pas que la solution dérenormalisée appartient à une classe Clay admissible.

## Horloge

On a

\[
\frac{r_s}{r}=-\kappa.
\]

Comme

\[
\tau=\frac{1-r^2}{2\kappa},
\]

\[
\frac{d\tau}{ds}
=-\frac{2rr_s}{2\kappa}
=r^2.
\]

L'identité inverse est

\[
r^2=1-2\kappa\tau.
\]

Avec la normalisation \(s=0\leftrightarrow\tau=0\), la limite \(s\to+\infty\) correspond au temps terminal

\[
\tau_*=\frac1{2\kappa}.
\]

Lorsque \(s\to-\infty\), \(\tau\to-\infty\). La transformation couvre donc \((-\infty,\tau_*)\), sous réserve que \(Z\) soit défini pour tout \(s\in\mathbb R\). Dans l'application réelle du cycle, \(Z\) est seulement utilisé pour \(s\le0\) : la même formule donne alors exactement \((-\infty,0]\), avec \(s=0\leftrightarrow\tau=0\).

## Règle de chaîne exacte

À \(x\) fixé,

\[
y=\frac{x}{r(s)}
\]

vérifie

\[
\partial_sy=-\frac{r_s}{r}y=\kappa y.
\]

De plus,

\[
\partial_s(r^{-1})=\kappa r^{-1}.
\]

Ainsi

\[
\left.\partial_sv\right|_x
=r^{-1}
\left[
\partial_sZ+\kappa(1+y\cdot\nabla_y)Z
\right].
\]

Puisque \(\tau_s=r^2\),

\[
\boxed{
\partial_\tau v
=r^{-3}
\left[
\partial_sZ+\kappa(1+y\cdot\nabla_y)Z
\right].}
\]

Les termes spatiaux satisfont séparément

\[
\Delta_xv=r^{-3}\Delta_yZ,
\]

\[
(v\cdot\nabla_x)v
=r^{-3}(Z\cdot\nabla_y)Z,
\]

\[
\nabla_xq=r^{-3}\nabla_y\Pi.
\]

Tous les termes possèdent donc le même facteur \(r^{-3}\), et le drift est absorbé exactement dans la dérivée temporelle.

## Divergence et jacobien

Comme \(\nabla_x=r^{-1}\nabla_y\),

\[
\boxed{
\nabla_x\cdot v
=r^{-2}\nabla_y\cdot Z.}
\]

La divergence nulle est donc préservée.

À temps fixé,

\[
dx=r^3dy.
\]

L'horloge donne

\[
d\tau=r^2ds.
\]

Par conséquent,

\[
\boxed{
dx\,d\tau=r^5dy\,ds.}
\]

Omettre le facteur temporel remplacerait fautivement \(r^5\) par \(r^3\).

## Énergie locale et quantité critique

La boule \(B_R\) en variables \(y\) correspond à \(B_{rR}\) en variables \(x\). On a

\[
\boxed{
\int_{B_{rR}}|v(\tau,x)|^2\,dx
=r\int_{B_R}|Z(s,y)|^2\,dy.}
\]

L'énergie locale normalisée par le rayon est invariante :

\[
\boxed{
\frac1{rR}\int_{B_{rR}}|v|^2\,dx
=\frac1R\int_{B_R}|Z|^2\,dy.}
\]

Pour la norme forte critique,

\[
\int_{B_{rR}}|v|^3\,dx
=\int_{B_R}|Z|^3\,dy.
\]

La fonction de distribution vérifie

\[
|\{x\in B_{rR}:|v(x)|>\lambda\}|
=r^3
|\{y\in B_R:|Z(y)|>r\lambda\}|.
\]

En posant \(\alpha=r\lambda\),

\[
\lambda^3r^3=\alpha^3.
\]

Ainsi

\[
\boxed{
K_3(v(\tau);B_{rR})
=K_3(Z(s);B_R).}
\]

La capture critique est conservée exactement, mais sur une boule physique dont le rayon varie avec le temps.

Pour l'inégalité d'énergie locale, posons (E_Z=|Z|^2/2) et

\[
\mathcal L_Z=
\partial_sE_Z-\Delta E_Z+|\nabla Z|^2
+\operatorname{div}((E_Z+\Pi)Z)
+\kappa\operatorname{div}(yE_Z)-\kappa E_Z.
\]

En dimension trois,

\[
\kappa\operatorname{div}(yE_Z)-\kappa E_Z
=\kappa(2E_Z+y\cdot\nabla E_Z),
\]

qui est exactement le terme supplémentaire produit par la dérivée de
(E_v=r^{-2}E_Z) à (x) fixé. Par conséquent,

\[
\boxed{\mathcal L_v=r^{-4}\mathcal L_Z.}
\]

Comme (dx\,d\tau=r^5dy\,ds), un test physique non négatif
(\phi(x,\tau)) se relève en

\[
r(s)\phi(r(s)y,\tau(s)),
\]

encore non négatif. Cette identité certifie le transfert distributionnel de
l'inégalité locale dès que les termes sont localement intégrables ; elle ne
fournit pas ces intégrabilités à elle seule.

## Pourquoi les exposants sont forcés

Écrivons plus généralement

\[
v=r^{-a}Z,
\qquad
q=r^{-b}\Pi,
\qquad
\tau_s=r^c.
\]

Les quatre puissances des termes physiques sont :

| terme | puissance de \(r\) |
|---|---:|
| \(\partial_\tau v\) | \(-a-c\) |
| \(\Delta v\) | \(-a-2\) |
| \((v\cdot\nabla)v\) | \(-2a-1\) |
| \(\nabla q\) | \(-b-1\) |

Les égaler à une puissance commune impose successivement

\[
a=1,\qquad b=2,\qquad c=2,
\]

et la puissance commune vaut \(-3\).

Avec l'horloge et le signe corrects mais des puissances arbitraires \(a,b\), factoriser \(r^{-a-2}\) laisse le résidu

\[
\boxed{
\kappa(a-1)Z
+(r^{1-a}-1)(Z\cdot\nabla)Z
+(r^{a+1-b}-1)\nabla\Pi.}
\]

Il s'annule identiquement pour tout champ seulement lorsque \(a=1\) et \(b=2\).

Les lois locales deviennent, pour une vitesse \(r^{-a}Z\),

\[
\frac1{rR}\int_{B_{rR}}|v|^2
=r^{2-2a}
\frac1R\int_{B_R}|Z|^2,
\]

\[
\int_{B_{rR}}|v|^3
=r^{3-3a}
\int_{B_R}|Z|^3,
\]

\[
K_3(v;B_{rR})
=r^{1-a}K_3(Z;B_R).
\]

Les trois invariances sélectionnent encore \(a=1\).

## Tests adverses

### 1. Mauvais signe de l'échelle

Si l'on prend

\[
r_s/r=+\kappa
\]

tout en conservant le drift renormalisé \(+\kappa D\), où

\[
D=1+y\cdot\nabla,
\]

la chaîne temporelle contient \(-\kappa D\) au lieu de \(+\kappa D\). Après utilisation de l'équation renormalisée, le résidu est

\[
\boxed{
-2\kappa r^{-3}DZ.}
\]

Il n'est pas annulé par un changement de pression.

### 2. Mauvais signe dans la PDE renormalisée

Si l'échelle correcte \(r_s/r=-\kappa\) est utilisée mais que la PDE contient le drift \(-\kappa DZ\), la chaîne ajoute toujours \(+\kappa DZ\). Le résidu devient

\[
\boxed{
+2\kappa r^{-3}DZ.}
\]

Les deux erreurs de signe sont distinctes et donnent des résidus opposés.

### 3. Vitesse sans facteur \(r^{-1}\)

Prenons \(a=0\) et ajustons \(b=1\) afin que la pression garde au moins la même puissance que le terme temporel factorisé. Le résidu, après factorisation de \(r^{-2}\), vaut

\[
\boxed{
-\kappa Z+(r-1)(Z\cdot\nabla)Z.}
\]

Il est non nul pour \(r\ne1\). Même en supprimant la non-linéarité, le terme \(-\kappa Z\) subsiste.

### 4. Mauvaise puissance de pression

Avec la bonne vitesse \(a=1\) mais \(b=1\),

\[
\boxed{
r^{-3}(r-1)\nabla\Pi}
\]

reste dans l'équation physique.

Avec \(b=3\), le coefficient devient

\[
\boxed{
r^{-3}(r^{-1}-1)\nabla\Pi.}
\]

Ces deux résidus s'annulent uniquement au temps de normalisation \(r=1\), pas sur un intervalle.

### 5. Horloge physique gelée

Gardons \(r_s/r=-\kappa\), mais prenons fautivement

\[
\tau=s,
\qquad \tau_s=1.
\]

Le terme temporel a alors la puissance \(r^{-1}\), tandis que diffusion, convection et pression ont la puissance \(r^{-3}\). Après substitution de la PDE renormalisée, le résidu est

\[
\boxed{
r^{-3}(r^2-1)
\left[
\partial_sZ+\kappa DZ
\right].}
\]

Pour \(0<r<1\), le coefficient \(r^2-1\) est strictement négatif.

Si l'on gèle également le rayon à \(r\equiv1\), aucune dérivée de chaîne ne génère le drift. Le résidu est alors directement

\[
\boxed{
-\kappa DZ.}
\]

Une identité correcte au seul instant \(r=1\) ne constitue donc pas une dérenormalisation.

## Portée PDE et Clay

Le certificat montre :

1. l'équivalence algébrique des équations classiques sous le changement exact ;
2. le transfert d'une force par \(\mathcal F\mapsto r^{-3}\mathcal F\) ;
3. la préservation de la divergence, de l'énergie locale normalisée et de \(K_3\) ;
4. les résidus précis produits par cinq erreurs de convention.

Il ne montre pas :

- que \(Z\) existe sur tout \(s\in\mathbb R\) ;
- que \(Z,\Pi\) ont la régularité nécessaire à la chaîne classique ;
- que l'identité passe à une limite faible ou adaptée ;
- que l'énergie locale ou la pression satisfont les conditions d'admissibilité au temps terminal ;
- que \(v\) possède une trace à \(\tau_*\) ;
- que la solution dérenormalisée est non triviale ou appartient à une classe de rigidité connue.

Dans une application Clay, ces points doivent être prouvés séparément. L'identité de scaling ne convertit pas à elle seule une limite renormalisée en solution ancienne admissible.

## Reproduction

~~~powershell
python -B experiments/navier-stokes/derenormalization/derenormalization_audit.py
~~~

Le script utilise uniquement la bibliothèque standard et fractions.Fraction. Il vérifie l'horloge sur des valeurs rationnelles de \(r,\kappa\), résout exhaustivement les contraintes d'exposants sur une grille entière, certifie les jacobiens et invariances locales, puis évalue exactement chaque coefficient résiduel fautif.

Statut : **CONTINUER**. Le prochain verrou est analytique : faire passer cette identité à la limite dans la classe faible/adaptée effectivement obtenue, avec pression, énergie locale et trace terminale suivies.
