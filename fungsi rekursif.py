#fungdi rekursif adalah fungsi yang memangil dirinya sendri

#fungsi mencari fakatorial

def faktorial (n):
    if n==0 or n==1:
        return 1
    else :
        return n*(faktorial(n -1))
    
    #mencari nilai faktorial

a= int(input("masukan nilai yang akan dicari :"))
cari_faktorial=faktorial(a)
print ("nilai dari ", a,"! adalah",cari_faktorial)
