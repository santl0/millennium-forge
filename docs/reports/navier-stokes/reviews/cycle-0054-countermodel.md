# Cycle 0054 — flux scalaire aveugle au mouvement tangent

Date d'exécution : 2026-08-15

## Verdict

Une énergie scalaire monotone et un flux total fini ne contrôlent pas nécessairement la norme du générateur. Le contre-modèle hilbertien exact satisfait

\[
G(0)=0,
\qquad
\int_{-\infty}^0J(s)\,ds=1,
\qquad
J=-E',
\]

mais

\[
\|G'(s)\|^2\ge\frac12
\]

pour tout \(s\le0\). Le flux ne voit que le mouvement radial de \(G\), tandis qu'une rotation tangentielle persistante garde le générateur loin de zéro.

Le modèle se réalise exactement dans le sous-espace solénoïdal engendré par deux polarisations réelles d'une même fréquence sur \(\mathbb T^3\). Cette réalisation est une **courbe dans un espace de Galerkin**, pas une solution Galerkin de Navier–Stokes. Son résidu Navier–Stokes est partout non nul.

## 1. Cadre hilbertien

Soient \(\phi_1,\phi_2\) deux vecteurs orthonormés dans un espace de Hilbert réel. Définissons

\[
e(s)=\cos s\,\phi_1+\sin s\,\phi_2,
\]

\[
t(s)=-\sin s\,\phi_1+\cos s\,\phi_2.
\]

Alors

\[
e'=t,
\qquad
t'=-e,
\qquad
\|e\|=\|t\|=1,
\qquad
\langle e,t\rangle=0.
\]

Pour \(s\le0\), posons

\[
q=e^s,
\qquad
h=1-q,
\qquad
G(s)=h(s)e(s).
\]

Comme \(q'=q\) et \(h'=-q\),

\[
\boxed{G'=-qe+ht.}
\]

La composante \(-qe\) est radiale ; la composante \(ht\) est tangentielle.

## 2. Énergie, flux et vitesse

Choisissons l'énergie scalaire

\[
E(s)=\|G(s)\|^2=h^2.
\]

Sa dérivée est

\[
E'=2\langle G,G'\rangle=-2qh.
\]

Le flux positif associé vaut donc

\[
\boxed{J=-E'=2q(1-q).}
\]

La composante tangentielle est exactement invisible :

\[
\langle he,ht\rangle=0.
\]

En revanche, la norme complète du générateur est

\[
D^2:=\|G'\|^2=q^2+h^2.
\]

En complétant le carré,

\[
\boxed{
D^2=2\left(q-\frac12\right)^2+\frac12
\ge\frac12.}
\]

Le minimum \(1/2\) est atteint à \(q=1/2\). À l'instant terminal \(s=0\),

\[
q=1,
\qquad
h=0,
\qquad
G(0)=0,
\qquad
D(0)^2=1.
\]

Ainsi, même l'annulation exacte de l'état terminal ne force pas l'annulation du générateur dans ce modèle abstrait.

## 3. Flux total exact

Le changement de variables \(dq=q\,ds\) donne

\[
J(s)\,ds=2(1-q)\,dq.
\]

Par conséquent,

\[
\int_{-\infty}^0J(s)\,ds
=\int_0^12(1-q)\,dq
=1.
\]

Sur l'intervalle tronqué \(s\in[-N\log2,0]\), on a \(q_0=2^{-N}\) et

\[
\int_{-N\log2}^0J(s)\,ds
=(1-2^{-N})^2.
\]

Le résidu vers le flux total vaut exactement

\[
1-(1-2^{-N})^2
=2^{1-N}-2^{-2N}.
\]

Il tend vers zéro, alors que \(D^2\ge1/2\) sur chaque coquille temporelle. En particulier,

\[
\int_{-N\log2}^0D(s)^2\,ds
\ge\frac{N\log2}{2}.
\]

Le calcul fermé est même

\[
\int_{-N\log2}^0D(s)^2\,ds
=N\log2-1+2^{1-N}-2^{-2N},
\]

qui diverge lorsque \(N\to\infty\). Le flux scalaire est intégrable, mais l'action quadratique du générateur ne l'est pas.

## 4. Obstruction asymptotique

Lorsque \(s\to-\infty\),

\[
q\to0,
\qquad
h\to1,
\qquad
J(s)\to0,
\qquad
D(s)^2\to1.
\]

Plus précisément,

\[
\frac{J}{D^2}
=\frac{2q(1-q)}{q^2+(1-q)^2}
\le4q.
\]

Sur la suite \(s_N=-N\log2\), le membre droit vaut \(2^{2-N}\). Le flux instantané tend donc vers zéro tandis que la vitesse reste minorée. Il n'existe aucune sous-suite \(s_n\to-\infty\) telle que \(D(s_n)\to0\).

La direction \(e(s)\) effectue en outre une infinité de rotations lorsque \(s\to-\infty\). La norme de \(G\) tend vers un, mais le champ n'a pas de limite forte sans extraction de phase ; toute limite de phase conserve un générateur tangent non nul.

## 5. Réalisation solénoïdale sur \(\mathbb T^3\)

Sur \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\), posons, après normalisation \(L^2\) commune,

\[
\phi_1(x)=Z^{-1}(0,\cos x_1,0),
\qquad
\phi_2(x)=Z^{-1}(0,0,\cos x_1).
\]

Ces champs sont réels, orthonormés et divergence-free. Ils correspondent aux deux polarisations \(e_2,e_3\) de la même paire de fréquences \(\pm(1,0,0)\), et

\[
-\Delta\phi_1=\phi_1,
\qquad
-\Delta\phi_2=\phi_2.
\]

Pour toute combinaison

\[
u(x)=g_1\phi_1(x)+g_2\phi_2(x),
\]

le champ dépend seulement de \(x_1\) et sa première composante est nulle. Par conséquent,

\[
(u\cdot\nabla)u=0.
\]

La courbe

\[
u(s)=G_1(s)\phi_1+G_2(s)\phi_2
\]

est donc une réalisation exacte du modèle hilbertien dans un sous-espace de Galerkin solénoïdal de dimension deux.

## 6. Résidu Navier–Stokes non nul

Sur ce sous-espace, avec viscosité un, sans force et après projection de Leray, Navier–Stokes se réduirait à

\[
G'+G=0,
\]

puisque la convection est nulle et \(-\Delta\) vaut l'identité. Pour la courbe prescrite,

\[
G'+G
=-qe+ht+he
=(1-2q)e+ht.
\]

Sa norme au carré est

\[
\|G'+G\|^2=(1-2q)^2+h^2>0
\]

pour tout \(0\le q\le1\) : les deux coefficients ne peuvent pas s'annuler simultanément. Comme ce résidu est divergence-free et appartient au sous-espace de Fourier transverse, aucun gradient de pression ne peut le compenser.

La véritable dissipation d'énergie Navier–Stokes, avec la convention \(E=\|G\|^2\), serait

\[
2\|\nabla u\|_2^2=2h^2.
\]

Elle n'est pas le flux artificiel

\[
J=2qh,
\]

sauf aux valeurs isolées \(q=1/2\) et \(q=1\). Le modèle ne satisfait donc ni l'équation ni son identité d'énergie. Une vraie solution du système de Galerkin terminant à zéro serait identiquement nulle par unicité de l'ODE ; notre courbe ne l'est pas.

## 7. Inferences réfutées au niveau abstrait

Le certificat exclut, sans hypothèse coercive supplémentaire, les implications suivantes :

1. \(J=-E'\ge0\) et \(J\in L^1\) impliqueraient \(G'\in L^2\) ;
2. une suite \(J(s_n)\to0\) impliquerait \(G'(s_n)\to0\) ;
3. une énergie ayant une limite à \(-\infty\) imposerait une limite forte de l'état ;
4. un état terminal nul et un flux total fini imposeraient une trajectoire stationnaire ;
5. un bilan scalaire contrôlerait les directions tangentielles à ses surfaces de niveau.

Une conclusion stationnaire exige une inégalité du type

\[
\|G'\|^2\le C J
\]

ou une identité PDE fournissant une coercivité équivalente. Le contre-modèle montre qu'une telle inégalité ne découle pas de \(J=-E'\) seul : ici \(D^2/J\to\infty\) lorsque \(s\to-\infty\).

## 8. Pourquoi rien ne se transfère automatiquement à Navier–Stokes sur \(\mathbb R^3\)

1. La courbe est prescrite ; elle ne résout pas Navier–Stokes même sur \(\mathbb T^3\).
2. Le flux \(J\) n'est pas la dissipation visqueuse de Navier–Stokes.
3. Les ondes planes périodiques ne sont ni \(L^2\) ni faible-\(L^3\) sur \(\mathbb R^3\).
4. Localiser ces modes introduirait d'autres fréquences, une remise en divergence et des termes convectifs absents du calcul.
5. Le modèle est de dimension deux ; il ne contient ni cascade, ni pression non locale, ni passage au continuum.
6. Une identité d'énergie suitable ou Leray–Hopf peut précisément apporter la coercivité que le modèle omet.

Le certificat ne construit donc aucune solution ancienne sur \(\mathbb R^3\), aucun profil de blow-up et aucune obstruction à un théorème PDE utilisant réellement la dissipation et l'équation.

## 9. Reproduction et certificat

Commande :

```powershell
python -B experiments/navier-stokes/tangential-flux/tangential_flux_audit.py
```

Sortie validée :

```text
tangential_flux_audit: PASS
exact_assertions=47259
model=q=e^s, h=1-q, G=h*e, G_prime=-q*e+h*t
energy=E=h^2, flux=J=-E_prime=2*q*(1-q)
speed=D^2=q^2+h^2=2*(q-1/2)^2+1/2
integral_J_from_minus_infinity_to_zero=1
terminal=G(0)=0_but_D(0)^2=1
ns_residual=G_prime+G_is_everywhere_nonzero
scope=Hilbert/Galerkin countermodel; not an NS or R3 solution
```

Le script utilise exclusivement la bibliothèque standard et `Fraction`. Il balaie des orientations rationnelles du cercle unité, tous les rationnels dyadiques jusqu'au dénominateur \(2^8\), 64 échelles anciennes et des partitions jusqu'à \(2^{10}\) cellules. Les 47259 assertions ont un résidu rationnel nul ; aucune approximation flottante n'intervient.

Empreinte SHA-256 du script validé :

```text
d5de9de189ed2f2a2db7887b88aa6530a6fe365388c6db0de99ce2c30814693e
```

## Décision contradictoire

**ABANDONNER** toute inférence « flux scalaire intégrable \(\Rightarrow\) générateur petit » sans coercivité démontrée. **CONTINUER** seulement si le candidat stationnaire issu de Navier–Stokes dispose d'une identité reliant quantitativement le défaut temporel complet à la dissipation PDE, avec constantes uniformes sous extraction, changement de base et passage au domaine infini.
