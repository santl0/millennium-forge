# Cycle 0030 — budget de nombreux tores disjoints

Date : 2026-08-14.

Type de passe : contre-modèle analytique reproductible et obstruction
quantitative. Cette passe est une dérivation IA interne, et non une revue
externe indépendante.

## Verdict

Le nombre croissant de composantes ne rouvre pas le contre-profil du cycle
0029 dans le régime le plus favorable de tores minces disjoints, de budgets
critiques égaux et de packing tridimensionnel séparé.

Pour \(N=m^3\) tores placés dans des cellules de côté
\(a=N^{-1/3}\), de rayon majeur \(R=\kappa a\), de rapport d'aspect
\(\eta=h/R\), et normalisés globalement par

\[
 \|W_N\|_{L^{3/2,\infty}}=1,
 \qquad
 \int_{\mathbb R^3}|W_N|^{3/2}\,dx=1,
 \tag{1}
\]

le budget faible critique de chaque composante vaut exactement

\[
 k_j=\|W_j\|_{L^{3/2,\infty}}=N^{-2/3}
 \tag{2}
\]

dans le modèle étagé. Une partition spatiale en cellules, suivie d'une
estimation multipolaire absolue des autres cellules, donne

\[
 \boxed{
 \|u_N\|_3
 \leq C N^{-1/3}\eta^{1/9}
 +C N^{-1/3}\eta^{2/3}(1+\log N).
 }
 \tag{3}
\]

Le premier terme de (3) est la somme cubique des champs propres, et non la
somme triangulaire grossière. Le deuxième est une borne absolue des queues
de Biot--Savart. Il reste donc valide pour toute cohérence des signes et des
orientations permise par la construction; annuler des moments signés ne
peut que le diminuer.

Les \(N\) corridors directionnels peuvent simultanément former une seule
extension unitaire globale et satisfaire le test BMO sur toutes les
boules. Avec

\[
 L=\log(q/h),\qquad q=R/L,\qquad
 \eta=e^{-L}/L,
 \tag{4}
\]

le coût local est \(O(L^{-1})\), tandis que le coût d'une boule rencontrant
plusieurs cellules est au plus \(O(L^{-3})\). Après insertion physique à
l'échelle \(\ell\), il suffit que

\[
 |\log\ell|+\log N\lesssim L
 \tag{5}
\]

pour que la semi-norme pondérée
\(\mathrm{bmo}_{1/|\log r|}\) reste uniforme. Cette condition autorise
même \(N=\exp(\theta L+o(L))\), avec \(\theta\) borné. Pourtant, pour ce
choix,

\[
 \log\!\left(N^{-1/3}\eta^{1/9}\right)
 =-\left(\frac{\theta}{3}+\frac19\right)L
   -\frac19\log L+o(L),
 \tag{6}
\]

et la queue dans (3) décroît plus vite encore. Par conséquent

\[
 \|u_N\|_3\longrightarrow0.
 \tag{7}
\]

Résultat scientifique négatif : le packing de nombreux tores disjoints,
la cohérence non locale et l'annulation d'un nombre fini de moments ne
produisent pas une vitesse critique non dégénérée. L'échappatoire restante
doit quitter au moins une des hypothèses : supports séparés à l'échelle des
cellules, budgets égaux, géométrie de tore mince, ou contrôle par somme
absolue des multipôles.

## 1. Configuration exacte

### 1.1 Packing

Soit \(N=m^3\), \(m\in\mathbb N\). Partitionnons le cube unité en \(N\)
cellules \(Q_j\) de côté

\[
 a=N^{-1/3}.
 \tag{8}
\]

Dans chaque cellule, plaçons un cercle \(\Gamma_j\), centré au centre
\(c_j\), de rayon

\[
 R=\kappa a,\qquad 0<\kappa<1/16.
 \tag{9}
\]

Tous les axes des cercles sont parallèles à \(e_3\), mais leurs axes sont
translatés avec les centres des cellules. Cette famille n'est donc pas
axisymétrique autour d'un axe global. Posons

\[
 h=R\eta,\qquad
 q=R/L,\qquad
 \eta=\frac{e^{-L}}L.
 \tag{10}
\]

Pour \(L\) assez grand, les tubes \(s_j<q\) sont contenus dans les cellules
et sont deux à deux disjoints.

### 1.2 Vorticité

Pour un profil radial fixe \(\varphi\), supporté dans le disque unité de la
section normale, et des signes \(\sigma_j\in\{-1,1\}\), définissons

\[
 W_j(x)=
 \sigma_j B\,
 \varphi\!\left(\frac{\operatorname{dist}(x,\Gamma_j)}h\right)
 e_{\theta,j}(x),
 \qquad
 W_N=\sum_{j=1}^N W_j.
 \tag{11}
\]

Chaque champ est tangent aux surfaces tubulaires et indépendant de son
angle azimutal. Ainsi

\[
 \nabla\cdot W_j=0,\qquad
 \int_{\mathbb R^3}W_j\,dx=0.
 \tag{12}
\]

La seconde identité vient de l'intégrale complète de \(e_{\theta,j}\) sur
le cercle. Elle est indépendante du signe.

Les identités exactes ci-dessous emploient le profil étagé
\(\varphi=\mathbf1_{[0,1]}\). Il est divergence-free au sens des
distributions puisque le saut est tangent à la frontière du tube. Un bump
lisse radial fixe conserve toutes les puissances de \(N,R,\eta,L\), avec
des constantes de profil au lieu des égalités exactes.

### 1.3 Mise à l'échelle physique

L'insertion à l'échelle \(\ell>0\) est

\[
 W_{N,\ell}(x)=\ell^{-2}W_N(x/\ell),
 \qquad
 u_{N,\ell}(x)=\ell^{-1}u_N(x/\ell).
 \tag{13}
\]

Elle conserve exactement

\[
 \|W_{N,\ell}\|_{L^{3/2,\infty}}
 =\|W_N\|_{L^{3/2,\infty}},
 \qquad
 \|u_{N,\ell}\|_3=\|u_N\|_3.
 \tag{14}
\]

La variable \(\ell\) intervient donc dans le poids BMO, mais ne peut pas
réparer la décroissance de (3).

## 2. Normalisation critique globale

Le volume d'un tube torique étagé est

\[
 V=2\pi^2Rh^2=2\pi^2R^3\eta^2.
 \tag{15}
\]

Les supports sont disjoints et ont la même amplitude. Le choix

\[
 B=(NV)^{-2/3}
 \tag{16}
\]

donne exactement

\[
 \|W_N\|_{L^{3/2,\infty}}
 =B(NV)^{2/3}=1,
 \qquad
 \int|W_N|^{3/2}=B^{3/2}NV=1.
 \tag{17}
\]

Pour chaque composante,

\[
 k_j=BV^{2/3}=N^{-2/3}.
 \tag{18}
\]

Les autres budgets globaux sont

\[
 \|W_N\|_1=(NV)^{1/3}
 \asymp \eta^{2/3},
 \tag{19}
\]

\[
 \|W_N\|_2^2=(NV)^{-1/3}
 \asymp \eta^{-2/3},
 \tag{20}
\]

car \(NR^3=\kappa^3\). La vorticité devient donc plus intermittente :
sa masse tend vers zéro et son enstrophie diverge.

Le volume actif et le volume total des corridors obéissent à

\[
 NV\asymp\eta^2,
 \qquad
 N R q^2\asymp L^{-2}.
 \tag{21}
\]

Ces deux identités sont indépendantes de \(N\). Le packing ne crée pas de
fraction volumique cachée.

## 3. Extension directionnelle unique et test all-ball

### 3.1 Une seule extension globale

Dans le corridor \(s_j<q\), posons

\[
 \alpha(s)=
 \begin{cases}
 \pi/2,&0\leq s\leq h,\\[1mm]
 \displaystyle\frac{\pi}{2}
 \frac{\log(q/s)}L,&h<s<q,\\[2mm]
 0,&s\geq q.
 \end{cases}
 \tag{22}
\]

Puis, avec la même direction extérieure \(e_3\) pour toutes les cellules,

\[
 \xi_N(x)=
 \sigma_j\sin\alpha(s_j)e_{\theta,j}
 +\cos\alpha(s_j)e_3
 \quad\text{si }s_j<q,
 \qquad
 \xi_N=e_3\quad\text{ailleurs}.
 \tag{23}
\]

Comme \(e_{\theta,j}\perp e_3\), ce champ est unitaire. Sur le support de
\(W_j\), il coïncide avec \(W_j/|W_j|\). Au bord du corridor, il rejoint
exactement \(e_3\). La disjonction des corridors rend (23) univoque : il
ne s'agit pas de \(N\) extensions incompatibles recollées a posteriori.

### 3.2 Boules locales

La troncature logarithmique dans (22), combinée à la courbure du cercle,
donne pour toute boule ne rencontrant qu'un corridor

\[
 \operatorname{MO}_B(\xi_N)
 \leq C\left(\frac1L+\frac qR\right)
 \leq \frac CL.
 \tag{24}
\]

Pour certaines boules de rayon \(ch\), avec \(c>1\) fixé et dont le centre
est sur l'interface du coeur, la variation radiale donne aussi

\[
 \operatorname{MO}_B(\xi_N)\geq \frac cL.
 \tag{25}
\]

Le coût local est donc réellement d'ordre \(L^{-1}\); il n'est pas un
artefact de majoration.

Après la mise à l'échelle (13), le poids de cette boule est

\[
 |\log(\ell h)|
 =|\log\ell|+\log(1/R)+L+\log L+O(1).
 \tag{26}
\]

Puisque \(\log(1/R)=\frac13\log N+O(1)\), la contribution pondérée reste
uniforme sous la condition (5).

### 3.3 Boules rencontrant plusieurs cellules

Dans une section normale,

\[
 \int_{s_j<q}|\xi_N-e_3|\,dA
 \leq C\frac{q^2}L.
 \tag{27}
\]

Après intégration le long du cercle,

\[
 \int_{s_j<q}|\xi_N-e_3|\,dx
 \leq C\frac{Rq^2}L
 =C\frac{R^3}{L^3}.
 \tag{28}
\]

Une boule de rayon \(\rho\geq a\) rencontre au plus
\(C(1+\rho/a)^3\) cellules. En divisant la somme de (28) par
\(|B_\rho|\), on obtient

\[
 \operatorname{MO}_{B_\rho}(\xi_N)
 \leq C\frac{(R/a)^3}{L^3}
 \leq \frac C{L^3}.
 \tag{29}
\]

Pour \(q<\rho<a\), la boule ne rencontre qu'un nombre borné de corridors;
la dilution de (28), jointe à (24), reste au plus \(C/L\). Les boules plus
grandes que le cluster ne coûtent pas davantage. Ainsi la vérification
porte bien sur toutes les boules euclidiennes tridimensionnelles.

La configuration est donc compatible avec

\[
 \sup_{0<r<r_0}
 |\log r|\,
 \sup_{\operatorname{rad}(B)=r}
 \operatorname{MO}_B(\xi_{N,\ell})
 \leq C
 \tag{30}
\]

dès que (5) est satisfaite. La constante de (30) est suivie
analytiquement mais n'est pas certifiée par arithmétique d'intervalles.

## 4. Moments signés

### 4.1 Impulsion d'un tore

L'impulsion hydrodynamique est

\[
 I(W)=\frac12\int_{\mathbb R^3}x\times W(x)\,dx.
 \tag{31}
\]

Pour un tore étagé d'axe \(e_3\),

\[
 I(W_j)=\sigma_j I_{\rm ring}e_3,
 \qquad
 I_{\rm ring}
 =B\left(\pi^2R^2h^2+\frac{\pi^2}{4}h^4\right).
 \tag{32}
\]

Une moitié de signes positifs et une moitié de signes négatifs annule donc
l'impulsion totale sans changer aucune norme du module.

### 4.2 Quartets annulant le premier moment spatial

Dans chaque bloc de quatre cellules coplanaires, prenons les positions
relatives

\[
 (-d,-d),\quad(-d,d),\quad(d,-d),\quad(d,d)
 \tag{33}
\]

et les signes

\[
 (1,-1,-1,1).
 \tag{34}
\]

Alors, exactement,

\[
 \sum_{\nu=1}^4\sigma_\nu=0,
 \qquad
 \sum_{\nu=1}^4\sigma_\nu x_\nu=0,
 \qquad
 \sum_{\nu=1}^4\sigma_\nu y_\nu=0,
 \tag{35}
\]

mais

\[
 \sum_{\nu=1}^4\sigma_\nu x_\nu y_\nu=4d^2\ne0.
 \tag{36}
\]

Répéter ces quartets annule l'impulsion et son premier moment spatial. Le
moment mixte (36) prouve que la distribution signée n'est pas nulle et
exhibe le premier moment non annulé de ce motif.

Cette correction est gratuite pour (1), (21), (23) et (30), car ces
quantités dépendent du module ou traitent chaque corridor séparément.
Elle n'est toutefois pas nécessaire à la borne (3), qui utilise la somme
absolue des queues.

## 5. Borne critique de la vitesse

Soit

\[
 u_j=\nabla\times(-\Delta)^{-1}W_j,
 \qquad
 u_N=\sum_{j=1}^N u_j.
 \tag{37}
\]

### 5.1 Champ propre dans chaque cellule

L'estimation tubulaire du cycle 0029 donne, uniformément en \(j\),

\[
 \|u_j\|_3\leq C k_j\eta^{1/9}.
 \tag{38}
\]

Définissons le champ local par

\[
 u_{\rm loc}(x)=
 \begin{cases}
 u_j(x),&x\in Q_j,\\
 0,&x\text{ hors du cube}.
 \end{cases}
 \tag{39}
\]

Les cellules étant disjointes,

\[
 \begin{aligned}
 \|u_{\rm loc}\|_3^3
 &=\sum_{j=1}^N\int_{Q_j}|u_j|^3\,dx\\
 &\leq \sum_{j=1}^N\|u_j\|_3^3
 \leq C N k_j^3\eta^{1/3}.
 \end{aligned}
 \tag{40}
\]

Avec \(k_j=N^{-2/3}\),

\[
 \|u_{\rm loc}\|_3
 \leq C N^{-1/3}\eta^{1/9}.
 \tag{41}
\]

La somme triangulaire aurait donné
\(CN^{1/3}\eta^{1/9}\). Elle est inadaptée parce qu'elle oublie la
localisation dominante des champs propres. L'amélioration de \(N^{2/3}\)
dans (41) est le point décisif de ce cycle.

### 5.2 Premier moment absolu et queue d'une composante

L'identité \(\int W_j=0\) permet de soustraire le noyau au centre \(c_j\)
dans Biot--Savart. Si \(D=|x-c_j|\geq CR\),

\[
 |u_j(x)|
 \leq C\frac{M_{1,j}}{D^3},
 \qquad
 M_{1,j}:=\int|y-c_j|\,|W_j(y)|\,dy.
 \tag{42}
\]

Or

\[
 M_{1,j}
 \leq C R\|W_j\|_1
 \leq C k_jR^2\eta^{2/3}.
 \tag{43}
\]

Avec \(k_j=N^{-2/3}\) et \(R\asymp a=N^{-1/3}\),

\[
 M_{1,j}\leq C N^{-4/3}\eta^{2/3}.
 \tag{44}
\]

### 5.3 Somme des coquilles du réseau

Pour \(x\in Q_i\), la coquille de rang \(s\geq1\) contient au plus
\(Cs^2\) centres à distance au moins \(csa\). Les contributions absolues
de cette coquille vérifient, par (42)--(44),

\[
 \sum_{j\ {\rm dans\ la\ coquille}\ s}|u_j(x)|
 \leq
 C s^2\frac{N^{-4/3}\eta^{2/3}}{(sa)^3}
 =
 C\frac{N^{-1/3}\eta^{2/3}}s.
 \tag{45}
\]

Il y a \(O(N^{1/3})\) coquilles. Par sommation harmonique,

\[
 \|u_N-u_{\rm loc}\|_{L^\infty(\text{cluster})}
 \leq
 C N^{-1/3}\eta^{2/3}(1+\log N).
 \tag{46}
\]

Le cluster a un volume borné. Dans une couronne extérieure bornée, le même
comptage s'applique. À grande distance, la somme absolue est bornée par

\[
 C\frac{NM_{1,j}}{|x|^3}
 \leq C\frac{N^{-1/3}\eta^{2/3}}{|x|^3},
 \tag{47}
\]

dont la norme \(L^3\) extérieure est finie. Il vient

\[
 \|u_N-u_{\rm loc}\|_3
 \leq
 C N^{-1/3}\eta^{2/3}(1+\log N).
 \tag{48}
\]

Les signes ne sont jamais utilisés dans (45)--(48). La borne couvre donc
la cohérence constructive maximale compatible avec les moments absolus de
chaque tube.

En combinant (41) et (48), on obtient (3).

### 5.4 Test de bord : paquet coaxial dense

Le packing volumique seul autorise une géométrie qui n'entre pas dans le
lemme C30. Considérons les échelles

\[
 R=2^{-3n},\qquad q=2^{-9n},\qquad h=2^{-12n},
 \qquad N=2^{12n-12}.
 \tag{48a}
\]

Une grille coaxiale des paramètres méridiens
\((R_j,z_j)\), de pas

\[
 \delta\asymp R/\sqrt N=64q,
 \tag{48b}
\]

place les \(N\) corridors disjoints dans un paquet de diamètre \(O(R)\).
Sa fraction de packing est

\[
 N(q/R)^2=2^{-12}.
 \tag{48c}
\]

Il n'y a pas de défaut BMO évident : avec
\(L=\log(q/h)=3n\log2\), les boules intermédiaires voient une densité
uniforme de corridors et une déviation moyenne \(O(L^{-1})\); à l'échelle
du paquet, la contribution est \(O(2^{-12}L^{-1})\). Le poids
\(|\log R|=L\) la laisse uniforme.

En revanche, cette grille viole fortement l'hypothèse de séparation de
C30 :

\[
 R N^{1/3}=2^{n-4}\longrightarrow\infty.
 \tag{48d}
\]

Les anneaux voisins sont à distance \(\delta\ll R\). On ne peut donc pas
leur appliquer (42), qui exige une distance au centre au moins comparable
à \(R\). L'interaction pertinente est celle de filaments presque
parallèles, de noyau local \(\Gamma/d\), où

\[
 B\asymp(NRh^2)^{-2/3}\asymp2^{10n+8},
 \qquad
 \Gamma\asymp Bh^2\asymp2^{-14n+8}.
 \tag{48e}
\]

Pour des signes identiques, les vitesses axiales s'ajoutent sur l'axe
commun. À l'échelle \(R\), leur ordre collectif est

\[
 |u_{\rm coll}|\asymp\frac{N\Gamma}{R}
 \asymp2^{n-4},
 \qquad
 \|u_{\rm coll}\|_{L^3(B_{cR})}
 \asymp N\Gamma\asymp2^{-2n-4}.
 \tag{48f}
\]

Le premier facteur diverge ponctuellement parce que le paquet se contracte;
la norme critique du paquet tend néanmoins vers zéro. La queue extérieure
issue de l'impulsion totale a le même ordre \(N\Gamma\) en \(L^3\).

Conclusion contradictoire : un majorant qui attribuerait aux interactions
de cette grille le régime multipolaire de (45) est invalide. Le proxy
filamentaire cohérent ne fournit toutefois pas de norme \(L^3\) non
dégénérée. De plus, la grille strictement coaxiale appartient à la classe
axisymétrique sans swirl. Fermer rigoureusement ce régime dense demanderait
une estimation séparée de paquet; elle n'est pas incluse dans la borne
multipolaire (3). Cette estimation est précisément fournie par le lemme
Morrey--Hedberg du rapport racine : son majorant cubique
`(h/q)^(4/3)=2^(-4n)`, soit un majorant de norme `2^(-4n/3)`, est compatible
avec le minorant filamentaire `2^(-2n-4)` et ferme également cette grille.

## 6. Test de croissance exponentielle

Prenons

\[
 L_n=n^2,\qquad
 \log N_n=\theta L_n+o(L_n),\qquad
 \eta_n=e^{-L_n}/L_n.
 \tag{49}
\]

Le terme proche vérifie

\[
 \log\!\left(N_n^{-1/3}\eta_n^{1/9}\right)
 =
 -\left(\frac{\theta}{3}+\frac19\right)L_n
 -\frac19\log L_n+o(L_n).
 \tag{50}
\]

Pour le terme lointain,

\[
 \begin{aligned}
 &\log\!\left[
 N_n^{-1/3}\eta_n^{2/3}(1+\log N_n)
 \right]\\
 &\quad=
 -\left(\frac{\theta}{3}+\frac23\right)L_n
 +O(\log L_n).
 \end{aligned}
 \tag{51}
\]

Les deux exposants tendent vers \(-\infty\) pour tout
\(\theta\geq0\). En particulier, saturer la marge BMO par un nombre
exponentiel de composants accélère la décroissance au lieu de la
compenser.

Le terme triangulaire grossier aurait eu l'exposant

\[
 \left(\frac{\theta}{3}-\frac19\right)L_n
 -\frac19\log L_n.
 \tag{52}
\]

Il aurait laissé croire à un seuil \(\theta=1/3\). Les cellules disjointes
réfutent ce seuil : la bonne sommation cubique change le signe du terme en
\(\theta\).

## 7. Énergie et pression

Par Hardy--Littlewood--Sobolev,

\[
 \|u_N\|_2\leq C\|W_N\|_{6/5}.
 \tag{53}
\]

Pour le profil étagé global,

\[
 \|W_N\|_{6/5}
 =B(NV)^{5/6}
 =(NV)^{1/6}
 \asymp\eta^{1/3}.
 \tag{54}
\]

Donc

\[
 \|u_N\|_2\lesssim\eta^{1/3}\longrightarrow0.
 \tag{55}
\]

Pour le champ initial lisse et divergence-free, la pression instantanée
normalisée par une constante vérifie

\[
 p_N=\mathcal R_i\mathcal R_j(u_{N,i}u_{N,j}),
 \qquad
 \|p_N\|_{3/2}\leq C\|u_N\|_3^2\longrightarrow0.
 \tag{56}
\]

Le packing ne cache donc ni énergie non dégénérée ni pression critique
non petite.

## 8. Test standard-library reproductible

Le programme suivant ne simule pas Navier--Stokes. Il vérifie :

- les annulations signées exactes avec des rationnels;
- la normalisation faible et forte du modèle étagé;
- les identités de packing des volumes actifs et des corridors;
- les proxies all-ball aux échelles coeur et cluster;
- la décroissance des deux termes de (3);
- l'écart avec la somme triangulaire grossière;
- la borne harmonique utilisée dans (46).

~~~python
from fractions import Fraction as F
from math import exp, log, pi

positions = [
    (F(-1), F(-1)),
    (F(-1), F(1)),
    (F(1), F(-1)),
    (F(1), F(1)),
]
signs = [F(1), F(-1), F(-1), F(1)]

assert sum(signs) == 0
assert sum(s * p[0] for s, p in zip(signs, positions)) == 0
assert sum(s * p[1] for s, p in zip(signs, positions)) == 0
assert sum(s * p[0] * p[1] for s, p in zip(signs, positions)) == 4
print("signed quartet: PASS")

previous_near = float("inf")
previous_far = float("inf")
max_identity_residual = 0.0

for n in (4, 8, 12, 16):
    depth = n * n
    theta = 1.0 / 3.0
    torus_count = max(4, 4 * int(exp(theta * depth) / 4))
    log_count = log(float(torus_count))

    log_cell = -log_count / 3.0
    log_radius = log_cell - log(32.0)
    log_eta = -depth - log(float(depth))
    log_h = log_radius + log_eta

    log_single_volume = (
        log(2.0 * pi * pi) + 3.0 * log_radius + 2.0 * log_eta
    )
    log_total_volume = log_count + log_single_volume
    log_amplitude = -(2.0 / 3.0) * log_total_volume

    weak_residual = abs(
        log_amplitude + (2.0 / 3.0) * log_total_volume
    )
    strong_residual = abs(
        1.5 * log_amplitude + log_total_volume
    )
    assert weak_residual < 2.0e-13
    assert strong_residual < 3.0e-13

    log_individual_budget = (
        log_amplitude + (2.0 / 3.0) * log_single_volume
    )
    assert abs(
        log_individual_budget + (2.0 / 3.0) * log_count
    ) < 3.0e-13

    active_geometry = (
        log_count + 3.0 * log_radius + 2.0 * log_eta
    )
    active_expected = -3.0 * log(32.0) + 2.0 * log_eta
    assert abs(active_geometry - active_expected) < 3.0e-13

    corridor_geometry = (
        log_count + 3.0 * log_radius - 2.0 * log(float(depth))
    )
    corridor_expected = (
        -3.0 * log(32.0) - 2.0 * log(float(depth))
    )
    corridor_residual = abs(corridor_geometry - corridor_expected)
    assert corridor_residual < 3.0e-13

    max_identity_residual = max(
        max_identity_residual,
        weak_residual,
        strong_residual,
        abs(
            log_individual_budget + (2.0 / 3.0) * log_count
        ),
        abs(active_geometry - active_expected),
        corridor_residual,
    )

    log_ell = -n * log(2.0) - log(float(n))
    core_weight = abs(log_ell + log_h)
    local_bmo_proxy = core_weight / depth
    cluster_bmo_proxy = abs(log_ell + log_cell) / depth**3
    assert local_bmo_proxy < 2.0
    assert cluster_bmo_proxy < local_bmo_proxy / 100.0

    near_log = -(1.0 / 3.0) * log_count + (1.0 / 9.0) * log_eta
    far_log = (
        -(1.0 / 3.0) * log_count
        + (2.0 / 3.0) * log_eta
        + log(1.0 + log_count)
    )
    triangle_log = (
        (1.0 / 3.0) * log_count + (1.0 / 9.0) * log_eta
    )

    assert near_log < triangle_log
    assert far_log < triangle_log
    assert near_log < previous_near
    assert far_log < previous_far
    previous_near = near_log
    previous_far = far_log

    print(
        "n=%d logN=%.6f localBMO=%.6f clusterBMO=%.3e "
        "logNear=%.6f logFar=%.6f logTriangle=%.6f"
        % (
            n,
            log_count,
            local_bmo_proxy,
            cluster_bmo_proxy,
            near_log,
            far_log,
            triangle_log,
        )
    )

for shell_count in (8, 64, 512, 4096):
    harmonic = sum(1.0 / k for k in range(1, shell_count + 1))
    assert harmonic <= 1.0 + log(float(shell_count))

print("packing identities: PASS")
print("all-ball proxies: PASS")
print("L3 obstruction: PASS")
print("harmonic shell bound: PASS")
print("maximum logarithmic identity residual: %.3e" % max_identity_residual)
~~~

Commande de reproduction PowerShell, depuis la racine du dépôt :

~~~powershell
$text = Get-Content docs/reports/navier-stokes/reviews/cycle-0030-countermodel.md
$start = [Array]::IndexOf($text, '~~~python') + 1
$stop = [Array]::IndexOf($text, '~~~', $start)
$tmp = Join-Path $env:TEMP 'cycle-0030-many-tori.py'
$text[$start..($stop - 1)] | Set-Content -Encoding utf8 $tmp
python $tmp
Remove-Item -LiteralPath $tmp
~~~

Précision : double IEEE 754 pour les identités logarithmiques, rationnels
exacts pour les moments signés. Les tolérances sont
\(3\times10^{-13}\) au plus. Graine aléatoire : aucune. Dépendances :
bibliothèque standard Python uniquement.

Ce script ne certifie pas les constantes analytiques de (24), (38) ou
(42). Il teste les conséquences algébriques des bornes démontrées.

Exécution locale observée le 2026-08-14 : les quatre familles
\(n=4,8,12,16\) passent; le résidu logarithmique maximal des identités de
normalisation et de packing vaut \(2.842\times10^{-14}\). Les proxies BMO
maximaux observés sont \(1.760620\) au coeur et
\(1.448\times10^{-3}\) au cluster. Aucune borne d'erreur continue n'est
inférée de ces proxies.

## 9. Passe contradictoire

### 9.1 Quantificateurs

L'obstruction démontrée vaut pour :

- des tores de même géométrie et de même amplitude;
- des supports séparés par des cellules de taille \(a\);
- \(R\leq\kappa a\), avec \(\kappa\) uniforme;
- un profil transverse fixe;
- la normalisation critique distribuée également entre les \(N\)
  composantes;
- une extension directionnelle globale du type (23).

Elle ne traite pas :

- une distribution très inégale du budget critique;
- des tubes qui se croisent, s'enlacent ou se rapprochent à distance
  \(o(a)\);
- des paquets de Fourier ou Mikado dont les champs ne sont pas localisés
  autour d'une cellule;
- une géométrie dont le premier moment absolu est plus grand que
  \(CR\|W_j\|_1\);
- une construction dynamique à plusieurs temps. La famille indexée par
  \(n\) est une famille de données, pas une cascade temporelle d'une
  solution unique.

Si une distribution inégale concentre une fraction fixe du budget sur un
nombre borné de tores, elle retombe sur l'obstruction du cycle 0029. Le
régime intermédiaire demande une inégalité de réarrangement séparée et
n'est pas revendiqué ici.

### 9.2 Pression et projection de Leray

La vitesse est recalculée par l'opérateur complet non local
\(\nabla\times(-\Delta)^{-1}\); elle n'est pas obtenue en intégrant un
modèle local de tube. La pression de (56) est elle aussi non locale. Les
estimations de coquilles sont précisément le test de l'interaction entre
cellules qui manquait à une simple addition de profils locaux.

### 9.3 Cohérence des signes

Une objection possible serait que les champs lointains s'additionnent en
phase. L'inégalité (45) additionne déjà leurs modules. Aucune cohérence ne
peut dépasser cette majoration. Les quartets de (33)--(36) apportent des
annulations supplémentaires et ne menacent donc pas l'obstruction.

### 9.4 Passage au lisse

Le profil étagé fournit les égalités de distribution exactes mais n'est pas
lisse. Une mollification radiale tangentielle au tube conserve la
divergence nulle et remplace les égalités (17)--(20) par des comparaisons
uniformes. La puissance négative de \(N\) dans (3) est stricte; ces
constantes ne changent pas la conclusion. Une certification quantitative
du profil mollifié reste néanmoins à produire avant toute revendication
assistée par ordinateur.

### 9.5 Absence de raccourci stationnaire

Ces champs sont des données initiales et non des solutions stationnaires.
Une solution stationnaire lisse, non forcée, d'énergie finie sur
\(\mathbb R^3\) ne peut pas être obtenue en déclarant simplement
\(W_N\) figé : le bilan d'énergie imposerait la dissipation nulle. Aucun
blow-up admissible n'est construit.

### 9.6 Rapport au problème Clay

Les champs lissés sont des données divergence-free régulières et
localisées en vorticité. Leurs vitesses ont des queues multipolaires et ne
sont en général pas de Schwartz; annuler un nombre fini de moments ne rend
pas la queue rapidement décroissante à tout ordre.

Surtout, (7) place ces données dans le régime de petitesse de la norme
critique \(L^3\) de la vitesse. Elles engendrent donc des solutions globales
régulières par la théorie critique standard, et non des singularités
candidates. Ce cycle élimine une branche de recherche; il ne démontre ni
la régularité globale pour données arbitraires ni l'existence d'un
blow-up.

## 10. Énoncé falsifiable retenu

### Lemme actif C30

Soient \(N=m^3\) tores de même profil, contenus dans des cellules cubiques
disjointes de côté \(N^{-1/3}\), avec
\(R\leq\kappa N^{-1/3}\), \(h/R=\eta\), et vorticité globale étagée
normalisée par (1). Alors la vitesse de Biot--Savart satisfait (3), avec
une constante indépendante de \(N\) et \(\eta\).

Statut : dérivation analytique IA interne, reproduite algébriquement, non
évaluée par une revue externe indépendante.

Falsificateur décisif : exhiber une telle famille séparée, de profil fixe,
pour laquelle

\[
 \|u_N\|_3
 \big/
 \left[
 N^{-1/3}\eta^{1/9}
 +N^{-1/3}\eta^{2/3}(1+\log N)
 \right]
 \longrightarrow\infty.
 \tag{57}
\]

Une telle famille invaliderait soit la localisation cubique (40), soit le
développement multipolaire (42), soit le comptage de réseau (45).

### Enregistrement proposé

~~~json
{
  "claim": "MANY_DISJOINT_TORI_L3_OBSTRUCTION",
  "status": "AI_DERIVATION",
  "equation": "3D incompressible Navier-Stokes initial-data kinematics via full-space Biot-Savart",
  "domain": "R^3",
  "solution_type": "smooth initial data after radial mollification; no evolution claim",
  "normalization": "global vorticity weak-L^(3/2) norm one",
  "hypotheses": [
    "N=m^3 separated equal-profile toroidal tubes",
    "R <= kappa N^(-1/3)",
    "equal critical budget N^(-2/3) per component",
    "aspect ratio eta=h/R"
  ],
  "conclusion": "velocity L3 <= C N^(-1/3)[eta^(1/9)+eta^(2/3)(1+log N)]",
  "adversarial_status": "internal same-model review completed; no external independent review",
  "next_test": "unequal critical budgets or overlapping/linked tubes"
}
~~~

## 11. Décision

État : **ABANDONNER** la branche des nombreux tores disjoints, égaux et
séparés comme source d'une norme \(L^3\) non dégénérée.

Recommandation propre à cette passe : déterminer si une distribution
fortement inégale de budgets critiques satisfait encore une version
réarrangée de (3), ou si des tubes liés/chevauchants peuvent battre
simultanément le coût all-ball BMO et la borne absolue des moments. La synthèse
du cycle donne priorité au gate compact directionnel, plus falsifiable après
le contre-profil de stacking.

Expérience décisive suivante : optimiser

\[
 \sum_j k_j^3\eta_j^{1/3}
 \quad\text{et}\quad
 \sup_x\sum_j\frac{k_jR_j^2\eta_j^{2/3}}
 {|x-c_j|^3}
 \tag{58}
\]

sous la contrainte exacte de distribution
\(\|\sum_jW_j\|_{L^{3/2,\infty}}\leq1\), sans supposer
\(k_j=N^{-2/3}\). Si l'optimum se concentre sur un nombre borné de
composantes, la branche entière des tubes disjoints sera fermée; s'il reste
diffus, il donnera le premier régime non couvert par les cycles 0029--0030.
