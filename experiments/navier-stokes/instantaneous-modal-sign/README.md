# Signes modaux instantanés sous SO(2)

Cette expérience construit des champs de Schwartz divergence-free sur \(\mathbb R^3\) à partir de potentiels

\[
A_m=h_m(x,y,z)e^{-|y|^2}e_3,
\qquad
Z_m=\nabla\times A_m.
\]

Les polynômes \(h_m\) appartiennent aux isotypes azimutaux réels \(m\). Le script certifie

\[
\mathcal R^2Z_m=-m^2Z_m,
\qquad
\nabla\cdot Z_m=\nabla\cdot(\mathcal RZ_m)=0.
\]

Pour

\[
d(Z)=\Delta Z-\mathbb P\operatorname{div}(Z\otimes Z)
-\kappa(1+y\cdot\nabla)Z,
\]

il calcule

\[
C_m=\langle \Pi_md(Z),\mathcal R\Pi_mZ\rangle_{L^2}.
\]

La projection de Leray est retirée seulement après certification de la solénoïdalité de chaque tangente :

\[
\langle\mathbb PF,\mathcal RZ_m\rangle
=\langle F,\mathcal RZ_m\rangle.
\]

## Familles explorées

1. Deux modes \(m=1,2\), orientations entières dans \([-2,2]\) : 576 cas exacts, tous en échec avec \(C_2=2C_1\).
2. Triade \(m=1,2,3\) : succès au troisième essai,
   \[
   (C_1,C_2,C_3)
   =
   \left(-\frac89,\frac{16}9,-\frac{16}3\right)
   \left(\frac\pi3\right)^{3/2}.
   \]
   La diffusion et le terme de similarité s'apparient à zéro, donc ce résultat est indépendant de \(\kappa\).
3. Deux modes \(m=1,3\) à phase radiale : la diffusion et la convection s'apparient à zéro, tandis qu'à \(\kappa=1\),
   \[
   (C_1,C_3)
   =
   \left(\frac72,-\frac{99}{2}\right)
   \left(\frac\pi2\right)^{3/2}.
   \]

## Reproduction

Depuis la racine du dépôt :

~~~powershell
python -B experiments/navier-stokes/instantaneous-modal-sign/instantaneous_modal_sign.py
git diff --check
~~~

Environnement :

- Python 3.11 ou ultérieur ;
- bibliothèque standard uniquement ;
- coefficients **Fraction** et moments gaussiens exacts ;
- aucune quadrature flottante ;
- graine non applicable ;
- aucune écriture produite par le script.

Les résultats et empreintes sont enregistrés dans [results.json](results.json).

## Portée

Chaque somme modale est un champ de Schwartz divergence-free, donc une donnée initiale admissible pour la théorie locale forte standard sur \(\mathbb R^3\). Le certificat reste instantané : il n'intègre aucune trajectoire en temps, ne construit aucune orbite Type I et ne donne aucun critère de régularité globale ou de blow-up.
