# Cycle 0003 — Défaut de tension de pression après zoom

Date : 2026-08-14.

## Décision du cycle

Trois actions sont comparées : contre-profil de pression multi-échelle (19/20),
défaut quadratique oscillatoire (17/20), extraction Liouville Type II (15/20).
Le premier test est choisi car il tranche exactement si une borne physique `L²`
seule rend uniforme le lemme du cycle 0002.

## Équation et type de solution

Pression instantanée de NS incompressible 3D sur `R^3`, reconstruite par

```text
p=K_ij*(u_i u_j),
K_ij=partial_i partial_j(1/(4pi|x|)).
```

Les objets adverses sont des champs `C_c^infinity`, divergence-free, pris comme
données initiales séparées. Ils ne sont pas une trajectoire NS commune, une
solution ancienne ou un blow-up.

## Échelle des quantités

Sous le zoom `U_n(y)=r_n v_n(r_n y)`, `P_n(y)=r_n²p_n(r_n y)`, on choisit

```text
L_n=2^-6n, r_n=2^-7n, mu_n=2^-3n, R_n=L_n/r_n=2^n.
```

Le moment physique `mu_n` devient `mu_n/r_n=R_n^4`;
`||v_n||_2²=2mu_n` tend vers zéro (l'énergie cinétique vaut `mu_n`), tandis que
`||U_n||_2²=2R_n^4`.

## Affirmations ajoutées ou modifiées

- `NS-PRESSURE-WEIGHTED-TAIL-CRITERION`, `COMPUTATION_ONLY` : une tension
  uniforme de `integral |U_n|²|y|^-4` suffit à contrôler la pression lointaine
  centrée.
- `NS-ENERGY-IMPLIES-PRESSURE-TAIL-TIGHTNESS`, `REFUTED` : la borne physique `L²`
  bornée ne fournit pas cette tension sous zoom arbitraire.
- `NS-L3-CONTROLS-PRESSURE-TAIL`, `COMPUTATION_ONLY` : Hölder donne la tension
  avec taux explicite `A^-3` sous une borne critique uniforme `L³`.
- `FAIL-NS-0006` enregistre le contre-profil et sa portée négative exacte.

## Preuve / source / calcul

Pour `|x|<=a`, `|y|>A>2a`, définissons la différence directement par

```text
D_n^far(x;A)=integral_(|y|>A)
  [K_ij(x-y)-K_ij(-y)]U_(n,i)U_(n,j)dy.
```

Le théorème des accroissements finis donne

```text
|D_n^far(x;A)|
 <= (21/pi)a(1-a/A)^-4
    integral_(|y|>A)|U_n(y)|²|y|^-4dy.
```

Hölder ferme cette queue sous `L³` avec la constante explicite
`(4pi/9)^(1/3)A^-3`. Le contre-profil montre que remplacer `L³` par l'énergie
physique détruit cette uniformité.

Un champ de base
`w=(partial_2 psi,-partial_1 psi,0)` avec `psi` radial est normalisé pour que
son moment soit `diag(1,1,0)` et son énergie `2`. Les paquets

```text
v_n(x)=sqrt(mu_n/r_n³) w((x-L_n e_1)/r_n)
```

sont lisses, compacts, divergence-free et d'énergie `2mu_n`. Après zoom, la
convergence multipolaire uniforme sur le support fixe de `w` donne

```text
integral |U_n|²|y|^-4 -> 2,
P_n(e_1)-P_n(0) -> 3/(4pi).
```

Le script exact vérifie le modèle de moment pour `1<=n<=12`, avec SHA-256
`c69d3c45b5383596cb3ccc1b804ad94ef3ccbfa9b5d49c7e7f237c72abbe12fd`.

## Écart avec le problème Clay

Chaque champ est une donnée Clay admissible, mais la suite change avec `n` et
aucun d'eux n'est montré singulier. Le contre-profil exclut une estimation
uniforme sur toutes données fondée seulement sur l'énergie. Il ne montre pas
qu'une suite issue d'un même premier blow-up peut réaliser ces échelles : la
dynamique, une borne critique ou la minimalité peuvent imposer la tension
manquante.

## Test adverse et résidu certifié

Six familles d'identités sont vérifiées exactement : distance, moment, balance
`mu_n r_n³/L_n^4=1`, queue pondérée ponctuelle, pression centrée et erreur vers
la limite `3`. Résidu maximal : `0/1`; erreur d'arrondi : zéro.

La passe contradictoire séparée confirme le sens des facteurs de zoom, la
réalisabilité exacte du moment, la limite uniforme du paquet lisse, la polarité
`REFUTED` et l'absence d'implication dynamique. Elle a détecté trois précisions
désormais intégrées : différence de pression définie directement, quantificateurs
universels explicites, et distinction entre énergie cinétique et norme `L²` au
carré.

## Artefacts mis à jour

Veille différentielle, script et protocole multi-échelle, deux claims, graphe,
journal supercritique, registre d'échecs, questions et carte adaptative.

## État : continuer

Le calcul exact passe; la passe contradictoire impose de définir directement la
différence distante, d'expliciter les quantificateurs universels réfutés et de
distinguer énergie cinétique de norme `L²` au carré. Ces corrections sont
intégrées.

## Prochaine expérience décisive

L'extraction ESS/GKP/KNSS/Seregin est désormais réalisée : une borne globale
`L³` force la tension en `A^-3`, mais cette borne est précisément conditionnelle.
Le cycle suivant construira donc une suite divergence-free localisée qui teste
la compacité de `u_n tensor u_n` et de la pression proche sous convergence
faible, puis identifiera l'hypothèse minimale qui élimine le défaut.
