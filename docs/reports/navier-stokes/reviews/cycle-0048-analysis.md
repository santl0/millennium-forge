# Cycle 0048 — trace faible-étoile et Duhamel à l'endpoint faible-\(L^3\)

Date : 2026-08-15.

Statut : AI_INTERNAL_DERIVATION appuyée sur l'estimation publiée de
Yamazaki; aucun résultat Clay, aucune simulation.

## Verdict

Soit \(I=[t_0,t_1]\) et soit \(v\) une solution distributionnelle de
Navier–Stokes incompressible non forcé sur \(\mathbb R^3\times(t_0,t_1)\),
telle que

\[
 \operatorname{div}v=0,\qquad
 v\in L^\infty(I;L^{3,\infty}(\mathbb R^3)),     \tag{1}
\]

avec pression dans la jauge globale

\[
 q=\mathcal R_i\mathcal R_j(v_iv_j).             \tag{2}
\]

Alors :

1. \(v\) possède un représentant unique

\[
 \boxed{
 v\in C_{w^*}(I;L^{3,\infty}_\sigma).}           \tag{3}
\]

2. Pour tous \(t_0\leq s<t\leq t_1\), la formule

\[
 \boxed{
 v(t)=e^{(t-s)\Delta}v(s)
 -\int_s^t e^{(t-\tau)\Delta}
   \mathbb P\operatorname{div}(v\otimes v)(\tau)\,d\tau}          \tag{4}
\]

vaut comme égalité dans \(L^{3,\infty}_\sigma\), à condition d'interpréter
l'intégrale comme une intégrale faible-étoile, ou de Gelfand, contre le
prédual \(L^{3/2,1}_\sigma\). Elle n'est pas obtenue comme intégrale de
Bochner de la norme \(L^{3,\infty}\).

3. Ce résultat ferme la formule de Duhamel endpoint faible-étoile. Il ne
donne pas

\[
 v\in C(I;L^{3,\infty})                          \tag{5}
\]

en norme. Or la définition publiée usuelle d'une solution mild
\(L^{3,\infty}\) impose précisément cette continuité forte, en plus de
l'identité duale. Le premier gap restant est donc la promotion

\[
 C_{w^*}(I;L^{3,\infty})
 \quad -?\!\!\longrightarrow\quad
 C(I;L^{3,\infty}),                              \tag{6}
\]

ou une hypothèse de remplacement telle que l'appartenance au sous-espace de
continuité du semi-groupe \(\widetilde L^{3,\infty}\).

4. La scission Barker–Seregin–Šverák et la mildness bornée de
Koch–Nadirashvili–Seregin–Šverák restent plus fortes. Une estimation
sous-critique séparée donne bien au correcteur
\(w=v-e^{(t-t_0)\Delta}v(t_0)\) la propriété
\(w\in C_tL^2_x\) sur toute bande finie. Elle ne donne pas
\(w\in L^2_t\dot H^1_x\), l'inégalité d'énergie perturbée globale, une borne
\(L^\infty_x\), ni la formule ponctuelle absolument convergente du noyau
d'Oseen.

Le verdict est donc POSITIF pour (3) et pour la version faible-étoile de
(4), mais RÉVISER toute affirmation de mildness forte, de classe scindée BSS
ou de classe bornée KNSS.

## 1. Préduaux Lorentz et projection de Leray

Fixons les espaces

\[
 X=L^{3,\infty}_\sigma(\mathbb R^3),\qquad
 Y=L^{3/2,1}_\sigma(\mathbb R^3).                \tag{7}
\]

Dans la convention de normes Lorentz,

\[
 X=Y^*.                                          \tag{8}
\]

L'espace \(Y\) est séparable et les champs solénoïdaux de Schwartz y sont
denses. La projection de Leray \(\mathbb P\) est bornée sur
\(L^{p,r}\) pour \(1<p<\infty\), \(1\leq r\leq\infty\); elle est auto-adjointe
dans les dualités compatibles et commute avec le semi-groupe de la chaleur.

Le produit de Lorentz d'O'Neil donne, presque partout en temps,

\[
 F:=v\otimes v\in L^{3/2,\infty},\qquad
 \|F(t)\|_{L^{3/2,\infty}}
 \leq C_O\|v(t)\|_{L^{3,\infty}}^2.              \tag{9}
\]

Le prédual de \(L^{3/2,\infty}\) utilisé pour ce produit est
\(L^{3,1}\), et non \(L^{3/2,1}\). Les deux niveaux de dualité sont donc

\[
 \begin{aligned}
 L^{3,\infty}&=(L^{3/2,1})^*,\\
 L^{3/2,\infty}&=(L^{3,1})^*.
 \end{aligned}                                   \tag{10}
\]

La pression de Riesz (2) vérifie

\[
 q\in L^\infty(I;L^{3/2,\infty}),\qquad
 \|q(t)\|_{3/2,\infty}\leq C_R\|v(t)\|_{3,\infty}^2.              \tag{11}
\]

Surtout, (2) autorise l'équation projetée globale

\[
 \partial_tv-\Delta v
 +\mathbb P\operatorname{div}F=0                \tag{12}
\]

dans les distributions tempérées. Une pression seulement locale, définie
modulo une composante harmonique ou affine non contrôlée, ne suffit pas à
identifier sans travail supplémentaire la formulation globale (12).

## 2. Construction du représentant \(C_{w^*}\)

Soit \(\phi\) un champ solénoïdal de Schwartz. En testant (12),

\[
 \frac d{dt}\langle v(t),\phi\rangle
 =\langle v(t),\Delta\phi\rangle
 +\langle F(t),\nabla\mathbb P\phi\rangle        \tag{13}
\]

dans les distributions en temps. Les deux termes du membre droit sont dans
\(L^\infty(I)\), car

\[
 \begin{aligned}
 |\langle v,\Delta\phi\rangle|
 &\leq \|v\|_{3,\infty}\|\Delta\phi\|_{3/2,1},\\
 |\langle F,\nabla\mathbb P\phi\rangle|
 &\leq \|F\|_{3/2,\infty}
       \|\nabla\mathbb P\phi\|_{3,1}.            \tag{14}
 \end{aligned}
\]

Ainsi \(t\mapsto\langle v(t),\phi\rangle\) admet un représentant absolument
continu pour tout \(\phi\) de cette classe dense.

Choisissons un ensemble dénombrable dense
\(\{\phi_m\}_{m\geq1}\subset Y\). Les représentants scalaires issus de (13)
définissent simultanément, à chaque \(t\in I\), une forme linéaire sur leur
span. La borne essentielle

\[
 M=\operatorname*{ess\,sup}_{t\in I}\|v(t)\|_X  \tag{15}
\]

et un passage à la limite depuis des temps de Lebesgue donnent une extension
de norme au plus \(M\) à tout \(Y\). Par (8), cette forme est un élément de
\(X\), noté encore \(v(t)\).

Pour \(\phi\in Y\), choisissons \(\phi_m\to\phi\) dans \(Y\). Uniformément en
\(t\),

\[
 |\langle v(t),\phi-\phi_m\rangle|
 \leq M\|\phi-\phi_m\|_Y.                        \tag{16}
\]

La continuité des pairings avec \(\phi_m\), puis (16), donnent la continuité
avec \(\phi\). On obtient (3), y compris les limites unilatérales aux
endpoints \(t_0,t_1\). Le même argument conserve
\(\operatorname{div}v(t)=0\) à chaque temps.

Ce représentant est unique : deux représentants faible-étoile continus qui
coïncident presque partout ont les mêmes pairings sur un ensemble dense de
temps, puis partout par continuité.

## 3. Formule distributionnelle de Duhamel

La variation des constantes appliquée à (12) donne d'abord, pour
\(t_0<s<t<t_1\),

\[
 v(t)=e^{(t-s)\Delta}v(s)
 -\int_s^t e^{(t-\tau)\Delta}
   \mathbb P\operatorname{div}F(\tau)\,d\tau     \tag{17}
\]

dans \(\mathcal S'(\mathbb R^3)\). À ce niveau, l'intégrale ne pose aucune
difficulté au bord \(\tau=t\) : pour un test de Schwartz fixé, le
semi-groupe agit sur le test et
\(\nabla e^{(t-\tau)\Delta}\mathbb P\phi\) reste dans
\(L^{3,1}\).

Plus explicitement,

\[
 \begin{aligned}
 \langle v(t),\phi\rangle
 ={}&\langle v(s),e^{(t-s)\Delta}\phi\rangle\\
 &+\int_s^t
 \langle F(\tau),
 \nabla e^{(t-\tau)\Delta}\mathbb P\phi\rangle\,d\tau.           \tag{18}
 \end{aligned}
\]

Le signe positif dans la seconde ligne correspond au signe négatif de
l'intégrale vectorielle dans (17), car

\[
 \langle\mathbb P\operatorname{div}F,\phi\rangle
 =-\langle F,\nabla\mathbb P\phi\rangle.          \tag{19}
\]

L'identité (18) s'étend à \(s=t_0\) et \(t=t_1\) grâce au représentant (3)
et à la continuité faible-étoile du semi-groupe.

Cette formule distributionnelle seule ne permet pas encore d'affirmer que
l'intégrale vectorielle appartient à \(X\). C'est précisément l'étape fermée
par Yamazaki.

## 4. Estimation de Yamazaki et intégrale endpoint

L'estimation ponctuelle d'opérateur est critique :

\[
 \|\nabla e^{h\Delta}\mathbb P\|_
 {L^{3/2,\infty}\to L^{3,\infty}}
 \leq Ch^{-1}.                                   \tag{20}
\]

Son intégrale diverge logarithmiquement en \(h=0\). Il serait néanmoins faux
d'en conclure que le terme de Duhamel n'existe pas dans \(X\), car (20)
prend le supremum sur les données avant l'intégration en temps.

L'estimation de Meyer–Yamazaki, dans la forme duale exacte nécessaire ici,
est

\[
 \int_s^t
 \left|
 \langle G(\tau),
 \nabla e^{(t-\tau)\Delta}\mathbb P\phi\rangle
 \right|\,d\tau
 \leq C
 \|G\|_{L^\infty(s,t;L^{3/2,\infty})}
 \|\phi\|_{L^{3/2,1}}.                           \tag{21}
\]

Elle vaut pour
\(G\in L^\infty_tL^{3/2,\infty}_x\) et
\(\phi\in Y\). Elle résulte de l'intégrabilité temporelle Lorentz du gradient
du semi-groupe dans \(L^{3,1}\), à la paire

\[
 \frac1{3/2}-\frac13=\frac13.                   \tag{22}
\]

La source primaire est Yamazaki, The Navier–Stokes equations in the
weak-\(L^n\) space with time-dependent external force, Math. Ann. 317
(2000), DOI 10.1007/PL00004418. Une réénonciation publiée directement
lisible est le lemme 7 de
On uniqueness of mild \(L^{3,\infty}\)-solutions on the whole time axis,
Math. Ann. (2024), DOI 10.1007/s00208-023-02702-x.

Définissons, indépendamment de l'équation satisfaite par \(v\),
\(\mathfrak B_{s,t}(F)\) par

\[
 \langle\mathfrak B_{s,t}(F),\phi\rangle
 :=
 -\int_s^t
 \langle F(\tau),
 \nabla e^{(t-\tau)\Delta}\mathbb P\phi\rangle\,d\tau.           \tag{23}
\]

L'estimation (21) montre que (23) est une forme linéaire bornée sur \(Y\).
Par (8),

\[
 \mathfrak B_{s,t}(F)\in X,\qquad
 \|\mathfrak B_{s,t}(F)\|_X
 \leq C\|F\|_{L^\infty(s,t;L^{3/2,\infty})}
 \leq CC_OM^2.                                  \tag{24}
\]

Il n'y a aucune circularité dans cette définition : l'élément de \(X\) est
construit par (21) avant d'utiliser l'identité (18). L'égalité dans
\(\mathcal S'\) identifie ensuite (23) au terme non linéaire de (17).
Comme les deux membres sont dans \(X\), (4) est une égalité dans \(X\).

L'intégrale (23) est une intégrale faible-étoile de Gelfand. Le ledger ne
prouve pas

\[
 \int_s^t
 \|e^{(t-\tau)\Delta}\mathbb P\operatorname{div}F(\tau)\|_X
 \,d\tau<\infty,                                \tag{25}
\]

qui est précisément ce que l'estimation \(h^{-1}\) ne fournit pas.

## 5. Comportement au bord \(t=s\)

Pour chaque test \(\phi\in Y\), l'intégrande scalaire de (23) est intégrable
par (21). L'absolue continuité de l'intégrale donne

\[
 \langle\mathfrak B_{s,t}(F),\phi\rangle\to0
 \quad\text{lorsque }t\downarrow s.              \tag{26}
\]

Donc le terme bilinéaire tend vers zéro faible-étoile.

En revanche, (24) est invariant par l'échelle critique et ne contient aucun
facteur tendant vers zéro avec \(t-s\). Il ne donne pas

\[
 \|\mathfrak B_{s,t}(F)\|_X\to0.                 \tag{27}
\]

De même, le semi-groupe de la chaleur est faible-étoile continu sur tout
\(L^{3,\infty}\), parce que son adjoint est fortement continu sur
\(L^{3/2,1}\), mais il n'est pas fortement continu sur tout
\(L^{3,\infty}\).

Ainsi (4) est compatible exactement avec (3), et pas automatiquement avec
(5). Utiliser (4) pour affirmer (5) en citant seulement (21) inverserait les
quantificateurs :

\[
 \forall\phi,\ \int |\cdots_\phi|<\infty
 \quad\not\Rightarrow\quad
 \int \sup_{\|\phi\|_Y\leq1}|\cdots_\phi|<\infty.                \tag{28}
\]

## 6. Quantificateurs temporels

La construction fournit un unique représentant pour lequel (4) vaut
simultanément pour tous

\[
 t_0\leq s<t\leq t_1.                            \tag{29}
\]

Le produit \(v\otimes v\) n'a besoin d'être défini que presque partout en
temps; ses valeurs aux temps exceptionnels n'affectent pas (23). En
revanche, le terme \(v(s)\) de (4) exige le représentant (3). Écrire la
formule « pour tout \(s\) » avant de construire cette trace est illégitime.

Si \(v\) est ancienne sur \((-\infty,T]\) et si

\[
 \sup_{\tau<T}\|v(\tau)\|_{3,\infty}\leq M,       \tag{30}
\]

alors (21) est uniforme sur \((-\infty,t)\). De plus,

\[
 e^{(t-s)\Delta}\phi\to0
 \quad\text{dans }L^{3/2,1}
 \quad\text{lorsque }s\to-\infty.                \tag{31}
\]

La première ligne de (18) disparaît faible-étoile et l'on obtient

\[
 \langle v(t),\phi\rangle
 =
 \int_{-\infty}^t
 \langle v(\tau)\otimes v(\tau),
 \nabla e^{(t-\tau)\Delta}\mathbb P\phi\rangle\,d\tau.           \tag{32}
\]

Cette formule entière est encore faible-étoile. Elle ne donne ni continuité
forte de la trajectoire, ni décroissance de sa norme vers le passé.

## 7. Quatre notions à ne pas confondre

### 7.1 Formule distributionnelle

La version la plus faible est (17) dans \(\mathcal S'\), testée contre des
fonctions de Schwartz. À ce niveau, le bord \(\tau=t\) est bénin parce que le
test est fixé et lissé à rebours. Cette formule ne déclare aucune intégrale
vectorielle dans \(L^{3,\infty}\).

### 7.2 Duhamel endpoint faible-étoile

Les équations (21)–(24) renforcent la formule : chaque terme de (4) est un
élément de \(X=Y^*\), et l'identité vaut contre tout
\(\phi\in Y\). La trajectoire est \(C_{w^*}\). C'est la conclusion exacte du
lemme actif.

### 7.3 Solution mild faible-\(L^3\) au sens publié

La définition Yamazaki reprise dans la littérature récente demande

\[
 v\in C(I;L^{3,\infty}_\sigma)                  \tag{33}
\]

en norme, ainsi que l'identité duale pour tous \(s<t\). La conclusion du
présent audit remplit l'identité mais seulement
\(C_{w^*}\), pas (33). La petitesse de Yamazaki intervient dans les théorèmes
d'existence et d'unicité par point fixe; elle n'est pas nécessaire pour
représenter une solution déjà donnée, mais son absence interdit d'importer
les conclusions de contraction.

Un cadre intermédiaire naturel est

\[
 \widetilde L^{3,\infty}
 =
 \overline{L^{3,\infty}\cap L^\infty}^{\,
 \|\cdot\|_{3,\infty}},                          \tag{34}
\]

sur lequel le semi-groupe possède de meilleures propriétés de continuité.
Rien dans (1) ne place automatiquement chaque \(v(t)\) dans (34).

### 7.4 Classe scindée Barker–Seregin–Šverák

À partir d'une donnée initiale \(u_0\in L^{3,\infty}_\sigma\), cette classe
impose

\[
 v(t)=e^{(t-t_0)\Delta}u_0+w(t),                 \tag{35}
\]

avec

\[
 w\in L^\infty_tL^2_x\cap L^2_t\dot H^1_x,       \tag{36}
\]

une trace énergétique nulle pour \(w\) au temps initial, une inégalité
d'énergie globale perturbée et une inégalité locale. La formule (4) identifie
formellement \(w\) au terme bilinéaire.

Il faut ici ajouter le gain sous-critique que l'estimation endpoint (24) ne
montre pas. Si \(K_h\) est le noyau de
\(e^{h\Delta}\mathbb P\operatorname{div}\), alors, pour
\(3/2<p<3\) et

\[
 \frac1k=\frac13+\frac1p,
\]

\[
 \|K_h\|_{L^{k,1}}
 \leq C_ph^{-3/2+3/(2p)}.                        \tag{36a}
\]

La convolution d'O'Neil et l'intégration en temps donnent

\[
 \|w(t)\|_{L^p}
 \leq C_pM^2(t-t_0)^{(3-p)/(2p)},\qquad
 w\in C([t_0,t_1];L^p).                          \tag{36b}
\]

En particulier,

\[
 w\in C([t_0,t_1];L^2),\qquad
 \|w(t)\|_2\leq CM^2(t-t_0)^{1/4}.               \tag{36c}
\]

La partie \(L^\infty_tL^2_x\) et la trace forte nulle du correcteur sont donc
héritées. En revanche, une dérivée spatiale supplémentaire change, pour
\(p=2\), le noyau temporel \(h^{-3/4}\) en \(h^{-5/4}\). La taille critique
seule ne donne ni
\[
 \nabla w\in L^2((t_0,t_1)\times\mathbb R^3),
\]
ni l'inégalité d'énergie perturbée globale. Ce sont les premières clauses BSS
encore absentes.

La classe BSS complète est donc strictement plus structurée que le lemme
actif. Sa stabilité faible-étoile ne peut pas être invoquée en retour pour
prouver la dissipation et l'inégalité globale : ce serait supposer les
clauses que l'on cherche à obtenir.

### 7.5 Ancienne mild bornée KNSS

La classe utilisée par Koch–Nadirashvili–Seregin–Šverák exige une solution
ancienne mild bornée en vitesse, avec formule de noyau d'Oseen/Leray sur les
bandes temporelles pertinentes. La borne

\[
 v\in L^\infty_tL^{3,\infty}_x                 \tag{37}
\]

n'implique pas

\[
 v\in L^\infty_{t,x}.                            \tag{38}
\]

L'identité faible-étoile (32) ne fournit pas non plus, sans lissage
supplémentaire, une formule ponctuelle absolument convergente. Le passage
vers KNSS manque donc d'abord de bornitude ou d'un mécanisme de
régularisation endpoint, puis de l'identification avec leur notion mild
ponctuelle.

## 8. Première erreur possible et circularités

Le calcul ferme une erreur négative et révèle une erreur positive.

**Erreur négative réfutée.** La singularité \(h^{-1}\) de la norme
d'opérateur (20) ne réfute pas l'existence du terme de Duhamel dans
\(L^{3,\infty}\). La dualité et (21) construisent bien cet élément.

**Erreur positive restante.** L'existence de cet élément dual ne prouve pas
la convergence de Bochner, la petitesse en norme sur les intervalles courts,
ni la continuité forte. Appeler immédiatement \(v\) « mild au sens
Yamazaki » serait donc trop fort.

Les circularités précises à exclure sont :

1. définir l'intégrale non linéaire par
   \(e^{(t-s)\Delta}v(s)-v(t)\), puis conclure qu'elle existe dans \(X\);
   (23) doit être construit indépendamment par (21);
2. invoquer la stabilité BSS pour produire le correcteur énergétique, alors
   que l'appartenance à la classe scindée est une hypothèse de cette
   stabilité;
3. invoquer l'unicité des petites solutions Yamazaki sans petitesse;
4. utiliser une définition mild qui exige \(C_tL^{3,\infty}\) après avoir
   seulement démontré \(C_{w^*}\);
5. remplacer la borne intégrée test par test de (21) par l'intégrale du
   supremum de (28).

## 9. Passe contradictoire

1. **Prédual incorrect.** La trace de \(v\) se teste dans
   \(L^{3/2,1}\); le stress \(v\otimes v\) se teste dans \(L^{3,1}\).
   Échanger ces espaces invalide (14) et (21).
2. **Projection omise.** La formule globale porte sur
   \(\mathbb P\operatorname{div}(v\otimes v)\). Dans la dualité, le test
   devient \(\nabla e^{h\Delta}\mathbb P\phi\). Une pression locale ne
   remplace pas ce ledger.
3. **Signe.** Le terme vectoriel de Duhamel est négatif, tandis que son
   pairing avec le stress est positif par l'intégration par parties (19).
4. **Temps exceptionnel.** La borne essentielle initiale ne donne pas une
   valeur \(v(s)\) à tout temps. Le représentant (3) doit être construit
   avant (29).
5. **Bord diagonal.** L'estimation brute \(h^{-1}\) diverge; Yamazaki
   intègre après fixation du test. Aucun argument de Fubini avec l'intégrale
   des normes \(X\) n'est autorisé.
6. **Continuité forte du semi-groupe.** Elle est fausse sur tout
   \(L^{3,\infty}\). Elle vaut faible-étoile par action sur le prédual, et
   fortement sur des sous-espaces plus petits.
7. **Petitesse.** Aucune petitesse n'est nécessaire pour l'identité d'une
   solution donnée. Elle redevient indispensable pour les conclusions de
   contraction ou d'unicité de Yamazaki.
8. **BSS.** Un terme bilinéaire borné dans faible-\(L^3\) n'est pas un
   correcteur d'énergie globale. La queue spatiale peut garder une énergie
   infinie.
9. **KNSS.** Une formule faible contre
   \(L^{3/2,1}\) n'est pas encore une solution ancienne bornée et lisse.
   Aucun théorème de Liouville KNSS ne s'applique à (32) seul.
10. **Passé infini.** Dans (32), le terme calorique disparaît seulement
    faible-étoile. Aucune convergence de
    \(\|e^{(t-s)\Delta}v(s)\|_{3,\infty}\) vers zéro n'est démontrée.
11. **Unicité.** Le représentant temporel est unique pour une solution
    distributionnelle donnée; cela ne prouve pas l'unicité de deux solutions
    ayant la même trace.
12. **Clay.** Fermer la formule endpoint ne contrôle ni Type II, ni la
    bornitude spatiale, ni un théorème de rigidité ancien général.

## 10. Statut logique et premier gap

L'implication auditée est

\[
 \begin{aligned}
 &v\text{ distributionnelle sur }\mathbb R^3\times I,\quad
 \operatorname{div}v=0,\quad
 v\in L^\infty_IL^{3,\infty}_x,\quad
 q=\mathcal R_i\mathcal R_j(v_iv_j)\\
 &\Longrightarrow
 v\in C_{w^*}(I;L^{3,\infty}_\sigma)\\
 &\Longrightarrow
 \text{Duhamel pour tout }s<t
 \text{ comme égalité faible-étoile dans }L^{3,\infty}.
 \end{aligned}                                                     \tag{39}
\]

Le premier gap restant est

\[
 \boxed{
 \text{Duhamel }C_{w^*}L^{3,\infty}
 \quad -?\!\!\longrightarrow\quad
 C_tL^{3,\infty}\text{ mild, ou classe de rigidité équivalente}.} \tag{40}
\]

Deux branches ultérieures doivent rester séparées :

\[
 \begin{aligned}
 &\text{branche BSS : obtenir le correcteur énergétique global (36);}\\
 &\text{branche KNSS : obtenir d'abord }L^\infty_{t,x}
   \text{ et la mildness bornée correspondante.}
 \end{aligned}                                                     \tag{41}
\]

Verdict de revue : CONTINUER. La trace faible-étoile et l'identité Duhamel
endpoint sont fermées. RÉVISER le graphe qui marquerait encore toute formule
Duhamel comme absente; conserver en revanche le gap de continuité forte,
de scission énergétique et de bornitude KNSS.
