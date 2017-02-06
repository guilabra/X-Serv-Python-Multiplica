
print ("Tablas de multiplicar\n")

list = (range(1,11))

for i in list:
    print"Tabla del ", i
    print"-----------"
    for j in list:
        print i, "por ", j, "es ", i*j
