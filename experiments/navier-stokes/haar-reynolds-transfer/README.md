# Transfert de Reynolds après moyenne de Haar

Cette expérience certifie par algèbre exacte un contre-modèle sur \(\mathbb R^3\) :

- \(V\) et \(W\) sont des champs de Schwartz divergence-free ;
- \(V\) est invariant sous SO(2) autour de \(e_3\) ;
- la moyenne de Haar de \(W\) est nulle ;
- le transfert
  \[
  T(V,W)=\int_{\mathbb R^3}(W\otimes W):\nabla V\,dx
  \]
  est strictement non nul ;
- \(T(-V,W)=-T(V,W)\).

## Champs

Avec \(G=e^{-(x^2+y^2+z^2)}\), les potentiels sont

\[
A_V=zG(-y,x,0),
\qquad
A_W=xG(0,0,1),
\]

et

\[
V=\nabla\times A_V,
\qquad
W=\nabla\times A_W.
\]

Le script construit les rotationnels, divergences, générateurs SO(2), polynôme de transfert et moments gaussiens à partir de coefficients **Fraction**.

Le résultat exact est

\[
T(V,W)
=-\frac8{27}\left(\frac{\pi}{3}\right)^{3/2}.
\]

## Reproduction

Depuis la racine du dépôt :

~~~powershell
python -B experiments/navier-stokes/haar-reynolds-transfer/haar_reynolds_transfer.py
git diff --check
~~~

Environnement :

- Python 3.11 ou ultérieur ;
- bibliothèque standard uniquement ;
- aucune graine aléatoire ;
- aucune écriture produite par le script.

La sortie attendue et les empreintes validées sont conservées dans [results.json](results.json).

## Portée

Le facteur gaussien rend les champs lisses et rapidement décroissants. Le certificat porte sur des identités exactes de champs tests, pas sur une trajectoire de Navier–Stokes. Il ne produit ni solution, ni preuve de régularité, ni singularité.
