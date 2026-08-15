# Cycle 0063 — sortie exacte d'un cône modal dynamique

Date d'exécution : 2026-08-15

## Décision du cycle

**CONSERVER** un contre-modèle exact à l'invariance instantanée du cône
\(C_m\geq0\). **ABANDONNER** la famille limitée aux modes \(m=1,2\), dont la
frontière n'est atteinte qu'à l'apex sur la recherche finie. **RÉVISER** toute
dérivation qui traite la partie locale non projetée comme divergence-free.

## Équation et type de solution

Le calcul porte sur Navier–Stokes incompressible non forcé sur \(\mathbb R^3\),
avec viscosité \(\nu=1\) :

\[
\partial_tZ=F(Z)
=\Delta Z-(Z\cdot\nabla)Z-\nabla p,
\qquad \nabla\cdot Z=0,
\]

\[
-\Delta p=\operatorname{div}((Z\cdot\nabla)Z).
\tag{1}
\]

Le paramètre de similarité est fixé à \(\kappa=0\). Les champs testés sont
réels, de Schwartz et exactement divergence-free. Ils constituent des données
initiales admissibles pour une solution forte locale classique. Le cycle
n'intègre pas cette solution.

## Échelle des quantités

Sous l'échelle Navier–Stokes

\[
Z_\lambda(x,t)=\lambda Z(\lambda x,\lambda^2t),
\]

on a \(F(Z_\lambda)=\lambda^3F(Z)(\lambda x,\lambda^2t)\). La rotation
\(\mathcal R\) est d'ordre zéro, donc

\[
C_m(Z)=\langle\Pi_mF(Z),\mathcal R\Pi_mZ\rangle
\]

se transforme comme \(C_m(Z_\lambda)=\lambda C_m(Z)\). Sa dérivée le long de
\(F\) se transforme comme

\[
DC_m(Z_\lambda)[F(Z_\lambda)]
=\lambda^3DC_m(Z)[F(Z)].
\]

Le signe de la condition tangentielle est donc invariant par remise à
l'échelle positive. Les facteurs gaussiens fixent seulement une échelle de
calcul commode.

## Affirmations ajoutées ou modifiées

Pour \(G=e^{-|x|^2}\), posons

\[
Z_m=\nabla\times(h_mG e_3),
\]

avec

\[
h_1=-x_1-x_2,
\]

\[
h_2=-x_1^2+x_2^2-2x_1x_2,
\]

\[
h_3=-x_1^3+3x_1x_2^2.
\tag{2}
\]

Pour \(Z=Z_1+Z_2+Z_3\), \(q_m=\mathcal RZ_m\), et

\[
C_m(Z)=\langle\Pi_mF(Z),q_m\rangle,
\]

le certificat exact donne

\[
\boxed{
(C_1,C_2,C_3)
=
\left(\frac89,\frac{16}9,0\right)
\left(\frac\pi3\right)^{3/2}.}
\tag{3}
\]

La dérivée active vérifie

\[
\boxed{
C'_3=DC_3(Z)[F(Z)]
=-\frac{1076547}{1281280}\pi^{3/2}<0.}
\tag{4}
\]

Comme \(C_1,C_2>0\), \(C_3=0\) et \(C'_3<0\), le champ de vecteurs traverse
vers l'extérieur la face active \(C_3=0\) du cône \(C_m\geq0\).

Résultat négatif conservé : pour les 576 orientations entières non nulles de
la famille à deux modes \(m=1,2\),

\[
C_2=2C_1.
\tag{5}
\]

Cette famille n'offre aucune face active non triviale.

## Preuve / source / calcul

Le cœur exact du cycle 0062 construit les isotypes et calcule (3). Le présent
script différentie ensuite le numérateur.

Écrivons

\[
A(Z)=\Delta Z-B(Z,Z),
\qquad B(a,b)=(a\cdot\nabla)b.
\]

Puisque \(q_m\) est solénoïdal,

\[
C_m(Z)=\langle A(Z),q_m\rangle.
\]

Pour \(H=F(Z)=A-\nabla p\),

\[
DC_m(Z)[H]
=\langle\Delta H-B(H,Z)-B(Z,H),q_m\rangle
+\langle A,\mathcal R\Pi_mH\rangle.
\tag{6}
\]

Le dernier terme s'annule exactement :

\[
\langle A,\mathcal R\Pi_mH\rangle
=\langle H,\mathcal R\Pi_mH\rangle
=\langle\Pi_mH,\mathcal R\Pi_mH\rangle=0.
\tag{7}
\]

La première égalité utilise l'orthogonalité des gradients aux champs
solénoïdaux ; la deuxième, l'orthogonalité des isotypes ; la dernière,
l'antisymétrie de \(\mathcal R\).

Le calcul direct de \(DA[A]\), séparé par taux gaussien après appariement avec
\(q_3\), donne

\[
(r_2,r_3,r_4)=\left(0,0,-\frac{675}{32}\right).
\]

Comme l'intégrale au taux 4 ajoute le facteur
\((\pi/4)^{3/2}=\pi^{3/2}/8\),

\[
\langle DA[A],q_3\rangle
=-\frac{675}{256}\pi^{3/2}.
\tag{8}
\]

La partie \(-\Delta\nabla p\) est un gradient. Pour le reste, deux
intégrations par parties donnent

\[
\langle B(\nabla p,Z)+B(Z,\nabla p),q_3\rangle
=\langle p,Q_3\rangle,
\]

\[
Q_3
=-\partial_j[(\partial_jZ_i)q_{3,i}]
+\partial_i[Z_j(\partial_jq_{3,i})].
\tag{9}
\]

Avec \(S=\operatorname{div}B(Z,Z)\), (1) et Parseval donnent

\[
\langle p,Q_3\rangle
=(2\pi)^{-3}\int
\frac{\widehat S\,\overline{\widehat Q_3}}{|\xi|^2}\,d\xi
=\frac{575457}{320320}\pi^{3/2}.
\tag{10}
\]

Les transformées de Fourier et tous les moments sont calculés avec des
fractions rationnelles exactes. Aucun échantillonnage flottant ni solveur de
Poisson discret n'intervient. La somme de (8) et (10) est (4).

## Écart avec le problème Clay

Le calcul concerne exactement l'opérateur Navier–Stokes incompressible sur
\(\mathbb R^3\), mais seulement son champ de vecteurs à un instant. Il ne
montre pas que le champ reste dans une classe modale finie, que la face est
atteinte par une trajectoire ancienne, ni qu'un signe persiste. Il ne fournit
aucun contrôle d'une norme critique, aucun profil Type I ou Type II, et aucune
alternative régularité/blow-up. C'est un contre-exemple borné à une stratégie
de cône modal universel, pas un résultat terminal du problème Clay.

## Test adverse et résidu certifié

La passe contradictoire a invalidé un premier calcul intermédiaire. Une
intégration par parties traitait implicitement

\[
A=\Delta Z-B(Z,Z)
\]

comme un champ divergence-free et produisait \(-1035/32\) au taux 4. Or

\[
\operatorname{div}A=-\operatorname{div}B(Z,Z)\neq0.
\]

La contraction composante par composante dans (6) donne \(-675/32\). Le terme
de pression doit alors être recalculé : il vaut (10), non
\(1025907/320320\,\pi^{3/2}\). Fait remarquable mais vérifié exactement, les
deux corrections se compensent et la valeur totale (4) ne change pas. Les
assertions du script figent désormais séparément le local, la pression et le
total, ce qui empêche cette erreur de rester masquée.

Les contrôles exacts supplémentaires sont :

- divergence de \(Z\) et de \(q_3\) : résidu nul ;
- identité isotypique \(\mathcal R^2Z_3=-9Z_3\) : résidu nul ;
- partie imaginaire de l'intégrale de Fourier : résidu nul ;
- identité fabriquée
  \(\langle-\Delta\phi,(-\Delta)^{-1}Q\rangle=\langle\phi,Q\rangle\) :
  résidu nul ;
- symétrie et positivité de \((-\Delta)^{-1}\) : validées exactement.

## Artefacts mis à jour

- `experiments/navier-stokes/dynamic-modal-cone/dynamic_modal_cone.py` ;
- `experiments/navier-stokes/dynamic-modal-cone/README.md` ;
- `experiments/navier-stokes/dynamic-modal-cone/results.json` ;
- `docs/reports/navier-stokes/reviews/cycle-0063-countermodel.md`.

Empreintes SHA-256 :

- script : `e80705842d6dad373328a67ce30d475b590e780ba454deffdf88e340bea29662` ;
- cœur exact cycle 0062 :
  `41bd221e7408fc1b02a2bc93ee6d08abe61e4e3533ba09eca1dbb5c7d3dedca4` ;
- champ polynomial :
  `c6a5442603d162cfaddefdcccdada9ec35d82bd777b6a1be229197ec4c45e5e2` ;
- polynômes \((S,Q_3)\) :
  `c7e2e87880097a10f417d209e4d09a97c496d73cefc3c96aa660a765a934e87a`.

## État : continuer

Le cône de signe modal simple n'est pas invariant, même au voisinage
instantané d'une face active non triviale.

## Prochaine expérience décisive

Tester si une correction de frontière dépendant des interactions adjacentes,

\[
\widetilde C_m
=C_m+\alpha_m\langle\Pi_{m-1}Z,\mathcal T_m\Pi_{m+1}Z\rangle,
\]

peut satisfaire une condition tangentielle sur une famille polynomial-
gaussienne compacte. Le test doit d'abord fixer explicitement
\(\mathcal T_m\), suivre son échelle, puis chercher soit des coefficients
\(\alpha_m\) rationnels admissibles, soit deux champs donnant des contraintes
linéaires incompatibles. Le second résultat fournirait un nouvel abandon
falsifiable à faible coût.
