def max (angka1, angka2, angka3):
    if((angka1 >angka2) and A(angka2 > angka3)):
        return angka1
    elif ((angka2 > angka1) and (angka2 > angka3)):
        return angka2
    else :
        return angka3
    


a= int(input("masukan angka 1:"))
b=int(input("masukan angka 2:"))
c=int(input("masukan angka 3:"))

cek_max = (a,b,c)
print ("nilai maksimal dari ",a,",",b,"dan",c,"adalah", cek_max)
