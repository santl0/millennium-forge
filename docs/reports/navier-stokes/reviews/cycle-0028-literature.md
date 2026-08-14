# Cycle 0028 — audit bibliographique indépendant

Date de veille : 2026-08-14 (Europe/Paris).

Périmètre : anneaux de vortex axisymétriques sans swirl, direction de
vorticité et critères BMO/log-BMO, concentration d'un tore mince,
extensions à valeurs dans la sphère, et veille primaire 2025–2026.

Statut de ce document : revue contradictoire indépendante. Les calculs
signalés « recalculé ici » ne sont pas des résultats publiés et ne doivent
pas recevoir le statut `PAPER_PROOF`.

## Verdict exécutif

1. Un champ axisymétrique sans swirl a
   \(u=u^r(r,z,t)e_r+u^z(r,z,t)e_z\) et
   \(\omega=\omega^\theta(r,z,t)e_\theta\). Cette classe visqueuse est
   globalement régulière sous les hypothèses classiques pertinentes. Un
   anneau lisse de ce type est donc une sous-classe déjà régulière du cas
   \(\mathbb R^3\) de Clay, pas un candidat de blow-up.
2. Les résultats quantitatifs modernes sur les anneaux visqueux contrôlent
   des filaments circulaires ou des anneaux minces, mais restent dans la
   classe sans swirl. Ils ne transfèrent pas un mécanisme singulier vers les
   données tridimensionnelles générales.
3. La norme log-BMO de Bradshaw–Grujić (2015) et celle du préprint de Grujić
   (2026) ne sont pas la même norme : la première emploie des cubes et une
   ancre \(L^1\), la seconde des boules et une ancre \(L^\infty\). Les
   constantes et les quantificateurs ne peuvent pas être identifiés sans
   lemme d'équivalence.
4. Une famille statique de tores minces avec
   \(h_n\ll q_n\ll R_n\), dont la direction active est \(e_\theta\), admet
   une extension \(S^2\)-valuée logarithmique vers \(e_z\) avec borne
   log-BMO uniforme. Chaque tube \(d_n<q_n\) reste loin de l'axe, même si
   \(R_n\to0\). Une formule et l'audit des quatre régimes de boules sont
   donnés ci-dessous.
5. Aucune source primaire trouvée ne formule cette combinaison exacte
   « tore actif rétrécissant + corridor logarithmique
   \(e_\theta\to e_z\) + estimation log-BMO uniforme ». Le verdict
   d'antériorité est donc
   **non trouvée dans la veille ciblée**, et non « nouveauté démontrée ».
6. Pour l'évolution exactement axisymétrique sans swirl sur \(\mathbb R^3\)
   d'un anneau unisigné, le tampon de vorticité nulle disparaît à tout temps
   positif. La direction devient \(e_\theta\) presque partout dans \(r>0\),
   et toute boule centrée sur l'axe a une oscillation moyenne d'ordre un. La
   condition log-BMO globale échoue alors. Cette conclusion dynamique ne se
   transfère pas automatiquement à la périodisation sur \(\mathbb T^3\), qui
   ne conserve pas la symétrie de rotation continue.

## 1. Équation exacte et régularité de la classe sans swirl

Sur \(\mathbb R^3\), sans force, avec \(\nu>0\),

\[
\partial_t u+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,
\qquad \nabla\cdot u=0.
\]

Dans la classe axisymétrique **sans swirl**,

\[
u=u^r(r,z,t)e_r+u^z(r,z,t)e_z,
\qquad
\omega=\nabla\times u=\omega^\theta(r,z,t)e_\theta.
\]

La quantité \(\eta=\omega^\theta/r\) vérifie

\[
\partial_t\eta+u^r\partial_r\eta+u^z\partial_z\eta
=\nu\left(\partial_r^2+\frac3r\partial_r+\partial_z^2\right)\eta.
\]

L'opérateur diffusif est le Laplacien radial en quatre dimensions, auquel
s'ajoute la variable \(z\). Cette structure de maximum-principe est le cœur
de la régularité globale de la classe. Elle disparaît en présence de swirl.

### Sources primaires

- **Publié.** O. A. Ladyzhenskaya, *On unique solvability “in the large” of
  three-dimensional Cauchy problem for Navier–Stokes equations with axial
  symmetry*, Zap. Nauchn. Sem. LOMI 7 (1968), 155–177.
  Source primaire : <https://www.mathnet.ru/eng/znsl2240>.
- **Publié.** M. R. Ukhovskii et V. I. Yudovich, *Axially symmetric flows of
  ideal and viscous fluids filling the whole space*, J. Appl. Math. Mech. 32
  (1968), 52–62. DOI :
  <https://doi.org/10.1016/0021-8928(68)90147-0>.
- **Publié.** S. Leonardi, J. Málek, J. Nečas et M. Pokorný, *On Axially
  Symmetric Flows in \(\mathbb R^3\)*, Z. Anal. Anwend. 18 (1999), 639–649.
  DOI : <https://doi.org/10.4171/ZAA/903> ; texte primaire :
  <https://ems.press/journals/zaa/articles/11075>. Leur définition de
  « axially symmetric vector field » impose explicitement l'absence de
  composante azimutale ; le titre ne doit donc pas être cité comme un
  théorème couvrant le swirl.
- **Publié.** T. Gallay et V. Šverák, *Remarks on the Cauchy problem for the
  axisymmetric Navier–Stokes equations*, Confluentes Math. 7 (2015), 67–95.
  DOI : <https://doi.org/10.5802/cml.25> ; arXiv :
  <https://arxiv.org/abs/1510.01036>. Ils démontrent existence globale et
  unicité si \(\omega_0^\theta\in L^1(\Omega,dr\,dz)\), avec extension à des
  mesures finies lorsque la partie atomique est petite devant la viscosité.
  Les solutions peuvent avoir une énergie tridimensionnelle infinie.

### Implication exacte vers Clay

Une donnée initiale lisse, rapidement décroissante, divergence-free,
axisymétrique et sans swirl est admissible dans le cas \(\mathbb R^3\) de
Clay et sa solution reste lisse globalement. L'implication est donc :

\[
\text{donnée Clay + axisymétrie sans swirl}
\Longrightarrow \text{régularité globale}.
\]

La réciproque n'existe pas, et aucun de ces théorèmes ne couvre les données
3D générales ni les écoulements axisymétriques avec swirl. Un profil torique
sans swirl peut tester une implication fonctionnelle proposée, mais ne peut
pas fournir une résolution négative de Clay tant que la symétrie est
conservée.

## 2. Anneaux minces et filaments circulaires : résultats quantitatifs

| Résultat primaire | Statut | Équation et conclusion contrôlée | Limite pour Clay |
|---|---|---|---|
| H. Feng et V. Šverák, *On the Cauchy Problem for Axi-Symmetric Vortex Rings*, Arch. Ration. Mech. Anal. 215 (2015), 89–123, [DOI](https://doi.org/10.1007/s00205-014-0775-4), [arXiv](https://arxiv.org/abs/1301.6317) | Publié | Navier–Stokes 3D, \(\mathbb R^3\), axisymétrique sans swirl ; existence depuis une vorticité mesure concentrée sur un cercle, sans petitesse de la circulation. | Donnée filamentaire non lisse, classe sans swirl déjà régulière pour ses approximations lisses. |
| T. Gallay et V. Šverák, *Uniqueness of axisymmetric viscous flows originating from circular vortex filaments*, Ann. Sci. ENS 52 (2019), 1025–1071, [DOI](https://doi.org/10.24033/asens.2402), [arXiv](https://arxiv.org/abs/1609.02030) | Publié | Unicité axisymétrique sans swirl à nombre de Reynolds de circulation arbitraire ; asymptotique gaussienne/Oseen au temps court et viscosité fixée. | Unicité dans la classe symétrique, pas parmi toutes les solutions 3D admissibles. |
| G. Lévy et Y. Liu, *Uniqueness ... positive linear combinations of circular vortex filaments*, J. Math. Fluid Mech. 20 (2018), 1835–1856, [DOI](https://doi.org/10.1007/s00021-018-0391-4), [arXiv](https://arxiv.org/abs/1801.10353) | Publié | Plusieurs filaments circulaires positifs coaxiaux, Navier–Stokes sans swirl. | Même restriction de symétrie et données mesures. |
| J. Bedrossian, P. Germain et B. Harrop-Griffiths, *Vortex Filament Solutions of the Navier–Stokes Equations*, CPAM 76 (2023), 685–787, [DOI](https://doi.org/10.1002/cpa.22091), [arXiv](https://arxiv.org/abs/1809.04109) | Publié | Global près d'une colonne d'Oseen droite dans des espaces critiques ; local pour un filament fermé lisse arbitraire. | Le résultat pour une courbe fermée générale est local, pas un théorème global 3D. |
| P. Buttà, G. Cavallaro et C. Marchioro, *Vanishing viscosity limit for concentrated vortex rings*, J. Math. Phys. 63 (2022), 123103, [DOI](https://doi.org/10.1063/5.0124516), [arXiv](https://arxiv.org/abs/2209.02666) | Publié | Limite jointe épaisseur–viscosité pour \(N\) anneaux sans swirl disjoints ; concentration et translation axiale sur le régime contrôlé. | Limite singulière et classe symétrique ; aucune singularité Navier–Stokes à viscosité fixée. |
| T. Gallay et V. Šverák, *Vanishing viscosity limit for axisymmetric vortex rings*, Invent. Math. 237 (2024), 275–348, [DOI](https://doi.org/10.1007/s00222-024-01261-5), [arXiv v3](https://arxiv.org/abs/2301.01092v3) | Publié | Filament circulaire, faible viscosité ; épaisseur \(\sqrt{\nu t}\), approximation par l'évolution linéaire translatée à la vitesse de Kelvin sur un long intervalle quantifié. | Contrôle d'une asymptotique \(\nu\to0\), pas blow-up de NS à \(\nu>0\). |

### Audit d'échelle d'un tore mince — recalculé ici

Considérons, à rayon majeur \(R>0\) fixé,

\[
\omega_h(r,\theta,z)
=A_h f\!\left(\frac{r-R}{h},\frac zh\right)e_\theta,
\]

où \(f\) est un profil fixe, borné, non nul et à support compact. Le volume actif est comparable à
\(R h^2\). À constantes de profil près,

\[
\|\omega_h\|_{L^{3/2,\infty}(\mathbb R^3)}
\asymp |A_h|(Rh^2)^{2/3}.
\]

La circulation méridienne vaut \(\Gamma_h\asymp A_hh^2\). Donc :

- si \(R\) et \(\Gamma_h=\Gamma\neq0\) sont fixes,
  \(A_h\asymp\Gamma h^{-2}\) et
  \(\|\omega_h\|_{L^{3/2,\infty}}
  \asymp\Gamma R^{2/3}h^{-2/3}\to\infty\) ;
- une borne critique uniforme à \(R\) fixé impose
  \(A_h=O(R^{-2/3}h^{-4/3})\), donc
  \(\Gamma_h=O(R^{-2/3}h^{2/3})\to0\) ;
- si tout l'anneau contracte à l'échelle \(\lambda\), avec
  \(R\asymp h\asymp\lambda\) et amplitude \(\lambda^{-2}\), alors le volume
  est \(O(\lambda^3)\) et la norme faible \(L^{3/2}\) reste invariante.

Ainsi, les résultats « anneau mince à circulation et rayon majeur fixes » ne
fournissent pas une famille uniformément bornée dans
\(L^{3/2,\infty}\). Le régime critique pertinent contracte simultanément le
rayon majeur et le cœur, ou fait décroître la circulation.

## 3. Critères de direction et conventions aux zéros

### 3.1 Critères géométriques publiés

- **Publié.** P. Constantin et C. Fefferman, *Direction of Vorticity and the
  Problem of Global Regularity for the Navier–Stokes Equations*, Indiana
  Univ. Math. J. 42 (1993), 775–789,
  <https://iumj.org/article/3627/>, DOI
  <https://doi.org/10.1512/iumj.1993.42.42034>. La cohérence directionnelle
  est imposée dans une région de grande vorticité ; les zéros n'entrent pas
  dans le quantificateur.
- **Publié.** H. Beirão da Veiga et L. C. Berselli, *On the regularizing
  effect of the vorticity direction in incompressible viscous flows*,
  Differential Integral Equations 15 (2002), 345–356, DOI
  <https://doi.org/10.57262/die/1356060864>, texte auteur
  <https://people.dm.unipi.it/beiraodaveiga/pdf/hbv-79.pdf>. Le seuil de
  cohérence spatiale est abaissé au régime Hölder \(1/2\) sous les
  hypothèses exactes de l'article.
- **Publié.** Z. Bradshaw et Z. Grujić, *A spatially localized
  \(L\log L\) estimate on the vorticity in the 3D NSE*, Indiana Univ. Math.
  J. 64 (2015), 433–440, DOI
  <https://doi.org/10.1512/iumj.2015.64.5496>,
  <https://arxiv.org/html/1309.2519v5>. Pour des cubes \(I(x,r)\), ils
  définissent

  \[
  \|f\|_{\widetilde{bmo}_\phi}
  =\|f\|_{L^1}
  +\sup_{x,0<r<1/2}\frac{\Omega(f,I(x,r))}{\phi(r)},
  \qquad \phi(r)=\frac1{|\log r|},
  \]

  et supposent
  \(\sup_{t<T}\|\psi\xi(t)\|_{\widetilde{bmo}_\phi}<\infty\), où
  \(\xi=\omega/|\omega|\) et \(\psi\) est une localisation compacte fixe.
  La conclusion est une borne locale uniforme \(L\log L\) sur la
  vorticité, pas à elle seule un théorème global de régularité pour toute
  donnée Clay.
- **Publié.** Y. Do, A. Farhat, Z. Grujić et L. Xu, *Oscillations and
  integrability of the vorticity in the 3D NS flows*, Indiana Univ. Math.
  J. 69 (2020), 1559–1578,
  <https://arxiv.org/abs/1801.09040>. Ils traitent des profils algébriques et
  des poids avec plusieurs logarithmes. Les exemples log-radiaux démontrent
  la permissivité de ces espaces scalaires ; ils ne constituent pas un
  théorème d'extension \(S^2\)-valuée d'une direction prescrite sur un tore.

### 3.2 Préprint 2026 : norme différente et statut non validé

Z. Grujić, *Logarithmic Depletion of Vortex Stretching and Singularity
Evasion in the 3D Navier–Stokes Equations*, arXiv:2607.08866v2, soumis le
2026-07-09, révisé le 2026-07-13 :
<https://arxiv.org/abs/2607.08866>.

**Statut : préprint, sans référence de revue trouvée au 2026-08-14.** La
section 2.3, équation (2), emploie des boules et

\[
\|f\|_{bmo_\phi}
=\|f\|_{L^\infty}
+\sup_{x,0<r<1/2}\frac1{\phi(r)}
 \fint_{B_r(x)}|f-f_{B_r(x)}|,
\qquad \phi(r)=\frac1{|\log r|}.
\]

Le manuscrit note que le terme \(L^\infty\) vaut 1 pour un champ de direction
unitaire. Il ne donne pas de convention explicite sur \(\{\omega=0\}\), ni
de construction d'une extension \(S^2\)-valuée. Le théorème principal est
conditionnel à un « critical point singularity » défini par un profil
\(O(|x|^{-2})\), à une borne uniforme
\(L_t^\infty L_x^{3/2,\infty}\) de la vorticité et à la borne directionnelle
log-BMO. Ce n'est pas une preuve de régularité globale inconditionnelle.

La présente veille vérifie le statut et les hypothèses, mais ne valide pas
les nouvelles estimations du préprint. Elles doivent rester `UNVERIFIED` ou
un statut équivalent jusqu'à une passe analytique dédiée et indépendante.

### 3.3 Que signifie \(\xi\) sur \(\{\omega=0\}\) ?

Il faut distinguer trois situations.

1. **Critères limités aux grandes vorticités.** La direction n'est comparée
   que là où \(|\omega|\) dépasse un seuil ; la valeur aux zéros est sans
   effet.
2. **Norme globale ou norme de \(\psi\xi\).** Si l'ensemble des zéros a une
   mesure positive, une extension mesurable de \(\xi\) y est nécessaire et
   peut changer la norme BMO. La construction torique statique ci-dessous
   exploite exactement cette liberté.
3. **Solution forte à temps positif.** La diffusion donne l'analyticité
   spatiale dans les classes usuelles ; voir Z. Grujić et I. Kukavica,
   *Space Analyticity for the Navier–Stokes and Related Equations with
   Initial Data in \(L^p\)*, JFA 152 (1998), 447–466, DOI
   <https://doi.org/10.1006/jfan.1997.3167>. Pour une vorticité analytique
   non identiquement nulle, le zéro commun de ses composantes est de mesure
   nulle. Modifier \(\xi\) exactement sur ce zéro ne change alors pas une
   norme BMO définie modulo presque-partout. Cela ne contrôle toutefois pas
   l'oscillation de la direction **près** du zéro.

Conclusion contradictoire : l'absence d'une convention explicite est
matériellement importante pour des profils statiques compacts, mais elle ne
suffit pas à réfuter un critère appliqué sur un intervalle pré-singulier où
la solution est forte et analytique.

## 4. Extension torique \(S^2\)-valuée : lemme élémentaire

### 4.1 Construction à corridor logarithmique — dérivation interne auditée

Soient \(h_n<q_n<R_n/8\) et

\[
d_n(r,z)=\sqrt{(r-R_n)^2+z^2},
\qquad L_n=\log(q_n/h_n).
\]

La vorticité active est supportée dans \(d_n\lesssim h_n\) et sa direction
y vaut \(e_\theta\). Choisissons une fonction lisse
\(\Theta:[0,1]\to[0,\pi/2]\), constante près de 0 et de 1, avec
\(\Theta(0)=0\), \(\Theta(1)=\pi/2\). Après lissage des deux raccords, posons

\[
s_n(d)=\operatorname{clamp}
\!\left(\frac{\log(q_n/d)}{L_n},0,1\right),
\qquad
\zeta_n=\cos(\Theta(s_n))e_z+\sin(\Theta(s_n))e_\theta.
\]

Alors \(|\zeta_n|=1\), \(\zeta_n=e_\theta\) sur le cœur et
\(\zeta_n=e_z\) hors de \(d_n<q_n\). Comme \(q_n<R_n/8\), tout le tube est
à distance au moins \(R_n-q_n\) de l'axe. En particulier, \(\zeta_n=e_z\)
sur le cylindre axial \(r<R_n-q_n\) : il n'y a aucune singularité de
coordonnées à \(t=0\).

L'audit all-ball se sépare en quatre régimes. À constantes géométriques près,

\[
\begin{array}{c|c}
\text{rayon }\rho & \operatorname{MO}_{B_\rho}(\zeta_n)\\ \hline
0<\rho\le h_n
 & C\left(\rho/(h_nL_n)+\rho/R_n\right),\\
h_n\le\rho\le q_n
 & C\left(L_n^{-1}+\rho/R_n\right),\\
q_n\le\rho\le R_n/2
 & C\left((q_n/\rho)^2/L_n+(h_n/\rho)^2\right),\\
\rho\ge R_n/2
 & C R_n(q_n^2/L_n+h_n^2)/\rho^3.
\end{array}
\]

Le terme \(L_n^{-1}\) du second régime vient de la BMO locale uniforme de
la distance logarithmique à une courbe lisse de codimension deux. Le terme
\(\rho/R_n\) suit la rotation azimutale. Les deux derniers régimes utilisent
la dilution du défaut \(\zeta_n-e_z\) dans le volume de la boule.

Le choix concret

\[
R_n=2^{-n},\qquad q_n=2^{-2n},\qquad h_n=2^{-n^2},\qquad n\ge4,
\]

donne \(L_n=(n^2-2n)\log2\) et rend uniformément bornées les quantités

\[
\frac{|\log h_n|}{L_n},\quad
\frac{|\log q_n|q_n}{R_n},\quad
\frac{|\log q_n|}{L_n}\left(\frac{q_n}{R_n}\right)^2,
\quad
|\log h_n|\left(\frac{h_n}{q_n}\right)^2.
\]

On obtient donc

\[
\sup_n\sup_{x,0<\rho<1/4}
|\log\rho|\operatorname{MO}_{B_\rho(x)}(\zeta_n)<\infty.
\]

Les boules axiales de rayon \(<R_n-q_n\) ont même une oscillation nulle ;
celles qui atteignent le tore ne créent qu'un défaut dilué, déjà inclus dans
les deux derniers régimes. La norme de 2026 est compatible avec
\(\|\zeta_n\|_\infty=1\). Sur \(\mathbb R^3\), \(\zeta_n=e_z\) à l'infini
et n'appartient pas à \(L^1\), mais \(\psi\zeta_n\) appartient à la norme
localisée et \(L^1\)-ancrée de 2015 pour une coupure compacte appropriée.

### 4.2 Topologie et littérature d'extension

La boucle \(\theta\mapsto e_\theta\) a un enroulement non nul dans
l'équateur \(S^1\), mais elle est contractile dans \(S^2\) puisque
\(\pi_1(S^2)=0\). L'interpolation vers \(e_z\) réalise explicitement cette
contraction. Une extension forcée à rester dans l'équateur aurait, elle, une
obstruction de degré.

Sources connexes, mais non équivalentes au lemme :

- **Publié.** H. Brezis et L. Nirenberg, *Degree theory and BMO; Part I:
  Compact manifolds without boundaries*, Selecta Math. 1 (1995), 197–263,
  DOI <https://doi.org/10.1007/BF01671566>. Cette théorie porte sur le degré
  et les applications VMO/BMO à valeurs dans une variété ; elle ne fournit
  pas l'estimation torique ci-dessus.
- **Publié.** A. Butaev et G. Dafni, *Approximation and Extension of
  Functions of Vanishing Mean Oscillation*, J. Geom. Anal. 31 (2021),
  6892–6921, DOI <https://doi.org/10.1007/s12220-020-00526-8>, préprint
  <https://arxiv.org/abs/1809.01049>. L'opérateur d'extension est linéaire
  et à valeurs vectorielles après application composante par composante ;
  il ne préserve pas automatiquement la contrainte \(|\Xi|=1\). Une
  normalisation exige en plus une borne qui éloigne l'extension de zéro.
- **Publié.** S. Janson, *On functions with conditions on the mean
  oscillation*, Ark. Mat. 14 (1976), 189–196, DOI
  <https://doi.org/10.1007/BF02385834>, et E. Nakai–K. Yabuta,
  *Pointwise multipliers for functions of bounded mean oscillations*, J.
  Math. Soc. Japan 37 (1985), 207–218. Ces sources fondent les espaces
  pondérés et le théorème de multiplicateurs utilisé en 2015 ; elles ne
  prescrivent pas une géométrie de vortex annulaire.

### 4.3 Verdict d'antériorité

Les recherches primaires ciblées ont combiné les chaînes suivantes :

- `"vortex ring" + bmo + vorticity direction` ;
- `toroidal + log-BMO + vorticity` ;
- `e_theta + BMO extension` ;
- `sphere-valued + VMO extension`.

Elles retrouvent séparément : (i) les anneaux dont la direction est
\(e_\theta\), (ii) les espaces log-BMO, et (iii) la topologie/extension des
applications VMO à valeurs variétales. Aucune source trouvée n'assemble
l'estimation uniforme exacte ci-dessus. Il est sûr de l'enregistrer comme
**dérivation élémentaire du laboratoire, antériorité non trouvée** ; il
serait non justifié de la déclarer nouvelle au sens bibliométrique exhaustif.

## 5. Passe adverse : pourquoi le lemme statique ne se propage pas

### 5.1 Transition qui rétrécit

Si la direction effectue une rotation d'ordre un dans une couche de largeur
\(O(h)\), une boule de rayon comparable à \(h\) coupant cette couche a une
oscillation moyenne \(\Omega\ge c>0\), sous une hypothèse non dégénérée sur
les deux fractions de volume. Alors

\[
\frac{\Omega}{1/|\log h|}\ge c|\log h|\to\infty.
\]

Une rotation comprimée sur la seule échelle \(h\) est donc exclue. Le
corridor logarithmique \(h_n<d_n<q_n\) évite précisément ce minorant : la
rotation vue à l'échelle \(h_n\) n'est que \(O(L_n^{-1})\), tandis que
\(|\log h_n|/L_n\) reste borné.

### 5.2 Axe de symétrie

Sur toute boule \(B_\rho\) centrée sur l'axe, le champ \(e_\theta\) a une
moyenne vectorielle nulle par symétrie. Par conséquent,

\[
\fint_{B_\rho}|e_\theta-(e_\theta)_{B_\rho}|=1,
\]

et

\[
|\log\rho|\,\Omega(e_\theta,B_\rho)=|\log\rho|\to\infty.
\]

Changer la valeur sur l'axe, ensemble de mesure nulle, ne répare rien.

Pour l'évolution sur \(\mathbb R^3\), exactement axisymétrique sans swirl,
d'un anneau unisigné non trivial, l'équation parabolique de
\(\omega^\theta\) et le principe du maximum donnent à temps positif
\(\omega^\theta(r,z,t)>0\) dans l'intérieur \(r>0\). C'est une inférence
standard à partir de l'équation sans swirl, pas un nouveau théorème sur les
données signées. Sa direction est donc \(e_\theta\) presque partout dans
chaque boule axiale : la norme log-BMO **globale** diverge. En revanche, une
coupure \(\psi\) supportée dans une boule autour du cœur et restant à
distance fixe de l'axe voit \(e_\theta\) comme un champ Lipschitz ; le critère
localisé de 2015 n'est pas contredit. Cette implication ne couvre ni une
vorticité signée, ni l'évolution périodique dont le noyau de Biot–Savart ne
préserve pas la symétrie de rotation continue du tore isolé.

### 5.3 Test reproductible minimal

Une expérience décisive doit évaluer séparément :

1. les boules/cubes centrés sur l'axe ;
2. les cellules coupant la couche de transition ;
3. les cellules centrées dans le cœur ;
4. les deux conventions de norme (ancre \(L^1\) ou \(L^\infty\)) ;
5. les échelles \(h_n\), \(q_n\), \(R_n\) du corridor logarithmique, puis
   une transition témoin comprimée sur \(O(h_n)\).

Résidus analytiques attendus :

- corridor logarithmique : quotient log-BMO uniformément borné dans les
  quatre régimes de boules ;
- transition \(O(h)\) : minorant \(c|\log h|\) ;
- direction dynamique \(e_\theta\) globale : oscillation axiale exactement 1
  et quotient divergent ;
- localisation loin de l'axe : majorant \(C\ell|\log\ell|\).

Tout calcul numérique donnant autre chose doit d'abord être suspecté d'avoir
omis les cellules axiales, utilisé une moyenne scalaire de l'angle plutôt
qu'une moyenne vectorielle, ou fixé une résolution incapable de voir la
couche \(O(h)\).

## 6. Veille primaire 2025–2026

| Source | Statut au 2026-08-14 | Résultat exact et transfert |
|---|---|---|
| Z. Lei, X. Ren et G. Tian, *A geometric characterization of potential Navier–Stokes singularities*, [arXiv:2501.08976v1](https://arxiv.org/abs/2501.08976) | Préprint, soumis 2025-01-15 ; aucune référence de revue trouvée | Pour une solution faible adaptée locale de NS, si les vecteurs de grande vorticité restent dans un double cône, régularité. L'ensemble complet des directions \(e_\theta\) décrit l'équateur : il n'est pas contenu dans un double cône étroit et rencontre tout grand cercle. Le critère ne l'exclut donc pas ; la régularité sans swirl l'exclut par une autre structure. |
| F. Gancedo, A. Hidalgo-Torné et F. Mengual, *Dissipative Euler Flows Originating from Circular Vortex Filaments*, Annals of PDE 11, art. 24 (2025), [DOI](https://doi.org/10.1007/s40818-025-00211-5) | Publié le 2025-07-30 | Euler 3D, \(\nu=0\), filament circulaire initial, infinité de solutions faibles \(C([0,T],L^{2^-})\) par intégration convexe, énergie finie/décroissante pour \(t>0\). Ni NS visqueux, ni solution classique Clay, ni blow-up classique. |
| Z. Grujić, *On taming Moffatt–Kimura vortices of doom in the viscous case*, [arXiv:2511.00725v3](https://arxiv.org/abs/2511.00725) | Préprint, soumis 2025-11-01, révisé 2026-06-10 ; aucune référence de revue trouvée | Propose un mécanisme conditionnel à deux couches pour le scénario de deux anneaux en collision et des espaces bmo log-composites. Ce n'est pas une preuve de régularité pour toute solution NS ni une validation du modèle Moffatt–Kimura comme solution exacte. |
| D. Guo, I.-J. Jeong et L. Zhao, *Global dynamics of a single vortex ring*, [arXiv:2602.20131v1](https://arxiv.org/abs/2602.20131) | Préprint, soumis 2026-02-23 ; aucune référence de revue trouvée | Euler 3D axisymétrique sans swirl : concentration globale, vitesse de Kelvin–Hicks au premier ordre et filamentation linéaire en temps pour une classe générique d'anneaux minces. Le résultat est inviscide et ne transfère pas à la régularité Clay de NS. |
| Z. Grujić, *Logarithmic Depletion ...*, [arXiv:2607.08866v2](https://arxiv.org/abs/2607.08866) | Préprint, soumis 2026-07-09, révisé 2026-07-13 ; aucune référence de revue trouvée | Résultat conditionnel pour des profils critiques ponctuels avec bornes \(L^{3/2,\infty}\) et log-BMO. La famille \(R_n\to0\), \(h_n\ll R_n\), peut garder une norme critique par son amplitude, mais son cœur torique anisotrope ne satisfait pas automatiquement la factorisation ponctuelle scale-invariant ou log-périodique et la borne de gradient exigées par le préprint. |

Aucune simple annonce de séminaire n'a été utilisée comme preuve. La veille
ciblée n'a trouvé aucune publication 2025–2026 démontrant une singularité de
Navier–Stokes incompressible 3D admissible au sens Clay, ni une validation
publiée indépendante du préprint arXiv:2607.08866.

## 7. Décision scientifique recommandée

Le maillon transférable n'est pas « les anneaux minces peuvent exploser » :
cette phrase est fausse dans la classe sans swirl visqueuse. Le lemme utile et
falsifiable est plus modeste :

> Pour \(h_n\ll q_n\ll R_n\) avec \(q_n<R_n/8\), la prescription
> \(e_\theta\) sur un cœur torique \(d_n\lesssim h_n\) admet, par rotation
> logarithmique dans \(h_n<d_n<q_n\), une extension \(S^2\)-valuée vers
> \(e_z\) dont la semi-norme log-BMO all-ball est uniforme sous les rapports
> d'échelles vérifiés ci-dessus.

Ce lemme élimine toute affirmation purement géométrique selon laquelle
l'enroulement azimutal d'un tore compact impose nécessairement un coût
\(|\log h|\) pour **toute** extension admissible aux zéros. Il ne dit rien sur
la propagation par Navier–Stokes. Le prochain test ayant la meilleure valeur
informationnelle est donc dynamique : mesurer ou borner la log-BMO de
\(\psi\xi(t)\) pour un anneau visqueux, avec \(\psi\) (a) loin de l'axe puis
(b) englobant l'axe, et suivre explicitement la dépendance en
\(\sqrt{\nu t}/R\). Le résultat négatif attendu dans le cas (b) est déjà
certifié analytiquement par l'oscillation axiale égale à 1.

## 8. Classification des affirmations issues de cet audit

| Affirmation | Niveau justifié |
|---|---|
| Régularité globale des données lisses axisymétriques sans swirl | `PAPER_PROOF`, avec sources classiques ci-dessus |
| Existence/unicité et asymptotiques de filaments circulaires | `PAPER_PROOF`, dans les domaines et classes exacts des articles |
| Échelle faible \(L^{3/2}\) du tore mince | `AI_DERIVATION`, calcul dimensionnel à vérifier contre la normalisation exacte du profil |
| Extension logarithmique \(e_\theta\to e_z\), \(h_n\ll q_n\ll R_n\) | `AI_DERIVATION`, preuve all-ball interne, pas d'antériorité trouvée |
| Échec log-BMO global de \(e_\theta\) autour de l'axe | `ANALYTIC_PROOF`, calcul exact de moyenne par symétrie |
| Théorèmes de arXiv:2501.08976, 2511.00725, 2602.20131, 2607.08866 | `PREPRINT_CLAIM` tant qu'aucune publication primaire n'est identifiée |
| Transfert de l'un de ces préprints vers une résolution Clay | Non établi |
