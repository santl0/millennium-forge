# Cycle 0052 — identité de flux en temps de base

Date : 2026-08-15.

Statut : AI_INTERNAL_DERIVATION; audit analytique indépendant, sans
simulation et sans conclusion Clay.

## Verdict

Fixons \(r<T\) et \(a>0\). Dans le cadre exact des cycles 0048--0051,

\[
 g_{s,r}=v(r)-S(r-s)v(s),\qquad
 G_a(s;r)=S(a)g_{s,r},\qquad
 E_a(s;r)=\|G_a(s;r)\|_2^2,                               \tag{1}
\]

pour \(s<r\). Alors

\[
 G_a(\cdot;r)\in
 AC_{\rm loc}((-\infty,r];L^2_\sigma),\qquad
 E_a(\cdot;r)\in AC_{\rm loc}((-\infty,r]),               \tag{2}
\]

et, pour presque tout \(s<r\),

\[
 \boxed{
 \partial_sG_a(s;r)
 =
 S(a+r-s)\mathbb P\operatorname{div}(v\otimes v)(s).}     \tag{3}
\]

Par conséquent,

\[
 \boxed{
 \partial_sE_a(s;r)
 =
 -2\int_{\mathbb R^3}
 (v\otimes v)(s):
 \nabla S(a+r-s)G_a(s;r)\,dx.}                            \tag{4}
\]

Comme

\[
 S(a+r-s)G_a(s;r)
 =S(2a+r-s)g_{s,r},                                       \tag{5}
\]

le lissage effectif du test dans le flux est \(2a+r-s\), et non
\(a+r-s\). Le facteur \(2\) de (4), le signe négatif et le second \(a\)
sont tous indispensables.

Définissons le flux orienté vers le temps terminal par

\[
 \Phi_a(s;r)
 :=
 2\int_{\mathbb R^3}
 (v\otimes v)(s):
 \nabla S(a+r-s)G_a(s;r)\,dx.                             \tag{6}
\]

Alors

\[
 \boxed{
 E_a(s;r)=\int_s^r\Phi_a(\sigma;r)\,d\sigma,}              \tag{7}
\]

parce que \(E_a(r;r)=0\), et, pour \(s_0<s_1<r\),

\[
 E_a(s_0;r)-E_a(s_1;r)
 =\int_{s_0}^{s_1}\Phi_a(\sigma;r)\,d\sigma.               \tag{8}
\]

La densité \(\Phi_a\) n'a pas de signe connu. Seule sa primitive complète
jusqu'à \(r\) est non négative, puisqu'elle égale une énergie.

Le critère infrarouge du cycle 0051 devient donc exactement

\[
\boxed{
\begin{aligned}
 \liminf_{s\to-\infty}\|g_{s,r}\|_2<\infty
 &\Longleftrightarrow
 \liminf_{s\to-\infty}
 \int_s^r\Phi_a(\sigma;r)\,d\sigma<\infty,\\
 \sup_{s<r}\|g_{s,r}\|_2<\infty
 &\Longleftrightarrow
 \sup_{s<r}
 \int_s^r\Phi_a(\sigma;r)\,d\sigma<\infty.
\end{aligned}}                                             \tag{9}
\]

Le quantificateur minimal pour la première ligne est

\[
 \exists s_n\to-\infty,\qquad
 \sup_n\int_{s_n}^r\Phi_a(\sigma;r)\,d\sigma<\infty.       \tag{10}
\]

Il ne demande ni convergence de l'intégrale impropre, ni intégrabilité
absolue de \(\Phi_a\), ni borne pour tous les temps de base.

Les hypothèses actuelles donnent seulement

\[
 |\Phi_a(s;r)|
 \le C M^2(a+r-s)^{-3/4}E_a(s;r)^{1/2},                  \tag{11}
\]

puis

\[
 E_a(s;r)^{1/2}
 \le CM^2\left[
 (a+r-s)^{1/4}-a^{1/4}\right].                            \tag{12}
\]

Le majorant absolu de (11) est d'ordre
\(M^4(a+r-s)^{-1/2}\) dans le passé; il n'est pas intégrable sur
\((-\infty,r)\). L'identité isole donc un verrou signé réel, mais ne le
ferme pas.

**Verdict conservateur : CONTINUER.** (3)--(10) sont exactes. La prochaine
étape doit obtenir une cancellation de la primitive signée \(\Phi_a\), pas
majorer son module. Aucun signe coercif du flux, aucune uniformité ancienne
et aucune rigidité Navier--Stokes ne sont démontrés.

## 1. Hypothèses exactes

Le domaine est \(\mathbb R^3\), la viscosité vaut un, la force extérieure
est nulle et il n'y a pas de frontière. La paire \((v,q)\) est une solution
ancienne faible adaptée locale de

\[
 \partial_tv-\Delta v+\operatorname{div}(v\otimes v)+\nabla q=0,
 \qquad \operatorname{div}v=0,                            \tag{13}
\]

avec pression globale

\[
 q=\mathcal R_i\mathcal R_j(v_iv_j),\qquad
 \sup_{\tau<T}\|v(\tau)\|_{L^{3,\infty}}\le M.            \tag{14}
\]

Le représentant temporel est celui du cycle 0048 :

\[
 v\in C_{w^*}((-\infty,T);L^{3,\infty}_\sigma).           \tag{15}
\]

Ainsi \(v(s)\) est défini à tout temps. Le correcteur satisfait, sur chaque
bande finie,

\[
 g_{s,r}\in L^2_\sigma\cap L^{3,\infty}_\sigma,\qquad
 \|g_{s,r}\|_2\le C_DM^2(r-s)^{1/4}.                      \tag{16}
\]

La globalisation BSS du cycle 0049 fournit en plus la dissipation sur chaque
bande. Elle n'est pas nécessaire pour différencier \(E_a\) : le lissage
strict \(a>0\), Duhamel et la borne du stress suffisent.

Posons

\[
 F=v\otimes v,\qquad
 \|F(\tau)\|_{3/2,\infty}\le C_OM^2.                      \tag{17}
\]

La jauge globale de pression autorise l'équation projetée

\[
 \partial_tv-\Delta v+\mathbb P\operatorname{div}F=0      \tag{18}
\]

dans les distributions tempérées et la formule de Duhamel faible-étoile.

## 2. Duhamel lissé et absolue continuité

Le cycle 0048 donne

\[
 g_{s,r}
 =-\int_s^r
 S(r-\tau)\mathbb P\operatorname{div}F(\tau)\,d\tau.      \tag{19}
\]

Après application de \(S(a)\),

\[
 \boxed{
 G_a(s;r)
 =-\int_s^r
 S(a+r-\tau)\mathbb P\operatorname{div}F(\tau)\,d\tau.}   \tag{20}
\]

Pour \(h>0\), le noyau de
\(S(h)\mathbb P\operatorname{div}\) vérifie

\[
 \|S(h)\mathbb P\operatorname{div}H\|_2
 \le C h^{-3/4}\|H\|_{3/2,\infty}.                        \tag{21}
\]

La puissance est la somme d'une demi-dérivée temporelle et du gain
\(L^{3/2,\infty}\to L^2\) :

\[
 \frac12+
 \frac32\left(\frac{2}{3}-\frac12\right)
 =\frac34.                                                \tag{22}
\]

Sur tout intervalle fini \(s\in[s_0,r]\), le paramètre du semi-groupe dans
(20) est au moins \(a\). L'intégrande est donc borné dans \(L^2\) par
\(CM^2a^{-3/4}\). Il est faiblement mesurable à valeurs dans le séparable
\(L^2\), puis fortement mesurable par Pettis. L'intégrale de (20) est une
intégrale de Bochner dans \(L^2\).

Le théorème fondamental des intégrales de Bochner donne

\[
 \partial_sG_a(s;r)
 =
 S(a+r-s)\mathbb P\operatorname{div}F(s)                  \tag{23}
\]

pour presque tout \(s\), avec le **signe positif** : la dérivée de
\(-\int_s^r\) est la valeur de l'intégrande au bord inférieur.
Il donne aussi

\[
 G_a\in W^{1,1}([s_0,r];L^2)
 \subset AC([s_0,r];L^2).                                 \tag{24}
\]

Comme \(s_0\) est arbitraire, (2) suit. On ne prétend pas que

\[
 G_a\in W^{1,1}((-\infty,r);L^2),                         \tag{25}
\]

car
\(\int_{-\infty}^r(a+r-s)^{-3/4}ds=\infty\).

Cette dérivation évite de différencier directement la trajectoire
faible-étoile \(v(s)\). Le calcul formel donne néanmoins le même signe :

\[
\begin{aligned}
 \frac d{ds}[S(r-s)v(s)]
 &=S(r-s)(\partial_sv-\Delta v)(s)\\
 &=-S(r-s)\mathbb P\operatorname{div}F(s),                \tag{26}
\end{aligned}
\]

donc \(\partial_sg_{s,r}\) est positif devant le terme projeté.

Au temps \(s=r\), \(G_a(r;r)=0\). La dérivée ponctuelle à \(r\) n'est pas
revendiquée, car \(F(r)\) n'a pas nécessairement un représentant fort en
temps; toutes les identités différentielles sont presque partout.

## 3. Dérivée de l'énergie et signe

Dans un espace de Hilbert, le carré de la norme d'une fonction absolument
continue est absolument continu. Ainsi

\[
 \partial_sE_a(s;r)
 =2\langle G_a(s;r),\partial_sG_a(s;r)\rangle_{L^2}       \tag{27}
\]

presque partout. En insérant (23),

\[
 \partial_sE_a(s;r)
 =2\left\langle
 G_a(s;r),
 S(a+r-s)\mathbb P\operatorname{div}F(s)
 \right\rangle.                                           \tag{28}
\]

Le semi-groupe et la projection de Leray sont auto-adjoints et commutent.
Le champ \(G_a\) est solénoïdal. En posant \(h=a+r-s\),

\[
\begin{aligned}
 \left\langle G_a,S(h)\mathbb P\operatorname{div}F\right\rangle
 &=\left\langle S(h)G_a,\mathbb P\operatorname{div}F\right\rangle\\
 &=\left\langle S(h)G_a,\operatorname{div}F\right\rangle\\
 &=-\int_{\mathbb R^3}F:\nabla S(h)G_a\,dx.               \tag{29}
\end{aligned}
\]

Le dernier signe est celui de l'intégration par parties de la divergence.
Les deux signes ne s'annulent pas : (23) est positif, (29) est négatif, ce
qui donne (4).

La quantité testée dans (29) est

\[
 S(h)G_a
 =S(a+r-s)S(a)g_{s,r}
 =S(2a+r-s)g_{s,r}.                                       \tag{30}
\]

Écrire \(S(a+r-s)g_{s,r}\) perdrait un facteur calorifique \(S(a)\) issu de
la définition quadratique de \(E_a\).

## 4. Justification de l'intégration spatiale et pression

Le lissage \(h=a+r-s>0\) donne

\[
 \|\nabla S(h)G_a(s;r)\|_{L^{3,1}}
 \le C h^{-3/4}\|G_a(s;r)\|_2.                            \tag{31}
\]

En effet, le noyau gradient appartient à \(L^{6/5,1}\), puisque

\[
 \frac12+\frac{5}{6}=1+\frac13,                           \tag{32}
\]

et sa norme a la puissance

\[
 h^{-2+3/(2(6/5))}=h^{-3/4}.                              \tag{33}
\]

La dualité de Lorentz donne donc

\[
 \int|F||\nabla S(h)G_a|
 \le C\|F\|_{3/2,\infty}
 \|\nabla S(h)G_a\|_{3,1}<\infty.                         \tag{34}
\]

L'intégration par parties (29) est ainsi globale et absolument convergente.
On peut aussi l'obtenir avec des cutoffs, puis les retirer par (34); aucun
flux spatial à l'infini ne reste.

La pression peut être suivie explicitement. Avec

\[
 \Psi_{a,s;r}=S(a+r-s)G_a(s;r),\qquad
 \operatorname{div}\Psi_{a,s;r}=0,                        \tag{35}
\]

la forme non projetée contiendrait

\[
 2\int (F+qI):\nabla\Psi_{a,s;r}.                         \tag{36}
\]

Or

\[
 \int qI:\nabla\Psi_{a,s;r}
 =\int q\,\operatorname{div}\Psi_{a,s;r}=0.               \tag{37}
\]

Cette annulation est légitime, et pas seulement formelle :
\(q\in L^{3/2,\infty}\) par la jauge de Riesz et
\(\nabla\Psi\in L^{3,1}\). Une pression seulement locale, modulo une
composante harmonique sans contrôle global, ne justifierait pas
automatiquement le test non compact \(\Psi\). La formulation projetée (18)
évite cette ambiguïté.

## 5. Primitive de flux

Par (2), \(E_a\) est continue sur toute bande \([s_0,r]\), avec
\(E_a(r;r)=0\). En intégrant (4) entre \(s\) et \(r\),

\[
\begin{aligned}
 0-E_a(s;r)
 &=\int_s^r\partial_\sigma E_a(\sigma;r)\,d\sigma\\
 &=-\int_s^r\Phi_a(\sigma;r)\,d\sigma.                    \tag{38}
\end{aligned}
\]

Ceci prouve (7). Plus généralement,

\[
 E_a(s_1;r)-E_a(s_0;r)
 =-\int_{s_0}^{s_1}\Phi_a(\sigma;r)\,d\sigma,             \tag{39}
\]

d'où (8).

Trois quantités doivent être distinguées :

\[
\begin{aligned}
 P_a(s;r)&=\int_s^r\Phi_a(\sigma;r)\,d\sigma=E_a(s;r),\\
 V_a(s;r)&=\int_s^r|\Phi_a(\sigma;r)|\,d\sigma,\\
 I_a(r)&=\lim_{s\to-\infty}\int_s^r\Phi_a(\sigma;r)\,d\sigma,
 \quad\text{si la limite existe}.                         \tag{40}
\end{aligned}
\]

Le critère minimal du cycle 0051 demande seulement que \(P_a(s_n;r)\)
reste borné sur une suite. Il ne demande pas :

- \(\sup_{s<r}P_a(s;r)<\infty\);
- l'existence de l'intégrale impropre signée \(I_a(r)\);
- la finitude de la variation \(V_a(-\infty;r)\).

Ces trois propriétés sont successivement plus uniformes ou plus fortes.
Comme \(\Phi_a\) peut changer de signe, aucune implication inverse ne doit
être ajoutée sans preuve.

## 6. Équivalence exacte avec la borne ancienne

Le cycle 0051 a démontré, pour chaque \(a>0\) fixé,

\[
 \sup_{s<r}\|(I-S(a))g_{s,r}\|_2\le CM^2a^{1/4}.          \tag{41}
\]

Par contraction et inégalité triangulaire,

\[
\begin{aligned}
 \|G_a(s;r)\|_2&\le\|g_{s,r}\|_2,\\
 \|g_{s,r}\|_2&\le
 \|G_a(s;r)\|_2+CM^2a^{1/4}.                              \tag{42}
\end{aligned}
\]

Puisque \(E_a=\|G_a\|_2^2=P_a\), (42) donne (9).

Le quantificateur minimal est exactement

\[
 \exists a>0,\ \exists s_n\to-\infty,\qquad
 \sup_nP_a(s_n;r)<\infty.                                 \tag{43}
\]

S'il est satisfait, alors
\(\sup_n\|g_{s_n,r}\|_2<\infty\), puis le cycle 0050 donne

\[
 v(r)\in L^2_\sigma.                                      \tag{44}
\]

La réciproque

\[
 v(r)\in L^2
 \Longrightarrow
 \liminf_{s\to-\infty}\|g_{s,r}\|_2<\infty                \tag{45}
\]

n'a pas été démontrée. En particulier, (43) est un critère suffisant pour
l'énergie de la trace, pas une caractérisation de toutes les traces
\(L^2\) possibles d'une solution ancienne.

## 7. Majorant absolu et coefficient critique

Les équations (17), (31) et (6) donnent

\[
 |\Phi_a(s;r)|
 \le CM^2(a+r-s)^{-3/4}E_a(s;r)^{1/2},                   \tag{46}
\]

ce qui est (11). On peut obtenir (12) sans diviser par
\(E_a^{1/2}\) aux zéros. La formule (20) et (21) donnent directement

\[
\begin{aligned}
 E_a(s;r)^{1/2}
 &=\|G_a(s;r)\|_2\\
 &\le CM^2
 \int_s^r(a+r-\tau)^{-3/4}\,d\tau\\
 &=4CM^2\left[
 (a+r-s)^{1/4}-a^{1/4}\right].                           \tag{47}
\end{aligned}
\]

Le facteur numérique \(4\) peut être absorbé dans \(C\), mais la différence
des deux quarts de puissance ne doit pas être remplacée près de \(s=r\)
par une quantité non nulle.

En combinant (46)--(47),

\[
 |\Phi_a(s;r)|
 \le CM^4(a+r-s)^{-3/4}
 \left[(a+r-s)^{1/4}-a^{1/4}\right].                      \tag{48}
\]

Pour \(r-s\to\infty\), ce majorant est
\(O(M^4(r-s)^{-1/2})\). Son intégrale sur le passé diverge comme
\((r-s)^{1/2}\), ce qui reproduit

\[
 E_a(s;r)\lesssim M^4(r-s)^{1/2}.                         \tag{49}
\]

Pour \(s\uparrow r\), la différence de (47) est
\[
 (a+r-s)^{1/4}-a^{1/4}
 =\frac14a^{-3/4}(r-s)+O((r-s)^2),                        \tag{50}
\]

donc le flux est localement intégrable jusqu'au temps terminal. Le
paramètre \(a>0\) supprime toute singularité diagonale.

L'estimation de la variation absolue,

\[
 \int_{-\infty}^r|\Phi_a(s;r)|\,ds<\infty,                \tag{51}
\]

serait un critère suffisant très fort pour la convergence de \(E_a(s;r)\)
quand \(s\to-\infty\). Elle ne découle pas de (48). Une preuve qui remplace
la primitive signée par (51) change donc substantiellement le problème.

## 8. Échelle

Sous la remise à l'échelle

\[
 v_\lambda(x,t)=\lambda v(\lambda x,\lambda^2t),          \tag{52}
\]

le correcteur et l'énergie filtrée satisfont

\[
\begin{aligned}
 g^\lambda_{s,r}(x)
 &=\lambda
 g_{\lambda^2s,\lambda^2r}(\lambda x),\\
 E^\lambda_a(s;r)
 &=\lambda^{-1}
 E_{\lambda^2a}(\lambda^2s;\lambda^2r).                  \tag{53}
\end{aligned}
\]

La densité de flux se transforme comme

\[
 \Phi^\lambda_a(s;r)
 =\lambda
 \Phi_{\lambda^2a}(\lambda^2s;\lambda^2r).                \tag{54}
\]

En effet, \(v\otimes v\) apporte \(\lambda^2\),
\(\nabla\Psi\) apporte \(\lambda^2\), et l'intégrale spatiale
\(\lambda^{-3}\). Ainsi

\[
 \int_s^r\Phi^\lambda_a(\sigma;r)\,d\sigma
 =\lambda^{-1}
 \int_{\lambda^2s}^{\lambda^2r}
 \Phi_{\lambda^2a}(\eta;\lambda^2r)\,d\eta,               \tag{55}
\]

exactement comme l'énergie (53). Le critère de primitive respecte donc
l'échelle de Navier--Stokes si \(a\) est remis à l'échelle avec le temps.

Fixer numériquement le même \(a\) après une remise à l'échelle changerait
le filtre physique. Cela ne détruit pas la propriété qualitative « il
existe un \(a>0\) », mais interdit de comparer les constantes sans
transformer \(a\).

## 9. Relation avec les flux dyadiques

Le cycle 0051 écrit

\[
 G_a(s;r)
 =-\int_s^r
 S(a+r-\tau)\mathbb P\operatorname{div}F(\tau)\,d\tau.    \tag{56}
\]

La dérivée en temps de base sélectionne exactement le bord inférieur de
cette intégrale. La densité (6) est donc une corrélation entre :

- le stress instantané \(F(s)=v(s)\otimes v(s)\);
- le correcteur terminal accumulé \(G_a(s;r)\);
- un filtre de taille \((a+r-s)^{1/2}\).

Elle n'est pas l'énergie instantanée de \(v(s)\), ni le flux spectral
classique à travers une coquille fixe. Le filtre dépend du temps de base et
du temps terminal.

En décomposant sur les couronnes, (4) devient formellement

\[
 \partial_sE_a(s;r)
 =
 2\sum_j
 \left\langle
 \Delta_jG_a(s;r),
 \Delta_jS(a+r-s)\mathbb P\operatorname{div}F(s)
 \right\rangle,                                           \tag{57}
\]

avec une partition presque orthogonale adaptée. La somme est justifiée dans
\(L^2\) par (23), pas par une somme carrée des blocs de \(v\).

Le critère du cycle 0051 exige une cancellation de l'accumulation basse des
intégrales vectorielles. L'identité (7) reformule ce verrou comme une borne
subséquentielle de la primitive signée de (6). Elle ne crée pas
automatiquement le signe ou la sommabilité manquants.

## 10. Solutions forward et solutions anciennes

Les identités (2)--(8) sont locales en temps de base. Elles valent sur tout
intervalle forward fini \([t_0,r]\) pour une solution possédant :

- le représentant temporel et la formule de Duhamel;
- la borne \(L^\infty(t_0,r;L^{3,\infty})\);
- la pression globale ou, équivalemment ici, la formulation projetée.

Dans ce cadre forward,

\[
 E_a(t_0;r)=\int_{t_0}^r\Phi_a(s;r)\,ds<\infty             \tag{58}
\]

est simplement une identité sur un intervalle fini. Elle ne produit aucune
borne indépendante de \(t_0\).

La solution ancienne des cycles précédents est conditionnelle à la branche
Type I étudiée. Son ancienneté permet de poser la limite
\(s\to-\infty\), mais ne fournit aucune domination supplémentaire du flux.
Importer une solution forward auto-similaire ou une solution BSS construite
à un temps initial fixe ne donnerait pas (10) sans un lemme de raccord
uniforme.

## 11. Passe contradictoire

1. **Signe de la borne inférieure.** La dérivée de
   \(-\int_s^r\) est positive. Le signe négatif de (4) apparaît seulement
   lors de l'intégration spatiale de \(\operatorname{div}F\).
2. **Facteur deux.** \(E_a=\|G_a\|_2^2\), donc sa dérivée contient
   \(2\langle G_a,\partial_sG_a\rangle\). Une formule sans ce facteur
   correspondrait à \(E_a/2\).
3. **Double lissage.** L'auto-adjonction déplace
   \(S(a+r-s)\) sur \(G_a=S(a)g\). Le test final est
   \(S(2a+r-s)g\). Omettre un \(a\) modifie le flux.
4. **Différentiabilité de la trace.** Aucune dérivée forte de \(v(s)\) dans
   \(L^{3,\infty}\) n'est supposée. L'absolue continuité vient de Duhamel
   après lissage strict.
5. **Temps exceptionnel.** (3)--(4) valent presque partout en \(s\). La
   forme intégrée (7)--(8) vaut pour tous les endpoints grâce à la
   continuité de \(G_a\).
6. **Pression omise.** Elle disparaît seulement contre le test global
   solénoïdal, avec dualité Lorentz justifiant l'intégrale. Une pression
   locale non contrôlée n'autorise pas le même test à l'infini.
7. **Bord spatial.** (34) rend le produit global \(L^1\). Aucun flux de
   cutoff caché n'est abandonné.
8. **Signe du flux.** \(\Phi_a(s;r)\) peut être négatif sur des
   sous-intervalles. L'identité \(E_a=\int_s^r\Phi_a\ge0\) ne donne ni
   \(\Phi_a\ge0\), ni monotonie de \(E_a\) lorsque la base recule.
9. **Primitive contre variation.** La borne d'une primitive signée sur une
   suite ne donne ni convergence de l'intégrale impropre, ni
   \(\int|\Phi_a|<\infty\).
10. **Division par l'énergie.** Passer de (46) à une inégalité pour
    \(E_a^{1/2}\) en divisant échoue aux zéros. La preuve par Duhamel (47)
    évite cette circularité.
11. **Paramètre filtrant.** \(a>0\) est fixé avant
    \(s\to-\infty\). Choisir \(a=r-s\) déplace la divergence dans le
    complément haute fréquence.
12. **Quantificateur.** Le \(\liminf\) demande une suite, pas une borne
    uniforme pour tout le passé. Inverser ces deux énoncés renforcerait
    silencieusement le lemme.
13. **Trace \(L^2\).** (43) implique \(v(r)\in L^2\), mais la réciproque
    n'est pas établie.
14. **Profil calorifique.** Le champ \(U_\sharp\) du cycle 0050 peut
    saturer la croissance \(E_a\sim C_U^2(r-s)^{1/2}\), mais il n'est pas
    une solution de Navier--Stokes; son générateur de flux n'est pas
    \(v\otimes v\) dans (6).
15. **Forward contre ancien.** Une identité vraie pour tout temps initial
    forward fixé ne donne pas une primitive uniformément bornée lorsque ce
    temps tend vers \(-\infty\).
16. **Clay.** Même (10) ne fournirait qu'une trace \(L^2\) à un temps de la
    solution ancienne conditionnelle. Un théorème de rigidité et le raccord
    à tout blow-up resteraient nécessaires.

## 12. Corrections bloquantes et prochain lemme

Les corrections suivantes doivent être propagées dans le graphe de preuve.

- La bonne identité est \(\partial_sE_a=-\Phi_a\), avec
  \(E_a(s)=\int_s^r\Phi_a\).
- Le test du stress est
  \(\nabla S(a+r-s)G_a=\nabla S(2a+r-s)g_{s,r}\).
- L'absolue continuité est locale sur chaque bande finie; aucune variation
  totale sur le passé n'est acquise.
- La pression s'annule par solénoïdalité dans une dualité globale
  \(L^{3/2,\infty}\)--\(L^{3,1}\).
- La primitive signée, la variation absolue et l'intégrale impropre sont
  trois objets différents.
- Le critère \(\liminf\) porte sur une suite ancienne et un \(a>0\) fixé.
- Les bornes disponibles donnent un flux absolu non intégrable
  \(O((r-s)^{-1/2})\); elles ne ferment pas le critère.

Le prochain lemme borné et falsifiable est :

\[
\boxed{
 \exists a>0,\ \exists s_n\to-\infty,\qquad
 \sup_n
 \int_{s_n}^r
 2\int_{\mathbb R^3}
 (v\otimes v)(\sigma):
 \nabla S(2a+r-\sigma)g_{\sigma,r}\,dx\,d\sigma
 <\infty.}                                                 \tag{59}
\]

Par (7), cet énoncé est exactement le critère du cycle 0051, et non encore
un progrès autonome. Pour le rendre démontrable, il faut ajouter une
hypothèse structurelle plus élémentaire, par exemple une cancellation
dyadique signée du flux dans une fenêtre autour de
\(|\xi|\simeq(r-\sigma)^{-1/2}\), puis prouver qu'elle implique (59).

Une version non tautologique et directement falsifiable est la suivante.
Posons

\[
\begin{aligned}
 E_{a,j}(s;r)&=\|\Delta_jG_a(s;r)\|_2^2,\\
 \Phi_{a,j}(s;r)
 &:=-2\left\langle
 \Delta_jG_a(s;r),
 \Delta_jS(a+r-s)\mathbb P\operatorname{div}F(s)
 \right\rangle.
\end{aligned}
\]

Alors

\[
 E_{a,j}(s;r)=\int_s^r\Phi_{a,j}(\sigma;r)\,d\sigma
 \ge0.                                                     \tag{60}
\]

Le prochain lemme substantiel est l'existence de
\(\varepsilon>0\), \(J\in\mathbb Z\), d'une suite
\(s_n\to-\infty\) et d'une constante \(C_r\) telles que

\[
 \boxed{
 \int_{s_n}^r\Phi_{a,j}(\sigma;r)\,d\sigma
 \le C_r2^{\varepsilon(j-J)}
 \quad\text{pour tout }j\le J,\ \text{uniformément en }n.} \tag{61}
\]

La somme géométrique de (61), l'équivalence Littlewood--Paley et le contrôle
uniforme des blocs \(j>J\) du cycle 0051 impliqueraient (59). Contrairement
à (59), (61) affirme un gain quantitatif par coquille et peut être attaquée
triade par triade.

Une obstruction algébrique doit toutefois être enregistrée. Sur le tore,
les fréquences

\[
 k=(N,0,0),\qquad \ell=(-N,0,1),\qquad q=(0,0,1)
\]

et des polarisations divergence-free convenables donnent une sortie
projetée haute--haute vers \(q\) indépendante de \(N\). La phase du mode
receveur inverse le transfert énergétique signé, tandis qu'une autre
polarisation annule entièrement la sortie. Ainsi :

- la projection de Leray élimine la croissance artificielle en \(N\), mais
  ne fournit pas à elle seule un gain en \(|q|/|k|\);
- la conservation triadique impose que les gains et pertes se compensent,
  pas le signe de la réception basse;
- (61) ne peut pas être une conséquence purement algébrique de
  l'incompressibilité.

Ce contre-test vit sur \(\mathbb T^3\) et porte sur une triade instantanée;
il ne construit pas une solution ancienne sur \(\mathbb R^3\). Il suffit
néanmoins à bloquer toute preuve de (61) fondée sur une coercivité
universelle des polarisations. Le gain recherché doit utiliser l'intégration
temporelle, la viscosité, une géométrie de phases ou une propriété
supplémentaire de la solution ancienne.

**Prochaine expérience décisive :** décomposer \(\Phi_a\) en triades
Littlewood--Paley, conserver les signes, puis tester une annulation après
somme des triades et intégration temporelle. La coercivité d'une triade
isolée est réfutée. Tout passage aux valeurs absolues avant la somme
dynamique reproduira seulement le coefficient non intégrable de (48).
