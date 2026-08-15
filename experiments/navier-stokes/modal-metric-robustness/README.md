# Robustesse métrique d'une phase canonique sur les isotypes \(k=1,2\)

Cette expérience travaille dans la représentation réelle

\[
H=\mathbb R^2\oplus\mathbb R^2,
\qquad
R=J\oplus2J,
\]

où \(J(x,y)=(-y,x)\). Les deux blocs sont les isotypes azimutaux distincts \(k=1\) et \(k=2\). Une métrique SO(2)-invariante est fixée par deux poids positifs :

\[
\langle u,v\rangle_w
=w_1u_1\cdot v_1+w_2u_2\cdot v_2.
\]

La phase canonique associée à une dérivée \(d\) et une tangente \(g=RZ\) est

\[
\beta_w=\frac{\langle d,g\rangle_w}{\langle g,g\rangle_w}.
\]

## Tests

Le premier état modal a une amplitude \(1\), le second une amplitude \(1/2\). Comme le second générateur est \(2J\), les deux tangentes \(RZ_1,RZ_2\) ont ainsi une norme égale à \(1\). Pour les vitesses modales \(+N\) et \(-N\),

\[
\beta_w=N\frac{w_1-w_2}{w_1+w_2}.
\]

Le certificat vérifie exactement :

- \(w_1=w_2=1\) : \(\beta_N=0\) ;
- \(w_1:w_2=2:1\) : \(\beta_N=N/3\).

Un second modèle utilise un état rapide d'amplitude \(1\), un état lent \(k=2\) d'amplitude \(1/(2N)\), et les vitesses \(N\) et \(1\). Les normes tangentielles sont donc \(1\) et \(1/N\).

- métrique fixe \((1,1)\) :
  \[
  \beta_N=\frac{N^3+1}{N^2+1},
  \qquad
  \text{part de Gram lente}=\frac1{N^2+1};
  \]
- métrique dépendant de \(N\), \((1,N^2)\) :
  \[
  \beta_N=\frac{N+1}{2},
  \qquad
  \text{part de Gram lente}=\frac12.
  \]
- métrique fortement dépendante de \(N\), \((1,N^4)\) :
  \[
  \beta_N=\frac{N^2+N}{N^2+1}\longrightarrow1,
  \qquad
  \text{part de Gram lente}=\frac{N^2}{N^2+1}.
  \]

Le dernier cas est volontairement non uniforme et interdit dans toute notion robuste de métrique fixe : son rapport de poids vaut \(N^4\).

Les identités de reconstruction, l'orthogonalité canonique et Pythagore ont toutes un résidu arithmétique nul.

## Reproduction

Depuis la racine du dépôt :

~~~powershell
python -B experiments/navier-stokes/modal-metric-robustness/modal_metric_robustness.py
git diff --check
~~~

Environnement :

- Python 3.11 ou ultérieur ;
- bibliothèque standard uniquement ;
- arithmétique **Fraction** ;
- graine non applicable ;
- aucune écriture produite par le script.

La sortie et les empreintes validées sont dans [results.json](results.json).

## Portée

Les deux isotypes \(k=1,2\) de la représentation SO(2) sont abstraits. Aucun champ divergence-free, aucune pression et aucune solution de Navier–Stokes ne sont construits.
