# Cycle 0041 — Audit du pont Type I vers capture faible-\(L^3\)

**Statut :**

- `PUBLISHED_SOURCE_VERIFIED` uniquement pour le théorème de
  Barker–Prange explicitement identifié ci-dessous ;
- `AI_INTERNAL_DERIVATION` pour le passage faible-\(L^3\) vers Morrey, le
  quotient relatif et la présente passe contradictoire ;
- ne pas classer ces dérivations `PAPER_PROOF`.

**Verdict :** le pont est valide sous la borne Type I globale
\(L^\infty_tL^{3,\infty}_x\), avec une réserve de notation sur les constantes
de l'extension Lorentz. Il donne une concentration faible-\(L^3\) absolue,
centrée au point singulier, sur le rayon exact
\[
 2S_{w,*}(C_M M)^{-1/2}\sqrt{T^*-t},
\]
puis la fraction
\[
 K_{\rm core}(t)/K_{\rm global}(t)>\gamma_w/M.
\]
Le seuil \(\gamma_w>0\) est universel mais non numérique dans la source ;
\(S_{w,*}\) dépend de la borne Type I et n'est pas une constante absolue.
Rien de cette conclusion relative ne subsiste automatiquement en Type II.

## 1. Source primaire et contrôle de version

La source auditée est :

Tobias Barker et Christophe Prange,
[*Localized Smoothing for the Navier–Stokes Equations and Concentration of
Critical Norms Near Singularities*](https://arxiv.org/abs/1812.09115v2),
arXiv:1812.09115v2, version datée du 10 janvier 2019 dans le PDF.

La version publiée est :

Tobias Barker et Christophe Prange,
[*Localized Smoothing for the Navier–Stokes Equations and Concentration of
Critical Norms Near Singularities*](https://doi.org/10.1007/s00205-020-01495-6),
*Archive for Rational Mechanics and Analysis* **236** (2020), 1487–1541,
DOI 10.1007/s00205-020-01495-6. Une
[version auteur acceptée](https://wrap.warwick.ac.uk/id/eprint/144345/1/WRAP-Localized-smoothing-Navier%E2%80%93Stokes-critical-norms-singularities-Barker-2020.pdf)
a également été contrôlée page par page.

Les numéros diffèrent légèrement :

| Objet | arXiv v2 | version publiée |
|---|---:|---:|
| borne Type I de Morrey | (14) | (15) |
| concentration \(L^3\) | (15) | (16) |
| définition du temps inférieur dans la preuve | section 4.2 | (95) |
| extension \(L^{3,\infty}\) | appendice B | appendice B |

La publication ne réénonce pas un « Théorème 2 faible-\(L^3\) » autonome.
Le Théorème 2 est écrit en \(L^3\), puis le texte affirme explicitement que
l'Appendice B étend le résultat à \(L^{3,\infty}\). L'Appendice B remplace
les estimations nécessaires par les inégalités de Hunt et d'O'Neil et donne
les modifications des sections 2, 3 et 4. Il faut donc citer à la fois le
Théorème 2 et l'Appendice B ; citer le seul Théorème 2 ne justifie pas une
conclusion faible-\(L^3\).

## 2. Équation et notion de solution

La source considère Navier–Stokes incompressible tridimensionnel, non forcé,
sur l'espace entier, avec viscosité normalisée à un :

\[
 \partial_tu+u\cdot\nabla u-\Delta u+\nabla p=0,
 \qquad \nabla\cdot u=0
 \quad\text{dans }\mathbb R^3\times(0,\infty). \tag{1}
\]

Le résultat de concentration s'applique à une solution de Leray–Hopf
d'énergie finie qui développe ses premières singularités au temps fini
\(T^*>0\). Un point \((x^*,T^*)\) est dit singulier si aucun cylindre
\[
 B(x^*,r)\times(T^*-r^2,T^*)
\]
ne porte une borne \(L^\infty_{x,t}\) pour \(u\). Le théorème suppose
l'existence de ce point ; il ne construit ni blow-up ni solution singulière.

Dans le cadre demandé, on suppose

\[
 \sup_{0<t<T^*}\|u(t)\|_{L^{3,\infty}(\mathbb R^3)}
 \le M<\infty.                                  \tag{2}
\]

Cette hypothèse est critique pour le scaling Navier–Stokes et n'est pas une
conséquence de l'inégalité d'énergie. Elle définit précisément la branche
Type I faible-\(L^3\) auditée ici.

La convention de quasi-norme de la source est

\[
 \|f\|_{L^{3,\infty}(E)}
 =\sup_{\alpha>0}
 \alpha\,|\{x\in E:|f(x)|>\alpha\}|^{1/3}.      \tag{3}
\]

Des normes Lorentz équivalentes changeraient les constantes numériques du
raccord ci-dessous.

## 3. Théorème source exact

### 3.1 Borne Type I utilisée par Barker–Prange

Le Théorème 2 ne prend pas (2) comme hypothèse primitive. Il suppose qu'il
existe \(A<\infty\) et \(r_0\in(0,\infty]\) tels que

\[
 \sup_{\bar x\in\mathbb R^3}
 \sup_{0<r<r_0}
 \sup_{T^*-r^2<t<T^*}
 r^{-1/2}\|u(t)\|_{L^2(B(\bar x,r))}
 \le A.                                         \tag{4}
\]

Le troisième supremum doit être lu sur
\((0,T^*)\cap(T^*-r^2,T^*)\) lorsque le bord inférieur est négatif.
Il s'agit d'une borne Morrey critique locale en espace, uniforme dans une
fenêtre temporelle rétrospective.

### 3.2 Conclusion \(L^3\) imprimée

Il existe un seuil universel \(\gamma_{\rm univ}>0\), une durée normalisée
\[
 S_*(A)\in(0,1/4],
\]
et un temps inférieur \(t_*(T^*,A,r_0)<T^*\), tels que, si
\((x^*,T^*)\) est singulier,

\[
 \|u(t)\|_{L^3(B(x^*,\rho_A(t)))}
 >\gamma_{\rm univ},                            \tag{5}
\]

pour tout \(t\in(t_*,T^*)\), où le rayon imprimé est exactement

\[
 \boxed{
 \rho_A(t)
 =2\sqrt{\frac{T^*-t}{S_*(A)}}.}                \tag{6}
\]

Le coefficient n'est donc pas un \(O(1)\) universel : il vaut
\(2S_*(A)^{-1/2}\) et dépend de la taille Type I.

Dans la preuve publiée, équation (95),

\[
 t_*(T^*,A,r_0):=T^*-S_*(A)r_0^2.              \tag{7}
\]

L'énoncé place néanmoins \(t_*\) dans \([0,\infty)\), et le texte précise
que \(t_*=0\) lorsque \(r_0=\infty\). Pour un \(r_0\) fini tel que le membre
de droite de (7) est négatif, la formulation cohérente sur le domaine
temporel est

\[
 t_*^{\rm phys}=\max(0,T^*-S_*(A)r_0^2).       \tag{8}
\]

Il s'agit d'une petite incohérence éditoriale entre la formule de preuve et
le codomaine annoncé, sans effet dans notre application \(r_0=\infty\).

### 3.3 Extension \(L^{3,\infty}\)

L'Appendice B remplace le petit espace critique initial \(L^3\) par
\(L^{3,\infty}\) et reprend les quatre étapes nécessaires à la preuve.
La contraposition au point singulier donne donc des constantes

\[
 \gamma_w>0,\qquad S_{w,*}(A)\in(0,1/4]         \tag{9}
\]

telles que

\[
 \boxed{
 \|u(t)\|_{L^{3,\infty}(B(x^*,\rho_{w,A}(t)))}
 >\gamma_w,\qquad
 \rho_{w,A}(t)
 =2\sqrt{\frac{T^*-t}{S_{w,*}(A)}}}             \tag{10}
\]

pour les mêmes quantificateurs temporels.

Le seuil \(\gamma_w\) est universel, c'est-à-dire indépendant de
\(u,T^*,x^*,A,r_0,t\). La fonction \(S_{w,*}\) dépend de \(A\). La source
construit ces quantités au moyen de plusieurs petites constantes universelles
et estimations de bootstrap ; elle ne fournit pas de valeur numérique
certifiée.

Par prudence, (9) emploie des noms distincts de ceux du théorème \(L^3\).
L'Appendice B permet de diminuer les seuils afin d'obtenir une notation
commune, mais ne démontre pas que les valeurs maximales admissibles dans les
deux cadres soient identiques.

## 4. Passage exact de \(L^{3,\infty}\) à Morrey local \(L^2\)

Soit \(E\subset\mathbb R^3\) mesurable de volume \(V<\infty\), et posons

\[
 K=\|f\|_{L^{3,\infty}(\mathbb R^3)}.
\]

La fonction de distribution locale satisfait

\[
 |\{x\in E:|f(x)|>s\}|
 \le\min(V,K^3s^{-3}).                           \tag{11}
\]

Avec \(s_0=KV^{-1/3}\), la formule des couches donne

\[
 \begin{aligned}
 \int_E|f|^2
 &=2\int_0^\infty
   s\,|\{x\in E:|f(x)|>s\}|\,ds\\
 &\le2V\int_0^{s_0}s\,ds
   +2K^3\int_{s_0}^{\infty}s^{-2}\,ds\\
 &=K^2V^{1/3}+2K^2V^{1/3}
 =3K^2V^{1/3}.                                  \tag{12}
 \end{aligned}
\]

Cette constante \(3\) est optimale si l'on n'utilise que (11) : la
réarrangée \(f^*(a)=Ka^{-1/3}\) sur \(0<a<V\) réalise l'égalité.

Pour \(E=B(x,r)\), avec \(\omega_3=4\pi/3\),

\[
 \boxed{
 r^{-1/2}\|f\|_{L^2(B(x,r))}
 \le C_M\|f\|_{L^{3,\infty}},
 \qquad
 C_M=\sqrt3\,\omega_3^{1/6}.}                  \tag{13}
\]

La constante numérique associée à la convention (3) vaut

\[
 C_M=\sqrt3(4\pi/3)^{1/6}\approx2.19909.        \tag{14}
\]

L'hypothèse globale (2) implique donc (4) avec

\[
 A=C_MM,\qquad r_0=\infty.                     \tag{15}
\]

Le rayon de concentration obtenu après composition est

\[
 \boxed{
 \rho_M(t)=
 2\sqrt{\frac{T^*-t}{S_{w,*}(C_MM)}}.}          \tag{16}
\]

Puisque \(r_0=\infty\), la remarque suivant le Théorème 2 fixe \(t_*=0\).
La conclusion (10) vaut par conséquent pour tout

\[
 0<t<T^*.                                      \tag{17}
\]

Il ne s'agit donc pas seulement d'une suite \(t_n\uparrow T^*\), ni de
« presque tout temps assez proche ». Sous la borne globale à toutes les
échelles, le quantificateur publié est chaque temps positif antérieur au
premier blow-up.

## 5. Fraction du numérateur global

Définissons, avec la même convention de quasi-norme,

\[
 K_{\rm core}(t)
 =\|u(t)\|_{L^{3,\infty}(B(x^*,\rho_M(t)))},
 \qquad
 K_{\rm global}(t)
 =\|u(t)\|_{L^{3,\infty}(\mathbb R^3)}.         \tag{18}
\]

Les équations (2) et (10) donnent immédiatement

\[
 K_{\rm core}(t)>\gamma_w,\qquad
 K_{\rm global}(t)\le M.                       \tag{19}
\]

Une solution possédant un point singulier n'est pas le champ nul, donc
\(K_{\rm global}(t)>0\) pour \(0<t<T^*\). Ainsi

\[
 \boxed{
 \frac{K_{\rm core}(t)}{K_{\rm global}(t)}
 >\frac{\gamma_w}{M}}
 \qquad(0<t<T^*).                              \tag{20}
\]

La réponse à la question du cycle est donc **oui**, sous exactement les
hypothèses écrites. La source fournit la minoration absolue ; la division
par la borne globale \(M\) est une dérivation élémentaire distincte.

L'inégalité est stricte parce que le théorème source utilise \(>\gamma_w\).
Si l'on préfère une convention fermée robuste aux changements de
représentant, on peut enregistrer la version plus faible
\(\ge\gamma_w/M\).

## 6. Scaling

Sous

\[
 u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
 \qquad
 p_\lambda(x,t)=\lambda^2p(\lambda x,\lambda^2t), \tag{21}
\]

on a

\[
 \|u_\lambda(t)\|_{L^{3,\infty}}
 =\|u(\lambda^2t)\|_{L^{3,\infty}},             \tag{22}
\]

et

\[
 r^{-1/2}\|u_\lambda(t)\|_{L^2(B(x,r))}
 =(\lambda r)^{-1/2}
  \|u(\lambda^2t)\|_{L^2(B(\lambda x,\lambda r))}. \tag{23}
\]

Les deux hypothèses Type I, le seuil \(\gamma_w\), le quotient (20) et le
rapport \(\rho_M(t)/\sqrt{T^*-t}\) sont critiques. Le passage (13) ne perd
aucune puissance d'échelle.

## 7. Passe contradictoire

### 7.1 Norme forte versus norme faible

La minoration \(L^3\) imprimée au Théorème 2 n'entraîne pas une minoration
faible-\(L^3\), car
\[
 \|f\|_{L^{3,\infty}}\le\|f\|_{L^3}.
\]
Une grande norme forte peut provenir d'une distribution multi-niveaux dont
la norme faible reste petite. L'Appendice B est indispensable.

### 7.2 Dépendance des constantes

\(\gamma_w\) est universel, mais \(S_{w,*}(A)\) dépend de \(A=C_MM\).
Écrire simplement
\[
 \rho(t)=C\sqrt{T^*-t}
\]
avec un \(C\) universel serait faux. Le coefficient correct est
\(2S_{w,*}(C_MM)^{-1/2}\), potentiellement très grand lorsque \(M\) croît.

Le papier suit symboliquement les constantes universelles de ses itérations,
mais ne donne pas une valeur décimale ou rationnelle certifiée de
\(\gamma_w\) ou \(S_{w,*}\). Le présent audit ne transforme pas ces constantes
existentielles en constantes calculables.

### 7.3 Quantificateur temporel

Pour \(r_0<\infty\), le théorème ne vaut que lorsque
\[
 T^*-t<S_{w,*}(A)r_0^2.
\]
Pour \(r_0=\infty\), la source dit explicitement \(t_*=0\). L'hypothèse
globale faible-\(L^3\) donne précisément ce second cas. Remplacer « pour tout
\(t\) » par « pour une suite \(t_n\) » affaiblirait inutilement le résultat ;
l'étendre à \(t=0\) ou \(t=T^*\) serait en revanche incorrect.

### 7.4 Supremum pointwise versus supremum essentiel

Le Théorème 2 écrit un supremum temporel pointwise dans (4). Si (2) signifie
seulement
\[
 \mathop{\rm ess\,sup}_{0<t<T^*}
 \|u(t)\|_{L^{3,\infty}}\le M,                 \tag{24}
\]
alors (13) donne d'abord (4) pour presque tout temps. Pour une solution de
Leray–Hopf, la continuité faible dans \(L^2\) et la semi-continuité inférieure
des normes locales permettent de prolonger la borne de Morrey à tous les
temps pour le représentant faible continu.

Pour le quotient (20), la voie la plus conservatrice est soit d'assumer
le supremum pointwise comme dans la question, soit de n'affirmer (20) que
pour presque tout temps. Une extension pointwise de la borne
\(L^{3,\infty}\) peut aussi être obtenue par compacité faible-étoile contre
\(L^{3/2,1}\), mais ce choix de représentant doit être déclaré.

### 7.5 Centre

La boule de (10) est centrée au point singulier \(x^*\) fixé. Le théorème ne
sélectionne pas un centre \(x(t)\) après inspection du champ. C'est précisément
le gain par rapport à des concentrations dont le centre peut dériver.

### 7.6 Premier temps singulier

Le rescaling de la preuve transforme le point
\((x^*,T^*)\) en temps normalisé \(S_{w,*}(A)\). Le lissage local produit une
contradiction parce que ce point est supposé singulier. Sans singularité
connue, la contraposée ne sélectionne aucune boule.

La qualification « premier blow-up » garantit en outre le cadre régulier
antérieur utilisé dans l'application. Le résultat ne doit pas être appliqué
sans vérification à une solution faible arbitraire déjà singulière auparavant.

### 7.7 Force, domaine et viscosité

La source traite l'équation non forcée sur \(\mathbb R^3\), sans frontière,
avec viscosité un. Le résultat ne se transfère pas automatiquement :

- à un domaine borné ou au demi-espace ;
- à des conditions de bord ;
- à une force extérieure ;
- à Euler, aux modèles hyperdissipatifs ou aux équations compressibles.

Pour une viscosité \(\nu\ne1\), une renormalisation explicite est nécessaire
avant de réutiliser les constantes.

### 7.8 Nature de la concentration

La conclusion porte sur la vitesse dans \(L^{3,\infty}\). Elle ne fournit
directement :

- ni concentration de \(\operatorname{curl}u\) dans
  \(L^{3/2,\infty}\) ;
- ni contrôle de la pression locale ;
- ni compacité forte d'une suite rescalée ;
- ni solution ancienne limite ;
- ni théorème de rigidité ;
- ni champ localisé satisfaisant encore Navier–Stokes non forcé.

Le quotient (20) est seulement une capture du numérateur critique.

## 8. Limite Type II

Si

\[
 \sup_{0<t<T^*}\|u(t)\|_{L^{3,\infty}}=\infty, \tag{25}
\]

le passage (13) ne produit aucune constante Type I uniforme \(A\).
On ne dispose alors ni d'une durée normalisée fixe
\(S_{w,*}(A)\), ni d'un rayon avec coefficient uniforme, ni d'un dénominateur
global \(M\) pour (20).

Même si une concentration absolue pouvait être prouvée le long d'une suite,
elle n'impliquerait pas
\[
 K_{\rm core}/K_{\rm global}\ge c>0,
\]
car \(K_{\rm global}\) peut diverger plus vite, se répartir entre plusieurs
centres ou se déplacer vers des échelles non paraboliques.

Il est également invalide de prendre
\(A=A(t)=C_M\|u(t)\|_{L^{3,\infty}}\) dans le théorème : l'hypothèse (4)
contrôle une fenêtre temporelle entière proche de \(T^*\), pas seulement une
tranche instantanée. Cette inversion de quantificateurs est le premier
contre-argument Type II.

## 9. Hypothèses silencieuses à conserver

Le pont complet utilise toutes les hypothèses suivantes :

1. Navier–Stokes incompressible tridimensionnel exact ;
2. domaine \(\mathbb R^3\), sans frontière ;
3. force nulle et viscosité normalisée à un ;
4. solution de Leray–Hopf d'énergie finie dans la classe de la source ;
5. premier temps singulier fini \(T^*\) ;
6. point singulier spatial fixé \(x^*\) ;
7. borne Type I globale faible-\(L^3\), et non simple finitude à chaque temps ;
8. même convention de quasi-norme Lorentz que (3) pour la constante (13) ;
9. interprétation pointwise du supremum temporel, ou traitement déclaré des
   temps exceptionnels ;
10. extension \(L^{3,\infty}\) de l'Appendice B, pas le seul Théorème 2
    \(L^3\) ;
11. dépendance \(S_{w,*}=S_{w,*}(C_MM)\) conservée dans le rayon ;
12. rayon \(r_0=\infty\), obtenu grâce au caractère global de (2) ;
13. absence de conclusion au temps terminal lui-même ;
14. aucune identification de la concentration statique avec une solution
    Navier–Stokes localisée.

## 10. Verdict logique final

L'implication auditée est

\[
 \begin{aligned}
 &u\text{ Leray--Hopf sur }\mathbb R^3,\quad
 (x^*,T^*)\text{ premier point singulier},\\
 &\sup_{0<t<T^*}\|u(t)\|_{L^{3,\infty}}\le M\\
 &\Longrightarrow
 \forall t\in(0,T^*),\
 \|u(t)\|_{L^{3,\infty}(B(x^*,\rho_M(t)))}>\gamma_w\\
 &\Longrightarrow
 \forall t\in(0,T^*),\
 \frac{K_{\rm core}(t)}{K_{\rm global}(t)}
 >\frac{\gamma_w}{M},
 \end{aligned}                                  \tag{26}
\]

avec

\[
 C_M=\sqrt3(4\pi/3)^{1/6},\qquad
 \rho_M(t)=2S_{w,*}(C_MM)^{-1/2}\sqrt{T^*-t}.   \tag{27}
\]

La première flèche combine un théorème publié et l'injection élémentaire
(13). La seconde est une dérivation interne immédiate. Ce résultat ferme le
verrou de capture relative du numérateur **uniquement dans la branche
Type I**. Le prochain verrou reste le contrôle au même centre d'une quantité
de vorticité critique, ou une substitution Type II ne supposant aucune borne
globale \(M\).

**Formulation prudente à retenir dans le registre :** employer les constantes
propres à l'extension, \(\gamma_w,S_{w,*}\), conserver leur dépendance en
\(C_MM\), et écrire « pour tout \(t\in(0,T^*)\) » seulement lorsque la borne
(2) est pointwise ou qu'un lemme de représentant a été invoqué. Sous la seule
notation usuelle \(L^\infty_t\) comprise comme supremum essentiel, enregistrer
le quotient pour presque tout \(t\), tout en conservant la concentration
source via la borne Morrey prolongée. Toute identification non justifiée
\(\gamma_w=\gamma_{\rm univ}\), toute indépendance de \(S_{w,*}\) par rapport
à \(M\), ou toute omission du point de représentant temporel doit être
classée `À_RÉVISER`.
