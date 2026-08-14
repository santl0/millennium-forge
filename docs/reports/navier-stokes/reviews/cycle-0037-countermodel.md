# Cycle 0037 — Pont mince persistant entre deux gouttes pure-swirl

Date : 2026-08-15
Statut : calcul exact sur squelette lipschitzien, stable par lissage \(C_c^\infty\)
Portée : donnée initiale cinématique sur \(\mathbb R^3\), pas de solution évolutive Navier–Stokes

## Verdict

Un pont de longueur \(LR\), largeur \(\delta R\), placé au niveau
\(b=a+\Delta\) au-dessus du cutoff \(a\), ne conserve pas un rapport
endpoint non dégénéré lorsque

\[
 {\Delta\over a}\ge\gamma>0,\qquad aR\asymp K_u,\qquad L\to\infty.
 \tag{37.1}
\]

Les parois radiales du pont imposent au curl original

\[
 {K_{w,\mathrm{paroi}}\over aR}
 \gtrsim {b\over a}L^{2/3}\delta^{-1/3}.
 \tag{37.2}
\]

Par ailleurs, \(aR\asymp K_u\) force \(\delta L\lesssim1\), puisque le
pont porte l'amplitude \(b\asymp a\) sur un volume
\(\asymp\delta LR^3\). Même avec la largeur maximale admissible
\(\delta\asymp L^{-1}\), (37.2) donne

\[
 K_w\gtrsim aRL,\qquad {K_u\over K_w}\lesssim L^{-1}.
 \tag{37.3}
\]

La persistence \(\Delta\to0\) peut rendre peu coûteux le **curl du champ
tronqué** \(G=(F-a)_+\), mais jamais le curl original tant que le niveau
absolu \(a\) doit fermer sur la même paroi compacte. Pour une paroi linéaire
naturelle \(b\to0\),

\[
 {K_{w,G,\mathrm{paroi}}\over aR}
 \asymp
 \left((1+\eta)\eta^2{L^2\over\delta}\right)^{1/3},
 \qquad \eta={\Delta\over a}.
 \tag{37.4}
\]

Un budget tronqué \(K_{w,G}\lesssim aR\) requiert donc

\[
 \boxed{\eta\lesssim{\sqrt\delta\over L}.}
 \tag{37.5}
\]

Sous \(\delta L\lesssim1\), le meilleur réglage donne
\(\eta\lesssim L^{-3/2}\). Ainsi l'unique échappement géométrique fait
disparaître la persistence du pont; il autorise alors une seconde troncature
entre \(a\) et \(b\), qui sépare de nouveau les deux gouttes.

## 1. Champ exact et paramètres

Le rayon majeur annulaire est \(\mathcal R=\kappa R\), avec
\(2\le\kappa\le4\). Dans les coordonnées cylindriques,

\[
 U={\mathcal R\over r}F(r,z)e_\theta,\qquad
 W=\nabla\times U
 =-{\mathcal R\over r}F_z e_r
 +{\mathcal R\over r}F_r e_z.
 \tag{37.6}
\]

Le champ est exactement divergence-free. Son support reste loin de l'axe.
On emploie le chapeau

\[
 h(x)=
 \begin{cases}
 1,&|x|\le1/4,\\
 2-4|x|,&1/4<|x|<1/2,\\
 0,&|x|\ge1/2,
 \end{cases}
 \tag{37.7}
\]

et une fonction axiale \(j_L\) égale à \(1\) sur un intervalle de longueur
\(LR\), puis décroissant linéairement vers zéro sur deux caps de longueur
\(R\). Le pont isolé est

\[
 F_B(r,z)=b\,
 h\!\left({r-\mathcal R\over\delta R}\right)j_L(z),
 \qquad b=a+\Delta=a(1+\eta).
 \tag{37.8}
\]

Deux gouttes de taille \(R\), de hauteur comprise entre \(b\) et \(2b\),
sont placées aux extrémités et recouvrent les caps. Elles peuvent être
prises sous forme produit

\[
 F_\pm=A_\pm
 h\!\left({r-\mathcal R\over R}\right)
 h\!\left({z-z_\pm\over R}\right),
 \qquad b\le A_\pm\le2b.
 \tag{37.9}
\]

Le champ total est \(F=F_-+F_B+F_+\). Le recouvrement des caps est choisi
de façon que \(\{F>a\}\) soit connexe. Toutes les minorations décisives sont
prises dans le tiers central du pont, où \(F_\pm=0\); aucune cancellation
avec les gouttes n'y est possible.

Après remplacement des rampes par des raccords monotones
\(C^\infty\) d'épaisseur relative \(\varepsilon\), le champ appartient à
\(C_c^\infty\). Les volumes témoins et les bornes perdent seulement un
facteur \(1-O(\varepsilon)\), uniformément en \(L,\delta,\eta\).

## 2. Curl complet du pont

À partir de (37.6)--(37.8),

\[
 W_{r,B}=-{b\mathcal R\over r}
 h\!\left({r-\mathcal R\over\delta R}\right)j_L'(z),
 \tag{37.10}
\]

\[
 W_{z,B}={b\mathcal R\over r\delta R}
 h'\!\left({r-\mathcal R\over\delta R}\right)j_L(z).
 \tag{37.11}
\]

La composante \(W_z\) vit sur les deux parois radiales; \(W_r\) vit sur les
deux caps. Il n'y a pas de composante azimutale. Comme

\[
 \int h={3\over4},\quad \int|h'|=2,\quad
 \int j_L=(L+1)R,\quad \int|j_L'|=2,
 \tag{37.12}
\]

les variations \(L^1\) sont exactement

\[
 \boxed{\|W_{z,B}\|_1
 =4\pi b\mathcal RR(L+1),}
 \tag{37.13}
\]

\[
 \boxed{\|W_{r,B}\|_1
 =3\pi b\mathcal R\delta R.}
 \tag{37.14}
\]

Le coût des parois est linéaire en \(L\) et indépendant de \(\delta\) en
\(L^1\); amincir le pont concentre seulement ce coût.

Les deux gouttes apportent chacune

\[
 K_{u,\pm}\asymp bR,\qquad K_{w,\pm}\asymp bR,
 \tag{37.15}
\]

et quatre raccords supplémentaires de volume \(\asymp R^3\). Ils ne
dépendent pas de \(L\). Les gradients dans les zones de recouvrement des
caps sont eux aussi \(O(b/R)\) sur \(O(R^3)\). Ils ne peuvent compenser le
témoin central de (37.11).

## 3. Fonctions de distribution

Pour \(0<t<1\), la distribution axiale exacte de \(j_L\) est

\[
 D_L(t)=R\,[L+2(1-t)].
 \tag{37.16}
\]

La distribution complète du pont est donc

\[
 \mu_{U_B}(q)=2\pi
 \int_{\mathcal R-\delta R/2}^{\mathcal R+\delta R/2}
 rD_L\!\left(
 {qr\over b\mathcal Rh((r-\mathcal R)/(\delta R))}
 \right)dr.
 \tag{37.17}
\]

Sur les parois, \(|h'|=4\), d'où

\[
 \mu_{W_{z,B}}(q)=2\pi
 \int_{\{h'\ne0\}}rD_L\!\left(
 {qr\delta R\over4b\mathcal R}
 \right)dr.
 \tag{37.18}
\]

Sur les caps, \(|j_L'|=R^{-1}\), donc

\[
 \mu_{W_{r,B}}(q)=4\pi R
 \int_{\mathcal R-\delta R/2}^{\mathcal R+\delta R/2}
 r\mathbf1_{\{b\mathcal Rh/(rR)>q\}}dr.
 \tag{37.19}
\]

Enfin la distribution vectorielle, y compris les quatre coins
paroi--cap, est exactement

\[
 \mu_{W_B}(q)=2\pi\int\!\!\int r\,
 \mathbf1_{\{(\mathcal R/r)^2[
 b^2h^2(j_L')^2+b^2(h')^2j_L^2/(\delta R)^2]>q^2\}}
 dr\,dz.
 \tag{37.20}
\]

Le pont plateau a volume

\[
 V_{B,\mathrm{plat}}=2\pi\mathcal R\,\delta LR^2
 =2\pi\kappa\delta LR^3.
 \tag{37.21}
\]

Les parois radiales sur ce plateau ont volume
\(\pi\kappa\delta LR^3\), amplitude comparable à
\(b/(\delta R)\). Les deux caps, restreints au plateau radial, ont volume
\(2\pi\kappa\delta R^3\), amplitude comparable à \(b/R\). Par conséquent,

\[
 K_{u,B}\asymp bR(\delta L)^{1/3},
 \tag{37.22}
\]

\[
 K_{w,z,B}\asymp
 bR\,L^{2/3}\delta^{-1/3},
 \qquad
 K_{w,r,B}\asymp bR\,\delta^{2/3}.
 \tag{37.23}
\]

Les parois dominent les caps dès \(L\ge1\).

Pour le champ total, les régions centrales des gouttes et du pont sont
disjointes, de même que leurs témoins de curl. On a donc les bornes
certifiées

\[
 c b^3R^3(2+\delta L)
 \le K_u^3
 \le C b^3R^3(2+\delta L),
 \tag{37.24}
\]

\[
 K_w^3\ge
 c b^3R^3\max\left\{1,{L^2\over\delta},\delta^2\right\}.
 \tag{37.25}
\]

Les constantes dépendent seulement de \(\kappa\) et du profil fixé, jamais
de \(L,\delta,a,\Delta\).

## 4. Échec pour une persistence relative fixe

Supposons \(\eta=\Delta/a\ge\gamma>0\). Alors \(b/a\ge1+\gamma\). Si
\(aR\asymp K_u\), (37.24) impose

\[
 \delta L\le C_0.
 \tag{37.26}
\]

Par (37.25),

\[
 {K_w^3\over(aR)^3}
 \ge c(1+\gamma)^3{L^2\over\delta}
 \ge {c(1+\gamma)^3\over C_0}L^3.
 \tag{37.27}
\]

C'est (37.3). Aucun choix \(\delta=\delta(L)\le1\) ne garde le rapport
global non nul. Sans même utiliser (37.26), le meilleur choix
\(\delta=1\) donne déjà \(K_u/K_w\lesssim L^{-1/3}\) lorsque le pont domine
\(K_u\).

Changer l'amplitude globale \(a=a_L\) ne sert pas : elle multiplie
simultanément \(K_u\) et \(K_w\). Les signes des deux gouttes ne servent pas
non plus, puisque le témoin (37.11) est situé loin des zones de
recouvrement.

## 5. Échappement \(\Delta\to0\) après troncature

Considérons maintenant

\[
 G=(F-a)_+,\qquad U_G={\mathcal R\over r}G e_\theta.
 \tag{37.28}
\]

Sur le plateau central, \(G=\Delta=a\eta\). Dans chaque rampe radiale
linéaire \(b\to0\), la région active \(F>a\) occupe exactement la fraction

\[
 \theta_\eta=1-{a\over b}
 ={\eta\over1+\eta}
 \tag{37.29}
\]

de la rampe. La dérivée ne devient pas \(\Delta/(\delta R)\) : elle reste
\(4b/(\delta R)\) sur cette couche plus mince. La règle de chaîne donne
\(\nabla G=\mathbf1_{\{F>a\}}\nabla F\) presque partout, sans mesure de
surface.

Le volume des deux couches radiales actives est donc, à la constante
géométrique exacte près,

\[
 V_{G,z}\asymp
 \delta LR^3{\eta\over1+\eta}.
 \tag{37.30}
\]

Il en résulte

\[
 K_{w,G,z}^3
 \asymp
 a^3R^3(1+\eta)\eta^2{L^2\over\delta},
 \tag{37.31}
\]

qui est (37.4). Les couches actives des caps ont longueur totale
\(2R\eta/(1+\eta)\), donc

\[
 K_{w,G,r}^3
 \asymp a^3R^3(1+\eta)\eta^2\delta^2.
 \tag{37.32}
\]

Elles sont sous-dominantes. Le pont tronqué lui-même vérifie

\[
 K_{u,G,B}^3\asymp a^3R^3\eta^3\delta L.
 \tag{37.33}
\]

Si les gouttes montent jusqu'à \(2a\), leur partie tronquée garde
\(K_{u,G,\pm}\asymp aR\). Ainsi (37.5) est à la fois la loi nécessaire et,
à constantes près pour ce squelette, suffisante pour rendre le coût tronqué
du pont comparable au coût des gouttes.

Sous la contrainte globale \(\delta L\lesssim1\), maximiser \(\delta\)
donne \(\delta\asymp L^{-1}\) et

\[
 {\Delta\over a}=\eta\lesssim L^{-3/2}.
 \tag{37.34}
\]

À ce régime, choisir un second niveau

\[
 a+c\Delta,\qquad 0<c<1,
 \tag{37.35}
\]

traverse la faible persistence du pont et sépare les deux gouttes. Le
grand diamètre n'est donc maintenu que dans une fenêtre de niveaux relative
qui tend vers zéro.

### Profil deux-étages, test le plus favorable

On peut artificiellement faire tomber \(b\) à \(a\) sur toute la largeur
\(\delta R\), puis exporter la fermeture de \(a\) sous le cutoff. Le gradient
actif devient alors \(\Delta/(\delta R)\) sur un volume
\(\asymp\delta LR^3\), et

\[
 {K_{w,G,z}\over aR}
 \asymp \eta L^{2/3}\delta^{-1/3}.
 \tag{37.36}
\]

La loi nécessaire plus faible est

\[
 \eta\lesssim\delta^{1/3}L^{-2/3},
 \quad\hbox{donc}\quad
 \eta\lesssim L^{-1}\ \text{si }\delta L\lesssim1.
 \tag{37.37}
\]

Ce profil ne sauve pas le champ original : le niveau de base \(a\) doit
encore fermer quelque part. S'il ferme dans la même largeur, (37.2)
revient; s'il ferme dans un halo plus large, ce halo apparaît dans les
fonctions de distribution aux seuils inférieurs, exactement comme aux
cycles 0035--0036.

## 6. Exploration rationnelle reproductible

Le script utilise les cubes des quasi-normes, ce qui évite toute racine dans
les assertions. Il parcourt des familles
\(L=n^2\), \(\delta=L^{-p}\), \(\eta=L^{-q/2}\), vérifie les distributions
étagées, les caps, la loi naturelle (37.5) et le profil deux-étages.

~~~python
from fractions import Fraction as Q


def bridge_cubes(L, delta, eta):
    # Units a=R=1; geometric constants common to all rows are suppressed.
    b = 1 + eta
    ku_original = b ** 3 * (2 + delta * L)
    kw_wall_original = b ** 3 * L ** 2 / delta
    kw_caps_original = b ** 3 * delta ** 2
    ku_truncated_bridge = eta ** 3 * delta * L
    kw_wall_truncated = (1 + eta) * eta ** 2 * L ** 2 / delta
    kw_caps_truncated = (1 + eta) * eta ** 2 * delta ** 2
    kw_wall_two_stage = eta ** 3 * L ** 2 / delta
    return {
        "ku": ku_original,
        "kw_wall": kw_wall_original,
        "kw_caps": kw_caps_original,
        "ku_g_bridge": ku_truncated_bridge,
        "kw_g_wall": kw_wall_truncated,
        "kw_g_caps": kw_caps_truncated,
        "kw_g_two_stage": kw_wall_two_stage,
    }


checks = 0
for n in range(2, 42):
    L = Q(n * n)
    for p in (1, 2, 3):
        delta = L ** (-p)
        assert delta * L <= 1

        # Fixed persistence: original wall cost is at least L^3 in cube.
        fixed = bridge_cubes(L, delta, Q(1, 2))
        assert fixed["kw_wall"] >= Q(27, 8) * L ** 3
        assert fixed["kw_wall"] >= fixed["kw_caps"]

        # Natural linear wall: eta=sqrt(delta)/L is rational because L=n^2.
        eta_natural = Q(1, n ** p) / L
        natural = bridge_cubes(L, delta, eta_natural)
        assert natural["kw_g_wall"] == 1 + eta_natural
        assert natural["kw_g_caps"] <= natural["kw_g_wall"]
        assert natural["ku_g_bridge"] <= 1

        checks += 1

# Two-stage saturation with L=n^3, delta=L^-3, eta=n^-5.
for n in range(2, 42):
    L = Q(n ** 3)
    delta = L ** (-3)
    eta_two = Q(1, n ** 5)
    two = bridge_cubes(L, delta, eta_two)
    # eta=delta^(1/3)L^(-2/3), hence eta^3 L^2/delta=1.
    assert two["kw_g_two_stage"] == 1
    checks += 1

# Under delta=1/L, the natural persistence law is eta=L^(-3/2).
for n in range(2, 82):
    L = Q(n * n)
    delta = 1 / L
    eta = Q(1, n ** 3)
    row = bridge_cubes(L, delta, eta)
    assert delta * L == 1
    assert row["kw_g_wall"] == 1 + eta
    assert row["kw_wall"] >= L ** 3
    checks += 1

print("exact checks =", checks)
print("exact residual = 0")
for n in (2, 4, 8, 16, 32):
    L = Q(n * n)
    delta = 1 / L
    eta = Q(1, n ** 3)
    row = bridge_cubes(L, delta, eta)
    print("L=%4d delta=%s eta=%s Kw_original^3=%s Kw_truncated^3=%s" %
          (L, delta, eta, row["kw_wall"], row["kw_g_wall"]))
~~~

## 7. Passe contradictoire

1. **Amincir le pont.** Cela réduit son volume, mais augmente
   \(K_{w,z}\) comme \(\delta^{-1/3}\).
2. **Allonger les caps.** Les caps sont déjà sous-dominants; réduire
   \(W_r\) ne change pas le mur radial présent sur toute la longueur.
3. **Faire \(\Delta\to0\).** Cela réduit le curl tronqué selon (37.31),
   pas le curl original, qui voit \(b=a+\Delta\).
4. **Confondre gradient \(\Delta/(\delta R)\) et gradient
   \(b/(\delta R)\).** Le premier correspond au profil deux-étages; une
   paroi linéaire \(b\to0\) conserve le second sur une couche active plus
   mince. Les lois (37.5) et (37.37) doivent rester distinctes.
5. **Cancellation avec les gouttes.** Le témoin est pris au centre du
   pont, hors de leurs supports.
6. **Seuil exactement égal à \(b\).** Les fonctions de distribution
   utilisent des inégalités strictes; on prend les limites à gauche. Les
   plateaux de mesure positive ne changent pas les quasi-normes.
7. **Passage au lisse.** Les identités exactes concernent le squelette.
   Le lissage monotone conserve les variations et les bornes à
   \(1-O(\varepsilon)\), mais les distributions lisses ne sont pas
   identiques point par point.
8. **PDE et pression.** Aucun calcul de pression, diffusion, stretching ou
   temps maximal n'est effectué. Le résultat est une obstruction
   cinématique, pas une preuve pour Clay.

## 8. Décision

**ABANDONNER** un pont au-dessus du cutoff dont la persistence relative
\(\Delta/a\) est minorée. Il force \(K_u/K_w\to0\), uniformément en sa
largeur.

**CONSERVER** l'échappement \(\Delta/a\to0\) seulement comme mécanisme de
topologie des superniveaux : dans le profil naturel, il exige
\(\Delta/a\lesssim\sqrt\delta/L\), et sous \(aR\asymp K_u\),
\(\Delta/a\lesssim L^{-3/2}\). Une seconde troncature sépare alors les
gouttes.

Le prochain lemme utile doit quantifier une sélection sur une fenêtre de
niveaux : soit une persistence relative positive fournit un coût de curl,
soit un niveau intermédiaire scinde la composante en morceaux de diamètre
\(O(R)\).
