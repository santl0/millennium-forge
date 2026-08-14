# Journal supercritique et contre-profils

Journal append-only. Chaque entrée fixe l'équation, le domaine, la notion de
solution ou précise qu'il s'agit seulement d'un champ test.

## 2026-08-14 — Échelle NS

- Équation : NS incompressible 3D, `R^3`, viscosité inchangée.
- Transformation : `u_lambda=lambda u(lambda x,lambda^2 t)`.
- Lois : `||u_lambda||_q=lambda^(1-3/q)||u||_q`,
  `||u_lambda||_dotH^s=lambda^(s-1/2)||u||_dotH^s`,
  `||u_lambda||_2²=lambda^-1||u||_2²`.
- Perte : l'énergie est supercritique vers les petites échelles; aucune
  interpolation entre énergie et dissipation ne donne seule `L∞_tL³_x`.
- Test adverse futur : paquets divergence-free concentrés et séparés.

## 2026-08-14 — Porte visqueuse d'un profil mono-échelle

- Objet : ansatz formel, pas solution démontrée.
- Domaine : localement `R^3`; `tau=T-t`.
- Calcul : inertie `~tau^(lambda-1)`, viscosité
  `~nu tau^(-lambda-2)`, rapport `~nu tau^(-1-2lambda)`.
- Seuil : perturbatif seulement pour `lambda<-1/2`, équilibré pour
  `lambda=-1/2`, dominant pour `lambda>-1/2`.
- Contre-portée : ne traite pas une cascade multi-échelle ni une annulation de
  `Delta U`.
- Artefact : `VAS-1`, résidu rationnel zéro.

## 2026-08-14 — Contre-triade de flux

- Objet : champ test réel divergence-free, pas trajectoire.
- Domaine : tore tridimensionnel normalisé.
- Modes : `+-a`, `+-b`, `+-c`, avec `c=a+b`.
- Invariants : `E=6`, `Z=9N²`, hélicité nulle mode par mode.
- Transfert : `Pi_N=-2 sigma N`, donc ratio au carré `1/54`.
- Conclusion négative : ni divergence nulle, ni hélicité globale nulle ne
  produisent un facteur universel `epsilon_N->0`.
- Résidus : tous nuls en rationnels gaussiens.

## 2026-08-14 — Désingularisation d'un profil homogène `-1`

- Objet : donnée initiale sur coquille, pas évolution PDE.
- Domaine : `R^3`, `u_0=r^-1 A(theta)` pour `epsilon<=r<=1`.
- Intégrale : `||u_0||_q^q=C_q integral_epsilon^1 r^(2-q)dr`.
- Seuil : borné pour `q<3`, logarithmique pour `q=3`, puissance pour `q>3`.
- Régularité : `||nabla u_0||_2²=C_grad(epsilon^-1-1)` si
  `C_grad>0`.
- Obstacle : aucune constante de stabilité dépendant uniformément de ces normes
  ne survit au cutoff; une stabilité exotique n'est pas exclue.
- Artefact : `DESINGULARIZATION-GATE-1`, résidu rationnel zéro.

## 2026-08-14 — Pression multi-échelle après zoom

- Objet : suite de données lisses compactes divergence-free, pas trajectoire.
- Échelles : distance `L_n=2^-6n`, zoom `r_n=2^-7n`, moment
  `mu_n=2^-3n`, distance rescalée `R_n=2^n`.
- Énergie : `||v_n||_2²=2mu_n->0`, mais
  `||r_n v_n(r_n·)||_2²=2R_n^4`.
- Quantité critique de queue :
  `Theta_n(A)=integral_(|y|>A)|U_n(y)|²|y|^-4dy`.
- Contre-profil : pour tout `A`, des indices avec `R_n>A` gardent
  `Theta_n(A)` proche de `2`; la pression centrée converge vers `3/(4pi)`.
- Perte localisée : l'énergie globale ne donne aucune tension uniforme après
  des zooms plus fins que l'échelle porteuse de l'énergie.
- Artefact : `PRESSURE-MULTISCALE-1`, résidus rationnels zéro.
