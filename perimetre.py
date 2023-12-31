import math
def perimetre(r,n):
    """
    calcule une approximation du perimetre du cercle de rayon r

    r:rayon
    n: nombre de tranche
    """

    alpha = 2 * math.pi / n
    h = r * math.sin(alpha)
    b = r - r * math.cos(alpha)
    c = math.sqrt(h * h + b * b)
    return n * c

def vperimetre(r):
    return 2 * math.pi * r

n=int(input("On repete combien de fois:"))
for i in range(2,n):
   p = perimetre(5,i)
   vp = vperimetre(5)
   print("L'approximation est %s la vrai est %s" % (p , vp))