# Cycle 0049 — fermeture énergétique du correcteur faible-\(L^3\)

Date : 2026-08-15.

Statut : `AI_INTERNAL_DERIVATION`; audit analytique indépendant, sans calcul
numérique et sans prétention de résolution du problème Clay.

## Verdict

Le lemme actif est **positif**, sous l'hypothèse explicite que \(v\) est une
solution faible adaptée locale et que sa pression est la pression globale de
Riesz. Le gain \(L^2\) déjà établi au cycle 0048 ferme exactement la
singularité temporelle qui paraissait critique.

Plus précisément, soit \(I=[t_0,t_1]\), \(T=t_1-t_0<\infty\), et soit
\(v\) une solution distributionnelle faible adaptée de

\[
 \partial_t v-\Delta v+\operatorname{div}(v\otimes v)
 +\nabla q=0,\qquad \operatorname{div}v=0                 \tag{1}
\]

sur \(\mathbb R^3\times(t_0,t_1)\), avec

\[
 q=\mathcal R_i\mathcal R_j(v_iv_j),\qquad
 M:=\operatorname*{ess\,sup}_{t\in I}
       \|v(t)\|_{L^{3,\infty}}<\infty .             \tag{2}
\]

On prend le représentant \(C_{w^*}L^{3,\infty}\) du cycle 0048, on pose

\[
 a=v(t_0),\qquad V(t)=e^{(t-t_0)\Delta}a,\qquad w=v-V.    \tag{3}
\]

L'estimation sous-critique du même cycle donne indépendamment de toute
inégalité d'énergie perturbée

\[
 w\in C([t_0,t_1];L^2),\qquad w(t_0)=0,\qquad
 \|w(t)\|_2\le C_D M^2(t-t_0)^{1/4}.                   \tag{4}
\]

Alors

\[
 \boxed{w\in L^\infty(I;L^2)\cap
 L^2(I;\dot H^1)}                                            \tag{5}
\]

et, pour tout \(t\in[t_0,t_1]\), après choix du représentant énergétique,

\[
 \boxed{
 \|w(t)\|_2^2+2\int_{t_0}^{t}\|\nabla w(s)\|_2^2\,ds
 \le
 2\int_{t_0}^{t}\!\int_{\mathbb R^3}
 (V\otimes w+V\otimes V):\nabla w\,dx\,ds .}        \tag{6}
\]

C'est l'inégalité d'énergie globale perturbée de la scission
Barker--Seregin--Šverák. Les deux termes du membre droit sont des
intégrales absolument convergentes. Le terme apparemment limite satisfait

\[
 \|V(t)\|_4^8\|w(t)\|_2^2
 \le C C_D^2 M^{12}(t-t_0)^{-1/2},                            \tag{7}
\]

et non une singularité non intégrable \((t-t_0)^{-1}\), précisément grâce
au facteur \(\|w(t)\|_2^2=O((t-t_0)^{1/2})\) de (4).

Le passage global ne requiert ni décroissance forte des queues de
\(L^{3/2,\infty}\), ni dissipation globale supposée à l'avance. Le flux
cubique et la pression sont d'abord absorbés à rayon fini avec un reste
\(O(R^{-1})\). Une fois (5) acquise, on repasse dans l'inégalité locale non
estimée et on fait tendre \(R\to\infty\) pour obtenir le membre droit signé
exact de (6).

## 1. Hypothèses exactes et portée

La conclusion utilise toutes les clauses suivantes.

1. Le domaine est l'espace entier \(\mathbb R^3\), sans frontière.
2. La viscosité est normalisée à (1), la force extérieure est nulle.
3. \(v\) est faible adaptée localement : elle satisfait l'inégalité locale
   d'énergie, et pas seulement l'équation distributionnelle.
4. La pression a la jauge globale (2). Une pression seulement locale, modulo
   une composante harmonique arbitraire, ne fournit pas la borne uniforme
   utilisée à l'infini.
5. Le temps \(t_0\) porte la trace faible-étoile construite au cycle 0048;
   (4) fixe en plus la trace forte nulle du correcteur.
6. Aucun argument de petitesse n'est utilisé; toutes les constantes peuvent
   dépendre polynomialement de \(M\).

La seule suitability locale de \(v\), sans (2), ne suffit donc pas à cette
globalisation précise. Inversement, une solution seulement distributionnelle
avec (2) ne donne pas la direction de l'inégalité (6), car le défaut local
d'énergie pourrait avoir un signe inconnu.

## 2. Échelle et estimations calorifiques

Sous l'échelle de Navier--Stokes

\[
 v_\lambda(x,t)=\lambda v(\lambda x,\lambda^2t),\qquad
 q_\lambda(x,t)=\lambda^2q(\lambda x,\lambda^2t), \tag{8}
\]

la norme \(L^{3,\infty}\) est invariante, tandis que

\[
 \|w_\lambda(t)\|_2^2=\lambda^{-1}\|w(\lambda^2t)\|_2^2,
 \qquad
 \int\|\nabla w_\lambda\|_2^2dt
 =\lambda^{-1}\int\|\nabla w\|_2^2dt.          \tag{9}
\]

La contraction du semi-groupe dans \(L^{3,\infty}\) et le lissage de
Lorentz donnent, avec \(h=t-t_0>0\),

\[
 \|V(t)\|_{3,\infty}\le C_3M,\qquad
 \|V(t)\|_4\le C_HM h^{-1/8}.                         \tag{10}
\]

Par conséquent,

\[
 \int_{t_0}^{t_1}\|V(t)\|_4^4dt
 \le 2C_H^4M^4T^{1/2},                                      \tag{11}
\]

et, en combinant (4) et (10),

\[
 \int_{t_0}^{t_1}\|V(t)\|_4^8\|w(t)\|_2^2dt
 \le 2C_H^8C_D^2M^{12}T^{1/2}.                              \tag{12}
\]

Les membres droits de (11)--(12) ont le bon poids d'échelle : \(T^{1/2}\)
se transforme comme une longueur, donc comme l'énergie dans (9). Il n'est
pas revendiqué que ces bornes soient uniformes sur des bandes de longueur
arbitraire.

## 3. Inégalité relative locale

Fixons \(\delta\in(t_0,t_1)\) qui soit un temps de Lebesgue admissible pour
l'inégalité locale d'énergie, et \(t\in(\delta,t_1]\). Sur cette bande,
\(V\) est lisse. Choisissons \(\chi\in C_c^\infty(\mathbb R^3)\), radiale
non croissante, \(0\le\chi\le1\), égale à \(1\) sur \(B_1\), nulle hors de
\(B_2\), et
posons

\[
 \chi_R(x)=\chi(x/R),\qquad \phi_R=\chi_R^2,\qquad
 \mathcal A_R=B_{2R}\setminus B_R.                         \tag{13}
\]

Les constantes géométriques vérifient

\[
 |\nabla\phi_R|\le C R^{-1}\chi_R,\qquad
 |\Delta\phi_R|\le C R^{-2}\mathbf1_{\mathcal A_R}.        \tag{14}
\]

L'équation formelle du correcteur est

\[
 \partial_tw-\Delta w+\operatorname{div}
 ((w+V)\otimes(w+V))+\nabla q=0.                         \tag{15}
\]

On ne teste pas globalement (15) par \(w\), puisque
\(\nabla w\in L^2_{t,x}\) est précisément à démontrer. La justification
locale correcte consiste à combiner :

- l'inégalité locale d'énergie de \(v\);
- l'égalité locale d'énergie du champ calorique lisse \(V\);
- l'identité polarisée obtenue en testant l'équation faible de \(v\) par
  une régularisation compacte de \(V\phi_R\).

Le passage à la limite dans la régularisation conserve le défaut d'énergie
non négatif de \(v\). Il fournit

\[
\begin{aligned}
 \frac12\int \phi_R|w(t)|^2
 +\int_\delta^t\!\int \phi_R|\nabla w|^2
 \le{}&\frac12\int \phi_R|w(\delta)|^2
 +\frac12\int_\delta^t\!\int
          |w|^2\Delta\phi_R                                      \\
 &+\int_\delta^t\!\int \phi_R
       (V\otimes w+V\otimes V):\nabla w
 +\int_\delta^t\!\int \mathcal F\cdot\nabla\phi_R,          \tag{16}
\end{aligned}
\]

où le flux de bord exact peut être pris comme

\[
 \mathcal F
 =\left(v\cdot w-\frac12|w|^2\right)v+q\,w.               \tag{17}
\]

Pour vérifier (17), on développe le terme intérieur. Avec la convention
\((a\otimes b)_{ij}=a_ib_j\),

\[
\begin{aligned}
 \int\phi_R(w\otimes w):\nabla w
   &=-\frac12\int |w|^2w\cdot\nabla\phi_R,\\
 \int\phi_R(w\otimes V):\nabla w
   &=-\frac12\int |w|^2V\cdot\nabla\phi_R,
\end{aligned}                                                 \tag{18}
\]

car \(\operatorname{div}w=\operatorname{div}V=0\). Les deux termes
restants sont exactement ceux de la troisième intégrale de (16). Le terme
de bord produit par \(\operatorname{div}(v\otimes v)\) est
\((v\cdot w)v\cdot\nabla\phi_R\), et la pression produit
\(qw\cdot\nabla\phi_R\), ce qui donne (17).

Une soustraction naïve des deux inégalités d'énergie ne justifierait pas
(16) : il faut l'identité croisée issue de l'équation faible. Cette étape
est valide à \(\delta>t_0\), où \(V\) est lisse; le bord \(t_0\) sera atteint
seulement après l'obtention de bornes intégrables uniformes.

## 4. Pression et flux cubique à l'infini

Avant toute globalisation, la borne faible-\(L^3\) donne exactement la
croissance d'énergie locale critique

\[
 \sup_{s\in I}\int_{B_R}
 \bigl(|v(s)|^2+|V(s)|^2+|w(s)|^2\bigr)\,dx
 \le C M^2R+C N_*^2,\qquad
 N_*=\sup_{s\in I}\|w(s)\|_2.                    \tag{18a}
\]

Pour \(v\) et \(V\), cela résulte de
\(\|f\|_{L^2(B_R)}\le C R^{1/2}\|f\|_{3,\infty}\); pour \(w\), la
borne globale (4) est meilleure. Le taux \(O(R)\) de (18a) suffit à
légitimer les calculs locaux, mais ne fait tendre aucun flux cubique vers
zéro. La fermeture ci-dessous utilise le facteur de dérivée du cutoff et
Sobolev; attribuer la globalisation à la seule borne \(O(R)\) serait une
correction bloquante.

Le produit de Lorentz d'O'Neil et la bornitude des transformées de Riesz
donnent, pour presque tout temps,

\[
 \|v\otimes v\|_{3/2,\infty}\le C_OM^2,\qquad
 \|q\|_{3/2,\infty}\le C_RC_OM^2.                 \tag{19}
\]

La contraction calorifique donne la même borne pour
\(V\otimes V\). Comme \(w=v-V\),

\[
 |\mathcal F|\le
 C\bigl(|v|^2+|V|^2+|q|\bigr)|w|.                         \tag{20}
\]

En effet,
\(|v||w|^2\le C(|v|^2+|V|^2)|w|\); il serait incomplet de majorer le
flux uniquement par \(|v|^2|w|\).

Le split de pression algébrique compatible avec la scission est

\[
\begin{aligned}
 q={}&q_{ww}+q_{wV}+q_{Vw}+q_{VV},\\
 q_{\alpha\beta}
 :={}&\mathcal R_i\mathcal R_j(\alpha_i\beta_j).
                                                               \tag{20a}
\end{aligned}
\]

Comme \(w,v,V\in L^\infty_tL^{3,\infty}_x\), chacune de ces quatre
composantes appartient à
\(L^\infty_tL^{3/2,\infty}_x\). Ce split n'ajoute toutefois aucun gain de
queue et n'est pas nécessaire à (23); la borne sur la pression complète
suffit. Deux propriétés distinctes ne doivent pas être confondues :

- la suitability supposée donne \(q\in L^{3/2}_{\mathrm{loc}}\), qui est
  la clause locale de la définition BSS;
- la jauge de Riesz globale donne en plus
  \(q\in L^\infty_tL^{3/2,\infty}_x\), qui ferme ici le cutoff à l'infini.

Une décomposition de pression locale avec une partie harmonique non
contrôlée ne peut pas être substituée à la seconde propriété.

Posons

\[
 G=|v|^2+|V|^2+|q|,\qquad
 \|G(t)\|_{3/2,\infty}\le C_GM^2.                 \tag{21}
\]

Sur l'ensemble fini \(\mathcal A_R\), l'inclusion de Lorentz donne

\[
 \|G(t)\|_{L^{6/5}(\mathcal A_R)}
 \le C|\mathcal A_R|^{1/6}\|G(t)\|_{3/2,\infty}
 \le C C_GM^2R^{1/2}.                                      \tag{22}
\]

Avec \(z_R=\chi_Rw\in H^1_0(B_{2R})\), Sobolev et (14) donnent

\[
\begin{aligned}
 \left|\int \mathcal F\cdot\nabla\phi_R\right|
 &\le \frac CR\|G\|_{L^{6/5}(\mathcal A_R)}\|z_R\|_6\\
 &\le C M^2R^{-1/2}\|\nabla z_R\|_2.             \tag{23}
\end{aligned}
\]

Or

\[
 \|\nabla z_R\|_2
 \le \|\chi_R\nabla w\|_2+C R^{-1}\|w\|_2.       \tag{24}
\]

Pour tout \(\varepsilon>0\), (23)--(24) impliquent donc

\[
 \left|\int \mathcal F\cdot\nabla\phi_R\right|
 \le \varepsilon\|\chi_R\nabla w\|_2^2
 +C_\varepsilon\frac{M^4}{R}
 +C\frac{M^2}{R^{3/2}}\|w\|_2.                       \tag{25}
\]

Le dernier terme peut aussi être remplacé, par Young, par une combinaison
de \(M^4/R\) et de \(R^{-2}\|w\|_2^2\). Après intégration temporelle,
tous les restes tendent vers zéro quand \(R\to\infty\).

Le point logique important est que (22) n'affirme pas

\[
 \|G\mathbf1_{\mathcal A_R}\|_{3/2,\infty}\to0.              \tag{26}
\]

Cette propriété est généralement fausse dans un espace faible. Le petit
facteur vient de \(R^{-1}|\mathcal A_R|^{1/6}=R^{-1/2}\), puis de l'absorption
Sobolev, et non d'une continuité absolue inexistante de la quasi-norme.

Le terme diffusif de cutoff est plus simple :

\[
 \left|\int_\delta^t\!\int |w|^2\Delta\phi_R\right|
 \le CR^{-2}\int_\delta^t\|w(s)\|_2^2ds\to0.            \tag{27}
\]

## 5. Termes intérieurs et singularité au temps initial

Notons

\[
 A_R(s)=\|\chi_R\nabla w(s)\|_2,\qquad
 N(s)=\|w(s)\|_2.                                      \tag{28}
\]

L'inégalité de Gagliardo--Nirenberg appliquée à \(z_R\) est

\[
 \|z_R\|_4\le C\|z_R\|_2^{1/4}\|\nabla z_R\|_2^{3/4}.     \tag{29}
\]

Le terme mixte s'estime sans dérivée de \(V\) :

\[
\begin{aligned}
 \left|\int\phi_R(V\otimes w):\nabla w\right|
 &\le \|V\|_4\|z_R\|_4 A_R\\
 &\le \varepsilon A_R^2
   +C_\varepsilon\|V\|_4^8N^2
   +C_\varepsilon\|V\|_4^2R^{-3/2}N^2.              \tag{30}
\end{aligned}
\]

La dernière contribution provient de
\(\|\nabla z_R\|_2\le A_R+CR^{-1}N\); elle est un terme de cutoff
et disparaît lorsque \(R\to\infty\). Le terme purement calorique vérifie

\[
 \left|\int\phi_R(V\otimes V):\nabla w\right|
 \le \varepsilon A_R^2+C_\varepsilon\|V\|_4^4.             \tag{31}
\]

Sans (4), le coefficient de (30) serait seulement

\[
 \|V(t)\|_4^8\simeq M^8(t-t_0)^{-1},                 \tag{32}
\]

et son intégrale logarithmique divergerait. Une application de Grönwall
depuis \(t_0\) serait alors illégitime. Ici, on ne remplace pas \(N^2\) par
une inconnue à fermer par Grönwall : on insère la borne indépendante (4),
ce qui donne (7), puis (12). C'est le maillon décisif du cycle.

Le terme de cutoff restant dans (30) est également intégrable près de
\(t_0\) :

\[
 \|V(t)\|_4^2N(t)^2
 \le C M^6(t-t_0)^{1/4}.                                  \tag{33}
\]

### 5.1 Réponse à l'objection de coercivité critique

L'estimation critique directe

\[
 \int |V||w||\nabla w|
 \le C\|V\|_{3,\infty}\|\nabla w\|_2^2
 \le CM\|\nabla w\|_2^2                                  \tag{33a}
\]

ne peut effectivement pas être absorbée pour \(M\) grand. Elle n'est pas
utilisée ici. À rayon fini, la chaîne exacte de (30) est

\[
\begin{aligned}
 \int\phi_R|V||w||\nabla w|
 &\le C\|V\|_4 N^{1/4}
       (A_R+CR^{-1}N)^{3/4}A_R\\
 &\le C\|V\|_4N^{1/4}A_R^{7/4}
      +C\|V\|_4R^{-3/4}NA_R\\
 &\le \varepsilon A_R^2
      +C_\varepsilon\|V\|_4^8N^2
      +C_\varepsilon\|V\|_4^2R^{-3/2}N^2.                \tag{33b}
\end{aligned}
\]

Le premier Young utilise les exposants \(8/7\) et \(8\). Son coefficient
non absorbé n'est donc pas \(CM\), mais
\(\|V\|_4^8N^2\). Le taux \(N^2\lesssim M^4h^{1/2}\), obtenu au cycle 0048
par Duhamel sous-critique sans aucune dissipation, transforme
\(\|V\|_4^8\lesssim M^8h^{-1}\) en \(CM^{12}h^{-1/2}\).

De même, l'absorption du flux total (23)--(25) se fait avec
\(z_R=\chi_Rw\in H^1_0(B_{2R})\), donc avec la dissipation **locale déjà
incluse dans la suitability**, et laisse \(CM^4/R\). Elle ne suppose ni
queue de dissipation globale, ni petitesse de \(M\). C'est seulement après
ces deux absorptions locales uniformes en \(R\) que Fatou construit la
dissipation globale. L'objection à (33a) est donc correcte contre la route
critique standard, mais ne crée pas de cercle dans (33b).

## 6. Première passe : obtenir la dissipation globale

On insère (25), (27), (30) et (31) dans (16), puis on choisit les trois
paramètres \(\varepsilon\) assez petits pour absorber une fraction fixe de
\(\int A_R^2\) dans le membre gauche. Pour tout bon temps
\(\delta>t_0\), on obtient une borne indépendante de \(R\) de la forme

\[
\begin{aligned}
 \int_\delta^t A_R(s)^2ds
 \le C\bigl[&N(\delta)^2
 +\int_\delta^t\|V\|_4^4ds
 +\int_\delta^t\|V\|_4^8N^2ds\bigr]\\
 &+o_R(1),                                      \tag{34}
\end{aligned}
\]

où \(o_R(1)\to0\) est dominé par une combinaison explicite de

\[
 R^{-1}M^4T,\qquad
 R^{-2}\int_\delta^tN(s)^2ds,\qquad
 R^{-3/2}\int_\delta^t\|V\|_4^2N^2ds.            \tag{35}
\]

Les équations (11)--(12) rendent le membre droit fini et uniforme lorsque
\(\delta\downarrow t_0\). En choisissant des cutoffs emboîtés et en
appliquant Fatou sur chaque boule, puis la convergence monotone des boules,
on obtient

\[
 \int_{t_0}^{t_1}\|\nabla w(s)\|_2^2ds
 \le C\bigl(M^4+M^{12}\bigr)T^{1/2}<\infty,          \tag{36}
\]

à modification des constantes universelles et des conventions de norme de
Lorentz. La puissance polynomiale n'est pas optimisée. La propriété
\(w\in L^\infty_tL^2_x\) était déjà contenue dans (4), donc (5) est
acquise.

Cette première passe ne doit pas être présentée comme prouvant directement
(6), car (30)--(31) ont remplacé le membre droit signé par des majorants
positifs. Son seul objet est d'obtenir (5) sans circularité.

## 7. Seconde passe : récupérer l'inégalité BSS exacte

Une fois (5) disponible, on revient à l'inégalité locale non estimée (16).
Les termes intérieurs sont maintenant absolument intégrables sur toute la
bande. En effet, les versions sans cutoff de (30)--(31) donnent

\[
\begin{aligned}
 \int_{t_0}^{t_1}\!\int |V||w||\nabla w|
 &\le \varepsilon\|\nabla w\|_{L^2_{t,x}}^2
 +C_\varepsilon\int_{t_0}^{t_1}\|V\|_4^8N^2dt<\infty,\\
 \int_{t_0}^{t_1}\!\int |V|^2|\nabla w|
 &\le \|V\|_{L^4_{t,x}}^2
       \|\nabla w\|_{L^2_{t,x}}<\infty.           \tag{37}
\end{aligned}
\]

Le flux de bord tend cette fois directement vers zéro. En intégrant (23)
en temps et en utilisant (24),

\[
\begin{aligned}
 \int_\delta^t
 \left|\int\mathcal F\cdot\nabla\phi_R\right|ds
 \le CM^2R^{-1/2}\Bigl(
 &\|\nabla w\|_{L^2((\delta,t)\times\mathcal A_R)}(t-\delta)^{1/2}\\
 &+R^{-1}\int_\delta^tN(s)ds\Bigr)\to0.          \tag{38}
\end{aligned}
\]

La première quantité tend vers zéro par l'intégrabilité globale de
\(|\nabla w|^2\); le facteur \(R^{-1/2}\) suffirait même sans utiliser toute
cette décroissance. Les termes d'énergie convergent par convergence dominée
et le terme de dissipation par convergence monotone ou Fatou. Ainsi, pour
presque tout bon \(\delta>t_0\) et presque tout \(t>\delta\),

\[
 \frac12N(t)^2+\int_\delta^t\|\nabla w\|_2^2ds
 \le \frac12N(\delta)^2
 +\int_\delta^t\!\int
 (V\otimes w+V\otimes V):\nabla w.                    \tag{39}
\]

Prenons une suite de bons temps \(\delta_n\downarrow t_0\). Par (4),
\(N(\delta_n)\to0\). Par (37), les intégrales sur
\((t_0,\delta_n)\) tendent vers zéro. Le passage \(\delta_n\downarrow t_0\)
donne (6) pour presque tout temps terminal.

Enfin, \(w\in C_tL^2_x\), l'intégrale de dissipation est une fonction
continue croissante du temps, et le membre droit de (6) est une intégrale
d'une fonction \(L^1_t\). L'inégalité s'étend donc à tout
\(t\in[t_0,t_1]\) par approximation par des bons temps.

## 8. Appartenance exacte à la classe BSS

La même construction qui donne (16), avec un cutoff espace-temps général
non négatif au lieu de \(\phi_R\), fournit l'inégalité locale perturbée du
correcteur. Elle n'est pas une conséquence de la seule inégalité globale
(6); elle est héritée directement de la suitability de \(v\), de l'égalité
calorifique de \(V\) et de l'identité croisée.

Pour la définition 1.1 publiée de Barker--Seregin--Šverák, il suffit en
réalité de vérifier la liste suivante après translation du temps initial :

1. \(a\in L^{3,\infty}_\sigma\) et \(v=V+w\), avec
   \(V=e^{(t-t_0)\Delta}a\);
2. \(w\in L^\infty_tL^2_x\cap L^2_t\dot H^1_x\);
3. \(w\) est faiblement continue dans \(L^2\) et a trace forte nulle;
4. l'inégalité globale perturbée (6);
5. l'équation distributionnelle, une pression
   \(q\in L^{3/2}_{\mathrm{loc}}\), et l'inégalité locale d'énergie de la
   paire complète \((v,q)\).

Les points 1 et 5 sont des hypothèses du lemme actif; (4) est plus forte que
le point 3; (5) et (6) démontrent les points 2 et 4. Par conséquent, sur
chaque bande finie issue d'un temps de trace \(t_0\),

\[
 \boxed{\text{\(v\) appartient à la classe BSS, définition 1.1,}}
                                                               \tag{39a}
\]

et pas seulement à une classe « de type BSS ». En résumé,

\[
 v=V+w,\quad
 V=e^{(t-t_0)\Delta}a,\quad
 w\in C_tL^2\cap L^2_t\dot H^1,\quad
 w(t_0)=0,                                      \tag{40}
\]

avec inégalités locale et globale perturbées. Cet audit ne vérifie pas ici
les conclusions ultérieures de stabilité, compacité ou unicité de l'article;
elles ont leurs propres quantificateurs. Il ferme exactement les deux
clauses laissées ouvertes au cycle 0048 : dissipation globale et inégalité
d'énergie perturbée.

## 9. Passe contradictoire

### 9.1 Test global prématuré

Écrire directement « on teste (15) par \(w\) » suppose la quantité
\(\int|\nabla w|^2\) recherchée. La première passe doit rester locale,
absorber les termes à rayon fini, puis utiliser Fatou.

### 9.2 Soustraction d'inégalités

Soustraire l'égalité d'énergie de \(V\) à l'inégalité de \(v\) ne contrôle
pas automatiquement le terme croisé \(\int v\cdot V\). L'identité faible
croisée est indispensable pour préserver le sens de l'inégalité.

### 9.3 Grönwall critique

La borne \(\|V\|_4^8\simeq h^{-1}\) n'est pas intégrable. Le calcul ne
l'intègre jamais seule et n'applique pas Grönwall avec ce coefficient. La
borne indépendante \(N^2=O(h^{1/2})\) est insérée avant l'intégration.

### 9.4 Queue faible de la pression

Il n'est pas supposé que
\(\|q\mathbf1_{\mathcal A_R}\|_{3/2,\infty}\to0\). L'estimation (22) sur
l'anneau fini et le facteur de cutoff fournissent le petit paramètre.

### 9.5 Flux cubique incomplet

Le flux ne se réduit pas à \(|v|^2|w|\). La cancellation locale produit
aussi \(|v||w|^2\), qui exige le terme \(|V|^2|w|\) dans (20). Omettre
\(V\otimes V\) de \(G\) laisserait un trou.

### 9.6 Pression locale contre pression globale

La transformation de Riesz dans (2) est non locale. Une decomposition
locale \(q=q_{\mathrm{Riesz}}+h\), avec \(h\) harmonique mais sans borne
globale uniforme, ne permet pas (21)--(25).

### 9.7 Bord temporel \(t_0\)

\(V\) n'est pas uniformément \(L^4\) jusqu'à \(t_0\). On travaille d'abord
sur \([\delta,t]\), \(\delta>t_0\), puis (11)--(12), (4) et la convergence
absolue de (37) autorisent le passage au bord.

### 9.8 Inégalité exacte après absorption

L'absorption prouve seulement une borne énergétique. Réutiliser directement
(34) comme inégalité BSS perdrait le signe du transfert. La seconde passe à
partir de (16) est nécessaire pour retrouver (6).

### 9.9 Quantificateurs temporels

L'inégalité locale part d'abord de bons temps \(\delta\) et aboutit à presque
tout \(t\). La continuité forte (4) et l'intégrabilité de (37), et non une
convention implicite sur les représentants, permettent l'extension à tous
les temps.

### 9.10 Dépendance des constantes

La constante de (36) dépend de \(M\), de \(T\), des constantes de Lorentz,
de Sobolev, d'O'Neil, de Riesz et du noyau calorifique. Elle est indépendante
du rayon \(R\) et du bon temps \(\delta\) après insertion de (4). Aucune
uniformité lorsque \(T\to\infty\) n'est obtenue.

## 10. Statut logique et écart avec Clay

L'implication fermée est

\[
\begin{aligned}
 &v\text{ faible adaptée locale sur }\mathbb R^3\times[t_0,t_1],
 \quad q=\mathcal R_i\mathcal R_j(v_iv_j),
 \quad v\in L^\infty_tL^{3,\infty}_x,\\
 &\qquad\qquad w=v-e^{(t-t_0)\Delta}v(t_0)
 \in C_tL^2_x,\quad
 \|w(t)\|_2\lesssim M^2(t-t_0)^{1/4}\\
 &\Longrightarrow
 w\in L^2_t\dot H^1_x
 \text{ et }w\text{ satisfait l'inégalité globale BSS (6).}
\end{aligned}                                                  \tag{41}
\]

Ce résultat ferme le premier maillon énergétique laissé ouvert au cycle
0048. Il ne donne cependant pas :

- la continuité forte de \(v\) dans \(L^{3,\infty}\);
- la bornitude \(L^\infty_{t,x}\) ou la mildness ponctuelle KNSS;
- une décomposition unique et cohérente depuis \(t=-\infty\);
- un théorème de rigidité pour toute solution ancienne faible-\(L^3\);
- l'exclusion des scénarios Type II;
- une borne critique globale pour les solutions lisses du problème Clay.

Sur une solution ancienne, (41) peut être appliquée séparément à chaque
bande \([t_0,t_1]\). Les constantes croissent comme \(T^{1/2}\) et le champ
calorique dépend de \(t_0\); on ne peut donc pas envoyer automatiquement
\(t_0\to-\infty\) pour produire un correcteur énergétique global sur tout
le passé.

## 11. Conclusion de revue

**Décision : CONTINUER.** Le premier terme prétendument irréductible ne
l'est pas. La combinaison du gain sous-critique \(C_tL^2\), de l'estimation
calorifique \(L^4\), de la suitability locale et du contrôle global de la
pression de Riesz ferme

\[
 w\in L^2_t\dot H^1_x
 \quad\text{et}\quad
 \text{l'inégalité énergétique perturbée BSS}.                \tag{42}
\]

Verdicts de correction bloquante :

- **soustraction locale :** valide seulement après ajout de l'identité
  faible--forte croisée; une soustraction nue des énergies est invalide;
- **borne locale \(O(R)\) :** vraie et critique, mais insuffisante seule;
  l'absorption (23)--(25) est le gain supplémentaire;
- **pression :** le split Riesz (20a) est valide et chaque composante est
  faible-\(L^{3/2}\), mais c'est la pression de Riesz globale complète qui
  ferme le cutoff; une pression seulement locale ne suffit pas;
- **classe BSS :** sous le sens standard de « faible adaptée » incluant
  \(q\in L^{3/2}_{\rm loc}\), l'appartenance à la définition 1.1 est exacte
  sur la bande finie. Si « suitable locale » ne contient pas cette clause
  de pression et l'inégalité locale d'énergie, cette conclusion doit être
  retirée.

Les résultats publiés voisins globalisent l'énergie après avoir supposé la
classe dissipative. La promotion de \(C_tL^2\) vers
\(L^2_t\dot H^1\) donnée ici est donc une dérivation nouvelle du ledger,
pas une attribution à Barker--Seregin--Šverák ou à
Albritton--Barker; elle doit rester au statut
AI_INTERNAL_DERIVATION jusqu'à une revue externe.

Le prochain verrou n'est plus la dissipation du correcteur sur une bande
finie. Il est le raccord entre cette classe scindée, qui dépend du temps de
base, et une classe de rigidité ancienne : soit une cohérence uniforme quand
\(t_0\to-\infty\), soit un mécanisme supplémentaire donnant bornitude et
mildness forte sans supposer la continuité de norme dans
\(L^{3,\infty}\).
