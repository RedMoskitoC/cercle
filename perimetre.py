import math
def perimetre(r,n):
    """
    calcule une approximation du perimetre du cercle de rayon r

    r:rayon
    n: nombre de tranche
    """

    alpha = 2 * math.pi / n
    a = r * math.sin(alpha)
    b = r - r * math.cos(alpha)
    x = math.sqrt(a * a + b * b)
    return n * x

def vperimetre(r):
    return 2 * math.pi*r
n=input("On repete combien de fois:")
for i in range(2,20):
   p = perimetre(5,i)
   vp = vperimetre(5)
   print("L'approximation est %s la vrai est %s" % (p , vp))