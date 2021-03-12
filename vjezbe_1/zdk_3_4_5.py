import matplotlib.pyplot as plt

def pravac(x1, y1, x2, y2):
    a = (y2 - y1) / (x2 - x1)
    print("y - {} = {} * (x - {})".format(y1, a, x1))

    if odabir == "DA":
        ime_slike = input("Unesite ime slike: ")
        plt.savefig('{}.pdf'.format(ime_slike))  
    else:
        plt.show()

x1 = int(input("Unesite x koordinatu za prvu točku: "))    
y1 = int(input("Unesite y koordinatu za prvu točku: "))

while True:
    x2 = int(input("Unesite x koordinatu za drugu točku: "))
    if x2 == x1:
        print("Netočan unos.")
    else:
        break
y2 = int(input("Unesite y koordinatu za drugu točku: "))

odabir = input("Unesite 'DA' ako želite spremiti sliku. Inače će slika biti samoprikazana: ")

plt.xlabel('x os')
plt.ylabel('y os')
plt.plot([x1, x2], [y1, y2])
plt.plot(x1, y1, marker='o', markerfacecolor='red', markersize=10)
plt.plot(x2, y2, marker='o', markerfacecolor='red', markersize=10)
 
pravac(x1, y1, x2, y2)


