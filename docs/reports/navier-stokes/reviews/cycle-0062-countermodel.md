# Cycle 0062 — signes instantanés de numérateurs modaux SO(2)

Date d'exécution : 2026-08-15

## Verdict

Deux certificats exacts indépendants produisent des coefficients modaux de signes opposés pour des champs de Schwartz divergence-free sur \(\mathbb R^3\).

Pour l'opérateur instantané

\[
d_\kappa(Z)
=
\Delta Z
-\mathbb P\operatorname{div}(Z\otimes Z)
-\kappa(1+y\cdot\nabla)Z,
\tag{1}
\]

et les projections isotypiques réelles \(\Pi_m\), posons

\[
C_m
=
\left\langle
\Pi_md_\kappa(Z),
\mathcal R\Pi_mZ
\right\rangle_{L^2(\mathbb R^3)}.
\tag{2}
\]

Une triade \(m=1,2,3\) donne, pour tout \(\kappa\),

\[
\boxed{
(C_1,C_2,C_3)
=
\left(
-\frac89,\frac{16}{9},-\frac{16}{3}
\right)
\left(\frac{\pi}{3}\right)^{3/2}.}
\tag{3}
\]

Une seconde famille \(m=1,3\), pilotée uniquement par le terme de similarité, donne à \(\kappa=1\)

\[
\boxed{
(C_1,C_3)
=
\left(
\frac72,-\frac{99}{2}
\right)
\left(\frac{\pi}{2}\right)^{3/2}.}
\tag{4}
\]

La première famille testée, limitée aux modes \(m=1,2\), échoue : sur 576 orientations rationnelles,

\[
C_2=2C_1,
\]

donc aucun signe opposé. Cet échec est conservé.

Ces calculs sont instantanés. Ils ne construisent ni trajectoire globale ni orbite Type I.

## 1. Champs polynomial–gaussiens et isotypes

Écrivons

\[
G(y)=e^{-|y|^2},
\qquad
y=(x_1,x_2,x_3).
\]

Pour un polynôme azimutal réel \(h_m\), définissons

\[
A_m=h_mG\,e_3,
\qquad
Z_m=\nabla\times A_m.
\tag{5}
\]

Chaque \(Z_m\) est un champ de Schwartz et

\[
\nabla\cdot Z_m=0.
\tag{6}
\]

Soit \(\rho_\theta U(y)=Q_\theta U(Q_{-\theta}y)\) l'action des rotations autour de \(e_3\), et \(\mathcal R\) son générateur. Les harmoniques

\[
\Re(x_1+ix_2)^m,
\qquad
\Im(x_1+ix_2)^m
\]

engendrent l'isotype réel \(m\). Le script vérifie directement, au niveau des polynômes,

\[
\mathcal R^2Z_m=-m^2Z_m
\tag{7}
\]

et

\[
\nabla\cdot(\mathcal RZ_m)=0.
\tag{8}
\]

Les valeurs de Gram sont strictement positives dans les deux familles retenues. Les champs contiennent donc réellement plusieurs isotypes non nuls.

## 2. Élimination justifiée de la pression

Cette étape précède le calcul convectif.

Posons

\[
T_m=\mathcal RZ_m.
\]

Par (8), \(T_m\) est solénoïdal ; comme \(Z_m\) est de Schwartz, \(T_m\) l'est aussi. Pour tout champ suffisamment intégrable \(F\),

\[
\langle\mathbb PF,T_m\rangle_{L^2}
=
\langle F,\mathbb PT_m\rangle_{L^2}
=
\langle F,T_m\rangle_{L^2}.
\tag{9}
\]

De façon équivalente, le terme de pression vérifie

\[
\int_{\mathbb R^3}\nabla p\cdot T_m\,dy
=
-\int_{\mathbb R^3}p\,\nabla\cdot T_m\,dy
=0,
\tag{10}
\]

sans terme de bord grâce à la décroissance rapide.

Par ailleurs, \(\Pi_m\) est la projection orthogonale sur l'isotype \(m\) et \(T_m\) appartient à cet isotype. Ainsi,

\[
\langle\Pi_mF,T_m\rangle
=
\langle F,T_m\rangle.
\tag{11}
\]

Ce n'est qu'après (9)–(11) que le script remplace

\[
\left\langle
\Pi_m\mathbb P\operatorname{div}(Z\otimes Z),T_m
\right\rangle
\]

par l'appariement sans pression. Puisque \(\nabla\cdot Z=0\),

\[
\operatorname{div}(Z\otimes Z)=(Z\cdot\nabla)Z.
\tag{12}
\]

## 3. Intégration gaussienne exacte

Toutes les composantes ont la forme \(P(y)G(y)\). Les appariements linéaires portent donc \(e^{-2|y|^2}\), tandis que le terme cubique porte \(e^{-3|y|^2}\).

Le script représente chaque polynôme par un dictionnaire de coefficients **Fraction** et utilise

\[
\frac{
\displaystyle\int_{\mathbb R}x^{2q}e^{-a x^2}\,dx
}{
\sqrt{\pi/a}
}
=
\frac{(2q-1)!!}{(2a)^q},
\tag{13}
\]

avec annulation exacte des moments impairs. Les intégrales tridimensionnelles sont les produits tensoriels de (13). Aucune quadrature flottante n'est effectuée.

## 4. Famille 1 abandonnée : seulement \(m=1,2\)

La première recherche utilise

\[
h_1=a_c\Re(x_1+ix_2)+a_s\Im(x_1+ix_2),
\]

\[
h_2=b_c\Re(x_1+ix_2)^2+b_s\Im(x_1+ix_2)^2,
\]

avec

\[
(a_c,a_s),(b_c,b_s)
\in
\{-2,-1,0,1,2\}^2\setminus\{(0,0)\}.
\]

Il y a exactement \(24^2=576\) combinaisons. Pour chacune, le calcul rationnel donne

\[
\boxed{C_2=2C_1.}
\tag{14}
\]

Des valeurs non nulles apparaissent, mais toujours avec le même signe. Cette famille ne peut donc pas fournir le test adverse recherché sur cette grille. Elle est conservée comme résultat négatif reproductible.

## 5. Famille 2 : triade convective \(1+2=3\)

La deuxième recherche ajoute le mode \(m=3\) et parcourt les orientations non nulles de \(\{-1,0,1\}^2\). Le premier partage de signes apparaît au troisième essai avec

\[
(a_{1c},a_{1s})=(-1,-1),
\]

\[
(a_{2c},a_{2s})=(-1,-1),
\]

\[
(a_{3c},a_{3s})=(-1,1).
\]

Les potentiels scalaires sont donc

\[
h_1=-x_1-x_2,
\]

\[
h_2=-x_1^2+x_2^2-2x_1x_2,
\]

\[
h_3
=
-x_1^3+3x_1x_2^2+3x_1^2x_2-x_2^3.
\tag{15}
\]

Avec \(Z^{\rm tri}=Z_1+Z_2+Z_3\), les Gram tangentiels valent

\[
\left(
\|T_1\|_2^2,\|T_2\|_2^2,\|T_3\|_2^2
\right)
=
(2,12,54)
\left(\frac{\pi}{2}\right)^{3/2}.
\tag{16}
\]

Ils sont tous strictement positifs.

Le script calcule séparément les trois contributions de (1). Pour chaque \(m=1,2,3\),

\[
\langle\Delta Z^{\rm tri},T_m\rangle=0,
\tag{17}
\]

\[
\left\langle
(1+y\cdot\nabla)Z^{\rm tri},T_m
\right\rangle=0.
\tag{18}
\]

La seule contribution vient donc de

\[
-\left\langle
(Z^{\rm tri}\cdot\nabla)Z^{\rm tri},T_m
\right\rangle.
\]

Les moments exacts donnent (3). Le résultat est indépendant de \(\kappa\). Le script le revérifie pour

\[
\kappa\in\left\{-3,-1,0,2,\frac57\right\}.
\]

## 6. Famille 3 : partage de signes par dérive

Le troisième test utilise

\[
h_m^{(a)}
=
\Re\left[
(x_1+ix_2)^m(1+ia|y|^2)
\right].
\tag{19}
\]

Les paramètres sont

\[
(m,a)=(1,+1),
\qquad
(m,a)=(3,-1).
\]

Explicitement,

\[
h_1=x_1-|y|^2x_2,
\]

\[
h_3
=
\Re(x_1+ix_2)^3
+|y|^2\Im(x_1+ix_2)^3.
\tag{20}
\]

Pour \(Z^{\rm drift}=Z_1+Z_3\), les Gram valent

\[
\left(
\|T_1\|_2^2,\|T_3\|_2^2
\right)
=
\left(
\frac{39}{16},\frac{2349}{16}
\right)
\left(\frac{\pi}{2}\right)^{3/2}.
\tag{21}
\]

Les appariements de diffusion et de convection sont exactement nuls :

\[
\left(
\langle\Delta Z^{\rm drift},T_1\rangle,
\langle\Delta Z^{\rm drift},T_3\rangle
\right)
=(0,0),
\tag{22}
\]

\[
\left(
-\langle(Z^{\rm drift}\cdot\nabla)Z^{\rm drift},T_1\rangle,
-\langle(Z^{\rm drift}\cdot\nabla)Z^{\rm drift},T_3\rangle
\right)
=(0,0).
\tag{23}
\]

En revanche, le terme de similarité avant multiplication par \(-\kappa\) vaut

\[
\left(
\left\langle(1+y\cdot\nabla)Z^{\rm drift},T_1\right\rangle,
\left\langle(1+y\cdot\nabla)Z^{\rm drift},T_3\right\rangle
\right)
=
\left(
-\frac72,\frac{99}{2}
\right)
\left(\frac{\pi}{2}\right)^{3/2}.
\tag{24}
\]

À \(\kappa=1\), le signe est inversé dans (1), ce qui donne (4).

La famille 2 isole donc un partage de signes convectif, tandis que la famille 3 isole un partage de signes dû à la dérive de similarité.

## 7. Portée mathématique

Les champs \(Z^{\rm tri}\) et \(Z^{\rm drift}\) sont des champs réels, de Schwartz et divergence-free sur \(\mathbb R^3\). Ils satisfont les hypothèses de régularité et d'incompressibilité d'une donnée initiale pour la théorie locale forte standard de Navier–Stokes.

Le calcul reste toutefois strictement instantané :

- aucune solution \(Z(s)\) de (1) n'est intégrée ;
- aucune force ni pression n'est reconstruite ;
- aucune persistance temporelle des signes n'est démontrée ;
- aucune orbite ancienne ou Type I n'est construite ;
- aucune borne globale ni singularité n'est obtenue.

Les coefficients \(C_m\) sont des numérateurs modaux à un instant donné. Ils constituent un test adverse exact contre une hypothèse de signe universel, pas une réalisation d'un scénario de blow-up.

## 8. Reproduction et certificats

Commandes :

~~~powershell
python -B experiments/navier-stokes/instantaneous-modal-sign/instantaneous_modal_sign.py
git diff --check
~~~

Sortie validée :

~~~text
instantaneous_modal_sign: PASS
exact_assertions=1201
family_1=modes_1_2_trials=576_failure_C2=2*C1
family_2=modes_1_2_3_success_at_trial=3
selected_coefficients=m1(-1,-1)_m2(-1,-1)_m3(-1,1)
C1=-(8/9)*(pi/3)^(3/2)
C2=+(16/9)*(pi/3)^(3/2)
C3=-(16/3)*(pi/3)^(3/2)
Gram(RZ1,RZ2,RZ3)=(2,12,54)*(pi/2)^(3/2)
family_3=modes_1_3_drift_sign_split_at_kappa=1
family_3_Gram=(39/16,2349/16)*(pi/2)^(3/2)
family_3_diffusion=(0,0); convection=(0,0)
family_3_drift=(-7/2,+99/2)*(pi/2)^(3/2)
family_3_C_kappa1=(+7/2,-99/2)*(pi/2)^(3/2)
pressure_pairing=0_by_exact_solenoidal_tangents
family_2_diffusion_pairings=0; similarity_pairings=0; kappa=arbitrary
residuals=divergence:0,isotype:0,reported_pairing_identities:0
field_sha256=457e520e86f78565a4a7a3e0242b6b60b7c101bcc6acc352f65624381498a72a
search_sha256=553a558c8cb794a876ea612c8ecc186961337707a2867a5b29e2fae47686594d
drift_field_sha256=68ffac0d31e24cf6b86aac8d4c52410356ba95cb2fd176369b23c49027540896
seed=n/a; arithmetic=Fraction; quadrature=none
scope=exact instantaneous NS vector field; no time integration / no ancient or Type-I orbit
sha256_self=41bd221e7408fc1b02a2bc93ee6d08abe61e4e3533ba09eca1dbb5c7d3dedca4
~~~

Validation :

~~~text
git_diff_check=PASS
~~~

Les 1201 assertions vérifient les divergences, identités isotypiques, orthogonalités, recherches finies, moments gaussiens, contributions linéaires et non linéaires. Tous les résidus annoncés sont exactement nuls. Graine : non applicable.

Empreinte SHA-256 du script :

~~~text
41bd221e7408fc1b02a2bc93ee6d08abe61e4e3533ba09eca1dbb5c7d3dedca4
~~~

Empreinte du champ triadique :

~~~text
457e520e86f78565a4a7a3e0242b6b60b7c101bcc6acc352f65624381498a72a
~~~

Empreinte de la recherche familles 1–2 :

~~~text
553a558c8cb794a876ea612c8ecc186961337707a2867a5b29e2fae47686594d
~~~

Empreinte du champ de dérive :

~~~text
68ffac0d31e24cf6b86aac8d4c52410356ba95cb2fd176369b23c49027540896
~~~

## Décision

**CONSERVER** les familles 2 et 3 comme certificats indépendants de signes modaux opposés. **CONSERVER** l'échec de la famille 1. **RÉVISER** toute conjecture de signe modal universel. Le résultat est admissible comme calcul sur une donnée instantanée de Schwartz, mais ne construit aucune trajectoire ni orbite Type I.
