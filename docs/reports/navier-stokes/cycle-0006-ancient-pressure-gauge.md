# Cycle 0006 — Jauge de pression des solutions anciennes

Date : 2026-08-14.

## Décision du cycle

Trois actions ont été notées : solution ancienne parasite et porte de pression
(19/20), audit abstrait de la préservation de mildness par zoom (16/20),
Liouville Type II général direct (13/20). La première est retenue parce qu'elle
teste le tout premier quantificateur de la classe ancienne.

## Équation et type de solution

Navier–Stokes incompressible 3D sur `R³ x (-infinity,0]`, sans frontière,
viscosité arbitraire `nu>0`, force nulle :

```text
partial_t u+(u dot nabla)u+nabla p=nu Delta u,
div u=0.
```

Le contre-profil est classique, ancien, à vitesse bornée et localement adapté
avec égalité d'énergie, mais sa pression affine est spatialement non bornée et
il n'est pas mild :

```text
u(x,t)=(-t/(1+t²))e_1,
p(x,t)=((1-t²)/(1+t²)²)x_1.
```

## Échelle des quantités

Le profil occupe le mode spatial zéro : convection et Laplacien sont nuls. Sous
le zoom NS, `b_lambda(t)=lambda b(lambda²t)` et le coefficient affine de
pression devient `lambda³b'(lambda²t)`, conformément à l'échelle du gradient de
pression. La vitesse est bornée par `1/2`, mais aucune norme globale
`L^q_x`, `q<infinity`, n'est finie aux temps non nuls.

## Affirmations ajoutées ou modifiées

- `NS-PARASITIC-ANCIENT-ZERO-TRACE-FAMILY`, `COMPUTATION_ONLY` : contre-profil
  exact et non-mildness.
- `NS-ANCIENT-SUITABLE-ZERO-TRACE-LIOUVILLE`, `REFUTED` : la classe locale
  adaptée sans jauge est trop large.
- `NS-KNSS-SPATIALLY-CONSTANT-MILD-RIGIDITY`, `SOURCE_VERIFIED` : une ancienne
  mild spatialement constante est constante en temps.
- `NS-SRC-0015` est précisé avec la distinction faible/mild de KNSS.

## Preuve / source / calcul

Avec `a(t)=-t/(1+t²)`,

```text
a'(t)=(t²-1)/(1+t²)²,
nabla p=-a'(t)e_1,
partial_t u+nabla p=0.
```

La borne vient de

```text
1/4-a(t)²=(t²-1)²/[4(1+t²)²]>=0.
```

L'énergie locale se ferme par
`partial_t(|u|²/2)+div(pu)=aa'-aa'=0`. En revanche, la formule mild entre
`s=-1` et `t=0` aurait imposé `a(0)=a(-1)`; son défaut exact vaut `-1/2`.

KNSS, Acta Mathematica 203 (2009), introduction, théorème 5.1 et remarque 6.1,
identifie explicitement `u=b(t), p=-b'(t) dot x` comme solution parasite et
emploie la notion mild pour l'exclure (`arXiv:0709.3599`,
DOI `10.1007/s11511-009-0039-6`).

Le script a pour SHA-256
`4853899209792e9608e01f49c2c0c66a1194502bd933595c9f397856b1dc8fc8`.

## Écart avec le problème Clay

La vitesse ne décroît pas à l'infini et n'appartient ni à `L²(R³)` ni à
`L³(R³)`. Ce n'est donc ni une donnée Clay, ni un blow-up admissible. Le résultat
attaque seulement une formulation trop faible du théorème de rigidité appliqué
après zoom. Une limite de blow-up construite dans une classe mild avec jauge
héritée exclut déjà ce contre-profil.

## Test adverse et résidu certifié

Pour six temps rationnels, le script vérifie divergence, convection, Laplacien,
momentum, équation de Poisson, énergie locale et borne de vitesse. Résidu maximal
exact : `0/1`. À `t=0`, `p=x_1`; son oscillation moyenne sur
`[-R,R]³` vaut exactement `R/2` pour six rayons, donc `p` n'est pas BMO.

Deux passes séparées ont confirmé le statut localement suitable, le signe de
pression, le témoin BMO, le défaut mild, les quantificateurs et l'attribution
KNSS. Elles ont précisé que la pression, contrairement à la vitesse, est
spatialement non bornée et que l'ancienne mild KNSS est définie via une suite
`T_l->-infinity`. Les trois claims passent à `adversarial_pass`, sans revue
externe revendiquée.

## Artefacts mis à jour

Veille, extraction KNSS, source `NS-SRC-0015`, script et protocole
`ANCIENT-PRESSURE-GAUGE-1`, trois claims, graphe, carte adaptative, journal
supercritique, registre d'échecs, questions et présent checkpoint.

## État : continuer

Le test réfute la rigidité dans la classe faible/adaptée sans jauge et valide la
porte mild dans la sous-classe du mode zéro. Il ne résout pas le Liouville mild
3D général.

## Prochaine expérience décisive

Construire une matrice ESS/GKP/KNSS indiquant, pour chaque zoom, la topologie de
convergence, la formule mild, la normalisation de pression, la trace terminale
et la non-trivialité effectivement transmises. Tester ensuite si « ancienne
mild bornée + trace terminale nulle dans la topologie exacte » tombe sous une
rétro-unicité sourcée ou laisse encore un scénario non trivial.
