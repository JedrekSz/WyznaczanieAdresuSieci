def bin(x):
    x=int(x)
    liczba = ""
    while x != 0:
        liczba = str(x%2) + liczba
        x = int(x/2)
    while len(liczba)<8:
        liczba="0" + liczba
    return liczba

def dez(x):
    i=len(x)-1
    dez = 0
    for n in x:
        dez += int(n) * pow(2,i)
        i -= 1
    return dez

print("Adres IP:")
ip=input().split(".")

print("Maska:")
maska=input().split(".")

odp=""
for i in range(4):
    ipZmiana=bin(ip[i])
    maskaZmiana=bin(maska[i])

    for n in range(8):
        if ipZmiana[n] == maskaZmiana[n] and ipZmiana[n] != "0":
            odp = odp + "1"
        else:
            odp = odp + "0"
    odp = odp + " "

odp2=odp.split(" ")

print(odp)
final=""
for x in range(4):
    final = final + str(dez(odp2[x]))
    final = final+"."
print(final)





