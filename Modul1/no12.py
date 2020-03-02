import random;

def Number(n):

    n = random.randint(0, 100)
    
    print("Permainan Tebak Angka")
    print("Ssya  Menyimpan Sebuah Angka bulat Antara 1 sampai 100. Coba tebak")

    kira2 = -1

    while kira2 != n:

        kira2 =  eval(input("Masukan Tebakan"))

        if kira2 == n:
            print("Ya. Anda Benar", n)
        elif kira2 > n:
            print("Itu Terlalu Besar. Coba Lagi")
        elif kira2 < n:
            print("Itu Terlalu Kecil. Coba Lagi")
print(Number(1))


