# Cycle 0011 — Porte de parité de la projection instable Hou–Wang–Yang

Date de gel : 2026-08-14.

## Décision du cycle

La veille différentielle n'a trouvé ni version postérieure à
`arXiv:2509.25116v2`, ni source primaire ultérieure fermant le raccord vers
une donnée Clay lisse. Trois actions réversibles ont été notées sur 5 :

| Action | Nouveauté | Tractabilité | Falsifiabilité | Levier | Total |
|---|---:|---:|---:|---:|---:|
| tester la sélection exacte par parité et l'horloge de la couche parabolique | 5 | 5 | 5 | 5 | **20** |
| reconstruire un projecteur adjoint quantitatif depuis les artefacts publics | 4 | 3 | 5 | 4 | 16 |
| établir un shadowing non linéaire complet de `t~epsilon²` à un temps fixe | 5 | 1 | 3 | 5 | 14 |

La première action est sélectionnée. Lemme actif unique : une couche intérieure
qui respecte la réflexion HWY est paire et ne peut exciter linéairement le mode
certifié impair. Expérience active unique :
`HWY-PARITY-PROJECTION-GATE-1`.

## Équation et type de solution

Le cadre dynamique est

```text
partial_t u + (u dot nabla)u - Delta u + nabla p = 0,
div u = 0
```

sur `R³ x (0,T)`, sans frontière ni force et avec viscosité `nu=1`. Pour une
donnée initiale lisse, compacte et divergence-free, la solution forte locale
unique est utilisée uniquement pour transmettre la symétrie. Une solution
faible de Leray–Hopf peut ensuite perdre l'unicité; aucune préservation de
symétrie n'est affirmée au-delà de la durée d'unicité faible–forte.

La source HWY annonce des solutions adaptées de Leray–Hopf, lisses pour
`t>0`, issues d'une donnée compacte mais singulière en zéro. Son profil
auto-similaire `U` est pair sous la réflexion ci-dessous; la fonction propre
certifiée `v` est impaire et la branche dans cette direction brise la
symétrie. Ces faits ne rendent pas la donnée admissible au cas Clay.

## Involution, pression et projecteurs

Posons `S=diag(1,1,-1)` et

```text
(J u)(x)=S u(Sx).
```

Le secteur pair `Ju=u` s'écrit en composantes

```text
u_x(x,y,-z)= u_x(x,y,z),
u_y(x,y,-z)= u_y(x,y,z),
u_z(x,y,-z)=-u_z(x,y,z).
```

Le secteur impair a les signes opposés et son projecteur est
`Q_-=(I-J)/2`. Une convolution radiale et un cutoff radial commutent avec `J`.
La non-localité n'est pas ignorée : dans les variables de Fourier,

```text
P(xi)=I-xi tensor xi/|xi|²,
P(Sxi)=S P(xi) S,
```

donc la projection de Leray commute elle aussi avec `J`. Le Laplacien commute
avec les isométries orthogonales et la non-linéarité satisfait
`B(Ju,Jv)=J B(u,v)`. Pour un profil pair `U`, l'opérateur linéarisé `L_U`
commute avec `J`; les secteurs pairs et impairs sont invariants.

Il s'ensuit exactement que

```text
J g_epsilon=g_epsilon
  => Q_- exp(t L_U)g_epsilon=0
  => <ell_-,exp(t L_U)g_epsilon>=0
```

pour tout fonctionnel adjoint impair continu `ell_-`. Ce résultat ne suppose
pas la normalisation numérique d'un vecteur propre adjoint.

## Échelle de la couche parabolique

Pour le modèle intérieur

```text
g_epsilon(x)=epsilon^-1 g(x/epsilon),
t=kappa epsilon²,
tau_epsilon=log(kappa)+2log(epsilon),
```

la chaleur vérifie exactement

```text
sqrt(t) exp(t Delta)g_epsilon(sqrt(t)xi)
  =sqrt(kappa)(exp(kappa Delta)g)(sqrt(kappa)xi).
```

Le profil de similarité est donc d'ordre un, et non petit, quand
`epsilon -> 0`. Si une composante impaire non nulle est introduite avec une
amplitude `mu_epsilon=epsilon^beta`, un mode dynamique de taux `a>0` la
multiplie entre `tau_epsilon` et zéro par

```text
exp(-a tau_epsilon)=kappa^-a epsilon^-2a.
```

Le dictionnaire de signe de la source transforme la valeur elliptique
candidate `tilde_lambda~-0.113142` en taux dynamique `a=-tilde_lambda>0`.
Sa borne conservatrice `a>=0.1085=217/2000` impose nécessairement
`beta>=2a>=217/1000` pour garder bornée une composante linéaire dont le
coefficient adjoint ne s'annule pas. La condition `beta>=0.217` n'est pas
suffisante sans borne supérieure certifiée sur `a` et sur le projecteur.
Elle ne constitue surtout pas une condition de tir non linéaire : la coordonnée
terminale contient aussi l'intégrale projetée du cutoff extérieur, de la
non-linéarité et de la pression via la projection de Leray. Une couche impaire
`O(1)` quitte le régime perturbatif après un temps encore `O(epsilon²)`; son
amplification formelle jusqu'à `tau=0` ne peut pas être extrapolée.

## Audit des artefacts publics

Le dépôt primaire a été relu en lecture seule au commit
`615ee6f3eca3abad7b5814fe9334bcd80bea0328`.

Le manifeste récursif contient 70 blobs totalisant `84 137 370` octets; son
SHA-256 de métadonnées triées est
`cde7bc4c6784d6c2b799714fd3ee034580cf3f3d28c42402da8ff20cf1274969`.

- `data/up_eig.mat` contient `lambda`, le profil et une fonction propre droite;
  aucun vecteur propre gauche identifié n'y est exposé.
- `data/eig.mat` contient les familles `eig_val_even`, `eig_val_odd`,
  `eig_vec_even`, `eig_vec_odd` utilisées dans les estimations de coercivité
  de rang fini; elles ne constituent pas un projecteur adjoint dynamique.
- `eigenpair_error_analysis.ipynb` applique une transposée discrète au vecteur
  propre droit pour calculer un résidu; ce n'est pas la construction d'une
  fonction propre gauche certifiée.
- la section 5.1 du manuscrit mentionne des vecteurs gauche et droit dans une
  procédure numérique, mais les livrables publics audités ne fournissent pas
  un fonctionnel adjoint normalisé avec encadrement d'intervalle.

La parité suffit pour la conclusion nulle du présent cycle. Elle ne suffit pas
pour calculer la projection d'un lissage asymétrique. Un certificat quantitatif
demanderait au minimum un vecteur propre gauche encadré, un minorant de son
pairing avec le vecteur droit, une norme de projecteur ou une borne de résolvante
sur contour, et une application bornée de la couche vers l'espace de profil.

## Test adverse et portée

Le script utilise des fractions exactes dans une base abstraite adaptée à la
parité. Il vérifie `J²=I`, l'idempotence et l'orthogonalité de `Q_+` et `Q_-`,
`[L,J]=0`, l'annulation du secteur impair d'une couche paire et l'exposant nul
de la couche au temps parabolique. Tous les résidus cibles valent exactement
zéro, sans flottant.

Le contre-test ajoute un couplage pair vers impair. Son commutateur a une
valeur absolue maximale `2` et la couche paire acquiert une composante impaire
de taille `3`. La commutation par réflexion est donc une hypothèse décisive et
falsifiable, pas un argument dimensionnel.

Trois limites restent ouvertes :

1. la CAP certifie un mode impair, pas l'absence de tout mode instable pair;
2. une perturbation asymétrique peut avoir un coefficient adjoint non nul;
3. l'unicité forte préserve la parité avant le breakdown, mais n'interdit pas
   des solutions faibles ultérieures qui brisent spontanément la symétrie.

De plus, changer le signe ou l'amplitude d'une perturbation impaire construit
des **données Clay différentes**. Même si elles sélectionnaient des limites
différentes de la donnée singulière, cela ne donnerait pas deux solutions pour
une même donnée Clay lisse.

La conclusion transférable au problème Clay est négative et précise : la
désingularisation symétrique naturelle ne transfère pas le mécanisme instable
impair certifié avant une perte de régularité forte. Elle ne démontre ni
régularité globale, ni blow-up, ni unicité faible globale.

Trois revues contradictoires séparées ont été conservées : audit PDE de la
balance projetée, audit primaire différentiel et audit en lecture seule des
artefacts publics. Elles confirment l'annulation par parité, mais imposent les
réserves sur le régime perturbatif, l'adjoint et la multiplicité spectrale.
Elles ont été produites par des agents Codex de la même famille de modèles et
ne constituent donc pas une revue indépendante externe.

## Décision

La route « lissage radial puis excitation générique du mode HWY certifié » est
abandonnée (`FAIL-NS-0014`). Le verrou est révisé vers une famille asymétrique
contrôlée `g_epsilon^+ + epsilon^beta g_epsilon^-`, avec `beta` suivi à
l'échelle critique et coefficient adjoint certifié. Le premier test décisif du
cycle suivant sera un audit des données publiques nécessaires pour normaliser
ce coefficient; à défaut d'artefact, le résultat négatif documentera la donnée
CAP minimale manquante avant tout calcul lourd. Ce test mesure une sensibilité
de sélection vers la donnée singulière; il ne sera pas présenté comme une
non-unicité pour une donnée Clay fixée.
