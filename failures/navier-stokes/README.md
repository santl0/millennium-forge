# Registre des échecs utiles — Navier–Stokes 3D

Ce registre est append-only : corriger une entrée consiste à ajouter un statut
ou une nouvelle affirmation, jamais à supprimer l'échec.

## `FAIL-NS-0001` — Transfert mono-échelle d'un profil Euler IA vers NS

- Date : 2026-08-14 (ré-audit d'une dérivation historique).
- Cible : profil de blow-up incompressible de type
  `u=tau^lambda U(x/tau^(1+lambda))`.
- Attaque : comparer exactement viscosité et inertie après remise à l'échelle.
- Résultat : le ratio est `nu C_U tau^(-1-2lambda)`. Pour
  `lambda>-1/2`, il diverge; le terme visqueux n'est pas perturbatif.
- Portée : réfute seulement le transfert mono-échelle direct pour ces exposants,
  pas l'existence de tout profil NS ni de toute construction multi-échelle.
- Statut : `REFUTED` pour l'arête de transfert; calcul rationnel à reproduire
  dans le nouveau dépôt.

## `FAIL-NS-0002` — Déplétion universelle par divergence et hélicité nulle

- Date : 2026-08-14 (ré-audit d'une expérience historique).
- Cible : une borne `|Pi_N| <= epsilon_N N E^(3/2)`, `epsilon_N -> 0`, valable
  pour tout polynôme trigonométrique divergence-free d'hélicité globale nulle.
- Attaque : triade exacte `a=(N,0,0)`, `b=(0,N,0)`, `c=(N,N,0)` avec phases
  signées et modes conjugués.
- Résultat : `E=6`, `Z=9N²`, hélicité `0`, mais `Pi_N=-2 sigma N`; le ratio
  normalisé ne tend pas vers zéro.
- Portée : ne réfute pas une déplétion avec cohérence locale de la direction de
  vorticité, intermittence contrôlée ou hypothèses dynamiques supplémentaires.
- Statut : contre-exemple algébrique fini à reproduire avant claim canonique.

## `FAIL-NS-0003` — Non-unicité faible présentée comme blow-up Clay

- Date : 2026-08-14.
- Cible : implications depuis Buckmaster–Vicol, Albritton–Brué–Colombo ou
  Hou–Wang–Yang vers une alternative (A)–(D).
- Attaque : vérifier force, donnée initiale, classe de solution et conclusion.
- Résultat : les constructions diffèrent respectivement par la classe
  énergétique, la présence d'une force, ou une donnée initiale singulière.
  Aucune n'exclut à elle seule une solution globale lisse pour toute donnée
  Clay.
- Statut : implication réfutée; les théorèmes ou prépublications sources ne sont
  pas réfutés.

## `FAIL-NS-0004` — Exclusion auto-similaire assimilée à exclusion de blow-up

- Date : 2026-08-14.
- Cible : conclure la régularité globale du théorème de Liouville pour profils
  rétrogrades `L³`.
- Attaque : comparer les quantificateurs à Type II, auto-similarité discrète et
  concentration multi-échelle.
- Résultat : le théorème élimine une sous-classe; les autres scénarios ne
  satisfont pas ses hypothèses.
- Statut : implication réfutée.

## `FAIL-NS-0005` — Grandes normes de cutoff assimilées à une obstruction dynamique

- Date : 2026-08-14.
- Cible : déduire de la divergence de `L^3` et `H^1` d'une famille lissée que
  son temps d'existence s'effondre ou qu'aucune stabilité dynamique ne subsiste.
- Attaque : solutions de cisaillement exactes sur `T^3`,
  `u_N=a_N exp(-nu N²t) sin(Nx_2)e_1`, pour lesquelles transport et pression
  s'annulent.
- Résultat : avec `a_N=(log N)^(1/3)` et
  `epsilon_N=[N²(log N)^(2/3)]^-1`, on a
  `||u_N(0)||_3^3` du même ordre que `log(1/epsilon_N)` et
  `||nabla u_N(0)||_2²` du même ordre que `epsilon_N^-1`, tout en ayant une
  solution globale lisse exacte.
- Portée : la coquille `r^-1` prouve la non-uniformité de certaines normes,
  mais pas une conséquence dynamique. Elle reste pertinente pour attaquer une
  preuve de stabilité dont la constante dépend précisément de ces normes.
- Statut : implication dynamique réfutée par la passe contradictoire séparée;
  le lemme radial restreint est conservé `COMPUTATION_ONLY`.

## Gabarit d'ajout

Chaque échec futur doit préciser cible, équation, domaine, type de solution,
hypothèses attaquées, test reproductible, résidu, portée négative exacte et
claim éventuellement supersédé.
