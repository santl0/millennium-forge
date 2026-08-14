# Revue d'analyse PDE — cycle 0012

## Verdict

Une condition de Cauchy imposée à un temps fini et une trace asymptotique imposée à
\(\tau=-\infty\) ne sont pas des données interchangeables.

Sur \(\mathbb R^3\), pour Navier–Stokes incompressible, deux solutions ayant la même
donnée à un temps fini \(t_0\) coïncident sur leur intervalle commun **vers le
futur** dès que l'une d'elles appartient à une classe de Serrin stricte. Le
coefficient de Grönwall est alors intégrable. En particulier, deux solutions de
Leray–Hopf issues de la même donnée lisse ne peuvent se séparer avant la perte de
la solution forte maximale.

Cette conclusion ne s'applique pas à une famille de branches qui vérifie seulement

\[
\Phi_c(\tau)\longrightarrow0
\qquad(\tau\to-\infty).
\tag{1}
\]

Le contre-modèle exact

\[
x'=ax-x^2,\qquad
x_C(\tau)=\frac{a}{1+Ce^{-a\tau}},
\qquad a>0,\ C>0,
\tag{2}
\]

possède un continuum de trajectoires globales ayant toutes la trace passée nulle,
mais des états distincts à chaque temps fini. Après \(t=e^\tau\), elles vérifient

\[
tX'=aX-X^2,\qquad
X_C(t)=\frac{at^a}{t^a+C},\quad t>0,
\tag{3}
\]

et s'étendent toutes continûment par \(X_C(0)=0\). Le champ
\((aX-X^2)/t\) est localement Lipschitz en \(X\) pour tout \(t>0\), mais sa
constante de Lipschitz est de taille \(1/t\), non intégrable à \(0\). Il n'y a
donc aucune contradiction avec l'unicité de Cauchy à temps fini.

Le premier maillon de raccord vers le problème Clay est ainsi négatif : la
multiplicité de branches partageant une trace singulière à \(t=0\), ou une trace
similaire à \(\tau=-\infty\), ne transmet pas une multiplicité pour une donnée
initiale lisse fixée. Une telle transmission exigerait d'abord une perte de la
classe forte, ou un théorème nouveau de sélection non unique après cette perte.

## 1. Équation, domaine et notions de solution

Le cadre de ce rapport est

\[
\partial_tu-\nu\Delta u+\mathbb P(u\cdot\nabla u)=0,
\qquad
\nabla\cdot u=0,
\qquad
(x,t)\in\mathbb R^3\times[t_0,T],
\qquad \nu>0,
\tag{4}
\]

sans force et sans frontière. Ici \(\mathbb P\) est la projection de Leray.
Les comparaisons ci-dessous exigent le même domaine, la même viscosité et la
même force ; une différence de force produirait un terme supplémentaire et
invaliderait l'énoncé d'unicité.

Une solution de Leray–Hopf \(v\) appartient à

\[
v\in L^\infty(t_0,T;L^2_\sigma)
\cap L^2(t_0,T;\dot H^1_\sigma),
\tag{5}
\]

est faiblement continue à valeurs dans \(L^2_\sigma\), satisfait (4) au sens
des distributions et l'inégalité d'énergie. Une solution de Serrin stricte
\(u\) est ici une solution assez régulière pour l'identité relative et telle que

\[
u\in L^s(t_0,T;L^q),
\qquad
3<q\leq\infty,
\qquad
\frac2s+\frac3q=1.
\tag{6}
\]

Pour \(q<\infty\),

\[
s=\frac{2q}{q-3}.
\tag{7}
\]

Le cas endpoint \(L^\infty_tL^3_x\) n'est volontairement pas inclus : sa
régularité est un théorème plus profond et ne résulte pas de l'estimation
d'énergie élémentaire utilisée ici.

Sous l'échelle de Navier–Stokes

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\tag{8}
\]

on a

\[
\|u_\lambda\|_{L^s_tL^q_x}
=\lambda^{1-3/q-2/s}\|u\|_{L^s_tL^q_x}.
\tag{9}
\]

La relation (6) est donc critique. En revanche,
\(\|u_\lambda(t)\|_2=\lambda^{-1/2}\|u(\lambda^2t)\|_2\) :
l'énergie est supercritique par rapport au contrôle des petites échelles.

## 2. Lemme d'unicité à temps de Cauchy fini

### Énoncé borné

Soient \(u\) et \(v\) des solutions de (4) sur \([t_0,T]\), avec

\[
u(t_0)=v(t_0)=a\in L^2_\sigma(\mathbb R^3).
\tag{10}
\]

Supposons \(v\) de Leray–Hopf et \(u\) dans la classe (6). Alors

\[
u=v
\quad\text{sur }[t_0,T].
\tag{11}
\]

Plus généralement, si les données diffèrent, la différence satisfait

\[
\|v(t)-u(t)\|_2^2
\leq
\|v(t_0)-u(t_0)\|_2^2
\exp\!\left(
C_{q,\nu}\int_{t_0}^{t}\|u(r)\|_q^s\,dr
\right),
\tag{12}
\]

où \(C_{q,\nu}\) est indépendant de \(t\), de \(u\) et de \(v\).
Pour \(q<\infty\), on peut suivre la dépendance

\[
C_{q,\nu}
=C_q\nu^{-(q+3)/(q-3)}.
\tag{13}
\]

La conclusion porte sur le futur commun à partir de \(t_0\). Cette dérivation
ne prouve pas qu'une égalité découverte à un temps terminal se propage vers le
passé ; une telle assertion demanderait un résultat distinct de backward
uniqueness.

### Dérivation

Posons \(w=v-u\). L'inégalité d'énergie relative donne

\[
\frac12\|w(t)\|_2^2
+\nu\int_{t_0}^{t}\|\nabla w(r)\|_2^2\,dr
\leq
\frac12\|w(t_0)\|_2^2
-\int_{t_0}^{t}\!\int_{\mathbb R^3}
(w\cdot\nabla)u\cdot w\,dx\,dr.
\tag{14}
\]

Le transport par le champ divergence-free s'annule. La pression s'annule
également contre \(w\) : elle est soit éliminée par \(\mathbb P\), orthogonale
dans \(L^2_\sigma\), soit intégrée contre \(\nabla\cdot w=0\). Cette annulation
ne rend pas la pression locale ; elle utilise seulement la structure globale
divergence-free et les intégrabilités autorisant l'intégration par parties.

Pour \(3<q<\infty\),

\[
\begin{aligned}
\left|\int(w\cdot\nabla)u\cdot w\right|
&=
\left|\int(w\cdot\nabla)w\cdot u\right|\\
&\leq
\|u\|_q
\|w\|_{2q/(q-2)}
\|\nabla w\|_2.
\end{aligned}
\tag{15}
\]

L'inégalité de Gagliardo–Nirenberg donne

\[
\|w\|_{2q/(q-2)}
\leq C_q
\|w\|_2^{1-3/q}
\|\nabla w\|_2^{3/q}.
\tag{16}
\]

Young, avec les exposants

\[
\frac{2q}{q+3}
\quad\text{et}\quad
\frac{2q}{q-3}=s,
\tag{17}
\]

donne alors

\[
\left|\int(w\cdot\nabla)u\cdot w\right|
\leq
\frac{\nu}{2}\|\nabla w\|_2^2
+C_q\nu^{-(q+3)/(q-3)}
\|u\|_q^s\|w\|_2^2.
\tag{18}
\]

Le cas \(q=\infty,\ s=2\) suit directement de

\[
\left|\int(w\cdot\nabla)w\cdot u\right|
\leq
\|u\|_\infty\|w\|_2\|\nabla w\|_2.
\tag{19}
\]

En absorbant le gradient dans (14), puis en appliquant Grönwall, on obtient
(12). L'intégrale du coefficient est finie par (6), et (10) impose
\(w=0\). Il s'agit du mécanisme classique d'unicité faible–forte, reproduit
ici avec son coefficient critique.

## 3. Version locale dans une classe forte

Pour \(m>5/2\), \(H^m(\mathbb R^3)\) s'injecte dans
\(W^{1,\infty}(\mathbb R^3)\). La non-linéarité projetée vérifie

\[
\left\|
\mathbb P(u\cdot\nabla u-v\cdot\nabla v)
\right\|_{H^{m-1}}
\leq
C_m\bigl(\|u\|_{H^m}+\|v\|_{H^m}\bigr)
\|u-v\|_{H^m}.
\tag{20}
\]

Elle est donc localement Lipschitz de \(H^m_\sigma\) vers
\(H^{m-1}_\sigma\). Combinée au lissage du semi-groupe de chaleur, cette
estimation donne l'existence et l'unicité locales dans

\[
C([t_0,T];H^m_\sigma)
\cap L^2(t_0,T;H^{m+1}_\sigma).
\tag{21}
\]

Le quantificateur exact est

\[
\forall a\in H^m_\sigma,\quad
\exists T(a)>t_0,\quad
\exists!\ u_a
\text{ solution forte maximale sur }[t_0,T^*(a)).
\tag{22}
\]

Pour une famille \(a_\varepsilon\), (22) donne seulement

\[
\forall\varepsilon,\ \exists T_\varepsilon>t_0.
\tag{23}
\]

Il ne donne pas

\[
\exists T>t_0,\ \forall\varepsilon,\ T_\varepsilon\geq T.
\tag{24}
\]

Une désingularisation peut faire diverger
\(\|a_\varepsilon\|_{H^m}\), et les bornes de durée d'existence locale
peuvent alors tendre vers zéro.

Corollaire utile : si deux solutions de Leray–Hopf issues d'une même donnée
lisse se distinguent à un temps \(t_1\), la solution forte maximale issue de
cette donnée ne peut pas couvrir tout \([t_0,t_1]\). Sinon (11) les
identifierait toutes deux à cette solution forte. Ce corollaire est une
obstruction logique ; il ne démontre pas qu'une perte de régularité se produit.

## 4. Contre-modèle scalaire exact

Considérons l'équation autonome localement Lipschitz

\[
x'=F(x),\qquad F(x)=ax-x^2,\qquad a>0.
\tag{25}
\]

Pour \(C\in\mathbb R\), tant que le dénominateur ne s'annule pas,

\[
x_C(\tau)=\frac{a}{1+Ce^{-a\tau}}.
\tag{26}
\]

Une dérivation directe donne

\[
x_C'(\tau)
=\frac{a^2Ce^{-a\tau}}{(1+Ce^{-a\tau})^2}
=ax_C(\tau)-x_C(\tau)^2.
\tag{27}
\]

### Signes et domaines maximaux

- Si \(C>0\), \(x_C\) est globale sur \(\mathbb R\),
  \(0<x_C(\tau)<a\), et
  \[
  \lim_{\tau\to-\infty}x_C(\tau)=0,
  \qquad
  \lim_{\tau\to+\infty}x_C(\tau)=a.
  \tag{28}
  \]
  À \(\tau=0\),
  \[
  x_C(0)=\frac{a}{1+C}.
  \tag{29}
  \]
  Lorsque \(C\) parcourt \((0,\infty)\), ces états parcourent
  \((0,a)\).
- La solution \(x\equiv0\) partage la même trace passée ; elle correspond
  formellement à \(C=\infty\), mais n'est pas contenue dans la
  paramétrisation par \(C\) fini.
- Si \(C=0\), (26) est l'équilibre \(x\equiv a\), qui n'a pas la trace
  passée nulle.
- Si \(C<0\), le pôle est
  \[
  \tau_*(C)=\frac1a\log(-C).
  \tag{30}
  \]
  Le domaine maximal de la branche passée est
  \((-\infty,\tau_*)\). Sur cette branche,
  \(x_C(\tau)<0\),
  \(x_C(\tau)\to0^-\) lorsque \(\tau\to-\infty\), et
  \(x_C(\tau)\to-\infty\) lorsque \(\tau\uparrow\tau_*\).
  La seconde branche maximale, sur \((\tau_*,\infty)\), part de
  \(+\infty\) et tend vers \(a\).

Pour \(C,D>0\), la différence exacte est

\[
x_C(\tau)-x_D(\tau)
=
\frac{a(D-C)e^{-a\tau}}
{(1+Ce^{-a\tau})(1+De^{-a\tau})}.
\tag{31}
\]

Elle vérifie

\[
(x_C-x_D)'
=\bigl[a-(x_C+x_D)\bigr](x_C-x_D).
\tag{32}
\]

Si \(x_C(\tau_0)=x_D(\tau_0)\) à un temps fini, alors (31) impose
\(C=D\). Cela concorde avec l'unicité de Cauchy de l'ODE. En revanche,

\[
x_C(\tau)\sim\frac aC e^{a\tau}
\qquad(\tau\to-\infty),
\tag{33}
\]

donc toutes les trajectoires \(C>0\) convergent vers le même équilibre passé
sans être identiques.

Les quantificateurs incompatibles sont

\[
\forall C>0,\quad
\lim_{\tau\to-\infty}x_C(\tau)=0,
\tag{34}
\]

et

\[
\exists\tau_0>-\infty,\quad
\forall C>0,\quad x_C(\tau_0)=0.
\tag{35}
\]

La première proposition est vraie ; la seconde est fausse.

## 5. Où échoue exactement Grönwall à \(-\infty\)

Pour \(z=x_C-x_D\), (32) donne sur \([-R,\tau]\)

\[
|z(\tau)|
\leq
|z(-R)|
\exp\bigl(a(\tau+R)\bigr).
\tag{36}
\]

Or (31) donne

\[
|z(-R)|
\sim
\frac{a|D-C|}{CD}e^{-aR}
\qquad(R\to\infty).
\tag{37}
\]

Le produit du défaut initial par l'amplification satisfait donc

\[
|z(-R)|e^{a(\tau+R)}
\longrightarrow
\frac{a|D-C|}{CD}e^{a\tau},
\tag{38}
\]

qui n'est pas nul. Pour \(y=|z|^2\), le même calcul remplace \(a\) par
\(2a\) dans l'exponentielle et \(e^{-aR}\) par \(e^{-2aR}\) dans la
donnée : la compensation est identique.

En général, une estimation

\[
y(\tau)\leq
y(-R)\exp\!\left(\int_{-R}^{\tau}L(s)\,ds\right)
\tag{39}
\]

ne permet d'envoyer \(R\) vers l'infini que si

\[
y(-R)\exp\!\left(\int_{-R}^{\tau}L(s)\,ds\right)
\longrightarrow0.
\tag{40}
\]

La seule convergence \(y(-R)\to0\) ne suffit pas. La limite et le facteur
de stabilité ne peuvent pas être séparés.

### Temps physique

Avec \(t=e^\tau\), (26) devient

\[
X_C(t)=x_C(\log t)
=\frac{at^a}{t^a+C},
\qquad t>0.
\tag{41}
\]

Elle satisfait exactement

\[
tX_C'(t)=aX_C(t)-X_C(t)^2.
\tag{42}
\]

Pour chaque \(\delta>0\), le champ

\[
G(t,X)=\frac{aX-X^2}{t}
\tag{43}
\]

est localement Lipschitz en \(X\) sur \([\delta,T]\). Près de \(X=0\),
sa constante de Lipschitz est asymptotique à \(a/t\), et

\[
\int_0^\delta\frac a t\,dt=\infty.
\tag{44}
\]

Toutes les solutions \(C>0\) s'étendent continûment par \(X_C(0)=0\),
mais (43) n'est pas une équation de Cauchy régulière à \(t=0\). La
multiplicité ne réfute donc aucun théorème de Picard–Lindelöf à temps fini.

## 6. Dictionnaire avec les branches de similarité

La source primaire récente considérée est T. Hou, Y. Wang et C. Yang,
[*Nonuniqueness of Leray–Hopf solutions to the unforced incompressible 3D
Navier–Stokes Equation*,
arXiv:2509.25116v2](https://arxiv.org/html/2509.25116v2), version révisée
du 19 mars 2026.

Dans leurs variables

\[
\xi=\frac{x}{\sqrt t},
\qquad
\tau=\log t,
\qquad
u(t,x)=t^{-1/2}V(\xi,\tau),
\tag{45}
\]

le temps initial physique \(t=0\) correspond à la frontière
\(\tau=-\infty\), pas à un instant fini du flot autonome en similarité.
Leurs coordonnées instables sont prescrites à un temps similaire fini puis
intégrées vers le passé ; leurs corrections décroissent à
\(\tau=-\infty\). Cette architecture est logiquement du type (34), et non
du type (10).

Le dictionnaire exact et ses limites sont les suivants.

1. **Trace commune.** La donnée HWY est une trace \(L^2\) singulière au
   point spatial critique, pas une donnée \(H^m\), \(m>5/2\). Une trace
   forte dans \(L^2\) ne suffit pas à déclencher l'unicité faible–forte.
2. **Lissage pour \(t>0\).** Les branches sont régulières pour tout temps
   strictement positif dans l'intervalle construit. À un temps
   \(\delta>0\), elles portent toutefois des états de Cauchy différents.
   L'unicité à partir de \(\delta\) propage chaque état ; elle ne les
   identifie pas.
3. **Coefficient critique.** Pour un profil auto-similaire non nul,
   \[
   \|u(t)\|_q
   =t^{-1/2+3/(2q)}\|U\|_q
   =t^{-1/s}\|U\|_q.
   \tag{46}
   \]
   Par conséquent,
   \[
   \int_0^{t_1}\|u(t)\|_q^s\,dt
   =\|U\|_q^s\int_0^{t_1}\frac{dt}{t}
   =\infty.
   \tag{47}
   \]
   La divergence est logarithmique et exactement critique. Le coefficient
   de Grönwall de (12) n'est donc pas intégrable depuis \(t=0\).
4. **Donnée lisse fixée.** Si une régularisation
   \(a_\varepsilon\in H^m_\sigma\) est fixée, elle produit une unique
   solution forte maximale \(u_\varepsilon\). Toute solution de
   Leray–Hopf ayant exactement la même donnée coïncide avec
   \(u_\varepsilon\) sur \([0,T_\varepsilon^*)\).
5. **Sélection de limites.** Des familles de données lisses
   \(a_{\varepsilon,c}\) distinctes peuvent converger vers la même donnée
   singulière et sélectionner des limites faibles distinctes. Cela
   démontrerait une instabilité ou une non-unicité de sélection de la trace
   singulière, pas deux solutions pour une donnée lisse Clay unique.
6. **Temps uniforme.** L'existence d'un temps
   \(T_\varepsilon^*>0\) pour chaque régularisation n'apporte aucune borne
   uniforme en \(\varepsilon\). Le passage au continuum doit suivre les
   normes fortes et le coefficient de (12), pas seulement la convergence
   \(L^2\) des données.

Le contre-modèle (25) ne modélise ni la pression ni les interactions
fréquentielles de Navier–Stokes. Il certifie uniquement le défaut logique
de l'implication « même limite à \(-\infty\) donc même trajectoire ».

## 7. Lemme de raccord falsifiable

### Lemme

Soit \(a_\varepsilon\in H^m_\sigma(\mathbb R^3)\), \(m>5/2\), une donnée
fixée, et soit \(u_\varepsilon\) sa solution forte maximale de (4).
Si \(v_{\varepsilon,1}\) et \(v_{\varepsilon,2}\) sont deux solutions de
Leray–Hopf de même donnée \(a_\varepsilon\), alors

\[
v_{\varepsilon,1}
=u_\varepsilon
=v_{\varepsilon,2}
\qquad\text{sur }[0,T_\varepsilon^*).
\tag{48}
\]

En conséquence, une famille de branches construites depuis une trace à
\(\tau=-\infty\) ne peut fournir deux solutions pour cette donnée lisse
fixée par la seule convergence de sa trace. Si les deux solutions
Leray–Hopf se séparent à un temps fini, leur séparation ne peut précéder
la perte de la solution forte maximale.

### Test décisif

Toute prétention de transfert depuis les branches HWY vers une donnée Clay
lisse fixée doit produire au moins l'un des objets suivants :

1. deux solutions de Leray–Hopf ayant **exactement le même**
   \(a_\varepsilon\), avec une première séparation à
   \(t\geq T_\varepsilon^*\) ;
2. une preuve que \(T_\varepsilon^*<\infty\), donc un blow-up de la
   solution forte maximale ;
3. un mécanisme de prolongement faible non unique après
   \(T_\varepsilon^*\), compatible avec l'inégalité d'énergie.

Une simple convergence

\[
a_{\varepsilon,c}\to a_0
\quad\text{dans }L^2
\tag{49}
\]

avec \(a_{\varepsilon,c}\) dépendant de \(c\), ou une convergence de
profils à \(\tau=-\infty\), échoue ce test.

## 8. Passe contradictoire

1. **Temps initial contre frontière asymptotique.** Aucun
   \(\tau_0>-\infty\) commun n'est fourni par la limite (1).
2. **Convergence contre taux stable.** Dans Grönwall, il faut (40), pas
   seulement \(y(-R)\to0\). Le contre-modèle sature exactement la perte.
3. **Donnée lisse contre trace \(L^2\) singulière.** La continuité forte
   dans \(L^2\) au temps zéro ne place pas la solution dans une classe
   Serrin.
4. **Régularité pour \(t>0\) contre régularité au bord.** Être lisse sur
   chaque \([\delta,T]\) ne fournit aucune borne uniforme lorsque
   \(\delta\downarrow0\).
5. **Même limite contre même donnée.** Deux suites de données différentes
   peuvent avoir la même limite. L'unicité de Cauchy compare des données
   égales, pas seulement convergentes.
6. **Quantificateur uniforme.** \(\forall\varepsilon\,\exists
   T_\varepsilon\) n'implique pas \(\exists T\,\forall\varepsilon\).
7. **Endpoint caché.** L'argument d'énergie ne couvre pas
   \(L^\infty_tL^3_x\) ; cet endpoint ne doit pas être introduit
   silencieusement.
8. **Sens temporel.** (12) prouve l'unicité en avant. Aucune unicité
   rétrograde de Navier–Stokes n'est utilisée.
9. **Pression.** Son annulation dans l'énergie dépend de
   l'incompressibilité et de la projection globale ; elle ne permet pas
   de localiser la dynamique des branches.
10. **Force et domaine.** Le résultat ne compare pas des solutions de
    viscosités, forces, domaines ou conditions aux limites différents.
11. **ODE contre PDE.** La logistique est un contre-exemple à une
    implication abstraite sur les traces asymptotiques. Elle n'est ni une
    solution de Navier–Stokes, ni une preuve de non-unicité PDE.
12. **Non-unicité faible contre blow-up classique.** Même une
    non-unicité de Leray–Hopf pour une donnée singulière ne produit pas un
    blow-up depuis une donnée lisse.

## Conclusion

**Résultat positif borné.** Le lemme (48) est établi par l'estimation
critique (14)–(18) : à un temps fini, l'unicité faible–forte ferme dès que
le coefficient de Serrin est intégrable.

**Résultat négatif.** Le continuum logistique (26) montre exactement
qu'une trace commune à \(\tau=-\infty\) ne détermine pas une trajectoire.
Le changement \(t=e^\tau\) identifie l'obstacle : la constante de
Lipschitz devient non intégrable au bord \(t=0\).

**Écart avec Clay.** La construction HWY concerne une donnée initiale
\(L^2\) singulière et des branches de Leray–Hopf. Elle ne fournit ni deux
solutions classiques issues d'une même donnée lisse, ni une perte de
régularité de la solution forte maximale. Toute désingularisation conserve
donc un verrou préalable : démontrer \(T_\varepsilon^*<\infty\), ou
construire un raccord non unique après cette perte.

**État : ABANDONNER** l'implication directe « multiplicité à
\(\tau=-\infty\) \(\Rightarrow\) multiplicité de Cauchy lisse ».
Conserver le lemme (48) comme test adverse obligatoire. Le prochain verrou
informatif est de quantifier, pour une famille de désingularisations, la
durée forte \(T_\varepsilon^*\) et la divergence éventuelle du coefficient
critique de Serrin ; sans cette perte uniforme, aucune branche multiple ne
peut émerger pour une donnée fixée.
