# Sortie dynamique d'un cône modal

Cette expérience étend l'algèbre polynomial-gaussienne exacte du cycle 0062.
Elle teste l'invariance instantanée du cône

\[
\mathcal K=\{Z:C_m(Z)\geq 0\text{ pour }m=1,2,3\}
\]

pour le champ de vecteurs Navier–Stokes incompressible sur \(\mathbb R^3\), à
viscosité \(\nu=1\), sans force et avec \(\kappa=0\) :

\[
F(Z)=\Delta Z-(Z\cdot\nabla)Z-\nabla p,
\qquad
-\Delta p=\operatorname{div}((Z\cdot\nabla)Z).
\]

Les données sont des champs réels de Schwartz divergence-free de la forme

\[
Z_m=\nabla\times\left(h_m e^{-|x|^2}e_3\right),
\]

où \(h_m\) est une harmonique azimutale de degré \(m\). Si \(\Pi_m\) est la
projection orthogonale sur l'isotype \(m\) et \(\mathcal R\) le générateur des
rotations autour de \(e_3\), le numérateur modal est

\[
C_m(Z)=\langle \Pi_mF(Z),\mathcal R\Pi_mZ\rangle_{L^2}.
\]

## Certificat

Pour les orientations

\[
(a_{1c},a_{1s})=(-1,-1),\qquad
(a_{2c},a_{2s})=(-1,-1),\qquad
(a_{3c},a_{3s})=(-1,0),
\]

le script obtient

\[
(C_1,C_2,C_3)
=
\left(\frac89,\frac{16}9,0\right)
\left(\frac\pi3\right)^{3/2}.
\]

Le mode \(m=3\) est donc sur la frontière de \(\mathcal K\). La dérivée le
long du champ exact \(F(Z)\) vaut

\[
C'_3
=
\left(
-\frac{675}{256}
+\frac{575457}{320320}
\right)\pi^{3/2}
=
-\frac{1076547}{1281280}\pi^{3/2}<0.
\]

Ainsi le champ de vecteurs sort strictement du cône à cette face active. Il
s'agit d'un résultat instantané : aucune invariance temporelle, orbite ancienne
ou trajectoire Type I n'est construite.

## Traitement exact de la pression

Écrivons \(A(Z)=\Delta Z-(Z\cdot\nabla)Z\) et \(q_m=\mathcal RZ_m\). Pour
\(H=F(Z)=A-\nabla p\),

\[
DC_m(Z)[H]
=
\langle DA(Z)[H],q_m\rangle
+\langle A(Z),\mathcal R\Pi_mH\rangle.
\]

Le second terme est nul par orthogonalité de la pression aux champs
solénoïdaux, orthogonalité des isotypes et antisymétrie de \(\mathcal R\) :

\[
\langle A,\mathcal R\Pi_mH\rangle
=\langle \Pi_mH,\mathcal R\Pi_mH\rangle=0.
\]

La partie \(-\Delta\nabla p\) de \(DA[-\nabla p]\) est un gradient et
s'apparie aussi à zéro avec \(q_m\). Les termes restants se réduisent, par
intégration par parties, à

\[
\langle B(\nabla p,Z)+B(Z,\nabla p),q_m\rangle
=\langle p,Q_m\rangle,
\]

\[
Q_m
=
-\partial_j\!\left[(\partial_jZ_i)q_{m,i}\right]
+\partial_i\!\left[Z_j(\partial_jq_{m,i})\right].
\]

Le script ne reconstruit pas \(p\) point par point. Il évalue exactement le
seul appariement requis. Avec

\[
S=\operatorname{div}((Z\cdot\nabla)Z),
\qquad -\Delta p=S,
\]

et la convention \(\widehat f(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx\),

\[
\langle p,Q_m\rangle
=
(2\pi)^{-3}\int_{\mathbb R^3}
\frac{\widehat S(\xi)\overline{\widehat Q_m(\xi)}}{|\xi|^2}\,d\xi.
\]

Comme \(S,Q_m\) sont des polynômes multipliés par \(e^{-2|x|^2}\), leurs
transformées sont des polynômes complexes rationnels multipliés par
\(e^{-|\xi|^2/8}\). Tous les moments de
\(e^{-|\xi|^2/4}/|\xi|^2\) sont rationnels après extraction de
\(\pi^{3/2}\). L'évaluation utilise uniquement `Fraction`, sans quadrature.

Trois contrôles fabriqués vérifient exactement

\[
\langle-\Delta\phi,(-\Delta)^{-1}Q\rangle=\langle\phi,Q\rangle,
\]

la symétrie de \((-\Delta)^{-1}\) et sa positivité.

## Passe contradictoire conservée

Une première réduction par intégration par parties donnait à tort le
coefficient local normalisé \(-1035/32\). Elle supposait silencieusement que

\[
A=\Delta Z-(Z\cdot\nabla)Z
\]

était divergence-free. En général
\(\operatorname{div}A=-\operatorname{div}((Z\cdot\nabla)Z)\neq0\). Le calcul
direct de \(DA[A]\) donne \(-675/32\). La contribution de pression corrigée
est simultanément \(575457/320320\,\pi^{3/2}\), et le total ci-dessus est
inchangé. Le script impose séparément ces deux valeurs corrigées.

La première famille explorée est également conservée comme échec : pour les
576 orientations entières non nulles des seuls modes \(m=1,2\), on a
exactement \(C_2=2C_1\). La frontière recherchée n'apparaît qu'à l'apex.

## Reproduction

Depuis la racine du dépôt :

~~~powershell
python -B experiments/navier-stokes/dynamic-modal-cone/dynamic_modal_cone.py
python -m json.tool experiments/navier-stokes/dynamic-modal-cone/results.json
git diff --check
~~~

Environnement :

- Python 3.11 ou ultérieur ;
- bibliothèque standard uniquement ;
- dépendance locale au cœur exact du cycle 0062, dont l'empreinte est vérifiée
  dans `results.json` ;
- arithmétique `Fraction` ;
- aucune quadrature et aucune graine aléatoire ;
- aucune écriture produite par le script.

Les champs sont admissibles comme données initiales pour la théorie locale
forte standard sur \(\mathbb R^3\). Le certificat ne démontre ni blow-up, ni
régularité globale, ni persistance des signes.
