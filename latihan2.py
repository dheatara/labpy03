








terbesar = []
while True:
    n = int(input ("Masukan Bilangan N: "))
    terbesar.append(n)
    if n == 0:
        break
print("Nilai Terbesar adalah : {}".format(max(terbesar)))