# Cycle 0055 — orbites rotationnelles, vitesse modulée et faible-$L^3$

**Date de coupure :** 15 août 2026

**Nature :** veille primaire indépendante, avec recherche d'absence bornée

**Question bornée :** pour Navier--Stokes incompressible 3D en variables
backward similaires, une trajectoire située exactement sur l'orbite d'un
profil fixe sous un groupe de rotations peut-elle avoir une vitesse angulaire
variable ? Le principe

\[
 \text{orbite exacte d'une PDE autonome et équivariante}
 \Longrightarrow
 \text{vitesse constante modulo le stabilisateur}          \tag{Q}
\]

est-il déjà publié sous cette forme pour Navier--Stokes, et les théorèmes de
rigidité faible-$L^3$ éliminent-ils le profil obtenu ?

## Verdict

1. **Bradshaw--Tsai (2017) est la source publiée la plus proche de (Q) pour
   Navier--Stokes.** L'article dérive explicitement l'équation dans un repère
   similaire tournant avec vitesse $\dot\theta(s)$ variable. Il impose ensuite
   $\dot\theta=\alpha$ constant : pour les RSS continues, la phase de rotation
   est logarithmique parce que la covariance pour tous les facteurs d'échelle
   exige l'équation de Cauchy
   $\vartheta(\lambda\mu)=\vartheta(\lambda)+\vartheta(\mu)$; pour les RDSS,
   un représentant constant est choisi parmi
   $\alpha_k=(2k\pi+\phi)/T$. Les auteurs disent ne pas avoir trouvé
   d'application à $\dot\theta$ non constant. Ils **ne démontrent pas** le
   théorème réciproque « une solution arbitraire restant sur une orbite de
   rotation a nécessairement une vitesse constante ».

2. **Pineau--Vicol `arXiv:2607.09619v2` contient une classification explicite
   mais non publiée.** La remarque 1.8 définit les solitons comme des orbites
   $u(t)=R(g(t))U$ d'un groupe de symétries et indique que, sous les conditions
   additionnelles de vitesse bornée et pression décroissante, les solitons de
   Navier--Stokes se classent, modulo conjugaison galiléenne, en états
   stationnaires, ondes tournantes à vitesse constante et RSS backward, avec
   leurs analogues forward. Au jour de coupure, la v2 du 6 août 2026 reste une
   **prépublication** sans DOI ni `journal-ref`; la classification figure dans
   une remarque, pas dans un théorème autonome assorti d'une preuve et d'une
   classe faible précise.

3. **Aucun article publié de Navier--Stokes énonçant exactement (Q) dans la
   classe suitable faible-$L^3$ n'a été identifié dans le corpus borné.** Ce
   n'est pas une preuve d'absence universelle. Les articles de dynamique
   équivariante de Field (1980) et Krupa (1990) donnent le cadre abstrait des
   orbites invariantes et des équilibres relatifs pour des champs de vecteurs
   lisses sur des variétés de dimension finie. La littérature computationnelle
   de Navier--Stokes définit également un équilibre relatif par une vitesse de
   phase constante. Aucun de ces textes ne fournit directement le passage
   distributionnel requis pour une solution suitable dans
   $L^{3,\infty}(\mathbb R^3)$.

4. **Le lemme à axe fixe est néanmoins une conséquence algébrique directe de
   l'équation autonome**, dès que la phase possède un relèvement absolument
   continu et que l'ansatz est valable dans un espace de distributions commun.
   Si

   \[
     V(s)=\rho_{\theta(s)}U,
   \]

   alors soit le générateur rotationnel $\mathcal RU$ est nul et la rotation
   est une jauge dans le stabilisateur, soit $\theta'(s)=\alpha$ presque
   partout. Cette dérivation est enregistrée ci-dessous comme **dérivation du
   laboratoire**, non comme `PAPER_PROOF`.

5. **Les théorèmes faible-$L^3$ de Chae--Wolf et Guevara--Phuc ne se
   transfèrent pas automatiquement au profil tourné.** Ils concernent
   l'équation stationnaire de Leray sans terme
   $\alpha\mathcal RU$. Guevara--Phuc élimine bien les profils faibles
   $U\in W^{1,2}_{\rm loc}\cap L^{3,\infty}$ dans ce cas non tourné; ajouter le
   générateur change l'équation testée et ses termes de coupure.

6. **Pineau--Vicol ne ferme pas le cas faible-$L^3$ tourné.** Ses exclusions
   RSS/RDSS supposent une solution lisse, une covariance exacte et la borne
   ponctuelle Type I

   \[
     |u(x,t)|\le \frac C{|x|+\sqrt{-t}},
   \]

   et ne couvrent que les vitesses angulaires petites ou grandes; la plage
   intermédiaire reste ouverte. La borne Type I implique
   $L^{3,\infty}$, mais la réciproque est fausse.

7. **« Rotation modulée » recouvre deux objets différents.** Une phase
   variable appliquée à un profil *fixe* est interdite par le lemme algébrique
   hors stabilisateur. Une onde tournante modulée ou une orbite relative
   périodique possède au contraire une forme qui varie dans le quotient des
   symétries; elle n'est pas de la forme $\rho_{\theta(s)}U$ avec $U$ fixe et
   n'est donc pas éliminée par ce lemme.

## 1. Équation exacte, groupe et échelle

Le cadre actif est Navier--Stokes incompressible standard, non forcé,
viscosité un, sur $\mathbb R^3\times(-\infty,0)$ :

\[
 \partial_tu-\Delta u+(u\cdot\nabla)u+\nabla p=0,
 \qquad \nabla\cdot u=0.                                  \tag{1}
\]

Les variables backward similaires sont

\[
 y=\frac{x}{\sqrt{-t}},\qquad s=-\log(-t),\qquad
 V(y,s)=\sqrt{-t}\,u(x,t),\qquad P(y,s)=(-t)p(x,t).       \tag{2}
\]

Elles donnent l'équation autonome

\[
 \partial_sV-\Delta V+\frac12V+\frac12y\cdot\nabla V
 +(V\cdot\nabla)V+\nabla P=0,
 \qquad \nabla\cdot V=0.                                  \tag{3}
\]

Soit $R_\theta$ la rotation autour de l'axe $e_3$, $J=R'_0$, et

\[
 (\rho_\theta U)(y)=R_\theta U(R_{-\theta}y),\qquad
 (\rho_\theta P)(y)=P(R_{-\theta}y).                     \tag{4}
\]

Le générateur infinitésimal sur les champs de vitesse est

\[
 \mathcal RU=JU-(Jy\cdot\nabla)U.                        \tag{5}
\]

La rotation préserve toutes les normes de Lorentz spatiales. En particulier,

\[
 \|\rho_\theta U\|_{L^{3,\infty}}=
 \|U\|_{L^{3,\infty}}.                                  \tag{6}
\]

La norme $L^{3,\infty}$ et la borne ponctuelle $|U(y)|\lesssim(1+|y|)^{-1}$
sont critiques pour l'échelle de (1), mais la seconde est strictement plus
forte. Le terme $\alpha\mathcal RU$ a la même dimension similaire que les
autres termes de (3); il n'est ni sous-critique ni perturbatif sans une
petitesse indépendante.

La rotation est une symétrie exacte de (3), pression comprise. On peut aussi
éliminer la pression avec la projection de Leray, qui commute aux rotations
orthogonales sur $\mathbb R^3$. Dans une argumentation locale, cette seconde
formulation ne dispense pas de contrôler la non-localité de la pression.

## 2. Audit des sources primaires

| Source et statut au 2026-08-15 | Équation, domaine, solution | Énoncé utile | Ce qui ne se transfère pas |
|---|---|---|---|
| Bradshaw--Tsai, *Rotationally Corrected Scaling Invariant Solutions to the Navier--Stokes Equations*, *Comm. PDE* 42(7) (2017), 1065--1087, [DOI 10.1080/03605302.2017.1323922](https://doi.org/10.1080/03605302.2017.1323922), [arXiv:1610.05680v1](https://arxiv.org/abs/1610.05680), **publié** | Navier--Stokes incompressible 3D, espace entier ou demi-espace, non forcé; constructions faibles forward pour données arbitrairement grandes dans $L^3_w=L^{3,\infty}$ | Définit RSS/RDSS, dérive le repère à $\dot\theta(s)$ variable, puis construit avec vitesse constante; discute le cas backward | Construction forward, pas rigidité backward; pas de théorème « orbite arbitraire $\Rightarrow\dot\theta$ constant » |
| Pineau--Vicol, *On Rotated Backwards Self-Similar Solutions of the Incompressible 3D Navier--Stokes Equations*, [arXiv:2607.09619v2](https://arxiv.org/abs/2607.09619v2), v1 10 juillet 2026, v2 6 août 2026, 37 pages, **prépublication** | (1), $\mathbb R^3\times[-1,0)$; profils RSS/RDSS globaux lisses | Th. 1.4 : RSS Type I triviale pour $|\alpha|$ petit ou grand; th. 1.7 : analogue RDSS à période courte; remarque 1.8 : classification de solitons | Pas de revue par les pairs identifiée; rotation intermédiaire ouverte; pas de suitable faible-$L^3$ général; la classification n'est qu'une remarque |
| Chae--Wolf, *Removing Discretely Self-Similar Singularities for the 3D Navier--Stokes Equations*, *Comm. PDE* 42(9) (2017), 1359--1374, [DOI 10.1080/03605302.2017.1358275](https://doi.org/10.1080/03605302.2017.1358275), [arXiv:1610.09464v2](https://arxiv.org/abs/1610.09464), **publié** | (1), solution backward lisse exactement $\lambda$-DSS sur l'espace entier | Sous Type I ponctuel, élimine la DSS si $\lambda>1$ est assez proche de un | Pas de rotation; ne traite ni la phase variable ni les périodes arbitraires |
| Chae--Wolf, *On the Liouville Type Theorems for Self-Similar Solutions to the Navier--Stokes Equations*, *Arch. Ration. Mech. Anal.* 225 (2017), 549--572, [DOI 10.1007/s00205-017-1110-7](https://doi.org/10.1007/s00205-017-1110-7), [arXiv:1609.06962v1](https://arxiv.org/abs/1609.06962), **publié** | Équation stationnaire de Leray non tournée; profil lisse | Th. 1.2 plus remarque 1.3 donnent la constance pour les profils $L^{p,\infty}$, $p>3/2$, donc zéro sous intégrabilité | Le corollaire 1.4 du PDF arXiv omet typographiquement sa conclusion; surtout, aucun terme $\alpha\mathcal RU$ n'est présent |
| Guevara--Phuc, *Leray's Self-Similar Solutions to the Navier--Stokes Equations with Profiles in Marcinkiewicz and Morrey Spaces*, *SIAM J. Math. Anal.* 50(1) (2018), 541--556, [DOI 10.1137/16M110099X](https://doi.org/10.1137/16M110099X), [arXiv:1509.08177v2](https://arxiv.org/abs/1509.08177), **publié** | Équation faible stationnaire de Leray sur $\mathbb R^3$; $U\in W^{1,2}_{\rm loc}$ | Th. 1.3 : $U=0$ si $U\in L^{q,\infty}$, $12/5<q<6$, donc notamment $q=3$ | Équation non tournée seulement; les tests énergétiques ne couvrent pas automatiquement $\alpha\mathcal RU$ |
| Field, *Equivariant Dynamical Systems*, *Trans. AMS* 259 (1980), 185--205, [DOI 10.1090/S0002-9947-1980-0561832-4](https://doi.org/10.1090/S0002-9947-1980-0561832-4), **publié** | Champs de vecteurs lisses équivariants sur variétés compactes de dimension finie | Prop. A : équivariance du flot et isotropie constante sur les courbes intégrales; prop. B1 : le flot sur un espace homogène se ferme en flots de tores, périodiques au rang un | Pas une PDE faible; compacité et unicité classique du flot font partie du cadre |
| Krupa, *Bifurcations of Relative Equilibria*, *SIAM J. Math. Anal.* 21(6) (1990), 1453--1486, [DOI 10.1137/0521081](https://doi.org/10.1137/0521081), **publié** | Champ de vecteurs $C^\infty$ équivariant sur $\mathbb R^n$, groupe compact | Définit un équilibre relatif comme une orbite de groupe invariante par le flot; cite les ondes tournantes $x(t)=\theta(t)x_0$ comme exemple et développe la réduction modulo isotropie | Dimension finie, solution classique et flot unique; pas d'énoncé faible Navier--Stokes |
| Willis--Cvitanović--Avila, *Revealing the State Space of Turbulent Pipe Flow by Symmetry Reduction*, *J. Fluid Mech.* 721 (2013), 514--540, [DOI 10.1017/jfm.2013.75](https://doi.org/10.1017/jfm.2013.75), [arXiv:1203.3701](https://arxiv.org/abs/1203.3701), **publié, numérique** | Navier--Stokes incompressible en conduite, frontière, forçage/flux de conduite; discrétisation spectrale | Définit un équilibre relatif par un vecteur vitesse constant dans l'espace tangent au groupe; distingue orbites relatives périodiques | Géométrie, frontière et forçage différents; calcul convergent mais non preuve de la classification backward Clay |

## 3. Ce que Bradshaw--Tsai établit exactement

Pour une RSS, Bradshaw--Tsai impose la covariance, pour tout $\lambda>0$,

\[
 v(x,t)=\lambda R(-2\alpha\log\lambda)
 v\!\left(\lambda R(2\alpha\log\lambda)x,\lambda^2t\right).
                                                               \tag{7}
\]

Leur discussion avant la définition explique qu'une phase
$\vartheta(\lambda)$ compatible avec la composition des dilatations doit
vérifier

\[
 \vartheta(\lambda\mu)=\vartheta(\lambda)+\vartheta(\mu).      \tag{8}
\]

Sous la régularité usuelle, (8) donne
$\vartheta(\lambda)=c\log\lambda$, donc une vitesse constante en temps
logarithmique. C'est une conséquence de la **définition d'une covariance de
groupe valable pour tout $\lambda$**, pas une classification de toute
trajectoire dont l'image serait seulement contenue dans une orbite.

L'article considère ensuite un changement de repère général

\[
 V(z,s)=R_{\theta(s)}u(y,s),\qquad
 y=R_{\theta(s)}^Tz,                                      \tag{9}
\]

et obtient, avec ses conventions forward,

\[
 \partial_su+\dot\theta Ju-\dot\theta(Jy)\cdot\nabla u
 -\frac12u-\frac12y\cdot\nabla u-\Delta u
 +(u\cdot\nabla)u+\nabla p=0.                              \tag{10}
\]

Ils notent :

- une RSS donne un $u$ stationnaire avec $\dot\theta=\alpha$;
- une RDSS de période $T$ et phase $\phi$ peut être représentée avec
  $\alpha_k=(2k\pi+\phi)/T$;
- pour une construction périodique, (10) pourrait rester non autonome mais
  périodique si $\dot\theta$ varie;
- faute d'application trouvée à ce cas, ils prennent ensuite
  $\dot\theta=\alpha$ constant.

La dernière décision n'est pas une preuve d'impossibilité de vitesse
variable. En outre, (9) est un **choix de coordonnées mobiles appliqué à un
champ $u(y,s)$ qui peut se déformer**. Il ne faut pas le confondre avec
$V(s)=\rho_{\theta(s)}U$ pour un seul profil fixe $U$.

## 4. Ce que Pineau--Vicol v2 ajoute

La notice primaire arXiv donne : Ben Pineau et Vlad Vicol, soumission initiale
le 10 juillet 2026, v2 le 6 août 2026, 37 pages, commentaire « additional
results and comments added ». Aucun DOI ou `journal-ref` n'était affiché à la
date de coupure. L'étiquette correcte est donc `PREPRINT_CLAIM`.

La remarque 1.8 est plus explicite que Bradshaw--Tsai sur le vocabulaire de
soliton. Elle part d'une équation d'évolution $\partial_tu=F[u]$ munie d'un
groupe de symétries $G$ et appelle soliton une solution de la forme
$u(t)=R(g(t))U$. Pour Navier--Stokes, elle annonce la classification, sous les
conditions de vitesse bornée et pression décroissante, en :

- états stationnaires;
- ondes tournantes
  $u(x,t)=R(\omega t)U(R(-\omega t)x)$;
- RSS backward et analogues forward;

à conjugaison par les symétries galiléennes près.

Trois précautions sont indispensables :

1. le texte est une remarque de prépublication, pas un théorème numéroté;
2. aucune démonstration séparée du relèvement $g(t)$ ou du cas faible suitable
   n'y est donnée;
3. les théorèmes 1.4 et 1.7 du même article supposent déjà la vitesse
   constante $\alpha$ et ne démontrent la trivialité que pour $|\alpha|$
   petit ou grand sous Type I.

La remarque 1.8 est donc une antériorité explicite pour l'**énoncé informel**
de classification, mais pas une publication évaluée ni le raccord faible
recherché.

## 5. Lemme algébrique à axe fixe

### Énoncé candidat du laboratoire

Soit $I\subset\mathbb R$ un intervalle. Supposons :

- que $(V,P)$ résout (3) dans
  $\mathcal D'(\mathbb R^3\times I)$;
- qu'il existe un profil distributionnel $(U,Q)$ et un relèvement
  $\theta\in W^{1,1}_{\rm loc}(I)$ tels que, pour presque tout $s$,

  \[
   V(s)=\rho_{\theta(s)}U,\qquad
   P(s)=\rho_{\theta(s)}Q+c(s),                           \tag{11}
  \]

  où $c(s)$ est spatialement constant;
- que tous les termes de (3), après substitution, appartiennent à un même
  espace de distributions spatiales.

Alors il existe $\alpha\in\mathbb R$ tel que l'une des alternatives suivantes
est vraie :

\[
 \begin{cases}
  \mathcal RU=0,
  &\rho_\theta U=U\text{ pour tout }\theta
    \quad\text{(stabilisateur continu)},\\[2mm]
  \theta'(s)=\alpha\text{ p.p.},
  &\theta(s)=\alpha s+\theta_0
    \quad\text{(vitesse constante)}.
 \end{cases}                                             \tag{12}
\]

### Dérivation

La chaîne distributionnelle et l'équivariance donnent

\[
 \partial_sV(s)=\theta'(s)\rho_{\theta(s)}\mathcal RU.   \tag{13}
\]

En notant $\mathcal L(U,Q)$ la partie de (3) autre que $\partial_sV$,

\[
 \mathcal L(\rho_\theta U,\rho_\theta Q)
 =\rho_\theta\mathcal L(U,Q).                            \tag{14}
\]

Après application de $\rho_{-\theta(s)}$, l'équation devient

\[
 \theta'(s)\mathcal RU+\mathcal L(U,Q)=0
 \quad\text{dans }\mathcal D'(\mathbb R^3)              \tag{15}
\]

pour presque tout $s$. En comparant deux points de Lebesgue $s_1,s_2$,

\[
 [\theta'(s_1)-\theta'(s_2)]\mathcal RU=0.               \tag{16}
\]

Si $\mathcal RU\ne0$ comme distribution, le coefficient scalaire est nul et
$\theta'$ est constant presque partout. Si $\mathcal RU=0$, l'intégration de
l'équation du groupe montre $\rho_\theta U=U$ : la phase ne change pas l'état
physique.

Cette preuve n'utilise pas l'unicité de Navier--Stokes, seulement l'ansatz
exact, la dérivabilité de la phase et l'équation dans un espace commun. Elle
ne résout toutefois pas le problème de **construire un relèvement absolument
continu** à partir de la seule propriété ensembliste
$V(s)\in\{\rho_\theta U\}$ pour presque tout $s$.

### Groupe général et stabilisateur

Pour un groupe de Lie $G$ et $V(s)=\rho_{g(s)}U$, l'analogue de (15) fixe le
vecteur fondamental de la vitesse de corps
$\xi(s)=g(s)^{-1}g'(s)$ :

\[
 \xi(s)_X(U)=-\mathcal L(U,Q).                            \tag{17}
\]

Ainsi $\xi(s)-\xi(s_0)$ appartient à l'algèbre de Lie du stabilisateur de
$U$. Pour un groupe non abélien, dire simplement « $g'(s)$ est constant » est
incorrect : la vitesse pertinente est la vitesse de corps, modulo isotropie,
et une conjugaison/condition de jauge intervient. Le cas d'un axe fixé
$SO(2)$ est abélien et (12) est exact.

## 6. Faible-$L^3$ : transfert et trou précis

Le profil RSS tourné à vitesse constante satisfait

\[
 -\Delta U+\frac12U+\frac12y\cdot\nabla U
 +(U\cdot\nabla)U+\alpha\mathcal RU+\nabla Q=0,
 \qquad \nabla\cdot U=0.                                 \tag{18}
\]

À $\alpha=0$, Guevara--Phuc démontre, pour une solution faible de l'équation
de Leray,

\[
 U\in W^{1,2}_{\rm loc}(\mathbb R^3)
 \cap L^{q,\infty}(\mathbb R^3),\quad
 \frac{12}{5}<q<6
 \Longrightarrow U=0.                                   \tag{19}
\]

Le cas $q=3$ est donc explicitement inclus. Chae--Wolf fournit une rigidité
encore plus large pour des profils lisses en $L^{p,\infty}$,
$p>3/2$.

Mais le terme supplémentaire de (18) donne, avec une coupure $\varphi_R$,
des contributions contenant

\[
 \alpha\int \varphi_R U\cdot JU,
 \qquad
 -\alpha\int \varphi_R U\cdot[(Jy)\cdot\nabla U].        \tag{20}
\]

Les annulations formelles valent pour un poids radial et une intégration
globale justifiée, mais les preuves de Liouville suivent aussi la pression, les
potentiels de Riesz, les termes de bord et des itérations locales. On ne peut
donc supprimer (20) ligne par ligne sans réauditer toutes les coupures et
toutes les constantes. Aucune des versions publiées auditées n'énonce ce
prolongement à $\alpha\ne0$.

Le raccord manquant est exactement l'un des deux lemmes suivants :

\[
 \boxed{
 \begin{aligned}
 &U\in W^{1,2}_{\rm loc}\cap L^{3,\infty},\quad U
 \text{ résout (18)}\\
 &\hspace{35mm}\Longrightarrow U=0
 \end{aligned}}                                          \tag{L1}
\]

uniformément pour tout $\alpha$, ou au moins pour la plage intermédiaire non
couverte par Pineau--Vicol; ou bien

\[
 \boxed{
 \begin{aligned}
 &V(s)\in\operatorname{Orb}_{SO(2)}(U)\text{ p.p.},
 \quad V\text{ suitable faible-$L^3$}\
 &\Longrightarrow
 \text{existence d'un relèvement }\theta\in W^{1,1}_{\rm loc}
 \end{aligned}}.                                         \tag{L2}
\]

Le lemme algébrique de la section 5 ferme alors immédiatement la vitesse
variable hors stabilisateur. Ni (L1) ni (L2) n'a été identifié comme théorème
publié dans le corpus borné.

## 7. Modulation et faux contre-exemples

Une onde tournante modulée s'écrit typiquement

\[
 V(s)=\rho_{\theta(s)}W(s),                               \tag{21}
\]

où $W(s)$ n'est pas constant dans l'espace quotient. Une orbite relative
périodique vérifie seulement

\[
 V(s+T)=\rho_\phi V(s).                                  \tag{22}
\]

Elle peut donc présenter une vitesse de phase instantanée variable selon la
jauge de réduction, sans contredire (12). De même, le profil RDSS de
Bradshaw--Tsai ou Pineau--Vicol peut être périodique dans le repère
co-tournant; il n'est pas en général une orbite pure d'un seul $U$.

Les situations suivantes ne réfutent donc pas le lemme :

- choix arbitraire de $\theta(s)$ lorsque $\mathcal RU=0$;
- saut de phase de $2\pi/k$ pour un profil à symétrie discrète $k$-fois;
- repère tournant à vitesse variable appliqué à un profil $W(s)$ déformable;
- orbite relative périodique ou quasi périodique;
- axe de rotation lui-même variable, qui relève de $SO(3)$ et de (17);
- proximité numérique d'une orbite sans identité exacte dans un espace
  fonctionnel.

## 8. Passe contradictoire

1. **Statut de Pineau--Vicol.** La mise en ligne arXiv n'est pas une
   publication évaluée. La remarque 1.8 ne doit pas recevoir le statut
   `PAPER_PROOF`.
2. **Définition contre théorème.** Bradshaw--Tsai obtient la phase
   logarithmique en imposant une représentation du groupe des dilatations.
   Cela ne prouve pas, à lui seul, le relèvement régulier d'une orbite donnée
   seulement comme ensemble.
3. **Stabilisateur.** Si $\mathcal RU=0$, une phase arbitraire ne produit
   aucune dynamique. La présenter comme une rotation variable physique serait
   un faux contre-exemple.
4. **Symétrie discrète.** Une phase n'est définie que modulo le stabilisateur
   discret; il faut choisir un relèvement continu avant de différencier.
5. **Faiblesse temporelle.** Une solution suitable possède une équation
   distributionnelle, mais l'absolue continuité du paramètre de groupe ne
   découle pas automatiquement d'une appartenance à l'orbite presque partout.
6. **Pression.** Une constante spatiale $c(s)$ dans (11) est indétectable,
   mais une pression tournée incorrectement invalide (14). La projection de
   Leray évite la jauge, pas la non-localité lors des localisations.
7. **Non-linéarité.** Pour $U\in L^{3,\infty}$, $U\otimes U$ définit bien une
   distribution locale, mais cela ne donne pas d'office
   $U\in W^{1,2}_{\rm loc}$ ni les traces nécessaires à (19).
8. **Rotation intermédiaire.** Les régimes petit et grand de Pineau--Vicol ne
   se rejoignent pas par continuité; leurs seuils dépendent de la constante
   Type I.
9. **DSS contre orbite pure.** Une périodicité relative n'est pas l'ansatz
   (11). Appliquer (16) à un profil périodique variable est une inversion de
   quantificateurs.
10. **Approximation.** De
    $\|V(s)-\rho_{\theta(s)}U\|\ll1$ on ne déduit pas
    $\theta'\approx\mathrm{constante}$ sans borne inférieure quantitative sur
    $\mathcal RU$, choix de jauge et contrôle du défaut de PDE.
11. **Cadre abstrait.** Field et Krupa supposent un flot classique unique en
    dimension finie. Les citer directement comme preuve pour une solution
    faible de Navier--Stokes serait circulaire.
12. **Pertinence Clay.** Même (L1) ne traiterait que les singularités ayant un
    profil RSS exact. Exclure cette famille ne prouve pas la régularité globale.

## 9. Recherche d'absence bornée

La recherche a couvert, à la date de coupure :

- arXiv, avec les chaînes
  `rotated backward self-similar Navier-Stokes`,
  `rotationally self-similar weak L3`,
  `Navier-Stokes relative equilibrium rotation`,
  `one-parameter subgroup Navier-Stokes rotating wave`,
  `variable angular velocity self-similar Navier-Stokes` et
  `modulated rotating wave Navier-Stokes`;
- Crossref et les pages primaires des éditeurs pour les titres et DOI exacts;
- les références des PDF Pineau--Vicol v2, Bradshaw--Tsai, Chae--Wolf et
  Guevara--Phuc;
- les sources générales primaires Field et Krupa découvertes par les termes
  `equivariant dynamical systems`, `relative equilibrium`, `isotropy` et
  `group orbit invariant under the flow`;
- la littérature primaire de réduction de symétrie pour les écoulements en
  conduite, afin de distinguer définition computationnelle, théorème de PDE et
  résultat backward.

Résultat de cette recherche bornée :

- **publié pour Navier--Stokes :** phase logarithmique d'une RSS définie comme
  covariance de groupe; équation dans un repère à $\dot\theta$ variable;
  définitions d'équilibres relatifs à vitesse constante;
- **prépublié :** classification explicite des solitons de la remarque 1.8 de
  Pineau--Vicol;
- **publié abstraitement :** structure des flots équivariants sur orbites
  homogènes de dimension finie;
- **non identifié sous la formulation exacte recherchée :** théorème
  Navier--Stokes suitable faible-$L^3$ donnant un relèvement de phase et la
  constance modulo stabilisateur.

Ce résultat d'absence est limité aux bases indexées, chaînes, références et
textes ci-dessus. Une terminologie différente, un manuscrit non indexé ou une
source postérieure au 15 août 2026 peut échapper à la recherche.

## 10. Traçabilité des textes audités

| PDF primaire | SHA-256 |
|---|---|
| Pineau--Vicol, `2607.09619v2` | `379591AA3C1036C9140702EBE71AAAB309FE207439A57DB5CEFF893F15D0AE8E` |
| Bradshaw--Tsai, `1610.05680v1` | `DE297541695B1E52AEE702930F8C5F723EFFC5DB13FA208B80CBAD7EFEE47C52` |
| Chae--Wolf DSS, `1610.09464v2` | `1F537BC2B6B2E7752DB275A1EB1C903782068510C4D7BCD68DBDD45D14C0EFDC` |
| Chae--Wolf Liouville, `1609.06962v1` | `274073640A2216FCA2F5E376F47462E23B53F5256831C50B86D38488F3F0A7E7` |
| Guevara--Phuc, `1509.08177v2` | `3AB53F7A6268767796837B7B09E5E9120B7E7773621C2FFD30D14242299593D9` |
| Field 1980, version AMS | `33595294ECB246CDB21E93133029EB545E397C96D7C337F43C44157F1435120A` |
| Krupa 1990, copie auteur/éditeur auditée | `8A7EBFE44DAC2C19866DA14F04287D84F1405F351D4628EA5C738793E09B2C28` |

Les pages 7--8 et 32--35 de Pineau--Vicol v2, la dérivation du repère général
dans Bradshaw--Tsai, la première page et les propositions de Field, ainsi que
la première page et la section 2 de Krupa ont été extraites; les pages clés de
Pineau--Vicol, Bradshaw--Tsai, Field et Krupa ont aussi été rendues ou
inspectées visuellement pour vérifier les signes, statuts et quantificateurs.

## 11. Décision scientifique

**CONTINUER**, avec séparation de deux niveaux.

Le résultat positif de ce cycle est le lemme algébrique (12) : il élimine la
vitesse modulée pour une orbite rotationnelle exacte à axe fixe dès qu'un
relèvement $W^{1,1}_{\rm loc}$ est acquis. Le résultat négatif est qu'aucune
source publiée auditée ne fournit ce relèvement ni la rigidité de (18) dans la
classe suitable faible-$L^3$.

La prochaine expérience décisive devrait attaquer **(L2) avant (L1)** : choisir
un profil non axisymétrique $U$ et un test $\psi$ tel que
$\langle\mathcal RU,\psi\rangle\ne0$, puis déterminer si la régularité
temporelle distributionnelle de (3) rend la coordonnée locale de phase
absolument continue, avec constantes uniformes lorsque
$\langle\mathcal RU,\psi\rangle$ s'approche de zéro. Un contre-profil où la
phase ne peut être contrôlée uniformément près du stabilisateur justifierait
de pivoter directement vers (L1) avec une modulation explicitement fixée.
