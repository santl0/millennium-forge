# Cycle 0057 — rotation rapide, variation du réciproque et faux effondrement

Date d'exécution : 2026-08-15

## Verdict

L'argument d'intégration par parties fondé sur

\[
q_n=\frac1{\beta_n}
\]

se ferme si les deux quantités

\[
\|q_n\|_{L^\infty}\to0,
\qquad
\operatorname{Var}(q_n)\to0
\]

sont contrôlées, avec une phase ne traversant pas \(\beta_n=0\), un état borné et des tests fixes de variation bornée.

La seule hypothèse \(\beta_n\to+\infty\), équivalente à \(\|q_n\|_\infty\to0\) ici, ne suffit pas. Un contre-modèle stroboscopique exact possède uniquement les vitesses positives

\[
\beta_N\in\{N,N^4\},
\]

mais

\[
\|q_N\|_\infty=\frac1N\to0,
\qquad
\operatorname{Var}(q_N)
=\left(2N^2-1\right)\left(\frac1N-\frac1{N^4}\right)
\sim2N.
\]

Les passages rapides occupent seulement une mesure

\[
\frac1{N^2+N+1}<\frac1{N^2}.
\]

L'orbite converge fortement dans tout \(L^p\), \(1\le p<\infty\), vers une phase constante modulo le groupe, mais pas uniformément. Ce modèle isole donc la variation de \(q_N\) sans changement de signe ni zéro de \(\beta_N\).

Un ancien modèle triangulaire signé est conservé séparément : il converge uniformément vers une orbite prescrite non stationnaire, mais ses vitesses changent de signe par sauts. Il attaque donc les portes « signe constant » et « régularité \(W^{1,1}\) », et non la variation seule.

Les autres contre-tests montrent que la division échoue lorsque \(\beta_n\) traverse zéro, qu'une convergence distributionnelle ne contrôle pas un test mobile, et qu'une moyenne angulaire axisymétrique ne rend pas le profil lui-même axisymétrique.

Tout le certificat est discret ou de dimension finie. Aucune solution de Navier–Stokes n'est construite.

## 1. Estimation discrète par parties

Sur une grille \(0=t_0<\cdots<t_M=1\), soient \(X_i\) des valeurs d'orbite, \(q_i\) les réciproques de modulation sur les cellules et \(\varphi_i\) un test. Posons

\[
S=\sum_{i=0}^{M-1}
q_i\varphi_i(X_{i+1}-X_i).
\]

Avec \(a_i=q_i\varphi_i\), la sommation par parties exacte donne

\[
S=a_{M-1}X_M-a_0X_0
+\sum_{i=1}^{M-1}(a_{i-1}-a_i)X_i.
\tag{1}
\]

Si \(|X_i|\le B\), alors

\[
|S|\le B\left[
2\|q\|_\infty\|\varphi\|_\infty
+\|\varphi\|_\infty\operatorname{Var}(q)
+\|q\|_\infty\operatorname{Var}(\varphi)
\right].
\tag{2}
\]

Cette identité est l'analogue discret de

\[
RX=qX',
\]

suivi d'une intégration par parties contre un test fixé.

## 2. Cas positif rationnel

Prenons \(M=N=2^m\) et

\[
q_i=\frac1N+\frac{(-1)^i}{N^3}.
\]

Tous les \(q_i\) sont strictement positifs, donc \(\beta_i=1/q_i\) est défini. Les deux quantités critiques valent exactement

\[
\|q\|_\infty=\frac{N^2+1}{N^3},
\]

\[
\operatorname{Var}(q)
=\frac{2(N-1)}{N^3}.
\]

Elles tendent toutes deux vers zéro. Le certificat choisit des valeurs rationnelles bornées de \(X_i\) et le test fixé discrétisé \(\varphi_i=i/N\), puis vérifie exactement (1), (2) et la décroissance du majorant sur neuf échelles.

La conclusion abstraite est la suivante : si \(X_n\) reste borné dans l'espace où le test agit, si \(q_n\to0\) uniformément, si \(\operatorname{Var}(q_n)\to0\), et si les tests ont des normes BV uniformes, alors le terme intégré contenant \(RX_n\) tend vers zéro.

## 3. Stroboscopie positive : variation isolée

Normalisons la période angulaire à \(1\). Pour \(N=2^m\), posons

\[
D_N=N^2+N+1,
\qquad
\delta_N=\frac{N+1}{D_N}<\frac1N.
\]

Chacun des \(N^2\) cycles comporte exactement deux passages :

| passage | angle parcouru | vitesse \(\beta_N\) | durée |
|---|---:|---:|---:|
| lent | \(\delta_N\) | \(N\) | \(\delta_N/N=(N+1)/(ND_N)\) |
| rapide | \(1-\delta_N\) | \(N^4\) | \((1-\delta_N)/N^4=1/(N^2D_N)\) |

Les deux durées ont pour somme exacte

\[
\frac{N+1}{ND_N}+\frac1{N^2D_N}=\frac1{N^2}.
\]

Ainsi, les \(N^2\) cycles remplissent exactement \([0,1]\), sans changement d'échelle temporelle caché. La phase relevée gagne exactement un tour par cycle et la phase modulo le groupe revient à zéro.

Les deux valeurs du réciproque sont

\[
q_{\rm lent}=\frac1N,
\qquad
q_{\rm rapide}=\frac1{N^4}.
\]

Elles sont strictement positives et

\[
\|q_N\|_\infty=\frac1N.
\]

La suite alternée contient \(2N^2-1\) sauts internes. Par conséquent,

\[
\boxed{
\operatorname{Var}(q_N)
=\left(2N^2-1\right)
\left(\frac1N-\frac1{N^4}\right)
=2N-\frac1N-\frac2{N^2}+\frac1{N^4}.}
\]

En particulier,

\[
N<\operatorname{Var}(q_N)<2N,
\]

pour \(N\ge2\). La mesure totale des passages rapides vaut exactement

\[
F_N=N^2\frac1{N^2D_N}
=\frac1{D_N}<\frac1{N^2}.
\]

Soit \(Q_\alpha\) une action unitaire de période \(1\), \(U\) un profil dans le domaine de son générateur \(R\), et prenons comme cible la phase constante \(Q_0U=U\). Sur les passages lents, la phase modulo le groupe appartient à \([0,\delta_N]\), donc

\[
\|Q_{\theta_N(t)}U-U\|
\le\delta_N\|RU\|.
\]

Sur les passages rapides, la borne triviale vaut \(2\|U\|\). Pour tout réel \(p\ge1\),

\[
\int_0^1\|Q_{\theta_N(t)}U-U\|^p\,dt
\le
(1-F_N)\delta_N^p\|RU\|^p
+F_N2^p\|U\|^p.
\tag{3}
\]

Le membre droit tend vers zéro. Le certificat rationnel vérifie (3), avec \(\|U\|=\|RU\|=1\), pour les exposants entiers \(p=1,\ldots,6\) et huit échelles. L'estimation analytique établit la convergence forte pour chaque \(1\le p<\infty\).

La convergence n'est pas uniforme : chaque passage rapide traverse exactement la demi-rotation. Pour une orbite planaire non triviale, par exemple \(U=e_1\), la distance à \(U\) y atteint \(2\). La mesure de cet ensemble disparaît, mais pas son amplitude.

Ce modèle sépare proprement l'hypothèse de variation : \(\beta_N\) est partout positif, \(\min\beta_N=N\to\infty\) et \(q_N\to0\) uniformément, tandis que \(\operatorname{Var}(q_N)\to\infty\).

## 4. Modèle triangulaire signé : porte distincte

Conservons aussi le modèle antérieur pour identifier une obstruction différente. Fixons \(\psi(t)=t\), partageons \([0,1]\) en \(N^2\) cellules, et ajoutons une fonction triangulaire \(a_N\) dont les valeurs aux nœuds alternent entre \(0\) et \(1/N\). Alors

\[
\theta_N=\psi+a_N,
\qquad
\beta_N\in\{N+1,1-N\},
\]

et

\[
\|q_N\|_\infty=\frac1{N-1},
\qquad
\operatorname{Var}(q_N)
=(N^2-1)\left(\frac1{N+1}+\frac1{N-1}\right)
=2N.
\]

Comme \(\|\theta_N-\psi\|_\infty=1/N\), toute orbite régulière vérifie

\[
Q_{\theta_N}U\longrightarrow Q_tU
\]

uniformément. Cette limite peut être non stationnaire. Toutefois, ce modèle change le signe de \(\beta_N\) par sauts. Il ne sépare donc pas la variation de l'absence de signe constant : tout lissage continu du changement de signe traverse zéro. Il est conservé comme contre-test spécifique à une preuve qui omettrait une hypothèse de signe ou de régularité \(W^{1,1}\), pas comme preuve principale du rôle de \(\operatorname{Var}(q_N)\).

## 5. Traversée de zéro

Considérons

\[
\beta(t)=2t-1.
\]

Sur la grille rationnelle

\[
t_i=\frac{i}{2N},
\]

on a

\[
\beta(t_N)=0.
\]

Le réciproque \(q=1/\beta\) n'est donc pas défini. Même en retirant le nœud zéro, les voisins vérifient

\[
|\beta|=\frac1N,
\qquad
|q|=N.
\]

La norme ponctuée de \(q\) diverge. Pour une modulation continue changeant de signe, le théorème des valeurs intermédiaires rend cette obstruction inévitable. Une preuve divisant par \(\beta\) doit établir une minoration uniforme de \(|\beta|\), pas seulement une grande valeur moyenne ou presque partout.

## 6. Résidu distributionnel et test mobile

Soit

\[
r_n(t)=(-1)^{\lfloor2^nt\rfloor}.
\]

Pour chaque test dyadique fixé \(\varphi_m\),

\[
\int_0^1r_n\varphi_m\,dt=0
\qquad(n>m).
\]

Par densité et borne uniforme, \(r_n\to0\) dans les distributions. Mais le test mobile

\[
\varphi_n=r_n
\]

donne

\[
\boxed{\int_0^1r_n\varphi_n\,dt=1.}
\]

Ainsi, un résidu tendant vers zéro dans \(\mathcal D'\) ne peut pas être testé contre une orbite, une phase ou un générateur dépendant de \(n\) sans une norme uniforme permettant de remplacer ce test mobile par un test fixe.

## 7. Moyenne angulaire versus symétrie du profil

Dans \(\mathbb R^3\), faisons agir les rotations du plan \((e_1,e_2)\) et prenons

\[
U=e_1+e_3.
\]

La moyenne exacte sur les quatre quarts de tour est

\[
\frac14\sum_{j=0}^3Q_{j\pi/2}U=e_3.
\]

Cette moyenne est fixée par toutes les rotations autour de l'axe : son générateur est nul. Pourtant,

\[
RU=e_2,
\qquad
\|RU\|=1.
\]

Le profil initial n'est pas axisymétrique. Une limite faible ou une moyenne de phases peut donc être stationnaire/axisymétrique tout en masquant une orbite entièrement non axisymétrique. Pour conclure sur le profil lui-même, il faut une convergence forte ou une concentration de la mesure de phase, pas seulement son barycentre.

## 8. Hypothèses réellement nécessaires

L'estimation positive requiert simultanément :

1. \(\beta_n\) défini et séparé de zéro sur l'intervalle pertinent ;
2. \(q_n=1/\beta_n\to0\) dans \(L^\infty\) ;
3. \(\operatorname{Var}(q_n)\to0\), y compris les sauts ;
4. des bornes uniformes sur l'orbite \(X_n\) ;
5. des tests fixes, bornés et de variation contrôlée ;
6. un résidu petit dans une norme duale compatible avec ces tests ;
7. une sous-suite commune à la phase, au profil et au résidu.

La stroboscopie positive réfute proprement l'omission de 3, même sous \(\beta_n>0\) et \(\min\beta_n\to\infty\). La stroboscopie signée teste séparément l'absence d'hypothèse de signe ou de régularité. La traversée de zéro réfute 1 ; le Rademacher réfute 6 ; la moyenne angulaire réfute toute conclusion de symétrie forte fondée seulement sur un barycentre.

## 9. Séparation stricte avec Navier–Stokes

Les phases stroboscopiques sont prescrites. Elles ne proviennent d'aucune équation de modulation Navier–Stokes et leurs dérivées ont des sauts. Dans le modèle positif, chaque saut de \(\beta_N\) entre \(N\) et \(N^4\) peut être lissé de façon monotone tout en gardant \(\beta_N>0\) ; en comprimant les zones de transition, les durées et la variation peuvent rester arbitrairement proches des valeurs certifiées. Cette observation n'est pas un certificat PDE : le script ne contrôle ni le résidu créé par ce lissage, ni une norme Navier–Stokes admissible.

Les vecteurs de \(\mathbb R^3\), grilles temporelles et fonctions de Rademacher ne contiennent ni vitesse incompressible tridimensionnelle, ni pression, ni projection de Leray, ni dissipation.

Dans une application PDE, il faudrait vérifier en plus :

- que la phase est absolument continue et que \(\beta_n=\theta_n'\) a le signe et la régularité requis ;
- que le générateur de rotation agit dans l'espace fonctionnel de la solution ;
- que l'intégration par parties est légitime avec les traces temporelles disponibles ;
- que les termes de pression et de convection passent dans la même sous-suite ;
- que le résidu est petit dans la norme duale nécessaire, pas seulement dans \(\mathcal D'\) ;
- que la limite n'est pas uniquement une moyenne de phase.

Aucune solution ancienne, suitable, Leray–Hopf ou classique n'est construite. Aucun résultat sur la régularité ou le blow-up Clay n'est revendiqué.

## 10. Reproduction et certificat

Commande :

```powershell
python -B experiments/navier-stokes/fast-rotation-collapse/fast_rotation_audit.py
```

Sortie validée :

```text
fast_rotation_audit: PASS
exact_assertions=44218
positive=||q_n||_infinity_to_zero_and_Var(q_n)_to_zero_close_IBP
positive_stroboscopy=beta_in_{N,N^4}_and_||q_n||_infinity=1/N
positive_stroboscopy_Var(q_n)=(2N^2-1)*(1/N-1/N^4)~2N
positive_stroboscopy_fast_measure=1/(N^2+N+1)_and_strong_Lp
signed_stroboscopy=uniform_nonstationary_limit_but_sign_and_W11_gate_fail
zero_crossing=q_n=1/beta_n_is_undefined_and_punctured_sup_grows
distributional=fixed_tests_vanish_but_mobile_test_pairing_is_one
angular_average=is_axis_fixed_while_profile_generator_norm_is_one
seed=n/a; scope=exact_discrete_models; no Navier-Stokes PDE claim
```

Le script utilise uniquement la bibliothèque standard et `Fraction`. Les 44218 assertions certifient la sommation par parties, les constantes BV, les deux grilles stroboscopiques, les mesures temporelles et bornes \(L^p\), les zéros de \(\beta\), les tests distributionnels et la moyenne angulaire. Graine : non applicable. Résidu rationnel : zéro ; aucune approximation flottante.

Empreinte SHA-256 du script validé :

```text
ab815a4d6db1a1b956a50b87c428f8fb6aaf97bc6e16abb3e977685758a1ea69
```

## Décision contradictoire

**CONSERVER** l'estimation par parties lorsque \(q_n\to0\) uniformément et \(\operatorname{Var}(q_n)\to0\). **ABANDONNER** toute conclusion d'effondrement fondée sur la seule grandeur de \(|\beta_n|\). **RÉVISER** l'application Navier–Stokes pour contrôler les zéros, la variation totale, la norme du résidu contre tests mobiles et la distinction entre convergence forte et moyenne angulaire.
