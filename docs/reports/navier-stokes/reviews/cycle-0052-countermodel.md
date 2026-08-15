# Cycle 0052 — triade infrarouge signée sur \(\mathbb T^3\)

Date d'exécution : 2026-08-15

## Verdict

L'incompressibilité et la projection de Leray n'imposent aucun signe au transfert d'énergie d'une triade haute–haute vers une fréquence relativement basse. Elles n'imposent pas davantage une coercivité algébrique de la sortie

\[
P_q\bigl[(a\cdot\ell)b+(b\cdot k)a\bigr].
\]

Une famille entière de triades sur \(\mathbb T^3\) donne une sortie basse non nulle indépendante de la séparation d'échelles \(N\), tandis que la phase du mode receveur inverse exactement le transfert signé sans modifier cette sortie. D'autres polarisations unitaires admissibles annulent totalement la sortie.

Le résultat est instantané et algébrique. Il ne construit ni cascade persistante, ni solution ancienne sur \(\mathbb R^3\), ni blow-up. Sur le tore fixe, la fréquence basse vaut au minimum un ; seule la séparation relative \(|q|/|k|\to0\) est réalisée.

## 1. Convention de Fourier et triade

Sur \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\), écrivons

\[
u(x)=\sum_{m\in\mathbb Z^3}\widehat u_m e^{im\cdot x},
\qquad
m\cdot\widehat u_m=0,
\qquad
\widehat u_{-m}=\overline{\widehat u_m}.
\]

La contribution non linéaire ordonnée au mode \(q=k+\ell\) est, avec le signe de l'équation placé ensuite,

\[
F_q=P_q\bigl[(\widehat u_k\cdot\ell)\widehat u_\ell
+(\widehat u_\ell\cdot k)\widehat u_k\bigr],
\qquad
\partial_t\widehat u_q\big|_{NL}=-iF_q,
\]

où

\[
P_mz=z-\frac{m(m\cdot z)}{|m|^2}.
\]

Pour \(N\ge2\), choisissons

\[
k=(N,0,0),
\qquad
\ell=(-N,0,1),
\qquad
q=k+\ell=(0,0,1),
\]

et les polarisations

\[
a=e_3,
\qquad
b=c=e_2.
\]

Elles vérifient exactement

\[
a\cdot k=0,
\qquad
b\cdot\ell=0,
\qquad
c\cdot q=0.
\]

## 2. Réalité du champ

Pour \(A,B,C\in\mathbb R\), posons

\[
\widehat u_k=Aa,
\qquad
\widehat u_\ell=Bb,
\qquad
\widehat u_q=iCc,
\]

et imposons les coefficients négatifs par conjugaison. Le champ physique porté par ces six modes est

\[
u(x)=2Aa\cos(k\cdot x)
+2Bb\cos(\ell\cdot x)
-2Cc\sin(q\cdot x).
\]

Il est réel et divergence-free. La phase imaginaire du mode \(q\) n'est donc pas une complexification non physique : elle correspond simplement à une polarisation sinus contre des modes hauts en cosinus.

Le script représente chaque coefficient par une paire de `Fraction` — rationnels de Gauss — et vérifie directement les relations de conjugaison et de divergence.

## 3. Sortie haute–haute projetée

Les produits scalaires utiles sont

\[
a\cdot\ell=1,
\qquad
b\cdot k=0.
\]

Par conséquent,

\[
F_q=ABP_qb=ABb,
\]

car \(b\cdot q=0\). La projection de Leray ne détruit donc pas cette interaction.

La norme de la sortie est indépendante de \(N\) lorsque les amplitudes sont fixées, bien que

\[
\frac{|q|^2}{|k|^2}=\frac1{N^2}\xrightarrow[N\to\infty]{}0.
\]

L'annulation issue de l'incompressibilité remplace les facteurs hauts par un facteur de fréquence de sortie :

\[
a\cdot\ell=a\cdot(q-k)=a\cdot q,
\qquad
b\cdot k=b\cdot(q-\ell)=b\cdot q.
\]

Elle évite une croissance artificielle en \(N\), mais elle ne fournit aucun petit facteur supplémentaire \(|q|/|k|\). Sur le tore fixé, \(|q|=1\), donc la sortie reste d'ordre un.

## 4. Transferts d'énergie signés

Pour le mode \(q\),

\[
\partial_t\widehat u_q\big|_{NL}=-iABb.
\]

La contribution à l'énergie de la paire réelle \(\{q,-q\}\) vaut

\[
T_q=2\operatorname{Re}\left(
\overline{\widehat u_q}\cdot
\partial_t\widehat u_q\big|_{NL}
\right)
=-2ABC.
\]

Les deux autres réceptions associées à la même triade et à sa conjuguée donnent

\[
T_k=0,
\qquad
T_\ell=2ABC.
\]

Ainsi

\[
\boxed{T_q+T_k+T_\ell=0.}
\]

La conservation triadique d'Euler est exacte. Elle impose seulement que le gain d'un mode soit compensé par la perte d'un autre ; elle n'impose pas la direction de l'échange.

En effet :

- remplacer \(C\) par \(-C\) laisse la sortie haute–haute \(F_q=ABb\) inchangée, mais inverse \(T_q\) ;
- remplacer \(A\) ou \(B\) par son opposé inverse à la fois la sortie vectorielle et le transfert ;
- les choix \(ABC>0\), \(ABC<0\) et \(ABC=0\) donnent respectivement les deux signes ou un transfert nul.

Il n'existe donc aucune positivité algébrique déduite de la seule divergence nulle.

## 5. Absence de coercivité par polarisation

Avec les mêmes fréquences, prenons maintenant

\[
a_0=b_0=e_2.
\]

Ces deux vecteurs restent unitaires et admissibles : \(a_0\cdot k=b_0\cdot\ell=0\). Mais

\[
(a_0\cdot\ell)b_0+(b_0\cdot k)a_0=0.
\]

Ainsi, à amplitudes et fréquences identiques, la sortie projetée peut être \(+e_2\), \(-e_2\) ou zéro selon la polarisation. Toute minoration coercive uniforme de sa norme par le produit des amplitudes est fausse.

## 6. Loi d'échelle fréquentielle

Multiplions tous les vecteurs d'onde par \(M\in\mathbb N\) :

\[
k_{N,M}=(MN,0,0),
\quad
\ell_{N,M}=(-MN,0,M),
\quad
q_M=(0,0,M).
\]

Alors

\[
P_{q_M}\bigl[(a\cdot\ell_{N,M})b
+(b\cdot k_{N,M})a\bigr]=Mb,
\]

et

\[
(T_q,T_k,T_\ell)=(-2ABCM,0,2ABCM).
\]

Le coefficient se transforme donc comme une dérivée, linéairement en \(M\), tandis que

\[
\frac{|q_M|}{|k_{N,M}|}=\frac1N.
\]

Le certificat suit séparément l'échelle absolue \(M\) et la séparation relative \(N\) ; les confondre produirait une fausse amélioration infrarouge.

## 7. Limites dynamiques du calcul

Le transfert instantané reste égal à \(2|ABC|\) quand \(N\to\infty\) à \(M=1\). Avec viscosité un et amplitudes unitaires, le temps dissipatif du mode \(k\) est cependant d'ordre \(N^{-2}\). Le ledger brut

\[
|T_q|\times N^{-2}=2N^{-2}
\]

tend vers zéro. Ce produit n'est pas une estimation de la dynamique non linéaire ; il signale simplement qu'un coefficient instantané non petit ne démontre pas un transfert cumulé non petit.

Autres limites indispensables :

1. les six modes initiaux ne forment pas un support invariant ; la non-linéarité engendre notamment des modes de différence ;
2. le calcul isole la contribution d'une triade dans la décomposition standard, pas une solution fermée à six modes ;
3. un système de Galerkin fini conserve l'énergie d'Euler et ne peut certifier un blow-up PDE ;
4. la viscosité ajoute une dissipation négative \(-2\nu|m|^2|\widehat u_m|^2\) à chaque paire ;
5. aucun contrôle de pression, de solution adaptée ou de passage au continuum n'est fourni.

## 8. Écart avec \(\mathbb R^3\) et le problème Clay

Sur \(\mathbb T^3\) fixé, il n'existe pas de fréquence non nulle plus petite que l'unité. La limite \(N\to\infty\) produit une sortie relativement basse, pas une fréquence absolue tendant vers zéro.

Faire tendre \(|q|\to0\) exige soit un tore de taille croissante, soit des paquets de Fourier sur \(\mathbb R^3\). Ces opérations changent le domaine, la normalisation de l'énergie, les volumes de support spectral et les erreurs de localisation. Aucun lemme de passage au domaine infini n'est établi ici.

Le certificat ne construit donc aucune solution ancienne sur \(\mathbb R^3\), aucune solution de Leray–Hopf ou suitable, aucun scénario Type I/II, et aucune singularité admissible du problème Clay.

## 9. Reproduction et certificat

Commande :

```powershell
python -B experiments/navier-stokes/infrared-triad/infrared_triad_audit.py
```

Sortie validée :

```text
infrared_triad_audit: PASS
exact_assertions=1058
polarizations=a:e3, b:e2, projected_low_output=e2
energy_transfer=(T_q,T_k,T_ell)=(-2ABC,0,+2ABC)
sign=receiving_phase_or_high_amplitude_reverses_transfer
coercivity=unit_divergence_free_polarizations_can_also_give_zero_output
scaling=|q|^2/|k|^2=N^-2 while output_is_N-independent
scope=instantaneous triad algebra on T3; no ancient R3 solution
```

Le programme utilise exclusivement la bibliothèque standard et une arithmétique complexe exacte construite sur `Fraction`. Il vérifie 1058 identités ou inégalités : réalité, divergence, projection de Leray, transferts, conservation, changements de signe et lois d'échelle. Résidu rationnel : zéro ; aucune discrétisation flottante.

Empreinte SHA-256 du script validé :

```text
946bdab1e449ed56a8bbdfe7f7f1d09557e41e2caa8012b055e77f334cc68417
```

## Décision contradictoire

**ABANDONNER** toute coercivité ou positivité universelle d'une triade infrarouge fondée uniquement sur l'incompressibilité. **CONTINUER** seulement avec une hypothèse supplémentaire portant sur les phases, la géométrie statistique, la dynamique temporelle ou une somme structurée de triades ; cette hypothèse devra elle-même être falsifiée contre les changements de polarisation ci-dessus.
