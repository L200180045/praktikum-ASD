batas = int(input("Masukkan Batas Angka : "));
for a in range (2,batas,1):
    mod =1;
    for b in range (2,a,1):
        if (a%b==0):
           mod=0;

    if (mod==1):
        print(a);
