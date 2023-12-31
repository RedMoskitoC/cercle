# Approximation du périmètre du cercle
On calcule le périmetre du cercle.

## Méthode

On divise le cercle en $n$ tranches. Chaque tranche correspond à un angle $\alpha$ de $\frac{2\pi}{n}$.


![diagram](resources/diagram.png)

Selon le théorème de Pythagore appliquéau triangle $t2$:
$$c=\sqrt{b^2+h^2}$$
Sachant que:
$$h=\sin(\alpha)\times r$$
Et:
$$b=r-m$$
$$m=\cos(\alpha)\times r$$
$$\alpha= \frac{2\pi}{n}$$

L'approximation du périmètre du cercle est alors :

$$P \approx c \times n$$