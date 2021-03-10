import matplotlib.pyplot as plt

def tocka_kruznica(r, p, q, x, y):
    if a > 1:
        print("Točka T({}, {}) nalazi se izvan tražene kružnice.".format(x, y))
    elif a == 1:
        print("Točka T({}, {}) nalazi se na traženoj kružnici.".format(x, y))
    elif a < 1:
        print("Točka T({}, {}) nalazi se unutar tražene kružnice.".format(x, y))

    if odabir == "DA":
        ime_slike = input("Unesite ime slike: ")
        plt.savefig('{}.pdf'.format(ime_slike))  
    else:
        plt.show()
    return a, odabir

r = -1
while r <= 0:
    r = float(input("Unesite radijus kružnice: "))
r2 = r**2
    
p = float(input("Unesite x koordinatu središta kružnice: "))
q = float(input("Unesite y koordinatu središta kružnice: "))
x = float(input("Unesite x koordinatu točke: "))
y = float(input("Unesite y koordinatu točke: "))

print("(x - {})^2 + (y - {})^2 = {}".format(p, q, r2))
print("T({}, {})".format(x, y))

odabir = input("Unesite 'DA' ako želite spremiti sliku. Inače će slika biti samoprikazana: ")
plt.xlabel('x os')
plt.ylabel('y os')
plt.ylim(-10, 10)
plt.xlim(-10, 10)
plt.plot(x,y,'ro')
circle1 = plt.Circle((p, q), r, color='r', fill = False)
plt.gca().add_patch(circle1)

a = ((x - p)**2) // r2 + ((y - q)**2) // r2
    
tocka_kruznica(r, p, q, x, y)
