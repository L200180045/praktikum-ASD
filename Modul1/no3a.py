def jumlahHurufVokal(x):
      vokal ="AIUEOaiueo"
      jmlhuruf=len(x)
      jmlvokal=0
      for karakter in x:
            if karakter in vokal:
                  jmlvokal+=1
      return (jmlhuruf, jmlvokal)
k=jumlahHurufVokal("Surakarta")
print(k)
