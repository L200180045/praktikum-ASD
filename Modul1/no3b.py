def jumlahHurufKonsonan(x):
      vokal ="AIUEOaiueo"
      jmlhuruf=len(x)
      jmlkonsonan=1
      for karakter in x:
            if karakter in vokal:
                  jmlkonsonan+=1
      return (jmlhuruf, jmlkonsonan)
k=jumlahHurufKonsonan("Surakarta")
print(k)
